---
title: 1.5 Formatos de datos
tags:
  - SBD
  - RA1
---

# 1.5. Formatos de datos para el análisis

En BDA elegiste el formato de **la carga**. Aquí eliges el formato para **consultar y combinar** (criterio **c)**). Un mal formato no se nota en 200 filas; en Athena se paga **cada lunes**.

Un formato útil en pipelines debería ser, en la medida de lo posible: independiente del lenguaje, expresivo (anidados), eficiente, evolutivo y **partible** (Hadoop/Spark/Athena lo trocean). CSV enorme en un solo JSON con un array `[...]` **no** se parte bien.

## Texto frente a binario

| Familia | Ejemplos | Cuándo |
| --- | --- | --- |
| Texto | CSV, JSON, XML | Depurar, Excel, APIs |
| Binario | Avro, Parquet, ORC | Volumen, clúster, coste de escaneo |

JSON clásico vs **JSONL** (un objeto por línea): el segundo se trocea; `None` es Python, en JSON se escribe `null`.

## Filas frente a columnas

CSV, JSON y Avro guardan **el registro junto** (fila). Parquet y ORC guardan **la columna junta**.

Si el informe solo usa `hotel` e `importe` de una tabla de 80 columnas, el columnar **no lee** las otras 78. Por eso comprime mejor (valores parecidos juntos) y Athena, que cobra por **dato escaneado**, sale más barata.

Inconveniente: reconstruir una fila suelta o **actualizar** un registro es caro. La caja del hotel (OLTP) no vive en Parquet.

Orden de magnitud que verás citado: 1 TB de CSV puede quedar en torno a **130 GB** en Parquet. La cifra exacta cambia; el procedimiento no.

## Avro (filas + esquema)

Binario compacto; el **esquema va en JSON** en la cabecera del fichero. Partible. Típico en buses (Kafka) y cuando el esquema **evoluciona**.

```json
{
  "type": "record",
  "name": "Empleado",
  "fields": [
    { "name": "nombre", "type": "string" },
    { "name": "altura", "type": "float" },
    { "name": "edad", "type": ["null", "int"], "default": null }
  ]
}
```

En Python, para volumen, **fastavro** suele ir mejor que la librería de referencia. Snappy prioriza **velocidad**; gzip, tamaño. En Big Data suele ganar el códec rápido.

Esquema de aula: [empleado.avsc](../assets/practicas/empleado.avsc).

## Parquet (columnas)

Pensado para análisis: *row groups*, datos por columna, metadatos al final, esquema embebido. Compresión alta (Snappy ~75 % es una cifra de catálogo, no un examen). Compatible con Spark, pandas y Athena.

```python
import pandas as pd

df = pd.read_csv("clientes.csv")
df.to_parquet("clientes.parquet")
solo = pd.read_parquet("clientes.parquet", columns=["ciudad", "edad"])
```

`columns=` es el criterio c) en una línea: **no escanees lo que no preguntas**.

PyArrow (`pip install pyarrow`) es el motor habitual debajo de pandas.

## ORC

Columnar, muy ligado a **Hive** (*Optimized Row Columnar*): *stripes* con índice y estadísticas. Alta compresión (zlib). pandas: `read_orc` / `to_orc`. Si el equipo es Spark/Athena, Parquet suele ser el default; ORC, si el destino es Hive.

## Cómo elegir (guion de aula)

| Necesidad | Formato |
| --- | --- |
| Que lo abra un compañero | CSV / JSON |
| Cola o esquema que crece | **Avro** |
| Informe de tres columnas / Athena | **Parquet** |
| Tablas Hive | **ORC** (o Parquet si el stack es Spark) |
| Actualizar una reserva en recepción | Ni Parquet ni ORC como almacén operativo |

!!! tip "Puente con el laboratorio"
    En [1.7](laboratorio-aws.md) Athena escanea S3. Un CSV con cabecera mal leída (`col1`…`col5`) es un fallo de **calidad**. El mismo volumen en Parquet es un fallo de **coste** si lo dejas en texto “porque es simple”.

## Actividad

Convierte [clientes.csv](../assets/practicas/clientes.csv) a Parquet y lee **solo** `ciudad`. Compara tamaño en disco (o di, en el lab, por qué Athena preferiría ese fichero).
