---
title: "RA1 y criterios de evaluación"
tags: [SBD, RA1]
---

# RA1 y criterios de evaluación

La referencia es la [Orden EDU/48/2024, Anexo VI, páginas 145–147 del PDF](https://boc.cantabria.es/boces/verAnuncioAction.do?idAnuBlob=410716#page=145). El módulo 5074 tiene 135 horas y 6 ECTS.

## Resultado de aprendizaje

**Aplica técnicas de análisis de datos que integran, procesan y analizan la información, adaptando e implementando sistemas que las utilicen.**

| CE | Texto oficial | Evidencia en esta unidad |
| --- | --- | --- |
| a | Se han identificado conceptos básicos de matemática discreta, lógica algorítmica y complejidad computacional, y su aplicación para el tratamiento automático de la información por medio de sistemas computacionales. | [1.2 Fundamentos](fundamentos.md) y [1.7 Spark](spark.md): conjuntos, grafo, predicado y comparación ejecutada de algoritmos |
| b | Se ha extraído de forma automática información y conocimiento a partir de grandes volúmenes de datos. | [1.4 Extracción](fuentes.md), [1.7–1.9](analisis.md) y [1.10 Flujo](streaming.md): código, indicadores y ensayo ampliado con volumen real medido |
| c | Se han combinado diferentes fuentes y tipos de datos. | [1.4 Fuentes](fuentes.md), [1.6 Integración](integracion.md) y [1.8 Escala](transformaciones-escala.md): CSV, catálogo, opiniones y eventos JSON |
| d | Se ha construido un conjunto de datos complejos y se han relacionado entre sí. | [1.5 Preparación](preproceso.md) y [1.6 Integración](integracion.md): diccionario, claves, cardinalidades y conjunto complejo comprobado |
| e | Se han establecido objetivos y prioridades, secuenciación y organización del tiempo de realización. | [1.3 Planificación](planificacion.md): Issues/Project, objetivos, prioridades, dependencias, estimaciones y revisiones durante el trabajo |
| f | Se han seleccionado e integrado sistemas de información que satisfacen las necesidades del problema. | [1.4 Fuentes](fuentes.md), [1.6 Integración](integracion.md) y [1.12 AWS](aws-s3-glue-athena.md): sistemas elegidos, contrato e integración ejecutada en el entorno asignado |
| g | Se han determinado criterios de coste y calidad necesarios para la eficacia y eficiencia de la implementación de un sistema Big Data. | [1.11 Mediciones](coste-calidad.md), [1.8 Escala](transformaciones-escala.md) y [1.12 AWS](aws-s3-glue-athena.md): calidad, tiempos, memoria, bytes y decisión justificada |

## Cómo se concreta

El bloque oficial incluye fundamentos matemáticos y algorítmicos, extracción de información, modelado y resolución de problemas, análisis en tiempo real y costes/calidad. Las herramientas seleccionadas son nuestra concreción didáctica; no están asignadas de forma exclusiva a un RA por su marca.

Para CE b habrá dos niveles: muestra comprobable y volumen ampliado en el entorno acordado con el profesor. Registra filas, bytes, recursos y tiempo. El fichero mínimo de seis reservas **no acredita por sí solo** trabajo con grandes volúmenes. El profesor concretará el ensayo de escala según los equipos del centro.

El test sirve para estudiar; las entregas evaluables se indican en Moodle. La [práctica](practica.md) reúne los siete criterios.

## Leer la matriz como guía de trabajo

**CE que se trabajan:** a–g. **Al terminar:** podrás localizar el texto curricular y asociar cada criterio con una evidencia concreta de tu proyecto. Los CE oficiales de la tabla se conservan; las páginas y evidencias son una concreción didáctica, no una modificación de la norma.

La [práctica 1.13](practica.md) reúne las evidencias. Docker es apoyo de entorno y no tiene calificación curricular propia en RA1. Una demostración AWS o local debe identificarse como tal: no equivale a una integración cloud realizada por el alumno. La modalidad concreta se acuerda con el profesor sin perder la exigencia de seleccionar e integrar sistemas del CE f.

!!! example "Comprobación curricular"
    Elige un archivo de tu entrega para cada CE y explica qué demuestra. Si un criterio solo apunta a una captura o a una definición memorizada, añade ejecución, razonamiento o seguimiento según corresponda.
