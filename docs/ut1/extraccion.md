---
title: 1.3 Extracción de información
tags:
  - SBD
  - RA1
---

# 1.3. Extracción de información

Tener datos no es tener información. **Extraer** es localizar fuentes, quedarte solo con lo que responde a la pregunta y dejarlo en una tabla que se pueda analizar (criterio **b)**). Relacionar después dos tablas ya extraídas es el criterio **d)**.

Los datos llegan en tres familias (las viste en BDA; aquí **las lees**):

| Tipo | Cómo lo reconoces | Ejemplo de extracción |
| --- | --- | --- |
| Estructurado | Filas y columnas fijas | SQL, CSV de clientes |
| Semiestructurado | Claves o marcas; el esquema puede variar | JSON de una API, logs |
| No estructurado | No hay columnas de entrada | HTML de una web, reseñas, fotos |

Idea clave: *sacar* lo que interesa de un volumen grande para una pregunta concreta. De una web de noticias: titular, fecha, autor → una tabla para contar noticias por día.

## Métodos

### Consultas SQL

Cuando el dato ya vive en una relacional, no descargas la base entera: **seleccionas**.

```sql
SELECT nombre, edad
FROM clientes
WHERE ciudad = 'Madrid';
```

Filtrar, ordenar y agregar (`GROUP BY`) **es** extracción. Encaja cuando el origen es una tabla y el volumen se sostiene en ese motor.

### APIs

Una API es una puerta: pides (request) y te traen JSON (response). Datos **actualizados** y, si está bien hecha, estructurados. Encaja con Open-Meteo, pasarelas de pago, el canal de reservas.

Práctica profesional: **caché** (no pidas lo mismo cien veces) y **reintento** (la red falla).

### Web scraping

Lees el HTML. En Python: BeautifulSoup para parsear; Selenium si hay JavaScript. Extraer precios de varias tiendas es el caso típico.

!!! warning "Límites"
    Respeta términos de uso, `robots.txt` y protección de datos. No todo se puede scrapear. Si hay API, **usa la API**.

### Minería de texto

Texto libre: comentarios, reseñas, tickets. Palabras clave, sentimiento, temas. En esta UT basta saber **cuándo** aplica; no entrenas un modelo.

## Data wrangling (el 80 % del tiempo)

Lo extraído suele venir sucio. **Preparar** no es un software: es el oficio.

| Pieza | Qué haces | Ejemplo |
| --- | --- | --- |
| Limpieza | Duplicados, faltantes, erratas | `Madird` / `Mdrid` → `Madrid` |
| Normalización | Un solo formato | Fechas a `datetime`; decimales con punto |
| Transformación | Columnas nuevas, códigos | Sí/No → 1/0; nacimiento → edad |

Si el dato está mal, el gráfico miente. El criterio b) no se cierra con un JSON crudo.

## Herramientas básicas

Excel sirve para **ver** 200 filas. El flujo de aula es **pandas** (y, a escala, Spark: [1.4](preproceso.md)). Lectura, filtro, `groupby`, escritura CSV/Parquet.

## Ejemplo 1 — CSV de clientes (estructurado)

Fichero: [clientes.csv](../assets/practicas/clientes.csv). Objetivo: clientes de Madrid **y** mayores de 30 años.

```python
import pandas as pd

df = pd.read_csv("clientes.csv")
filtrado = df[(df["ciudad"] == "Madrid") & (df["edad"] > 30)]
print(filtrado)
```

Eso es extracción por filtro (lógica ∧ del [1.2](fundamentos.md)). Cuaderno de referencia de aula: [Colab del filtro](https://colab.research.google.com/drive/1CPaRcZNcPMXLAwHdfv6KEuQpBUz1G1j_?usp=sharing).

## Ejemplo 2 — API meteorológica (semiestructurado)

Open-Meteo devuelve temperatura horaria. Pides JSON, **armas** un DataFrame (`date`, `temperature_2m`). Coordenadas de aula: Castro Urdiales o Santander.

```python
import pandas as pd
import urllib.request
import json

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=43.3828&longitude=-3.2204"
    "&hourly=temperature_2m&forecast_days=1"
)
with urllib.request.urlopen(url) as response:
    payload = json.loads(response.read().decode())

hourly = pd.DataFrame(
    {
        "date": payload["hourly"]["time"],
        "temperature_2m": payload["hourly"]["temperature_2m"],
    }
)
print(hourly.head())
print(hourly["temperature_2m"].max(), hourly["temperature_2m"].min())
```

La API garantiza estructura; **tú** transformas a tabla. Cuaderno de aula: [Open-Meteo](https://colab.research.google.com/drive/13w9YOpfMhjh49lAb3UY2MOpfw_UVrA1H?usp=sharing).

## Actividad 1 — Limpieza con pandas (b y d)

Material: [clientes_actividad.csv](../assets/practicas/clientes_actividad.csv) (también en [GitHub raw](https://raw.githubusercontent.com/josedavidmi/iabd-sbd/refs/heads/main/clientes_actividad.csv) si el profesor lo mantiene).

1. Carga el CSV a `df`.
2. `drop_duplicates()`.
3. Unifica `ciudad` (`Madird`, `Mdrid`, `Valenca`, `Barcleona`).
4. `pd.to_datetime` en `fecha_registro` y un formato visible `DD/MM/AAAA`.
5. Informe: número de clientes por ciudad (`value_counts` o `groupby`).

Planifica esta actividad en [1.6](planificacion.md) (esencial frente a gráfico de barras opcional).

## Actividad 2 — API (b)

Pronóstico horario `temperature_2m` de **Santander** (lat. 43.4408, lon. −3.8224), un día. DataFrame con hora y temperatura; imprime máximo y mínimo.

!!! success "Criterio b) en un examen"
    Fuente + método (SQL / API / fichero / scraping) + qué columnas te quedas + un resumen numérico. “He usado pandas” sin pregunta no puntúa.
