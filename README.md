# Sistemas de Big Data — UT1 · 2026/2027

IES Ataúlfo Argenta · módulo **5074** · Cantabria · **135 horas y 6 ECTS** (módulo completo).

Esta entrega desarrolla **UT1 (SBD-RA1)**, alineada con la Orden EDU/48/2024, Anexo VI.

- [Apuntes](https://iesataulfoargentasor.github.io/sbd_2026_2027_new/)
- [Cambios curriculares](CAMBIOS_CURRICULARES.md)

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

Adaptado a partir de los paquetes eXeLearning de aula de SBD UT1 (licencia [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)), del PDF *Preproceso*, del laboratorio AWS Academy (S3 + Glue + Athena) y de la práctica de planificación con GitHub Projects. Se conserva la apariencia Material del sitio de BDA (paleta, CSS, motor de cuestionario y logo del centro). Los paquetes HTML originales no se publican en este repositorio.

Logotipos y recursos de terceros conservan sus derechos de origen. No se atribuye una licencia nueva a recursos ajenos.
