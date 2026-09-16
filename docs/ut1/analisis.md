---
title: "1.9. Extracción automática de información"
tags: [SBD, RA1]
---

# 1.9. Extracción automática de información

**CE que se trabajan:** b, d. Consulta el [texto oficial](ra1.md).

**Al terminar:** obtener indicadores automáticamente y defender su significado y sus límites.

## Definir antes de sumar

Calcularemos reservas, noches iniciales, importe nominal y proporción de reservas con cancelación. Agrupamos por hotel y canal. El denominador de la tasa son las reservas de cada grupo, no todos los eventos ni todas las reservas del hotel.

Sobre el DataFrame `integrado` de [integración](integracion.md):

```python
resumen = integrado.groupBy('hotel', 'canal').agg(
    F.count('*').alias('reservas'),
    F.sum('noches').alias('noches'),
    F.sum('importe').alias('importe'),
    F.sum('cancelada').alias('canceladas')
).withColumn('tasa_cancelacion', F.round(F.col('canceladas') / F.col('reservas'), 4))
resumen.orderBy('hotel', 'canal').show()
```

`count('*')` cuenta filas; `count('importe')` excluye nulos de esa columna. No intercambies ambos sin conocer la calidad. Una media global no se obtiene promediando medias de grupos de tamaños distintos.

## Resultado de referencia

| Hotel | Canal | Reservas | Noches | Importe nominal (€) | Canceladas | Proporción |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Laredo | ota | 1 | 2 | 180 | 1 | 1,0000 |
| Laredo | web | 2 | 4 | 400 | 0 | 0,0000 |
| Potes | ota | 1 | 4 | 480 | 0 | 0,0000 |
| Potes | web | 2 | 5 | 600 | 1 | 0,5000 |

Totales: **6 reservas, 15 noches, 1 660 euros nominales y 2 reservas canceladas**. La proporción global es 2/6, no la media de las cuatro proporciones.

## Información e interpretación

Podemos afirmar que, en esta muestra, OTA de Laredo tiene una cancelación de una reserva. No demuestra que el canal cause cancelaciones ni permite generalizar a otro periodo. Con una observación, el porcentaje es muy inestable.

El script `referencia.py` calcula estos datos con Python estándar; `verificar.py` contrasta la salida de Spark con los valores esperados. Dos programas que producen el mismo error no bastan: comprueba también a mano las seis filas y el significado del indicador.

## Tarea para practicar en clase

Añade una salida por canal, conservando una fila por reserva. Resultado global por canal: web tiene cuatro reservas y una cancelada; OTA, dos y una. Explica por qué ordenar solo por número de cancelaciones y ordenar por proporción responde a preguntas diferentes.

Guarda resultados pequeños en CSV y el conjunto integrado en Parquet. Las visualizaciones y cuadros de mando tendrán su desarrollo posterior en SBD.

## Preparar, integrar y analizar producen cosas distintas

| Operación | Resultado | Fase |
| --- | --- | --- |
| Quitar espacios del canal | Categorías coherentes | Preparación |
| Añadir localidad por clave de hotel | Dataset relacionado | Integración |
| Calcular cancelaciones/reservas por canal | Indicador | Análisis |
| Contrastar el indicador y explicar sus límites | Respuesta defendible | Interpretación |

Un proceso automático debe poder repetir la extracción y el cálculo con otro lote sin editar a mano sus resultados. Registra parámetros, versiones y controles. La evidencia del CE b incluye el ensayo ampliado de [coste y calidad](coste-calidad.md), no solo ejecutar sobre seis filas.

## Indicadores adicionales y texto

Añade recuento de reservas por mes, importe nominal medio por reserva y distribución de noches. Define qué representa la fecha. Para comparar periodos necesitas datos de varios periodos; el generador original no los incluye.

Sobre `opiniones` del ejemplo de [integración](integracion.md), una extracción elemental de texto puede contar menciones explícitas a «atención»:

```python
menciones = (opiniones.withColumn("menciona_atencion",
    F.when(F.lower(F.coalesce(F.col("texto"), F.lit(""))).rlike(r"\batención\b"), 1).otherwise(0))
    .groupBy("id_hotel").agg(F.sum("menciona_atencion").alias("menciones"),
                            F.count("*").alias("opiniones")))
menciones.orderBy("id_hotel").show()
```

La muestra da una mención en cada hotel. Es una regla textual, no un modelo de sentimiento: «mala atención» también coincide, y un sinónimo podría no hacerlo. Para distinguir lenguaje favorable, negación o ironía necesitaríamos otra definición y evaluación. No atribuimos causalidad a una asociación entre puntuación del hotel y cancelaciones.

## De la tabla a una conclusión

Escribe cuatro frases: pregunta, resultado con denominador, comprobación realizada y limitación. Por ejemplo: «En la muestra, web tiene una cancelación de cuatro reservas (25 %). La integración conserva las seis reservas. Es una muestra sintética de un único día y no permite generalizar a la temporada».

!!! example "Comprobación final"
    Obtén la proporción global desde sumas de numerador y denominador y compárala con la media simple de proporciones de grupos. Explica por qué difieren. Añade una opinión sin la palabra exacta pero con significado similar y describe el falso negativo de la regla textual.
