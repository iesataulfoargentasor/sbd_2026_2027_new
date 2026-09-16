---
title: Costes y calidad
tags:
  - SBD
  - RA1
---

# Costes y calidad del análisis

Este apartado trabaja el criterio **g)**. El [laboratorio AWS](laboratorio-aws.md) lo concreta: Athena cobra por **dato escaneado** y Glue tiene que reconocer la cabecera.

## Coste

No es solo la factura del cloud:

- Infraestructura: on-prem (amortizas máquinas) frente a nube (pagas uso).
- Almacenamiento y **retención** (cuánto tiempo guardas el log).
- CPU, red, shuffle.
- Licencias frente a software libre.
- Personas (el 80 % del tiempo en limpiar también es coste).

Orden de magnitud de catálogo (cambia; el procedimiento no): 1 TB en objeto barato puede estar en torno a **20–25 €/mes**. En Athena el coste malo es **releer un CSV enorme** cada lunes.

## Calidad

| Dimensión | Pregunta |
| --- | --- |
| Exactitud | ¿El valor es el verdadero? |
| Completitud | ¿Cuántos nulos? |
| Consistencia | ¿`Madird` y `Madrid` son la misma ciudad? |
| Actualidad | ¿El dato es de hoy o de 2019? |
| Relevancia | ¿Esta columna responde a la pregunta? |

Una aerolínea con retrasos mal tipados **inventa** puntualidad. El fallo `col1`…`col5` del crawler es calidad de **esquema**.

## Actividades

1. Sobre un CSV de ~1 000 filas (o [clientes_actividad.csv](../assets/practicas/clientes_actividad.csv)): estima % de nulos, duplicados y erratas; di qué dimensión duele.
2. Sobre el papel: 100 GB on-prem frente a S3 + Athena. ¿Qué cambia si consultas tres columnas cada día? (Puente con [1.5](formatos.md): Parquet.)

!!! success "g) en un párrafo"
    Coste = formato + dato escaneado + retención. Calidad = esquema reconocido + nulos/duplicados documentados. No hace falta un presupuesto de empresa.
