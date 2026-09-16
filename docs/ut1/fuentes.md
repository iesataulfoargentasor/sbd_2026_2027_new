---
title: "1.4. Fuentes y extracción de información"
tags: [SBD, RA1]
---

# 1.4. Fuentes y extracción de información

**CE que se trabajan:** b, c, f. Consulta el [texto oficial](ra1.md).

**Al terminar:** seleccionar campos, leer fuentes heterogéneas y documentar su contrato.

## Primero: qué representa cada registro

La **granularidad** es el significado de una fila. Una fila de reservas representa una reserva; una fila de eventos representa un hecho ocurrido sobre ella. Una reserva puede tener varios eventos. Mezclar ambas granularidades antes de sumar puede duplicar importes.

| Fuente | Clave | Campos principales | Granularidad |
| --- | --- | --- | --- |
| reservas.csv | id_reserva | id_hotel, canal, fecha, noches, importe | Una reserva |
| hoteles.csv | id_hotel | hotel, localidad | Un hotel |
| eventos.jsonl | id_evento | id_reserva, tipo, detalle.origen | Un evento |

Los identificadores son enteros; `fecha` es fecha; `importe` usa decimal con dos posiciones. El JSON incluye un objeto anidado `detalle`. No se deduce el significado de una columna únicamente por su tipo.

## Calidad antes de integrar

1. Comprobar campos obligatorios y tipos.
2. Detectar claves repetidas.
3. Validar noches positivas e importe no negativo.
4. Normalizar el canal: espacios y mayúsculas no deben crear categorías artificiales.
5. Comprobar correspondencia entre reservas, hoteles y eventos.
6. Conservar fuente y registrar cualquier cambio.

En el paquete, `analizar.py` rechaza valores inválidos y claves duplicadas. No aplica una eliminación arbitraria de duplicados: dos reservas con la misma clave y distinto importe necesitan una regla de negocio.

## Ejemplo: un dato ausente

Si falta `importe`, reemplazarlo por cero hace que el total parezca completo. Una política posible es separar el registro y publicar cobertura; otra es detener el cálculo. Nuestro laboratorio detiene el proceso, para que ninguna ausencia quede oculta.

Una fecha que no se puede interpretar debe detectarse. El esquema se declara y la lectura usa modo estricto; además se comprueba que no queden nulos en campos obligatorios.

## Tarea para practicar en clase

Genera una carpeta de datos nueva y altera una copia: introduce un identificador de hotel inexistente, unas noches negativas o repite una reserva. Ejecuta el análisis y conserva el mensaje del control que lo detiene. Restaura generando otra carpeta, no borrando el registro para ocultar el problema.

??? success "Qué debe observarse"
    No se genera un informe válido si hay una referencia huérfana, una clave repetida o un valor fuera de dominio. El original permanece disponible y la corrección debe tener una explicación.

Guarda un diccionario con nombre, tipo, significado, unidad, regla y procedencia. Es parte de CE c, d y g.

## Extraer lo necesario de cada fuente

Extraer datos significa acceder a los registros necesarios. Extraer información, en [1.9](analisis.md), supone responder preguntas con ellos. El contrato de extracción debe registrar origen, fecha de acceso, periodo cubierto, campos, tipos, volumen y condiciones de repetición.

| Fuente | Lectura del analista | Comprobación imprescindible |
| --- | --- | --- |
| CSV | Cabecera, delimitador, comillas, codificación y decimal | Una coma dentro de comillas no es una columna nueva |
| JSON | Objetos, listas y campos anidados | No todos los documentos tienen todos los campos |
| JSONL | Un objeto JSON por línea | Cada línea debe ser un objeto completo |
| SQL | SELECT con proyección y filtro | Periodo, tipos y resultado de la consulta |
| API | Petición, respuesta JSON y paginación | Estado HTTP, cobertura y límite de peticiones |
| Web | Extraer elementos de un HTML autorizado | El selector puede dejar de coincidir |
| MongoDB | Consulta y proyección sobre una colección disponible | Ausencias, arrays y correspondencia de identificadores |

Parquet se lee seleccionando columnas y filtros cuando el lector lo permite. Avro y ORC pueden aparecer como fuentes: reconoce el formato y utiliza su lector. Su diseño interno y elección como almacenamiento se coordinan con BDA.

### Ficheros y SQL: ejemplo local reproducible

Después de generar `datos/` con el [laboratorio](entorno.md):

```python
import csv, json, sqlite3
from pathlib import Path

with open("datos/reservas.csv", encoding="utf-8", newline="") as f:
    filas = list(csv.DictReader(f))  # Solo la muestra pequeña
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE reservas (id INTEGER, canal TEXT, fecha TEXT)")
    con.executemany("INSERT INTO reservas VALUES (?, ?, ?)",
                   [(int(r["id_reserva"]), r["canal"], r["fecha"]) for r in filas])
    print(con.execute("SELECT id, canal FROM reservas WHERE fecha >= ? AND fecha < ?",
                      ("2026-09-01", "2026-10-01")).fetchall())
with open("datos/eventos.jsonl", encoding="utf-8") as f:
    for linea in f:
        evento = json.loads(linea)
        print(evento["id_reserva"], evento.get("detalle", {}).get("origen"))
```

La consulta devuelve seis reservas. En una base preparada por BDA aplicaríamos el mismo principio: seleccionar campos y periodo en origen. Los parámetros evitan construir SQL concatenando valores. En grandes entradas, lee por lotes y evita formar una lista con todo el contenido.

### API: contrato antes de programar

Este patrón presupone una API docente que devuelve `items` y `next_cursor`. Sustituye `API_URL` por la dirección facilitada por el profesor; otras APIs exigen adaptar la paginación.

```python
import os, json, urllib.request, urllib.parse
cursor = None
vistos = set()
with open("extraccion_api.jsonl", "x", encoding="utf-8") as salida:
    while True:
        params = {"desde": "2026-09-01", "hasta": "2026-10-01"}
        if cursor is not None:
            params["cursor"] = cursor
        url = os.environ["API_URL"] + "?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=20) as respuesta:
            pagina = json.load(respuesta)
        if not isinstance(pagina.get("items"), list):
            raise ValueError("Respuesta fuera del contrato")
        for item in pagina["items"]:
            salida.write(json.dumps(item, ensure_ascii=False) + "\n")
        cursor = pagina.get("next_cursor")
        if cursor is None:
            break
        if cursor in vistos:
            raise ValueError("Cursor repetido: extracción incompleta")
        vistos.add(cursor)
```

Una interrupción deja una extracción parcial: registra el fallo y no la declares completa. Si hay cuotas o respuesta 429, sigue la política del proveedor; no repitas peticiones sin límite. Conserva una muestra sintética para repetir el análisis sin depender de la conexión.

### Web: extracción mínima sin dependencia de una página externa

```python
from html.parser import HTMLParser

class Titulos(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dentro = False
        self.textos = []
    def handle_starttag(self, tag, attrs):
        if tag == "h2": self.dentro = True
    def handle_endtag(self, tag):
        if tag == "h2": self.dentro = False
    def handle_data(self, data):
        if self.dentro: self.textos.append(data.strip())

lector = Titulos()
lector.feed("<h2>Hotel Laredo</h2><p>Oferta</p><h2>Hotel Potes</h2>")
print(lector.textos)
```

Obtendrás dos nombres; no has extraído precios ni reservas. Es un parser didáctico para ese HTML simple. Antes de aplicarlo a una web real, comprueba acceso permitido, condiciones de uso y existencia de una API. Documenta el selector y verifica el número de elementos: cero resultados puede significar cambio de estructura, no ausencia de hoteles.

MongoDB dispone ya de un [extractor y contrato](integracion.md#puente-con-mongodb-y-bda). Úsalo sobre la colección suministrada, seleccionando solo los campos necesarios; no se instala aquí una plataforma de ingesta.

!!! example "Comprobación de extracción"
    Entrega el mismo inventario de hoteles obtenido desde CSV y desde la fuente asignada (SQL, API o MongoDB). Compara claves, tipos y número de registros. Explica cómo detectarías una página de API omitida y por qué no debes confundir «HTTP correcto» con «dataset completo».

La política de calidad se aplica en [preparación](preproceso.md); las relaciones entre fuentes, en [integración](integracion.md).
