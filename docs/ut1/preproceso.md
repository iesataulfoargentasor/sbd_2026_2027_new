---
title: "1.5. Preparación y calidad de datos"
tags: [SBD, RA1]
---

# 1.5. Preparación y calidad de datos

**CE que se trabajan:** b, d, g. Consulta el [texto oficial](ra1.md).

**Al terminar:** limpiar con reglas explícitas, medir el efecto y distinguir preparación analítica de preparación para ML.

## Limpieza → integración → transformación

Trabajamos primero con una muestra que cabe en memoria. **Limpieza** corrige o separa registros según reglas; **integración** relaciona fuentes; **transformación** obtiene una representación útil. El orden puede requerir volver atrás: un join puede revelar un hotel desconocido. Conserva fuente, regla aplicada y recuentos en cada paso.

No existe una receta de «borrar todos los nulos». En el hotel un importe ausente no equivale a una reserva gratuita; un canal desconocido puede conservarse con una categoría explícita. Las reglas dependen del indicador.

## Inspección y decisiones

| Problema | Pregunta previa | Decisión del ejemplo |
| --- | --- | --- |
| Nulo | ¿Es obligatorio para el indicador? | Separar noches o importe ausentes; marcar canal desconocido |
| Fila repetida | ¿Es repetición de transporte o un hecho distinto? | Quitar copia exacta con registro del recuento |
| Misma clave, otros valores | ¿Hay versión o regla de precedencia? | Detener y resolver; no elegir la primera arbitrariamente |
| Tipo incorrecto | ¿Hay contrato de fecha y decimal? | Convertir y registrar errores |
| Columna irrelevante | ¿Se necesita para análisis o trazabilidad? | Proyectar solo las necesarias sin perder el original |
| Valor atípico | ¿Es error o una reserva excepcional real? | Marcar y revisar, sin recortar automáticamente |

## Ejemplo completo en pandas

Usa el entorno Python del aula con pandas instalado (`python -m pip install pandas`). Registra su versión. Este ejemplo crea su propia muestra; no altera los datos originales del laboratorio.

```python
import pandas as pd

bruto = pd.DataFrame([
    [1, 1, " WEB ", "2026-09-01", "3", "300.00"],
    [1, 1, " WEB ", "2026-09-01", "3", "300.00"],
    [2, 1, None, "2026-09-02", "2", "180.00"],
    [3, 2, "ota", "fecha-mal", "0", "desconocido"],
    [4, 2, "web", "2026-09-03", "40", "9000.00"],
], columns=["id_reserva", "id_hotel", "canal", "fecha", "noches", "importe"])
print(bruto.isna().mean().mul(100))
x = bruto.drop_duplicates().copy()
assert not x["id_reserva"].duplicated().any(), "Claves en conflicto"
x["fecha"] = pd.to_datetime(x["fecha"], format="%Y-%m-%d", errors="coerce")
for col in ["noches", "importe"]:
    x[col] = pd.to_numeric(x[col], errors="coerce")
x["canal_ausente"] = x["canal"].isna()
x["canal"] = x["canal"].astype("string").str.strip().str.lower().fillna("desconocido")
valida = (x[["id_reserva", "id_hotel", "fecha", "noches", "importe"]].notna().all(axis=1)
          & x["noches"].gt(0) & x["importe"].ge(0)
          & x["noches"].mod(1).eq(0))
rechazadas = x.loc[~valida].copy()
preparadas = x.loc[valida].copy()
preparadas["revisar_estancia"] = preparadas["noches"].gt(30)
preparadas["mes"] = preparadas["fecha"].dt.month
print(len(bruto), len(x), len(preparadas), len(rechazadas))  # 5, 4, 3, 1
print(preparadas[["id_reserva", "canal", "revisar_estancia"]])
```

La reserva 4 queda marcada para revisión y se conserva. El límite de 30 noches es una regla didáctica, no una prueba de error. Para dinero, el ejemplo usa números decimales de pandas solo para explorar; en el análisis final usa céntimos enteros o un decimal exacto como `decimal(12,2)` de Spark. `errors="coerce"` facilita localizar fallos, pero obliga a contar los nuevos ausentes y guardar los valores originales.

!!! warning "Una imputación cambia lo que estás midiendo"
    Rellenar importes con la mediana inventa importes. Puede servir en una exploración documentada, pero no para afirmar un total contable observado. Mantén columna original, indicador de imputación y cobertura. Si no hay observaciones válidas, tampoco existe una mediana utilizable.

## Transformar lo necesario

| Transformación | Ejemplo | Límite |
| --- | --- | --- |
| Normalizar etiquetas | `WEB` → `web` | No confundirlo con escalado numérico |
| Variable derivada | Mes de reserva | La fecha de reserva no es la fecha de estancia |
| Discretización | Estancias cortas/largas | Publicar los límites de los intervalos |
| Min–max | (x − mínimo)/(máximo − mínimo) | Indefinido si máximo = mínimo; sensible a extremos |
| Estandarización | (x − media)/desviación típica | No convierte una distribución en normal; desviación cero requiere regla |
| Encoding | Indicador `es_web` | Los códigos 1/2 de canales no expresan una distancia |

```python
preparadas["tramo_noches"] = pd.cut(
    preparadas["noches"], bins=[0, 2, 7, float("inf")],
    labels=["1–2", "3–7", "8 o más"], right=True)
preparadas["es_web"] = preparadas["canal"].eq("web").astype(int)
```

No hace falta escalar importes para sumarlos ni aplicar one-hot para agrupar por canal. Los pipelines de entrenamiento, selección avanzada de variables y MLlib quedan como ampliación opcional en coordinación con aprendizaje automático. Si el objetivo fuera ML, los parámetros de transformación se estimarían con entrenamiento para evitar filtraciones desde test.

## Del concepto a Spark

| Concepto | pandas | PySpark |
| --- | --- | --- |
| Ausentes | `isna`, `fillna`, `dropna` | `isNull`, `na.fill`, `na.drop` |
| Copias exactas | `drop_duplicates()` | `distinct()` o `dropDuplicates()` |
| Selección | `loc`, columnas | `filter`, `select` |
| Tipos | `to_numeric`, `to_datetime` | Esquema explícito y funciones de conversión |
| Etiquetas y reglas | `str`, máscaras | `trim`, `lower`, `when` |

En [1.8](transformaciones-escala.md) conservaremos estas reglas y cambiaremos la ejecución. No basta con sustituir nombres de funciones.

!!! example "Práctica y comprobación"
    Añade una copia exacta y una reserva con importe vacío. Predice los cuatro recuentos antes de ejecutar. Guarda una tabla con problema, regla, filas afectadas y efecto en el indicador. Demuestra que entrada = copias retiradas + rechazadas + preparadas; explica por qué esto no demuestra por sí solo exactitud.

El vídeo docente de demostración ETL/Colab es apoyo complementario si el profesor lo facilita en Moodle; la explicación y los controles necesarios están escritos aquí. Véase [procedencia](referencias.md).
