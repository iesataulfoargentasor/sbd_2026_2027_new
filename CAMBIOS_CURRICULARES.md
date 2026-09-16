# Adaptación curricular de SBD UT1

## Referencia y alcance

Orden EDU/48/2024, de 8 de octubre, Anexo VI: módulo **5074 Sistemas de Big Data**, **135 horas y 6 ECTS**. Las horas corresponden al módulo completo. Fuente: [BOC](https://boc.cantabria.es/boces/verAnuncioAction.do?idAnuBlob=410716#page=148).

Esta entrega desarrolla exclusivamente **UT1 / SBD-RA1** (siete CE). El resto de RA de SBD y el módulo BDA (5075) se coordinan, no se duplican.

## Correspondencia con Moodle

La asociación eXeLearning/PDF → CE se conserva. Los paquetes HTML, vídeos y el ZIP de Docker **no** entran en el repositorio.

| Material de aula | CE | Página |
| --- | --- | --- |
| Introducción a Big Data SBD | vocabulario | `docs/ut1/marco-big-data.md` |
| Introducción al procesamiento y análisis | b | `docs/ut1/ciclo-analisis.md` |
| Técnicas de análisis de datos en Big Data (eXe combinado + vídeo) | a, b | `docs/ut1/inicio-python.md`, 1.1, 1.2 y `docs/ut1/cuadernos.md` |
| Fundamentos matemáticos y algoritmos | a | `docs/ut1/fundamentos.md` |
| Técnicas y procesos de extracción | b, d | `docs/ut1/extraccion.md` |
| Preproceso (PDF) | b, d | `docs/ut1/preproceso.md` |
| Formato de datos SBD | c | `docs/ut1/formatos.md` |
| Planificación con GitHub Projects | e | `docs/ut1/planificacion.md` |
| Laboratorio AWS S3/Glue/Athena | f, g | `docs/ut1/laboratorio-aws.md` |
| Manual Docker | apoyo | `docs/ut1/docker.md` |
| Vídeo ETL Colab | b | integrado en 1.1 y 1.3 |
| Todos los Colab de los eXe | prácticas | `docs/ut1/cuadernos.md` (y enlaces en cada apartado) |

## Decisiones didácticas

- Estilo y tema copiados del sitio de BDA (Material, paleta del centro, motor de test).
- Frontera: BDA diseña el almacén y PDI; SBD ejecuta pandas, API, SQL Athena y justifica coste/calidad. El paquete *Introducción a Big Data* se publica como 1.0 (marco), no como copia del diseño de BDA.
- Manual Docker: chuleta + actividad Hadoop + vídeo (ZIP de Moodle no entra en git).
- Anexos Word del eXe combinado (Temas 4–7): modelado, tiempo real, costes/calidad y proyecto integrador.
- Preproceso Spark se presenta como reconocimiento, no como laboratorio obligatorio de clúster.
- El fallo `col1`…`col5` del crawler se documenta con classifier `Contains header: PRESENT`.
- Autoevaluación: 20 preguntas. Entregas en Moodle.

## Validación

- `mkdocs build --strict` debe completar en local y en GitHub Actions.
- Los CSV de clientes son de juguete y están contrastados a ojo (duplicados y erratas a propósito).
- El script `generar_logs.py` requiere `faker` en el equipo del alumnado. No se ha ejecutado aquí el laboratorio AWS Academy.

Los apuntes eXe de partida se declaran [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Se mantiene esa atribución en las adaptaciones de dichos contenidos.
