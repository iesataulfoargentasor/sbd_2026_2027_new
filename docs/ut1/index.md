---
title: "U.T. 1. Integración, procesamiento y análisis de datos"
tags: [SBD, RA1]
---

# U.T. 1. Integración, procesamiento y análisis de datos

El grupo hotelero quiere conocer sus reservas y cancelaciones por hotel y canal. Tiene CSV, catálogos y eventos JSON, pero todavía no dispone de una respuesta fiable. Una suma puede ser correcta y responder a una pregunta equivocada: primero definiremos qué cuenta cada registro.

## Lo que aprenderás

Al terminar podrás formular una pregunta, planificar tareas, combinar fuentes, ejecutar un análisis automático y justificar su calidad y coste. La unidad desarrolla [SBD-RA1](ra1.md), con **58 horas orientativas**, ajustables por el profesor.

| Recorrido | Resultado | Horas orientativas |
| --- | --- | ---: |
| [1.1 Del dato al problema de análisis](problema.md) | Preguntas e indicadores | 2 |
| [1.2 Fundamentos matemáticos y algorítmicos](fundamentos.md) | Relaciones, lógica y comparación de algoritmos | 6 |
| [1.3 Planificación del proyecto de análisis](planificacion.md) | Issues, prioridades y seguimiento | 3 |
| [1.4 Fuentes y extracción de información](fuentes.md) | Contrato y extracción de fuentes | 4 |
| [1.5 Preparación y calidad de datos](preproceso.md) | Reglas y controles con pandas | 5 |
| [1.6 Integración de datos](integracion.md) | Conjunto con claves y granularidad verificadas | 5 |
| [1.7 Procesamiento distribuido con Spark](spark.md) | DataFrames, acciones y SQL | 6 |
| [1.8 Transformaciones a escala](transformaciones-escala.md) | Lectura, ventanas y joins distribuidos | 5 |
| [1.9 Extracción automática de información](analisis.md) | Indicadores y conocimiento contrastado | 4 |
| [1.10 Procesamiento de datos en tiempo real](streaming.md) | Flujo y ventanas sencillas | 4 |
| [1.11 Coste, calidad y eficiencia](coste-calidad.md) | Comparaciones y decisiones medidas | 3 |
| [1.12 Laboratorio AWS S3–Glue–Athena](aws-s3-glue-athena.md) | Integración de sistemas y coste de consulta | 4 |
| [1.13 Práctica integradora RA1](practica.md) | Proyecto reproducible y defensa | 7 |
| **Total** | **Incluye prácticas, comprobaciones y defensa** | **58** |

Esta distribución de unas **55–60 horas** es una estimación didáctica ajustable, no una carga oficial fija asignada a UT1. La planificación se inicia en 1.3 y se revisa durante todo el proyecto; la práctica integradora reutiliza las evidencias de los bloques anteriores.

## Antes de empezar

Necesitas funciones, listas y diccionarios en Python; selección y agrupación en SQL; y saber distinguir CSV y JSON. Prueba a explicar `len`, una condición `and`, una clave y un `JOIN`. Si alguno no te resulta familiar, trabaja primero los ejemplos de fundamentos con el profesor.

Descarga el [laboratorio completo](entorno.md). Cada apartado contiene explicación, ejemplo, ejercicio y comprobación. El pequeño conjunto tiene resultados calculables a mano; la ampliación permite observar costes. Una ejecución local no acredita distribución entre máquinas.

## Cómo seguir el recorrido

**CE que se trabajan:** a–g, con trazabilidad en [RA1](ra1.md). Los conceptos de preparación e integración se trabajan primero con pandas y se retoman con Spark. Los ejemplos Spark de integración se ejecutan después de 1.7; no necesitas conocer Spark para comenzar 1.6.

Sigue la [autoevaluación](autoevaluacion.md) para localizar lagunas y consulta la [continuidad con BDA](continuidad.md) para separar competencias. El [entorno](entorno.md) es auxiliar. Las [referencias](referencias.md) distinguen currículo, materiales docentes y documentación técnica.

!!! example "Comprobación inicial"
    Describe qué representa una reserva y qué representa un evento. Señala una pregunta que puedas responder con estas fuentes y otra para la que falten datos. Conserva la respuesta para revisarla al terminar la unidad.
