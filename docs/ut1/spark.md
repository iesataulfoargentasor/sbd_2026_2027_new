---
title: "1.7. Procesamiento distribuido con Spark"
tags: [SBD, RA1]
---

# 1.7. Procesamiento distribuido con Spark

**CE que se trabajan:** a, b, g. Consulta el [texto oficial](ra1.md).

**Al terminar:** construir DataFrames, transformar, agregar y ejecutar consultas SQL reproducibles.

## Una tabla que se transforma

Un DataFrame contiene columnas con tipos definidos. PySpark permite describir operaciones y Spark prepara su ejecución. En esta unidad trabajamos con DataFrames y SQL; la administración de nodos se coordina con BDA.

En una terminal del entorno, `pyspark --master local[2]` abre una sesión interactiva con dos hilos locales. Desde la carpeta del laboratorio:

```python
from pyspark.sql import functions as F
esquema = 'id_reserva long, id_hotel int, canal string, fecha date, noches int, importe decimal(12,2)'
r = spark.read.schema(esquema).option('header', True).option('mode', 'FAILFAST').csv('datos/reservas.csv')
r.printSchema()
r.show()
r = r.withColumn('canal', F.lower(F.trim('canal')))
r.filter((F.col('canal') == 'web') & (F.col('noches') > 0)).select('id_reserva', 'noches').show()
```

`select` proyecta columnas; `filter` conserva filas; `withColumn` devuelve otro DataFrame. Los paréntesis de cada comparación evitan ambigüedades al combinar expresiones.

## Transformaciones y acciones

`select` y `filter` describen transformaciones. `count`, `show` y una escritura provocan ejecución. Definir una transformación y medir únicamente esa línea no mide el análisis completo. Varias acciones pueden recalcular trabajo si no se decide reutilizar resultados.

```python
r.createOrReplaceTempView('reservas')
spark.sql("SELECT canal, COUNT(*) AS reservas FROM reservas GROUP BY canal").show()
```

La vista temporal permite expresar operaciones sobre el mismo DataFrame con SQL. No es una copia persistente de los datos.

## Guardar una etapa

```python
r.write.mode('errorifexists').parquet('preparado_01')
```

Parquet conserva esquema y organiza datos por columnas. No resuelve por sí mismo errores de significado. Elegimos rutas distintas para fuente y salida.

## Tarea para practicar en clase

Filtra las reservas web y calcula cuántas son. Repite con SQL. Para el conjunto pequeño deben ser **4**. Comprueba que normalizar no cambia el total de seis reservas. Después explica por qué `collect()` sobre millones de filas puede desbordar la memoria del proceso conductor.

??? success "Idea clave"
    `show()` muestra una muestra limitada; `collect()` lleva todas las filas al proceso Python. Para exportar un conjunto grande, escribe desde Spark y recoge solo resúmenes pequeños.

El script completo [del laboratorio](entorno.md) añade controles y métricas a estas operaciones.

## Un repertorio pequeño y suficiente

Continúa sobre `r` creado al comienzo de esta página. Son operaciones independientes de demostración; decide cuáles necesita tu análisis.

```python
# Esquema y proyección: no trasladar columnas innecesarias.
r.select("id_reserva", "id_hotel", "importe").printSchema()
r.select("canal").distinct().show()
r.drop("fecha").show(3)

# Regla por columnas: ninguna fila pasa por un bucle Python.
clasificadas = (r.withColumn("mes", F.month("fecha"))
    .withColumn("tramo", F.when(F.col("noches") <= 2, "corta")
                         .otherwise("larga")))
clasificadas.select("id_reserva", "mes", "tramo").show()

# Categoría ausente: demostración, sin inventar importes.
r.na.fill({"canal": "desconocido"}).show(3)
r.na.drop(subset=["id_reserva", "id_hotel"]).show(3)

# Copias exactas; con conflictos por clave hace falta otra regla.
r.dropDuplicates().show(3)
r.groupBy("canal").agg(
    F.count("*").alias("reservas"), F.sum("importe").alias("importe_nominal"),
    F.avg("noches").alias("noches_medias"),
    F.min("fecha").alias("primera_fecha"), F.max("fecha").alias("ultima_fecha")
).show()
```

En la muestra, web suma 1 000 euros y OTA 660. Las fechas mínimas y máximas son iguales porque el generador fija un día; no inventes una tendencia temporal con esa fuente.

`na.drop` no es un control de calidad por sí solo: si lo eliges como política, registra cuántas filas excluyes y por qué. `dropDuplicates(["id_reserva"])` no selecciona necesariamente la versión más reciente. Para eso están las [ventanas con orden](transformaciones-escala.md).

## Qué significa ejecución distribuida

Spark divide el trabajo en particiones. Un filtro puede aplicarse a cada partición; una agrupación por canal puede requerir reunir datos de distintas particiones (**shuffle**, intercambio de datos). Eso conecta la lógica y la complejidad del CE a con el coste del CE g.

La evaluación diferida (*lazy evaluation*) permite planificar varias transformaciones antes de ejecutar una acción. El motor puede adelantar filtros o eliminar columnas no utilizadas. Para observar la consulta:

```python
consulta = r.filter(F.col("canal") == "web").groupBy("id_hotel").agg(F.sum("importe"))
consulta.explain(mode="formatted")
consulta.show()
```

Busca lectura, filtro, agregación e intercambio si lo hay. Los nombres concretos pueden variar entre versiones y estrategias. No necesitas configurar nodos ni administrar el clúster para razonar sobre ese plan.

### SQL equivalente

```python
clasificadas.createOrReplaceTempView("reservas_clasificadas")
spark.sql("""
SELECT id_hotel, canal, COUNT(*) AS reservas, SUM(importe) AS importe_nominal
FROM reservas_clasificadas
WHERE noches > 0
GROUP BY id_hotel, canal
ORDER BY id_hotel, canal
""").show()
```

!!! example "Práctica de cierre"
    Añade una columna `fin_semana` según la fecha, explica si representa reserva o estancia y calcula un resumen equivalente con DataFrames y SQL. Verifica igualdad de filas y totales, no el orden accidental de salida. Señala qué líneas describen trabajo y cuáles lo ejecutan.

Los ejemplos fijan el contrato de lectura. En [1.8](transformaciones-escala.md) diferenciaremos fallos de formato, nulos y reglas de negocio, sin silenciar errores.
