---
title: "1.8. Transformaciones a escala"
tags: [SBD, RA1]
---

# 1.8. Transformaciones a escala

**CE que se trabajan:** b, c, d, g. Consulta el [texto oficial](ra1.md).

**Al terminar:** aplicar las reglas de preparación con operaciones distribuidas y justificar el coste del plan.

## Las mismas reglas, otro modo de ejecutarlas

Parte de la sesión y datos de [Spark](spark.md). A escala interesa evitar bucles sobre filas en Python, declarar tipos y reducir transferencias. Una operación nativa como `when` permite al motor planificar el trabajo. La lógica de negocio sigue siendo la de [preparación](preproceso.md).

## Lectura estricta y cuarentena

El laboratorio original utiliza `FAILFAST`: un error de lectura detiene el cálculo. Es una política válida para la entrega. Para estudiar otra política, trabaja en una copia y separa los registros problemáticos en una salida de cuarentena.

En Apache Spark 3.5.6 usamos `PERMISSIVE` y `columnNameOfCorruptRecord` para capturar errores del lector CSV. No suponemos que `badRecordsPath`, presente en algunos entornos, sea una opción portátil. La [documentación del lector CSV](https://spark.apache.org/docs/3.5.6/sql-data-sources-csv.html) detalla estas opciones.

```python
from pyspark.sql import functions as F
schema = """id_reserva long, id_hotel int, canal string, fecha date,
            noches int, importe decimal(12,2), _corrupt_record string"""
leidos = (spark.read.schema(schema).option("header", True)
    .option("mode", "PERMISSIVE")
    .option("columnNameOfCorruptRecord", "_corrupt_record")
    .csv("datos/reservas.csv")
    .withColumn("fuente", F.input_file_name()))
# Materializar toda la lectura: no consultar solo la columna corrupta en el CSV.
leidos.write.mode("errorifexists").parquet("lectura_auditable_01")
x = spark.read.parquet("lectura_auditable_01")
obligatorios = ["id_reserva", "id_hotel", "fecha", "noches", "importe"]
valido = F.col("_corrupt_record").isNull()
for campo in obligatorios:
    valido = valido & F.col(campo).isNotNull()
valido = valido & (F.col("noches") > 0) & (F.col("importe") >= 0)
marcados = x.withColumn("valido", F.coalesce(valido, F.lit(False)))
rechazos = marcados.filter(~F.col("valido"))
limpios = marcados.filter("valido").drop("_corrupt_record", "valido")
rechazos.write.mode("errorifexists").parquet("cuarentena_01")
assert marcados.count() == limpios.count() + rechazos.count()
```

El modo tolerante no detecta todo: una fila con menos campos puede producir nulos y una con más campos no necesariamente queda marcada como corrupta. Separa **errores de formato** de **reglas semánticas** (dominio, claves, referencias). Si el número exacto de campos es parte del contrato, compruébalo también con un lector CSV que respete comillas. Una fecha válida puede pertenecer al periodo equivocado. Conserva el fichero original y contabiliza los rechazos antes de continuar.

## Duplicados: identidad y precedencia

Para copias idénticas, `dropDuplicates()` sirve. Si existen versiones, necesitamos un orden de negocio determinista. El siguiente ejemplo es autónomo y no cambia la regla de cancelación del laboratorio:

```python
from pyspark.sql.window import Window
versiones = spark.createDataFrame([
    (1, "2026-09-01 10:00:00", 1, "web"),
    (1, "2026-09-01 11:00:00", 2, "ota"),
    (2, "2026-09-01 10:00:00", 3, "web"),
], "id_reserva long, actualizado string, id_cambio long, canal string")
spark.conf.set("spark.sql.session.timeZone", "UTC")
versiones = versiones.withColumn("actualizado", F.to_timestamp("actualizado"))
assert versiones.filter("actualizado IS NULL OR id_cambio IS NULL").count() == 0
assert versiones.groupBy("id_cambio").count().filter("count > 1").count() == 0
w = Window.partitionBy("id_reserva").orderBy(
    F.col("actualizado").desc(), F.col("id_cambio").desc())
ultima = versiones.withColumn("orden", F.row_number().over(w)).filter("orden = 1").drop("orden")
ultima.orderBy("id_reserva").show()  # Reserva 1: ota; reserva 2: web.
```

`id_cambio` desempata con una prioridad acordada. Si no existe desempate válido, detecta el conflicto en lugar de escoger una fila arbitraria. La ventana agrupa y ordena, por lo que puede generar intercambio y coste adicional.

## Transformaciones y nulos por grupos

Normaliza categorías con `lower(trim(...))`, deriva fechas con `year`/`month`, y expresa tramos con `when`. Cuando la política permite imputar una variable exploratoria, calcula el estadístico por un grupo pertinente y relaciónalo sin recoger toda la tabla:

```python
# Demostración opcional: no usar importes imputados como total contable real.
medianas = r.groupBy("id_hotel").agg(F.expr("percentile_approx(importe, 0.5)").alias("mediana"))
exploracion = (r.join(medianas, "id_hotel", "left")
    .withColumn("importe_imputado", F.col("importe").isNull())
    .withColumn("importe_exploratorio", F.coalesce("importe", "mediana")))
```

Si todo el grupo es nulo, la mediana también lo es. Registra esa cobertura. Conserva los importes originales; la aproximación y la imputación forman parte de la interpretación.

## Joins, broadcast y desigualdad de tamaños

Con `h` validado como catálogo pequeño y único en [integración](integracion.md):

```python
necesarias = r.filter(F.col("canal") == "web").select("id_reserva", "id_hotel", "importe")
resultado = necesarias.join(F.broadcast(h), "id_hotel", "left")
resultado.explain(mode="formatted")
resultado.groupBy("hotel").agg(F.sum("importe")).show()
```

**Broadcast** distribuye una tabla pequeña a los procesos de ejecución para evitar un intercambio grande en ciertos joins. No lo fuerces con una tabla que no cabe holgadamente en su memoria: mide su tamaño y deja decidir al optimizador si no tienes evidencia. «Pequeña» se refiere también a bytes y representación, no solo a filas.

El **skew** aparece cuando una clave concentra mucha más carga que las demás; por ejemplo, casi todas las reservas pertenecen a un hotel. Aumentar particiones no divide necesariamente una única clave caliente. Detecta la frecuencia por clave y compara etapas; las técnicas avanzadas de redistribución quedan fuera de este bloque.

## Leer y mover menos

- **Column pruning:** leer solo columnas necesarias cuando el formato lo permite.
- **Predicate pushdown:** trasladar filtros hacia la lectura cuando el origen y el motor lo permiten.
- **Particiones de procesamiento:** porciones de trabajo. `repartition` puede repartir de nuevo, pero introduce coste; no fijamos un número mágico.
- **Particiones de almacenamiento:** carpetas por valores como fecha. Pueden permitir omitir rutas, pero no son lo mismo que las particiones del cálculo.

En Parquet prueba `spark.read.parquet("preparado_01").select("canal", "importe").filter("importe > 100").explain("formatted")`. Busca el esquema leído y filtros. Que el filtro aparezca no garantiza ahorrar todos los bytes: depende de estadísticas y distribución.

`collect()` y `toPandas()` llevan el conjunto al proceso conductor. Agrega primero y recoge solo un resumen acotado. `show(10)` ayuda a inspeccionar, pero no valida diez millones de filas. Una escritura distribuida evita reunir todo en un único proceso. Evalúa `cache` solo cuando reutilizas una etapa y libera los recursos después; no es una mejora automática.

!!! example "Práctica y comprobación"
    En una copia introduce un importe no numérico, una clave nula y una noche negativa. Demuestra dónde acaba cada fila y registra recuentos. Compara después un join con y sin proyección/filtro, verificando el mismo resultado. Adjunta el plan y explica dónde esperas lectura o intercambio, distinguiendo medición y predicción.

La administración de clústeres y el dimensionamiento de la plataforma se coordinan con BDA. Aquí justificamos decisiones de procesamiento sobre un entorno disponible.
