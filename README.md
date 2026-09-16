# Sistemas de Big Data — UT1 · 2026/2027

IES Ataúlfo Argenta · módulo **5074** · Cantabria · **135 horas y 6 ECTS** (módulo completo).

Esta entrega desarrolla **UT1 (SBD-RA1)**, alineada con la Orden EDU/48/2024, Anexo VI.

- [Apuntes (GitHub Pages)](https://iesataulfoargentasor.github.io/sbd_2026_2027_new/)
- [Cambios curriculares](CAMBIOS_CURRICULARES.md)

## Inicio con Python (cuaderno de arranque)

El eXe *Técnicas de análisis de datos en Big Data* pide consultar **este** Google Colab **antes** de las prácticas del tema (portada del paquete, portada de fundamentos y actividad *Inicio con Python*):

- Alumnado: [https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)
- Solución profesorado: [https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing](https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing)
- Página de los apuntes: [Inicio con Python](https://iesataulfoargentasor.github.io/sbd_2026_2027_new/ut1/inicio-python/)
- Índice de todos los Colab: [Cuadernos](https://iesataulfoargentasor.github.io/sbd_2026_2027_new/ut1/cuadernos/)
- Vídeo de aula (SharePoint, Educantabria): [técnicas de análisis / ETL](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/EeKBcqViPHZMn0uMthdtUJkBkyb1SHk3crRjD2Rrd8gEPQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=b1SA87)
- Vídeo del laboratorio AWS: [S3, Glue y Athena](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/IQA_J2q1KXh9TbFUekUIK95zAY6sW6S5HnwHYyYyzhuF5Rc?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=dsJfm6)

## Desarrollo local

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs build --strict
mkdocs serve
```

GitHub Actions comprueba y publica el sitio en GitHub Pages desde `main`. Las entregas evaluables siguen en Moodle.

## Procedencia

Adaptado a partir de los paquetes eXeLearning de aula de SBD UT1 (licencia [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)), del PDF *Preproceso*, del laboratorio AWS Academy (S3 + Glue + Athena) y de la práctica de planificación con GitHub Projects. Los **cuadernos de Google Colab** de esos eXe están enlazados en los apuntes ([índice](https://iesataulfoargentasor.github.io/sbd_2026_2027_new/ut1/cuadernos/)). Se conserva la apariencia Material del sitio de BDA (paleta, CSS, motor de cuestionario y logo del centro). Los paquetes HTML originales no se publican en este repositorio.

Logotipos y recursos de terceros conservan sus derechos de origen. No se atribuye una licencia nueva a recursos ajenos.
