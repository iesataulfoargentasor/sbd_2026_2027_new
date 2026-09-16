---
title: "1.11. Coste, calidad y eficiencia"
tags: [SBD, RA1]
---

# 1.11. Coste, calidad y eficiencia

**CE que se trabajan:** g. Consulta el [texto oficial](ra1.md).

**Al terminar:** comparar soluciones con resultados equivalentes y métricas de calidad y eficiencia.

## Elegir según el problema

| Opción | Uso razonable en este caso | Coste que considerar |
| --- | --- | --- |
| Python estándar | Referencia pequeña y lógica sencilla | Desarrollo manual y memoria de estructuras |
| SQL en origen | Filtrar o agrupar datos ya disponibles en la base | Carga sobre el sistema operativo de negocio |
| Spark | Integrar fuentes y repetir transformaciones a mayor escala | Arranque, coordinación y recursos |
| Servicio gestionado | Entorno que el centro haya seleccionado | Coste, transferencia y administración |

No se exige contratar servicios. La elección se justifica con requisitos, no con popularidad. Spark local no es siempre más rápido que una consulta SQL o Python en una muestra pequeña.

## Medir una ejecución completa

```bash
python generar.py --salida datos_grandes --copias 10000
python analizar.py --entrada datos_grandes --salida resultados_grandes
python verificar.py resultados_grandes --copias 10000
```

Esto produce 60 000 reservas y 80 000 eventos. Es un escalón para medir, no un umbral universal de Big Data. El profesor ajustará el volumen para el ensayo del CE b y decidirá si debe ejecutarse en recursos del centro.

`metricas.json` registra filas, bytes de entrada, duración total del proceso de análisis —incluye arranque, controles y escrituras— y maestro Spark. Para medir memoria utiliza el monitor de procesos del entorno y registra también la JVM, no solo Python. Anota CPU, RAM, disco, versiones y procesos competidores.

Repite una comparación con la misma entrada y registra al menos tres ensayos si quieres discutir variabilidad. No compares una ejecución completa con otra que solo muestra diez filas. Si se alcanza un límite de memoria, conserva el error y reduce el tamaño.

## Calidad medible

| Dimensión | Control |
| --- | --- |
| Completitud | Cero ausencias en campos obligatorios |
| Unicidad | Una fila por clave de reserva y hotel |
| Validez | Fechas interpretables, noches positivas e importes no negativos |
| Relación | Cero claves huérfanas |
| Reconciliación | Reservas e importes conservados al integrar |
| Trazabilidad | Fuentes, reglas, versión y salida identificadas |

Estos umbrales son del laboratorio. En un proyecto real se acuerdan según uso. Menos tiempo no compensa una respuesta incorrecta. Registra también mantenimiento y esfuerzo de preparación; el coste no se reduce a segundos.

## Tarea para practicar en clase

Compara dos tamaños y explica cómo cambian tiempo y bytes. Separa lo medido de lo esperado. Después formula una decisión: continuar localmente, filtrar antes de transferir o solicitar otro entorno. No extrapoles linealmente a 500 GB sin probar los límites de memoria y E/S.

## Cuatro dimensiones de calidad con denominadores

Define el alcance antes de medir: fichero bruto, filas distintas, registros aceptados o salida integrada. Si mides solo las filas ya aceptadas, muchas tasas serán 100 % y ocultarán el coste de los rechazos.

| Métrica | Definición operativa | Ejemplo |
| --- | --- | --- |
| Completitud de importe | Importes presentes / filas recibidas | 95/100 = 95 % |
| Unicidad de clave | Claves distintas no nulas / filas recibidas | 98/100 = 98 %, junto con nulos y conflictos |
| Validez | Filas que cumplen las reglas / filas recibidas | 96/100 = 96 % |
| Consistencia referencial | Reservas con hotel conocido / reservas recibidas | 99/100 = 99 % |

Estas métricas no sustituyen el análisis de conflictos: una misma clave con dos importes exige resolución aunque el porcentaje global parezca alto. Con cero filas, informa «no aplicable», no un porcentaje inventado. La exactitud requiere contraste con una fuente fiable; no se deduce solo de tipos correctos.

## Comparaciones reproducibles

### A. CSV y Parquet desde la lectura

Sobre el mismo DataFrame validado `r`, guarda `r.write.mode("errorifexists").parquet("medida_parquet_01")`. Compara una consulta de suma por canal leyendo el CSV con su esquema y leyendo ese Parquet. Usa la misma normalización, filtro y salida. Mide una acción completa, no la construcción del plan.

```python
from time import perf_counter
from pyspark.sql import functions as F

def medir(df):
    inicio = perf_counter()
    salida = (df.withColumn("canal", F.lower(F.trim("canal")))
        .filter(F.col("importe") >= 0).groupBy("canal")
        .agg(F.sum("importe").alias("total")).orderBy("canal").collect())
    return salida, perf_counter() - inicio

csv = spark.read.schema(esquema).option("header", True).option("mode", "FAILFAST").csv("datos/reservas.csv")
parquet = spark.read.parquet("medida_parquet_01")
a, tiempo_csv = medir(csv)
b, tiempo_parquet = medir(parquet)
assert a == b
print(tiempo_csv, tiempo_parquet)
```

Aquí `collect()` recoge únicamente dos grupos conocidos, no todas las reservas. Con cardinalidad no acotada, escribe el resumen. Separa el coste de convertir a Parquet del coste de consultas posteriores. El tamaño de los ficheros no equivale a bytes realmente leídos. En la muestra pequeña el arranque y otros costes pueden dominar.

### B. Filtrar antes o después de relacionar

```python
antes = r.filter("canal = 'web'").join(h, "id_hotel", "left")
despues = r.join(h, "id_hotel", "left").filter("canal = 'web'")
antes.explain("formatted")
despues.explain("formatted")
assert antes.exceptAll(despues).count() == 0
assert despues.exceptAll(antes).count() == 0
```

Con catálogo único y filtro sobre la reserva son equivalentes. Spark puede producir el mismo plan al adelantar el filtro: si ocurre, esa es la conclusión correcta. No inventes una aceleración. Filtrar una columna derecha después de un `left` puede eliminar nulos y cambiar la semántica; esa transformación exige otra comprobación.

### C. Traer filas o agregar en Spark

Solo sobre las seis reservas, compara `sum(f.importe for f in r.collect())` con `r.agg(F.sum("importe")).first()[0]`: ambos dan 1 660. El primero transfiere seis filas (n a escala); el segundo un escalar tras la agregación distribuida. Mide tiempos y volumen transferido si está disponible, pero no provoques una falta de memoria con el conjunto grande para demostrar el riesgo.

## Hoja de mediciones

| Ensayo | Filas/bytes de entrada | Resultado validado | Tiempo total | Memoria Python + JVM | Lectura/shuffle | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| CSV, consulta A | Medido | Sí/no y control | Medido | Medido o no disponible | Medido o no disponible | Versiones, caché, alcance |
| Parquet, consulta A | Medido | Mismo resultado | Medido | Medido o no disponible | Medido o no disponible | Conversión por separado |

Usa las métricas de ejecución disponibles para bytes y shuffle; no los deduzcas del número de filas. Alterna el orden de las pruebas, registra calentamiento/cachés y repite en condiciones comparables. La observación de una consulta sirve al análisis; la monitorización sostenida de la plataforma corresponde a BDA.

En [AWS](aws-s3-glue-athena.md), añade bytes escaneados y coste estimado con las condiciones vigentes del aula. La eficacia significa responder bien; la eficiencia, hacerlo con recursos y esfuerzo proporcionados.

!!! example "Decisión final"
    Entrega una comparación que conserve el resultado y mejora alguna métrica, o explica por qué no mejora. Recomienda una opción para una ejecución única y otra para consultas repetidas, considerando también mantenimiento y conversión.
