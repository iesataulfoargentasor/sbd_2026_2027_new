---
title: RA1 y criterios de evaluación
tags:
  - SBD
  - RA1
---

# Resultado de aprendizaje 1 (RA1)

Esta unidad desarrolla el **RA1** del módulo *Sistemas de Big Data* (código **5074**), según la [Orden EDU/48/2024, de 8 de octubre, Anexo VI](https://boc.cantabria.es/boces/verAnuncioAction.do?idAnuBlob=410716#page=148) (BOC de 16 de octubre de 2024). Duración del módulo: **135 horas; 6 ECTS**.

## Enunciado

**RA 1:** Aplica técnicas de análisis de datos que integran, procesan y analizan la información, adaptando e implementando sistemas que las utilicen.

## Criterios de evaluación

| CE | Criterio (texto oficial) | Dónde se trabaja en la UT1 |
| --- | --- | --- |
| **a)** | Se han identificado conceptos básicos de matemática discreta, lógica algorítmica y complejidad computacional, y su aplicación para el tratamiento automático de la información por medio de sistemas computacionales. | [1.2 Fundamentos](fundamentos.md) y [modelado](modelado.md) |
| **b)** | Se ha extraído de forma automática información y conocimiento a partir de grandes volúmenes de datos. | [1.1](ciclo-analisis.md), [1.3](extraccion.md) y [1.4](preproceso.md) — [cuadernos](cuadernos.md) |
| **c)** | Se han combinado diferentes fuentes y tipos de datos. | [1.5 Formatos](formatos.md) (y joins en [1.4](preproceso.md)) |
| **d)** | Se ha construido un conjunto de datos complejos y se han relacionado entre sí. | [1.3](extraccion.md) y [1.4](preproceso.md) |
| **e)** | Se han establecido objetivos y prioridades, secuenciación y organización del tiempo de realización. | [1.6 Planificación](planificacion.md) |
| **f)** | Se han seleccionado e integrado sistemas de información que satisfacen las necesidades del problema. | [1.7 Laboratorio AWS](laboratorio-aws.md) |
| **g)** | Se han determinado criterios de coste y calidad necesarios para la eficacia y eficiencia de la implementación de un sistema Big Data. | [1.7](laboratorio-aws.md) y [costes y calidad](costes-calidad.md) |

## Contenidos orientativos del Anexo VI que toca esta UT

Del bloque *Aplicación de técnicas de integración, procesamiento y análisis de información*:

- Conceptos básicos de matemática discreta, lógica algorítmica y complejidad computacional para análisis de datos.
- Técnicas y procesos de extracción de la información de los datos.
- Modelado, razonamiento, resolución de problemas.
- Análisis en tiempo real (reconocer el reloj; el detalle de ventanas queda para más adelante).
- Costes y calidad asociados al proceso de análisis de la información.

El RA2 (cuadros de mando), el RA3 (almacenar para explotar) y el RA4 (visualizar) se retoman después. Aquí el foco es **extraer, limpiar, relacionar, consultar y justificar el sistema**.

!!! note "Cómo se evalúa"
    Los criterios son el referente. En las prácticas se pide **ejecutar** (pandas, SQL en Athena) y **explicar** (por qué esa fuente, ese formato, ese servicio). Las entregas formales siguen en Moodle.

    Para practicar por tu cuenta: [cuadernos Colab](cuadernos.md) y [autoevaluación de la UT1](autoevaluacion.md).

## Evidencias que cierran RA1

| CE | Evidencia observable |
| --- | --- |
| a | Explicar con un ejemplo por qué un algoritmo O(n²) no vale para millones de filas, y aplicar una operación de conjuntos o un filtro lógico ([1.2](fundamentos.md); vocabulario en [1.0](marco-big-data.md)). |
| b | Extraer de CSV/API (o SQL) y producir un resumen (conteo, máximo, filtro) sin copiar a mano. |
| c | Justificar CSV frente a Parquet/Avro según si vas a **leer tres columnas** o a **pasar mensajes**. |
| d | Unir o concatenar al menos dos fuentes y dejar un dataset coherente (claves, duplicados, tipos). |
| e | Tablero con objetivo, tareas esenciales/deseables y un mini-sprint (GitHub Project o equivalente). |
| f | Cadena S3 → Glue (catálogo) → Athena que responde a una pregunta de negocio. |
| g | Criterio de coste (dato escaneado, formato, cabecera reconocida) y de calidad (esquema, no `col1`…`col5`). |

La [coordinación con BDA](continuidad.md) evita repetir el diseño del almacén. SBD no sustituye a BDA-RA1: lo **usa**.
