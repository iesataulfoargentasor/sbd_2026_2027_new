---
title: Cuadernos de Google Colab
tags:
  - SBD
  - RA1
---

# Cuadernos de Google Colab de la UT1

Abre los cuadernos con la cuenta de Educantabria (o la que indique el profesor). Si Colab pide “hacer una copia”, **cópialo a tu Drive** antes de ejecutar.

La [autoevaluación](autoevaluacion.md) no sustituye estos cuadernos. Las entregas formales siguen en Moodle.

## Primero: Inicio con Python

Consulta este cuaderno antes de las prácticas de análisis y fundamentos. Página dedicada: [Inicio con Python](inicio-python.md).

**[https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)**

## Ejemplos y actividades para el alumnado

Los cuadernos combinan demostraciones resueltas y ejercicios. La columna «Cómo trabajarlo» indica qué se espera en cada caso. Las actividades adicionales de los apuntes pueden pedir pasos que debes añadir en tu copia.

| Tema | Cuaderno | Contenido | Cómo trabajarlo |
| --- | --- | --- | --- |
| Introducción | [Inicio con Python](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing) | Variables, colecciones, bucles, funciones y ejemplos con NumPy, pandas y Matplotlib. | Ejemplos explicados; ejecutar y modificar. |
| Fundamentos | [Matemática discreta aplicada a Big Data](https://colab.research.google.com/drive/1LZkMTdbtTa_XFnw_9ZzDI0HUoFlr0lpl?usp=sharing) | Conjuntos, relaciones, funciones, lógica, grafos, combinatoria, suma modular, cifrado César y estructuras. | Ejemplos resueltos. |
| Fundamentos | [Tipos de datos y fundamentos en Python](https://colab.research.google.com/drive/1zLLp2cZTXoTCLczo8ibElVPZX7eIZEPx?usp=sharing) | Tipos, mutabilidad, JSON y ejemplos matemáticos; termina con tres actividades de conjuntos, matriz y complejidad. | Repaso y actividades por completar; incluye un árbol de clasificación como ampliación. |
| Fundamentos | [Combinatoria con menús](https://colab.research.google.com/drive/1lOe3pA0-L7iGGNWAmDtZwt1ZxXv4L-zO?usp=sharing) | Producto cartesiano de entrantes y principales; pares de platos con y sin orden. | Ejemplos resueltos con `itertools`. |
| Fundamentos | [Miniproyecto de compras y relaciones entre productos](https://colab.research.google.com/drive/1YYxgnXcdUw0_qgwGdYeGwvOjxh-dLlsj?usp=sharing) | Repaso de matemática discreta y proyecto con compras simuladas, grafo de co-compra, clientes VIP y gráficos. | Ejemplo integrador resuelto; modificar e interpretar. |
| Fundamentos | [Big-O: teoría y curvas de crecimiento](https://colab.research.google.com/drive/1InYuv7O8DWM0g4mFHRIpw3-LGPrfYlxu?usp=sharing) | Tabla de complejidades y gráfico de O(1), O(log n), O(n) y O(n²). | Ilustración teórica; no mide tiempos de algoritmos. |
| Fundamentos | [Búsquedas, memoria y alternativa con Dask](https://colab.research.google.com/drive/1QMJKYknyyv_-pyOQ5WaNdqCZZ2u8KyPS?usp=sharing) | Búsquedas lineal, binaria y hash; prueba de agotamiento de RAM, liberación de colecciones y ejemplo Dask. | Demostración guiada; reducir tamaños antes de ejecutar ([indicaciones](fundamentos.md#cuadernos-de-complejidad)). |
| Fundamentos | [Búsquedas en listas, conjuntos y diccionarios](https://colab.research.google.com/drive/1mZfjK-IH2qmyKHnUe2LU6kiarKepmveX?usp=sharing) | Compara tiempos de búsqueda lineal, binaria y pertenencia en `set` y `dict`. | Ejemplos con tamaños grandes; reducirlos antes de ejecutar ([indicaciones](fundamentos.md#cuadernos-de-complejidad)). |
| Fundamentos | [Vectores, matrices, decisiones y estructuras](https://colab.research.google.com/drive/1W1yXeDfUYtK2BtPVmWIHRrnu7oD1EihK?usp=sharing) | Temperaturas, notas, compras, reglas VIP, árbol DFS, grafo social y búsquedas hash. | Ejemplos y mini-ejercicios con celdas por completar. |
| Fundamentos | [Logística: cuaderno de actividades](https://colab.research.google.com/drive/1cWbe73qRxhDEDg5FCM-Fdwj8GvIVLj58?usp=sharing) | Centros, camiones, rutas y pedidos; conjuntos, relaciones, tarifas, prioridades y grafos. | Ejemplos base y seis tareas con `TU CÓDIGO AQUÍ`. |
| Extracción | [Filtrar clientes de Madrid mayores de 30](https://colab.research.google.com/drive/1CPaRcZNcPMXLAwHdfv6KEuQpBUz1G1j_?usp=sharing) | Lee `clientes.csv` desde GitHub y aplica `ciudad == "Madrid"` y `edad > 30`. | Ejemplo resuelto; muestra las filas filtradas, sin limpieza ni ordenación. |
| Extracción | [Open-Meteo: temperatura horaria de Castro Urdiales](https://colab.research.google.com/drive/13w9YOpfMhjh49lAb3UY2MOpfw_UVrA1H?usp=sharing) | Consulta un día de temperatura horaria, con caché y reintentos, y muestra un DataFrame con fechas UTC. | Ejemplo base; la actividad añade máxima, mínima, interpretación y adaptación a Santander. |
| Extracción | [Extracción y preparación: ejemplos y actividades](https://colab.research.google.com/drive/1JvpH-IoMbgZzOoRdAXq2zTusWKUXLk74?usp=sharing) | CSV/Excel, limpieza, APIs reales y simuladas, scraping, integración y análisis de opiniones. | Cuaderno extenso con ejemplos resueltos y actividades; [guía de lectura](extraccion.md#cuaderno-general-de-extraccion). |
| Formatos | [Avro: escritura y lectura de empleados](https://colab.research.google.com/drive/1zxfPwEdHjaYHjkKjPOwXuj9fXGD8Anc1?usp=sharing) | Instala `avro`, lee `empleado.avsc`, escribe dos empleados y recupera registros y esquema. | Ejemplo resuelto; subir primero el esquema local enlazado en [formatos](formatos.md). |
| Formatos | [Fastavro: escritura y lectura de empleados](https://colab.research.google.com/drive/1z0ZsCX2Ws-3kSFLQEJS74CDkkot--Y-n?usp=sharing) | Mismo dataset y esquema con `fastavro`; escribe `empleadosf.avro` y lo lee. | Ejemplo resuelto; no incluye medición comparativa de velocidad. |
| Formatos | [Pandas y fastavro: ventas de Alemania](https://colab.research.google.com/drive/1zaM4132cmUIsOWL5rbiCre5dCIyVL1RC?usp=sharing) | Lee `pdi_sales.csv`, recorta espacios de `Zip`, filtra Alemania y escribe `sales.avro`. | Ejemplo resuelto y celda final de ejercicio; requiere subir el CSV. |

Datos de apoyo en GitHub de aula:

- [clientes.csv](https://raw.githubusercontent.com/josedavidmi/iabd-sbd/refs/heads/main/clientes.csv) (copia local: [clientes.csv](../assets/practicas/clientes.csv))
- [clientes_actividad.csv](https://raw.githubusercontent.com/josedavidmi/iabd-sbd/refs/heads/main/clientes_actividad.csv) (copia local: [clientes_actividad.csv](../assets/practicas/clientes_actividad.csv))

## Solución de referencia (profesorado)

Estos cuadernos contienen las soluciones del profesor. Úsalos **después** de intentar el cuaderno de alumnado, o en corrección.

| Tema | Cuaderno |
| --- | --- |
| Datos simulados en un diccionario, limpieza, exportación a CSV y métricas de clientes. Referencia para la actividad de [1.1](ciclo-analisis.md); la lectura de un CSV de entrada debe añadirse. | [ETL de clientes resuelto](https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing) |
| Conjuntos y premium, matriz de compras 4×3, doce menús y regla de descuento. Soluciones de las cuatro actividades de [fundamentos](fundamentos.md#actividades-hacer-en-colab). | [Cuatro actividades resueltas de fundamentos](https://colab.research.google.com/drive/14PapYsQgCl1E8a2Nm1mKHrGNOTQ14dVd?usp=sharing) |
| Mismo escenario logístico, con las seis tareas completadas. Comparar con el cuaderno de logística del alumnado después de intentarlo. | [Logística: tareas resueltas](https://colab.research.google.com/drive/1H0_0yrT77FVNvCoxepL4bRy-dHlhf6ij?usp=sharing) |
| Formatos (Kaggle, profesorado) | [fork-of-trabajo-actividad-de-formato-de-datos](https://www.kaggle.com/code/dmiprof01/fork-of-trabajo-actividad-de-formato-de-datos) |

El índice de cada apartado enlaza el mismo cuaderno junto a la teoría, para no tener que volver aquí.

## Vídeos de aula

Hace falta la cuenta de Educantabria. Los de YouTube son públicos; los de SharePoint son los de Moodle.

| Tema | Recurso |
| --- | --- |
| Técnicas de análisis / ETL en Colab | [SharePoint (Educantabria)](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/EeKBcqViPHZMn0uMthdtUJkBkyb1SHk3crRjD2Rrd8gEPQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=b1SA87) · [página Inicio con Python](inicio-python.md) |
| Laboratorio AWS (S3, Glue, Athena) | [SharePoint (Educantabria)](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/IQA_J2q1KXh9TbFUekUIK95zAY6sW6S5HnwHYyYyzhuF5Rc?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=dsJfm6) · [1.7 Laboratorio](laboratorio-aws.md) |
| Formato de datos | [Avro, Parquet y ORC (YouTube)](https://youtu.be/DafzYp5XRmA) |
| GitHub Projects | [Issues en GitHub (YouTube)](https://youtu.be/7eeHBaPnUGM) · [1.6 Planificación](planificacion.md) |
| Manual Docker | [Hadoop con Docker (YouTube)](https://youtu.be/f6FJ91f-qpA) |

## Datos de apoyo (fuera de este repo)

- [pdi_sales.csv](https://aitor-medrano.github.io/iabd/de/resources/pdi_sales.csv) — ventas para el tercer cuaderno Avro (separador `;`)
- [empleado.avsc](https://aitor-medrano.github.io/iabd/de/resources/empleado.avsc) — esquema Avro (copia local: [empleado.avsc](../assets/practicas/empleado.avsc))
- [Kaggle: retrasos de vuelos 2009–2018](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018) — actividad de [1.5](formatos.md)
