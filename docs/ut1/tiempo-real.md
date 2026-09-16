---
title: Análisis en tiempo real
tags:
  - SBD
  - RA1
---

# Análisis, registro y almacenamiento en tiempo real

Anexo Word del eXe *Técnicas de análisis* (Tema 5). El Anexo VI pide **reconocer** el análisis en tiempo real. En UT1 no despliegas Kafka en producción; sí eliges el **reloj** ([1.1](ciclo-analisis.md)).

## Batch frente a streaming

| | Batch | Streaming |
| --- | --- | --- |
| Cuándo | Un bloque al cabo de un periodo | A medida que llega |
| Ejemplo | Informe de ventas al cierre | Fraude en la transacción, parar la máquina |
| Precio | Volumen y precisión | Infraestructura y latencia |

Lambda: batch (histórico) **y** streaming (ahora) en paralelo. Kappa: casi todo entra por streaming.

## Tecnologías (nombres de aula)

| Oficio | Ejemplos |
| --- | --- |
| Ingesta / mensajería | **Kafka**; **MQTT** en sensores IoT |
| Proceso | Spark Streaming (micro-lotes), **Flink** (streaming puro) |
| Almacén | MongoDB, Cassandra; series temporales **InfluxDB**, TimescaleDB |
| Panel | Grafana; Kibana (ELK) |

## Flujo de ejemplo (invernadero)

1. El sensor publica JSON a Kafka cada segundo (`sensor_id`, `timestamp`, `temperatura`).
2. Spark (o un script) calcula la media de 5 minutos y alerta si temperatura > 30 °C.
3. Se guarda en InfluxDB o Mongo.
4. Grafana muestra la serie y la alerta.

## Actividades (nivel básico)

1. Script que simula temperaturas y las imprime (o las escribe en un CSV) cada segundo.
2. Demo guiada de un dashboard Grafana (la monta el profesor).
3. Opcional: Kafka → proceso → Mongo, si el laboratorio lo permite.

El detalle de ventanas y watermarks se retoma después. Aquí basta decir si tu pregunta es *¿qué pasó ayer?* o *¿qué está pasando ahora?*
