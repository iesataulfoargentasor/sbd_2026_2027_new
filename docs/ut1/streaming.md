---
title: "1.10. Procesamiento de datos en tiempo real"
tags: [SBD, RA1]
---

# 1.10. Procesamiento de datos en tiempo real

**CE que se trabajan:** b, c, f. Consulta el [texto oficial](ra1.md).

**Al terminar:** transformar un flujo y observar cómo cambian sus agregaciones y ventanas.

## Un informe que se actualiza

Batch procesa un conjunto delimitado. Un flujo puede seguir recibiendo datos. En esta introducción emplearemos microprocesamiento por lotes: cada grupo de eventos actualiza el resultado. No hay una promesa de respuesta instantánea.

El laboratorio cuenta **eventos por tipo**; no calcula el estado definitivo de las reservas. Eso permite ver la llegada incremental sin confundir un evento con una reserva.

## Ensayo reproducible

En la carpeta del laboratorio, con el entorno activo:

```bash
python streaming.py --entrada datos --trabajo flujo_01
```

El programa crea un directorio de entrada vacío y un checkpoint. Publica un primer fichero con confirmaciones, espera a procesarlo y comprueba seis eventos. Después publica otro con dos cancelaciones y comprueba ocho. Escribe `flujo_01/evidencias.json` y detiene la consulta. Para repetir, utiliza una carpeta nueva.

El núcleo del ensayo es:

```python
flujo = spark.readStream.schema(esquema_eventos).json(carpeta_entrada)
conteo = flujo.groupBy('tipo').count()
consulta = conteo.writeStream.outputMode('complete').format('memory').queryName('conteo_eventos').start()
```

El script descargable añade checkpoint, publicación de lotes, espera y verificaciones. La tabla en memoria es una salida de demostración, no un almacén de producción ni una prueba de recuperación duradera.

## Tiempo del hecho y tiempo de llegada

Una cancelación puede producirse a las 10:00 y recibirse a las 10:05. Nuestro primer ensayo solo distingue el orden de llegada. Si quisiéramos informes por hora real, necesitaríamos fecha del evento y política para datos tardíos. A continuación introducimos ventanas sencillas; watermarking avanzado y joins entre flujos se ampliarán después.

## Tarea para practicar en clase

Explica qué pasaría si el segundo fichero se volviera a publicar con otro nombre: se trataría como otra entrada y el conteo de eventos podría repetirse. Un checkpoint no sustituye una regla de deduplicación por identidad de negocio.

??? success "Comprobación"
    Primera etapa: seis confirmaciones. Segunda: seis confirmaciones y dos cancelaciones. No son ocho reservas; siguen siendo seis. Guarda los dos resultados y la duración observada, sin extrapolar garantías a un clúster.

Consulta técnica: [guía oficial de Structured Streaming](https://spark.apache.org/docs/3.5.6/structured-streaming-programming-guide.html).

## Ventanas por tiempo del evento

Una ventana agrupa eventos de un intervalo, por ejemplo [10:00, 10:05). El extremo final no se incluye: 10:05 pertenece a la ventana siguiente. La hora del evento describe cuándo ocurrió; la hora de procesamiento, cuándo lo calculamos.

Este segundo ensayo es autónomo. En una sesión PySpark crea directorios nuevos y publica dos lotes pequeños. La zona UTC evita ambigüedades en el ejemplo. Cada fichero terminado se mueve a la entrada antes de procesarlo.

```python
from pathlib import Path
import json
from pyspark.sql import functions as F

spark.conf.set("spark.sql.session.timeZone", "UTC")
base = Path("ventanas_01")
entrada = base / "entrada"
entrada.mkdir(parents=True, exist_ok=False)
flujo = spark.readStream.schema("id_evento long, ts timestamp, tipo string").json(str(entrada))
ventanas = (flujo.filter(F.col("ts").isNotNull())
    .groupBy(F.window("ts", "5 minutes"), "tipo").count())
q = (ventanas.writeStream.format("memory").queryName("ventanas_hotel")
    .outputMode("complete").option("checkpointLocation", str(base / "checkpoint")).start())

def publicar(nombre, registros):
    temporal = base / nombre
    temporal.write_text("".join(json.dumps(r) + "\n" for r in registros), encoding="utf-8")
    temporal.rename(entrada / nombre)

try:
    publicar("lote1.json", [
        {"id_evento": 1, "ts": "2026-09-01T10:01:00Z", "tipo": "confirmacion"},
        {"id_evento": 2, "ts": "2026-09-01T10:05:00Z", "tipo": "confirmacion"}])
    q.processAllAvailable()
    spark.sql("SELECT * FROM ventanas_hotel ORDER BY window.start").show(truncate=False)
    publicar("lote2.json", [
        {"id_evento": 3, "ts": "2026-09-01T10:02:00Z", "tipo": "confirmacion"}])
    q.processAllAvailable()
    spark.sql("SELECT * FROM ventanas_hotel ORDER BY window.start").show(truncate=False)
finally:
    q.stop()
```

Primero hay un evento en 10:00–10:05 y otro en 10:05–10:10. Después, el evento tardío incrementa la primera ventana a dos. No se deduplica por `id_evento` en este ejemplo: republicarlo como otra entrada volvería a contarlo.

### Salida y estado

`complete` publica la tabla agregada completa; `update`, las filas modificadas cuando la consulta y el destino lo admiten; `append`, las nuevas filas finales compatibles con el plan. No cambies de modo sin revisar la semántica. La salida en memoria es únicamente docente; para conservar resultados, elige un destino soportado por la consulta.

Este ensayo sin watermark mantiene el estado de las ventanas y solo es adecuado para la demostración acotada. Un **watermark** expresa una tolerancia temporal respecto al progreso del tiempo de evento y permite limitar estado en operaciones compatibles. No es un temporizador de reloj que cierre todo exactamente cinco minutos después. Su uso exige decidir cómo tratar eventos muy tardíos; no añadimos aquí joins complejos ni garantías de plataforma.

!!! example "Práctica y comprobación"
    Añade un evento exactamente a las 10:10 y otro tardío a las 10:04. Predice las ventanas y observa sus recuentos. Entrega la evolución, la regla de intervalo y la diferencia entre contar eventos y contar reservas. Un checkpoint no corrige duplicados de negocio.
