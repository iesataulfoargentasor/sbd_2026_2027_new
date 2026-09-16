---
title: "U.T. 1. Integración, procesamiento y análisis de información"
tags:
  - Big Data
  - SBD
  - RA1
---

# U.T. 1. Integración, procesamiento y análisis de información

El título sigue el **[RA1](ra1.md)**: *aplica técnicas de análisis de datos que integran, procesan y analizan la información, adaptando e implementando sistemas que las utilicen*.

En BDA caracterizaste el almacén, la ingesta y el formato de la carga. Aquí el dato **ya entra**: hay que extraerlo, dejarlo limpio, relacionarlo con otras fuentes y **consultarlo** con un coste y una calidad justificables.

Lee cada apartado **en orden**. En todos hay un caso (hotel, clientes, logs de una tienda, meteorología de Castro Urdiales) y una pregunta del estilo “¿qué harías con el dato y por qué?”. Si puedes explicárselo a un compañero sin mirar la tabla, el apartado está asimilado. La [autoevaluación](autoevaluacion.md) comprueba vocabulario. Ninguna sustituye a Moodle.

Empieza por **[Inicio con Python](inicio-python.md)** (el Colab de portada del eXe *Técnicas de análisis de datos en Big Data*). El resto de cuadernos está en [Cuadernos Colab](cuadernos.md) y junto a la teoría de cada apartado. Ábrelos en tu Drive antes de ejecutar.

## Qué vas a trabajar

| Apartado | Criterio | Qué te llevas |
| --- | --- | --- |
| [Inicio con Python](inicio-python.md) | **b)** | Colab de arranque del eXe *Técnicas de análisis* (ETL mínimo en pandas) |
| [1.0 Marco Big Data](marco-big-data.md) | vocabulario | 3–7 V, ciencia de datos, BI, warehouse/lake, roles (paquete *Introducción a Big Data*) |
| [1.1 Integrar, procesar y analizar](ciclo-analisis.md) | **b)** | Dato → información → decisión; ETL; batch/streaming; tipos de análisis |
| [1.2 Fundamentos matemáticos y algoritmos](fundamentos.md) | **a)** | Conjuntos, lógica, grafos y complejidad (por qué un algoritmo no escala) |
| [1.3 Extracción de información](extraccion.md) | **b)** / **d)** | SQL, API, scraping, texto y dos prácticas completas con pandas |
| [1.4 Preproceso de datos](preproceso.md) | **b)** / **d)** | Limpieza, integración y transformación en pandas, y la misma receta a escala en PySpark |
| [1.5 Formatos de datos](formatos.md) | **c)** | Filas frente a columnas; Avro, Parquet, ORC y códecs para **consultar** |
| [1.6 Planificación con GitHub Projects](planificacion.md) | **e)** | Objetivos, mini-sprints, plantillas Colab e issues |
| [1.7 Laboratorio AWS](laboratorio-aws.md) | **f)** / **g)** | S3 + Glue + Athena; coste por dato escaneado y calidad del esquema |
| [Modelado](modelado.md) | **a)** | Diagramas, grafos, árboles (anexo Word Tema 4) |
| [Tiempo real](tiempo-real.md) | reconocimiento | Kafka, MQTT, Grafana; el reloj del streaming (Tema 5) |
| [Costes y calidad](costes-calidad.md) | **g)** | Dimensiones de calidad y coste on-prem/nube (Tema 6) |
| [Entorno Docker](docker.md) | apoyo / **f)** | Chuleta Docker y clúster Hadoop del manual de aula |
| [Cuadernos Colab](cuadernos.md) | prácticas | Todos los enlaces de los eXe (alumnado y solución de profesorado) |
| [Autoevaluación](autoevaluacion.md) | — | 20 preguntas de la unidad (no puntúa en Moodle) |

## Del Moodle a esta unidad

Cada paquete eXeLearning (o PDF) de la UT1 de Moodle queda asociado al mismo CE. Los HTML originales **no** se publican aquí.

| En Moodle | CE | Dónde lo trabajas aquí |
| --- | --- | --- |
| Introducción a Big Data SBD | vocabulario | [1.0](marco-big-data.md) |
| Introducción al procesamiento y análisis | **b)** | [1.1](ciclo-analisis.md) |
| Técnicas de análisis de datos en Big Data (vídeo SharePoint + eXe combinado + Word Temas 4–7) | **a)**–**g)** | [Inicio con Python](inicio-python.md), [1.1](ciclo-analisis.md), [1.2](fundamentos.md), [modelado](modelado.md), [tiempo real](tiempo-real.md), [costes](costes-calidad.md) |
| Manual Docker (clúster Hadoop) | apoyo / **f)** | [Entorno Docker](docker.md) |
| Fundamentos matemáticos y algoritmos | **a)** | [1.2](fundamentos.md) |
| Técnicas y procesos de extracción | **b)** / **d)** | [1.3](extraccion.md) |
| Preproceso de datos (PDF) | **b)** / **d)** | [1.4](preproceso.md) |
| Formato de datos SBD | **c)** | [1.5](formatos.md) |
| Planificación con GitHub Projects | **e)** | [1.6](planificacion.md) |
| Laboratorio logs web AWS (S3, Glue, Athena) | **f)** / **g)** | [1.7](laboratorio-aws.md) (vídeo SharePoint en la misma página) |
| Vídeo ETL en Colab (SharePoint) | **b)** | [Inicio con Python](inicio-python.md) y [1.1](ciclo-analisis.md) |

!!! info "Frontera con BDA"
    El diseño del lago y Pentaho se quedan en BDA. El paquete *Introducción a Big Data* se recupera en [1.0](marco-big-data.md) para no perder el material de Moodle. Aquí la evidencia es **código, consulta y justificación**, no un `.ktr`.
