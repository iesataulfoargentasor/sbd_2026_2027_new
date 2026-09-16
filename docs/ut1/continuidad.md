---
title: Continuidad con BDA y RA2–RA4
tags:
  - SBD
  - RA1
---

# Continuidad con BDA y con el resto de SBD

La frontera no es el logo. Hadoop, Spark, Kafka o AWS pueden aparecer en BDA y en SBD. Cambia **la competencia**.

| Tema | BDA (diseñar / operar el sistema) | SBD UT1 (esta unidad) | Después en SBD |
| --- | --- | --- | --- |
| 5 V, lake, warehouse | Caracterizar el problema y el almacén | Recuperas el vocabulario, no lo reimpartes | — |
| Ingesta / ETL | Procedimiento y PDI | pandas / API / SQL: **transformar** de verdad | Flume, Sqoop, pipelines de RA3 |
| Formatos | Elegir la carga | Leer, convertir, coste de escaneo | Particionado y motores de RA3 |
| Procesamiento | Etapa del pipeline; lote vs flujo | Extraer conocimiento; complejidad | Ventanas, streaming, Spark a fondo (RA4 e) |
| Presentación | Tabla clara al cliente | Consulta Athena / resumen pandas | Cuadros de mando (RA2) y visualización (RA4) |
| Cloud | Destino posible (S3, Glue) | Integrar S3+Glue+Athena y hablar de coste | Otros servicios según el RA |

## Qué guardas al terminar UT1

1. CSV originales y el limpio (clientes, logs).
2. Notebook o script de extracción y preproceso.
3. Tablero de GitHub Project (objetivo y prioridades).
4. Capturas Athena + párrafo de coste/calidad.
5. Parquet de prueba, si lo generaste.
6. Copias en Drive de los Colab que hayas ejecutado ([índice](cuadernos.md)).

RA2 parte de **indicadores y gráficos** sobre esos datasets. RA3 profundiza en importar y almacenar para explotar. RA4, en visualizar y en programar transformaciones con más recorrido.

## Proyecto integrador (anexo Word Tema 7)

El eXe combinado cierra UT1 con un pipeline opcional (invernadero u otro caso): objetivo → ETL → modelo → streaming o micro-lotes → almacén → Grafana → informe de coste/calidad → presentación de 10 min. Cubre **a)–g)**. En esta entrega se reconoce el mapa; la evidencia mínima de RA1 sigue siendo pandas + Athena + tablero, no un invernadero Kafka obligatorio.
