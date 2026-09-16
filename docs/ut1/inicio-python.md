---
title: Inicio con Python
tags:
  - SBD
  - RA1
  - Colab
---

# Inicio con Python (cuaderno de arranque)

Consulta este cuaderno de Google Colab **antes** de realizar las prácticas del tema.

## Cuaderno del alumnado

**[Abrir Inicio con Python en Google Colab](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)**

`https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing`

Cópialo a tu Drive (Archivo → Guardar una copia) con la cuenta de Educantabria o la que indique el profesor. No edites el original compartido.

## Qué se hace en ese cuaderno

El cuaderno se titula **Curso básico de Python para Big Data (Google Colab)**. Combina explicaciones con ejemplos de código para preparar las prácticas de la unidad.

1. **Variables y tipos básicos:** enteros, decimales, cadenas, booleanos y operaciones numéricas.
2. **Colecciones:** listas, tuplas, diccionarios y conjuntos.
3. **Control del programa:** condicionales `if/else` y bucles `for` y `while`.
4. **Funciones:** definirlas, pasar argumentos y reutilizar cálculos.
5. **Librerías:** primeros ejemplos con `math`, `random`, NumPy, pandas y Matplotlib.
6. **Ampliación:** arrays y matrices con NumPy; selección de columnas, filtros y estadísticas con pandas; gráficos de líneas y barras con Matplotlib.

Ejecuta las celdas en orden, modifica algunos valores y comprueba cómo cambia el resultado. Al terminar, deberías poder explicar un filtro de pandas, calcular una media y reconocer cómo se construye un gráfico sencillo.

## Siguiente paso: práctica ETL de clientes

Con esa base, pasa a la [actividad ETL de 1.1 Integrar, procesar y analizar](ciclo-analisis.md). Allí trabajarás la extracción, limpieza, carga y análisis de datos de clientes en un cuaderno propio.

El **cuaderno resuelto de ETL** enlazado más abajo corresponde a esa actividad posterior. Parte de datos de clientes simulados en un diccionario de Python, los convierte en un DataFrame, elimina duplicados, trata valores faltantes y formatos, guarda `clientes_limpio.csv` y calcula clientes por ciudad y edad media.

## Vídeo de aula (Moodle / SharePoint)

Esta grabación acompaña la práctica posterior de análisis y ETL (cuenta Educantabria):

**[Vídeo: técnicas de análisis y ETL en Colab](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/EeKBcqViPHZMn0uMthdtUJkBkyb1SHk3crRjD2Rrd8gEPQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=b1SA87)**

## Solución de referencia: ETL de clientes (profesorado)

Este segundo cuaderno se titula **RESUMEN DEL PROCESO ETL COMPLETADO**. Úsalo **después** de intentar la actividad ETL de clientes, o durante su corrección. No es una solución de los ejemplos del curso básico de Python.

**[Abrir el ETL de clientes resuelto](https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing)**

`https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing`

El resto de cuadernos de la unidad (fundamentos, extracción, Avro…) está en [Cuadernos Colab](cuadernos.md).
