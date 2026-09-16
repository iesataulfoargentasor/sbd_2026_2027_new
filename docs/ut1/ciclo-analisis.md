---
title: 1.1 Integrar, procesar y analizar
tags:
  - SBD
  - RA1
---

# 1.1. Integrar, procesar y analizar

Un dato **aislado** no vale. Cada clic, cada reserva, cada lectura de un sensor solo se convierte en decisión cuando se **integra** con otros, se **procesa** y se **analiza**.

Eso es el criterio **b)** empezando a trabajar: extraer información y conocimiento de volúmenes que no vas a leer a ojo.

!!! example "Un clic no vale nada solo"
    - **Dato bruto:** «Usuario X hizo clic en un anuncio a las 13:04».
    - **Información:** «El 60 % de los clics ocurre después de las 13:00».
    - **Conocimiento:** «Conviene publicar anuncios por la tarde».

En el hotel de BDA el mismo viaje llega hasta el **valor** (menos habitaciones vacías). Aquí te quedas en el oficio de **producir esa información**: código, consulta, dataset limpio.

## Integración de datos

**Integrar** es combinar fuentes distintas hasta una visión coherente.

Una empresa de logística puede tener la base de clientes, el GPS de los camiones y el registro del almacén. Juntos responden: *qué cliente recibió el pedido, por qué ruta pasó y cuánto tardó*. El hotel hace lo mismo con reservas, cobros y catálogo.

### El proceso ETL

El método más habitual sigue tres verbos. Las siglas **ETL** (extraer → transformar → cargar) solo recuerdan el orden.

1. **Extract.** Lees el origen: tabla SQL, CSV, API, log.
2. **Transform.** Unificas fechas, quitas duplicados, cruzas claves, corriges `Madird` → `Madrid`.
3. **Load.** Dejas el resultado en un sitio consultable (otro CSV, un Parquet, una tabla del catálogo).

**ELT** cambia el orden: cargas el bruto y transformas en el destino (Spark, Athena, el warehouse). En esta UT practicas **ETL en Python** (pandas). En BDA viste el mismo oficio en Pentaho; no repitas Spoon: cambia el motor.

!!! tip "Primer flujo (nivel inicial)"
    Genera o descarga un CSV con errores (fechas mezcladas, duplicados, nulos) → extrae → unifica y deduplica → carga un CSV limpio → un recuento (clientes por ciudad, edad media). Ese es el vídeo de aula en Colab. La evidencia de RA1 no es “abrir el cuaderno”: es **el fichero limpio y el resumen**.

## Procesamiento: el reloj

| Modalidad | Idea | Pregunta | Familia (nombres, no despliegue) |
| --- | --- | --- | --- |
| **Batch** (lotes) | Procesas un bloque al cabo de un periodo | *¿Qué pasó ayer?* | Spark en lote, un script pandas, un job nocturno |
| **Streaming** (flujo) | Procesas a medida que llega | *¿Qué está pasando ahora?* | Kafka, Flink, Spark Streaming |

El lote encaja con el cierre de cobros del hotel. El flujo, con el fraude de una tarjeta o el semáforo de habitación libre. Streaming **no** es latencia cero: tiene un plazo objetivo.

Warehouse, lake, Lambda y Kappa son recetas de **dónde** y **cómo** se combinan esos caminos. El diseño profundo está en BDA; aquí basta elegir el reloj de **tu consulta**.

## Análisis: tres tipos, no tres productos

| Tipo | Pregunta | Ejemplo |
| --- | --- | --- |
| **Descriptivo** | ¿Qué **ya** pasó? | «El 30 % de las reservas de agosto entraron por la web.» |
| **Predictivo** | ¿Qué **puede** pasar? | «En Navidad esperamos un 10 % más de noches.» |
| **Prescriptivo** | ¿**Qué hacemos**? | «Subir cupo el puente y ofrecer tarifa flexible el viernes.» |

Un `groupby` de pandas o un `GROUP BY` de Athena suelen ser **descriptivos**. No los vendas como prescripción.

## Dónde se ve fuera del aula

| Caso | Qué hacen | Reloj o tipo |
| --- | --- | --- |
| Netflix | Recomienda el siguiente título | Flujo + predictivo |
| Amazon | Personaliza búsquedas y compras | Variedad + descriptivo/predictivo |
| Banca | Contrasta cada transacción | Flujo (fraude **ahora**) |
| Industria 4.0 | El sensor avisa si la máquina se desvía | Flujo + prescriptivo (parar o no) |

!!! success "Al terminar 1.1"
    Di, con un caso, las tres frases: qué fuentes unes, si el proceso es lote o flujo, y si el resultado describe, predice o prescribe. Después extraes de verdad en [1.3](extraccion.md).
