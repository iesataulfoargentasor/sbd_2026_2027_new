---
title: "1.6. Integración de datos"
tags: [SBD, RA1]
---

# 1.6. Integración de datos

**CE que se trabajan:** c, d, f. Consulta el [texto oficial](ra1.md).

**Al terminar:** elegir claves y joins, anticipar cardinalidades y comprobar el conjunto integrado.

## Construir primero el conjunto en pandas

Integrar es combinar registros que describen realidades compatibles. Define **clave**, **granularidad** (qué cuenta una fila), **cardinalidad** (cuántas correspondencias puede haber) y **semántica** (unidad, periodo y significado). Un identificador numérico en dos sistemas no garantiza que represente el mismo hotel.

| Operación | Pregunta | Efecto esperado |
| --- | --- | --- |
| `concat` / `unionByName` | ¿Añadir más reservas del mismo contrato? | Apila filas; puede introducir duplicados |
| `inner` | ¿Conservar solo correspondencias? | Pierde registros sin pareja |
| `left` | ¿Enriquecer todas las reservas? | Conserva las de la izquierda, pero puede multiplicarlas |
| `left_anti` en Spark | ¿Qué reservas no encuentran hotel? | Devuelve las huérfanas |

Tras [preparar el entorno](entorno.md) y generar `datos/`, ejecuta en Python con pandas:

```python
import pandas as pd
reservas = pd.read_csv("datos/reservas.csv")
hoteles = pd.read_csv("datos/hoteles.csv")
assert reservas["id_reserva"].is_unique
assert hoteles["id_hotel"].notna().all() and hoteles["id_hotel"].is_unique
assert reservas["id_hotel"].notna().all()
unidas = reservas.merge(hoteles, on="id_hotel", how="left",
                        validate="many_to_one", indicator=True)
assert unidas["_merge"].eq("both").all(), "Hotel desconocido"
assert len(unidas) == len(reservas)
assert round(unidas["importe"].sum(), 2) == round(reservas["importe"].sum(), 2)
print(unidas.drop(columns="_merge"))

# Dos lotes disjuntos: apilar, no relacionar columnas.
lotes = pd.concat([reservas.iloc[:3], reservas.iloc[3:]], ignore_index=True)
assert len(lotes) == 6 and lotes["id_reserva"].is_unique
```

`validate="many_to_one"` detiene el join si el catálogo no es único. pandas puede emparejar claves nulas entre sí, a diferencia de un join SQL por igualdad; por eso las claves obligatorias se validan antes. Consulta la [documentación de combinaciones de pandas](https://pandas.pydata.org/docs/user_guide/merging.html).

Si una fuente aporta `"01"` y otra `1`, decide según contrato: ¿es el mismo identificador o un código con ceros significativos? No fuerces la conversión sin documentarlo. Alinea moneda, zona horaria, nombres y periodo. Si ambos lados contienen `fecha`, renombra como `fecha_reserva` y `fecha_evento`; un sufijo automático no explica su significado.

### Cardinalidad y control de multiplicación

Si una clave aparece n veces a la izquierda y m a la derecha, el join genera n × m pares para esa clave. Dos reservas de un hotel y dos filas de catálogo producen cuatro filas. Un `left` no garantiza preservar el recuento original. En una relación muchos-a-muchos, agrega antes o construye una tabla de relación explícita según la pregunta.

Los siguientes ejemplos son la continuación con Spark después de [1.7](spark.md): primero entendemos la relación en pandas y después la ejecutamos a escala.

## El join tiene consecuencias

En la sesión de [Spark](spark.md), carga el catálogo:

```python
h = spark.read.schema('id_hotel int, hotel string, localidad string').option('header', True).csv('datos/hoteles.csv')
r.join(h, 'id_hotel', 'left').show()
r.join(h, 'id_hotel', 'left_anti').show()
```

El `left` conserva reservas; si falta hotel, sus atributos serán nulos. El `left_anti` detecta reservas sin correspondencia. Un `inner` las descartaría, pudiendo ocultar errores. El catálogo debe tener una sola fila por clave.

## JSON anidado y múltiples eventos

```python
e = spark.read.schema('id_evento long, id_reserva long, tipo string, detalle struct<origen:string>').json('datos/eventos.jsonl')
e.select('id_evento', 'id_reserva', 'detalle.origen').show()
```

Una reserva confirmada y después cancelada tiene dos eventos. Si unimos ambos directamente y sumamos el importe, la reserva aparece dos veces. Para nuestra pregunta primero resumimos los eventos a **una fila por reserva**:

```python
canceladas = e.filter(F.col('tipo') == 'cancelacion').select('id_reserva').distinct().withColumn('cancelada', F.lit(1))
integrado = r.join(h, 'id_hotel', 'left').join(canceladas, 'id_reserva', 'left').fillna({'cancelada': 0})
```

Aquí `distinct` es correcto porque la regla es existencia de cancelación, no número de eventos. Una reapertura exigiría otra regla y una secuencia temporal: no la inventamos.

## Comprobaciones

- Seis reservas antes y después del join en el conjunto mínimo.
- Cero reservas sin hotel y cero eventos sin reserva.
- Dos reservas con cancelación.
- El importe total inicial sigue siendo 1 660 euros.

`unionByName` sirve para apilar lotes de estructura compatible; no relaciona una reserva con un hotel. Requiere revisar tipos y duplicados entre lotes.

## Puente con MongoDB y BDA

El paquete incluye `extraer_mongo.py`, que lee **solo** `id_hotel`, `hotel` y `localidad` desde una colección y exporta el catálogo. No contiene credenciales. Con una colección preparada por el profesor:

```bash
python -m pip install pymongo==4.10.1
python extraer_mongo.py --base hotel --coleccion hoteles --salida catalogo_mongo.csv
```

La URI se proporciona en la variable `MONGO_URI` del entorno, nunca en los apuntes. Los documentos deben tener las claves del diccionario; si los de BDA tienen otra forma, documenta la correspondencia antes de usarlos. El análisis admite `--catalogo catalogo_mongo.csv`. Así conectamos el sistema de origen, el fichero intermedio y Spark sin reconstruir el replica set.

Extensión guiada en `mongosh`: `db.hoteles.aggregate([{$project: {_id: 0, id_hotel: 1, hotel: 1, localidad: 1}}])`. Seleccionar en origen reduce transferencia; no prueba distribución del cálculo.

## Tarea para practicar en clase

Predice el resultado de unir reservas con **todos** los eventos antes de resumir. En el conjunto pequeño aparecerán ocho filas y el total inflado será 2 040 euros. Explica de dónde vienen los 380 euros adicionales y corrige el orden del proceso.

## Añadir opiniones sin cambiar la unidad de análisis

El paquete original conserva reservas, hoteles y eventos. Para ampliar el proyecto, crea un fichero nuevo `datos/opiniones.json` con este contenido sintético (una lista JSON, no JSONL):

```json
[
  {"id_opinion": 1, "id_hotel": 1, "puntuacion": 4, "texto": "Buena atención"},
  {"id_opinion": 2, "id_hotel": 1, "puntuacion": 2, "texto": "Espera prolongada"},
  {"id_opinion": 3, "id_hotel": 2, "puntuacion": 5, "texto": "Buena atención y ubicación"}
]
```

```python
opiniones = spark.read.schema(
    "id_opinion long, id_hotel int, puntuacion int, texto string"
).option("multiLine", True).json("datos/opiniones.json")
assert opiniones.filter("id_opinion IS NULL OR id_hotel IS NULL OR puntuacion IS NULL OR puntuacion < 1 OR puntuacion > 5").count() == 0
assert opiniones.groupBy("id_opinion").count().filter("count > 1").count() == 0
assert opiniones.join(h, "id_hotel", "left_anti").count() == 0
por_hotel = opiniones.groupBy("id_hotel").agg(
    F.count("*").alias("n_opiniones"),
    F.avg("puntuacion").alias("puntuacion_media")
)
integrado_opiniones = integrado.join(por_hotel, "id_hotel", "left")
assert integrado_opiniones.count() == integrado.count()
```

La media de Laredo es 3 y la de Potes 5. Estas características describen al hotel, no la opinión individual de quien hizo cada reserva. No sumes `n_opiniones` sobre las reservas: repetirías las mismas opiniones. Una media global de opiniones se calcula sobre opiniones o ponderando por sus recuentos, no sobre el dataset de reservas.

!!! example "Comprobación adicional"
    Duplica un hotel con otra localidad. Debe fallar la validación del catálogo antes del join. Añade después una opinión a un hotel inexistente: debe detectarse como huérfana. Dibuja la granularidad antes y después de resumir opiniones y eventos.

La salida integrada conservará una fila por reserva, atributos del hotel, bandera de cancelación y contexto de opiniones. El diccionario debe indicar qué columnas son aditivas y cuáles no.
