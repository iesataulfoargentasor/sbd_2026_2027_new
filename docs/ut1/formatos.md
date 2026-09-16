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

Tipos primitivos: `null`, `boolean`, `int`, `long`, `float`, `double`, `bytes`, `string`. Compuestos: `record`, `enum`, `array`, `map`, `union`, `fixed`. El `empleado.avsc` de aula usa el namespace `SeveroOchoa`.

`pip install avro-python3` (referencia) o `pip install fastavro` (más rápido, Cython). Códecs: gzip/deflate comprimen más; **Snappy** prioriza velocidad (`pip install python-snappy`). Un CSV de ventas de ~6,9 MiB puede quedar ~1,9 MiB gzip y ~2,8 MiB Snappy.

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

En Python, para volumen, **fastavro** suele ir mejor que la librería de referencia (`avro-python3`): parte del código está en Cython. Snappy prioriza **velocidad**; gzip, tamaño. En Big Data suele ganar el códec rápido.

Esquema de aula: [empleado.avsc](../assets/practicas/empleado.avsc) (copia de apoyo: [empleado.avsc en GitHub de IABD](https://aitor-medrano.github.io/iabd/de/resources/empleado.avsc)).

Vídeo del eXe (Avro, Parquet, ORC): [YouTube DafzYp5XRmA](https://youtu.be/DafzYp5XRmA).

### Cuadernos Avro (hacer los tres)

Copia cada cuaderno a tu Drive. En los dos primeros **adjunta** `empleado.avsc`; en el tercero, el CSV de ventas.

| Cuaderno | Qué haces | Enlace |
| --- | --- | --- |
| Avro (librería de referencia) | Serializar / deserializar con `avro-python3` y `empleado.avsc` | [1zxfPwEdHjaYHjkKjPOwXuj9fXGD8Anc1](https://colab.research.google.com/drive/1zxfPwEdHjaYHjkKjPOwXuj9fXGD8Anc1?usp=sharing) |
| Fastavro | El mismo caso, más rápido | [1z0ZsCX2Ws-3kSFLQEJS74CDkkot--Y-n](https://colab.research.google.com/drive/1z0ZsCX2Ws-3kSFLQEJS74CDkkot--Y-n?usp=sharing) |
| Fastavro + pandas | Leer [pdi_sales.csv](https://aitor-medrano.github.io/iabd/de/resources/pdi_sales.csv) (separador `;`), filtrar Alemania y escribir Avro | [1zaM4132cmUIsOWL5rbiCre5dCIyVL1RC](https://colab.research.google.com/drive/1zaM4132cmUIsOWL5rbiCre5dCIyVL1RC?usp=sharing) |

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

## Actividad 1 — Parquet (aula)

Convierte [clientes.csv](../assets/practicas/clientes.csv) a Parquet y lee **solo** `ciudad`. Compara tamaño en disco (o di, en el lab, por qué Athena preferiría ese fichero).

## Actividad 2 — Kaggle, vuelos (criterio c)

El eXe de formatos pide un notebook en [Kaggle](https://www.kaggle.com/) sobre [retrasos y cancelaciones de vuelos 2009–2018](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018). Elige **un** CSV anual (campos separados por `,`) y genera:

| Fichero | Contenido |
| --- | --- |
| `air<año>.parquet` | El CSV completo en Parquet |
| `air<año>.orc` | El CSV en ORC |
| `air<año>_snappy.orc` | ORC con códec Snappy |
| `air<año>_small.avro` | Solo `FL_DATE`, `OP_CARRIER`, `DEP_DELAY` en Avro |
| `air<año>_small.parquet` | Las mismas tres columnas en Parquet |

En pandas, el recorte de columnas es:

```python
df_small = df[["FL_DATE", "OP_CARRIER", "DEP_DELAY"]]
```

Anota tamaños (`os.path.getsize`) y tiempos (`time.time()`) en una celda Markdown. Con cuenta gratuita, Kaggle da más RAM (hasta ~30 GB / 73 GB de disco); sin cuenta, ~1 GB y el dataset no cabe.

Si el portátil o Kaggle se quedan cortos, usa una muestra de 100 000 filas y **documenta** el recorte. El criterio c) es **elegir formato por la pregunta**, no completar el dataset entero.

Entrega: captura del cuaderno o el `.ipynb` descargado (si Kaggle pide datos personales para compartir, adjunta el fichero en Moodle).

Solución de referencia (profesorado): [notebook Kaggle dmiprof01](https://www.kaggle.com/code/dmiprof01/fork-of-trabajo-actividad-de-formato-de-datos).

## Bibliografía (eXe)

- [Introducción a formatos (Aitor Medrano)](https://aitor-medrano.github.io/iabd/de/formatos.html)
- [An Introduction to Big Data Formats (Nexla, PDF)](https://webcdn.nexla.com/n3x_ctx/uploads/2018/05/An-Introduction-to-Big-Data-Formats-Nexla.pdf)
- [Data serialization in Hadoop (XenonStack)](https://www.xenonstack.com/blog/data-serialization-hadoop)
- [Handling Avro files in Python](https://www.perfectlyrandom.org/2019/11/29/handling-avro-files-in-python/)
- [Big Data File Formats Demystified (Datanami)](https://www.datanami.com/2018/05/16/big-data-file-formats-demystified/)

Índice: [Cuadernos Colab](cuadernos.md).
