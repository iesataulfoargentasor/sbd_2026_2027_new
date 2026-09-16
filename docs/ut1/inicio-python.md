---
title: Inicio con Python
tags:
  - SBD
  - RA1
  - Colab
---

# Inicio con Python (cuaderno de arranque)

Este es el Google Colab que el eXe *Técnicas de análisis de datos en Big Data* (y el de *Introducción al procesamiento*) pide **consultar antes** de cualquier práctica del tema.

En la portada del eXe aparece así: *«Para poder realizar las prácticas o ejemplos prácticos que se mencionan en este tema, te sugiero que antes consultes este GoogleColab»*. El mismo enlace se repite al abrir *Fundamentos matemáticos y algorítmicos* y en la actividad 6 (*Inicio con Python*).

## Cuaderno del alumnado

**[Abrir Inicio con Python en Google Colab](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)**

`https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing`

Cópialo a tu Drive (Archivo → Guardar una copia) con la cuenta de Educantabria o la que indique el profesor. No edites el original compartido.

## Qué se hace en ese cuaderno

Es un **flujo ETL mínimo** en Python (pandas), no un tutorial genérico de sintaxis:

1. Se genera un CSV de clientes con errores (fechas mezcladas, duplicados, valores faltantes).
2. **Extracción:** abrir y leer el fichero.
3. **Transformación:** unificar fechas, eliminar duplicados, corregir erratas.
4. **Carga:** guardar un CSV limpio.
5. Recuento: clientes por ciudad y edad media.

Eso convierte dato bruto en información útil. La evidencia no es “haber abierto Colab”: es el fichero limpio y el resumen.

La teoría que envuelve esta práctica (valor del dato, ETL, batch/streaming, descriptivo/predictivo/prescriptivo) está en [1.1 Integrar, procesar y analizar](ciclo-analisis.md).

## Vídeo de aula (Moodle / SharePoint)

El eXe *Técnicas de análisis de datos en Big Data* se acompaña de esta grabación (cuenta Educantabria):

**[Vídeo: técnicas de análisis y ETL en Colab](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/EeKBcqViPHZMn0uMthdtUJkBkyb1SHk3crRjD2Rrd8gEPQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=b1SA87)**

## Solución de referencia (profesorado)

Página *Solución Profesor* del mismo eXe. Úsala **después** de intentar el cuaderno, o en corrección.

**[Solución profesorado](https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing)**

`https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing`

El resto de cuadernos de la unidad (fundamentos, extracción, Avro…) está en [Cuadernos Colab](cuadernos.md).
