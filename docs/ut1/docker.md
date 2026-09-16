---
title: Entorno Docker
tags:
  - SBD
---

# Entorno Docker (apoyo)

Docker **no** es un criterio del RA1. Es la forma habitual de **reproducir** un entorno de datos: misma versión de Python, mismo motor, en el portátil del aula y en el del compañero.

En BDA ya viste contenedores para Hadoop o Mongo si el profesorado los usó. Aquí basta lo mínimo para no pelearte con “en mi máquina funciona”.

## Qué problema resuelve

Instalar pandas, Java, un cliente de AWS y tres versiones de Python en el sistema del centro termina en conflictos. Un **contenedor** empaqueta la receta. Un **Compose** levanta varias piezas con un fichero.

## Ideas que sí debes manejar

| Concepto | En una frase |
| --- | --- |
| Imagen | La receta (`python:3.12-slim`) |
| Contenedor | La receta **en marcha** |
| Volumen | Carpeta del host montada (tus CSV) |
| Puerto | Cómo entras desde el navegador |
| Compose | Varios servicios descritos juntos |

No memorices flags. Sí: **no guardes secretos** (claves AWS) en la imagen ni en el `compose` que subes a Moodle.

## Flujo mínimo para esta UT

Para pandas y el generador de logs, un venv local basta:

```sh
python -m venv .venv
source .venv/bin/activate
pip install pandas pyarrow faker
```

Usa Docker cuando el profesor entregue un `compose.yaml` (laboratorio, Spark local, etc.). El manual de aula *Manual para Docker en Big Data* permanece en Moodle como referencia de capturas; no se duplica aquí.

!!! tip "Criterio f), sin marear"
    Elegir S3 + Glue + Athena **es** integrar sistemas. Elegir Docker es **cómo** ejecutas el cliente. No los mezcles en la misma frase de examen como si fueran el mismo oficio.
