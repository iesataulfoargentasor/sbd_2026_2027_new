---
title: "Fuentes y atribución"
tags: [SBD, RA1]
---

# Fuentes y atribución

## Currículo

[Orden EDU/48/2024, Anexo VI](https://boc.cantabria.es/boces/verAnuncioAction.do?idAnuBlob=410716#page=145): SBD 5074, RA1 y criterios a–g. La secuencia, ejemplos y horas orientativas son una propuesta didáctica propia.

## Referencia técnica y didáctica

Aitor Medrano organiza sus [materiales de IABD](https://aitor-medrano.github.io/iabd/index.html) en bloques. Se han consultado como apoyo:

- [Ingeniería de datos](https://aitor-medrano.github.io/iabd/de/de.html).
- [Spark DataFrames y SQL](https://aitor-medrano.github.io/iabd/spark/dataframeAPI.html).
- [Agregaciones y joins](https://aitor-medrano.github.io/iabd/spark/agregaciones.html).
- [Conectividad](https://aitor-medrano.github.io/iabd/spark/catalog.html).
- [MongoDB: agregaciones](https://aitor-medrano.github.io/iabd/sa/agregaciones.html) y [PyMongo](https://aitor-medrano.github.io/iabd/sa/pymongo.html).
- [Streaming](https://aitor-medrano.github.io/iabd/spark/streaming.html).

Su sitio declara licencia CC BY-NC-SA. No se han copiado sus páginas, imágenes ni conjuntos de ejercicios: se han redactado explicaciones y un laboratorio propio sobre el hotel, con correspondencia curricular de Cantabria. Las referencias conservan autoría y licencia de origen.

## Documentación de las herramientas

- [Instalación PySpark 3.5.6](https://spark.apache.org/docs/3.5.6/api/python/getting_started/install.html).
- [Spark SQL](https://spark.apache.org/docs/3.5.6/sql-programming-guide.html).
- [Structured Streaming](https://spark.apache.org/docs/3.5.6/structured-streaming-programming-guide.html).
- [Documentación PyMongo](https://pymongo.readthedocs.io/en/4.10.1/).

## Apariencia y procedencia

Tema Material, CSS, motor de autoevaluación y logotipo procedentes del repositorio del mismo titular [BDA](https://github.com/iesataulfoargentasor/bda_2026_2027_new). Se conserva la atribución IES Ataúlfo Argenta. El logotipo y las dependencias mantienen sus derechos y licencias; no se les asigna otra licencia por incluirlos aquí.

## Materiales docentes internos de referencia

**CE de referencia:** a–g. **Al terminar:** podrás distinguir la autoridad curricular de una fuente técnica y atribuir las ideas utilizadas. La organización en RA y módulos se decide por la Orden EDU/48/2024; las etiquetas de otros materiales no sustituyen esa referencia.

| Material aportado por el docente | Uso en UT1 |
| --- | --- |
| PREPROCESO.pdf | Limpieza → integración → transformación; pandas y equivalentes distribuidos en 1.5, 1.6, 1.8 y 1.11 |
| Introducción a Big Data SBD | Contexto de dato, información y análisis en 1.1 |
| Introducción al procesamiento y análisis de información | Secuencia del análisis y procesamiento en 1.1/1.7 |
| Fundamentos matemáticos y algoritmos | Conjuntos, lógica, relaciones, grafos y coste en 1.2 |
| Técnicas y procesos de extracción de información | Acceso a fuentes y preparación en 1.4/1.5 |
| Formato de Datos SBD | Contratos de lectura y explotación en 1.4/1.11 |
| Planificación de proyectos de análisis de datos con GitHub Projects | Objetivos, dependencias y seguimiento en 1.3 |
| Laboratorio de logs web AWS S3–Glue–Athena | Sistemas, catálogo e incidencia de cabecera, reelaborados en 1.12 |
| Manual para Docker en Big Data | Chuleta auxiliar en entorno; no se incorpora el manual Hadoop |
| Técnicas de Análisis de Datos en Big Data SBD | Se tiene en cuenta su síntesis en la planificación previa; paquete no recuperado en esta revisión |

Los materiales recuperados se han consultado como referencias docentes internas, con ejemplos y redacción nuevos. No se redistribuyen los ZIP eXeLearning ni se copia su secuencia curricular. Se conserva el laboratorio original del repositorio y sus resultados de control.

### Vídeos complementarios

- «Reunión en General», 10/10/2025: apoyo ETL/Colab según la planificación docente; no disponible para revisión directa en esta actualización.
- «Introducción Práctica AWS S3 Glue Athena», 02/12/2025: apoyo al laboratorio 1.12, adjunto recuperado de la conversación; no se ha realizado una transcripción ni análisis audiovisual.

El acceso se mantiene en Moodle o en la ubicación que facilite el profesor. No hay una URL pública verificada para enlazarlos desde estos apuntes. Los vídeos no sustituyen instrucciones escritas ni se añaden como binarios al repositorio.

## Documentación adicional para esta ampliación

- [pandas: combinación de conjuntos](https://pandas.pydata.org/docs/user_guide/merging.html).
- [Spark 3.5.6: lectura CSV](https://spark.apache.org/docs/3.5.6/sql-data-sources-csv.html).
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).
- [Docker Compose](https://docs.docker.com/reference/cli/docker/compose/).
- [Glue: clasificadores](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html).
- [Athena: lector CSV](https://docs.aws.amazon.com/athena/latest/ug/csv-serde.html).
- [Athena: CTAS](https://docs.aws.amazon.com/athena/latest/ug/ctas-examples.html).
- [Athena: optimización de lectura](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).

Revisión de esta ampliación: septiembre de 2026. Spark se mantiene en la versión del laboratorio para reproducibilidad. Las interfaces cloud, permisos y condiciones económicas deben comprobarse en el entorno docente de cada edición.

!!! example "Comprobación de fuentes"
    Justifica un CE citando la norma y una opción de lectura citando la documentación técnica. Explica por qué una etiqueta curricular de un tutorial no cambia la matriz de esta unidad.
