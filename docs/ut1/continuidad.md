---
title: "Continuidad con BDA y otros RA de SBD"
tags: [SBD, RA1]
---

# Continuidad con BDA y otros RA de SBD

| Material previo | En esta UT | Continuidad |
| --- | --- | --- |
| BDA-UT1: fuentes, formatos, Pentaho | Reutilizamos el diseño y ampliamos el conjunto sintético | No repetimos el tutorial de Spoon |
| BDA-UT2: Hadoop y sistemas distribuidos | Aplicamos transformaciones sobre fuentes disponibles | Administración y tolerancia a fallos siguen coordinadas con BDA |
| MongoDB del hotel | Lectura programática y cruce de datos | Gestión y programación más amplia en SBD-RA3 |
| Calidad | Comprobamos significado, claves y resultados | BDA-RA3 conserva mecanismos de integridad |
| Tiempo y recursos | Medición de un ensayo | BDA-RA4 desarrolla monitorización sostenida |
| Tablas de resultados | Entregamos información comprobada | Cuadros de mando y visualización en SBD-RA2 y RA4 |
| Análisis empresarial | Definimos y verificamos preguntas | BDA-RA5 conserva su validación de BI |
| Streaming | Primera observación de llegada incremental | Ventanas sencillas aquí; datos tardíos avanzados y flujos complejos después |

Las tecnologías pueden reaparecer cuando cambia la competencia. Se guardan fuentes, esquema, reglas y resultados para no repetir instalaciones sin un objetivo nuevo.

Los datos de esta UT son una extensión sintética del caso didáctico, no una modificación de los ficheros de BDA. Si los módulos avanzan en paralelo, utiliza el paquete autónomo y retoma las conexiones cuando se hayan trabajado en BDA.

[Apuntes BDA](https://iesataulfoargentasor.github.io/bda_2026_2027_new/).

## Frontera de esta ampliación

**CE de referencia:** a–g, como orientación de alcance. **Al terminar:** podrás explicar qué competencia trabajas al reutilizar una tecnología, sin asignarle un módulo únicamente por su nombre.

| Tecnología o problema | Aquí, en SBD-RA1 | Coordinación con BDA |
| --- | --- | --- |
| CSV, JSON, Parquet, Avro, ORC | Lectura, contrato, proyección y coste de consulta | Selección profunda del formato y diseño de almacenamiento |
| Spark | DataFrames/SQL, transformaciones, joins, agregaciones y coste | Despliegue y administración del clúster |
| Datos en movimiento | `readStream`, salidas y ventanas simples | Brokers, réplicas y operación de la plataforma |
| Calidad analítica | Nulos, claves, granularidad y validez del resultado | Integridad, tolerancia a fallos y recuperación de sistemas |
| Eficiencia | Tiempo, memoria, bytes y shuffle de una ejecución | Monitorización continua y dimensionamiento de plataforma |
| Docker | Abrir el entorno suministrado | Manual completo de contenedores y Hadoop |
| AWS | S3 + catálogo + SQL como sistemas integrados | Diseño y operación de infraestructura |

Es un acuerdo didáctico para evitar duplicaciones, no una prohibición tecnológica derivada literalmente de la norma. Otros RA de SBD mantienen su propio alcance; esta actualización solo desarrolla RA1.

!!! example "Comprobación de frontera"
    Clasifica dos tareas: corregir un join que duplica importes y configurar réplicas de un broker. La primera aporta evidencias de integración/calidad aquí; la segunda corresponde al trabajo de plataforma coordinado con BDA.
