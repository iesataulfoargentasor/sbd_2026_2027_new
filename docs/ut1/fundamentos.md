---
title: 1.2 Fundamentos matemáticos y algoritmos
tags:
  - SBD
  - RA1
---

# 1.2. Fundamentos matemáticos y algoritmos

!!! warning "Cuaderno de inicio"
    Antes de los ejemplos de este tema, consulta el Colab **Inicio con Python**:

    **[Inicio con Python](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)** · [página](inicio-python.md)

Los datos no solo se guardan: hay que **organizarlos, recorrerlos y analizarlos**. Con la lista de la compra da igual cómo lo hagas; con millones de filas, la forma de organizarlos decide si algo tarda un segundo o una semana. Para trabajar a esa escala necesitas dos piezas (criterio **a)**):

- **Matemática discreta:** la "gramática" para representar datos como **conjuntos, relaciones, funciones y grafos**. No es un adorno teórico: es el lenguaje en el que luego se expresan las operaciones de pandas, SQL o Spark.
- **Algoritmos y su complejidad:** el algoritmo es la **secuencia de pasos** que resuelve la tarea; su **complejidad** dice si ese paso escala o se vuelve inviable cuando los datos crecen.

Una intuición antes de empezar: buscar un número en una lista de 10 elementos es fácil, miras uno a uno y ya está. En 10 millones ya no vale "mirar uno a uno" si puedes partir por la mitad. Todo este apartado gira en torno a esa idea.

Al terminar serás capaz de:

- reconocer matemática discreta aplicada a datos;
- traducir una regla de negocio a lógica y a código;
- identificar la complejidad temporal y espacial de una solución;
- explicar por qué O(n²) no escala;
- elegir entre lista, matriz, conjunto, diccionario, árbol o grafo;
- aplicar un grafo o un filtro lógico sencillo.

Sigue el apartado en el cuaderno de Colab de *Fundamentos matemáticos y algoritmos*:

- Matemática discreta: [Matemática discreta aplicada a Big Data](https://colab.research.google.com/drive/1LZkMTdbtTa_XFnw_9ZzDI0HUoFlr0lpl?usp=sharing)
- Combinatoria: [Combinatoria con menús](https://colab.research.google.com/drive/1lOe3pA0-L7iGGNWAmDtZwt1ZxXv4L-zO?usp=sharing)
- Repaso y miniproyecto de compras (resuelto): [Miniproyecto de compras y relaciones entre productos](https://colab.research.google.com/drive/1YYxgnXcdUw0_qgwGdYeGwvOjxh-dLlsj?usp=sharing)

## Conjuntos

### Qué es la matemática discreta (y por qué te importa)

Cuando piensas en "matemáticas" quizá te vienen curvas, funciones continuas, cálculo. Esa matemática trabaja con magnitudes que varían sin saltos: el tiempo, la temperatura, la velocidad.

Pero un ordenador no guarda curvas: guarda **objetos contables y separables** — un nombre, una fila de una tabla, un clic, una lectura de un sensor. La **matemática discreta** es la rama que estudia ese tipo de objetos: bits, listas, conjuntos, relaciones y grafos. Encaja de forma natural con lo que almacena un ordenador porque es la matemática de *lo que se puede contar de uno en uno*. Por eso aparece detrás de todo lo que harás en este módulo.

### Conjuntos y sus operaciones

Un **conjunto** es una colección de elementos **bien definidos** (dado cualquier elemento, sabes si pertenece o no), **sin orden** (da igual el orden en que los escribas) y **sin repetidos** (si un elemento aparece dos veces, cuenta una).

Las operaciones sobre conjuntos las **ya usas** — quizá sin saberlo — al cruzar datasets:

| Operación | Idea | En el hotel / clientes |
| --- | --- | --- |
| Unión A ∪ B | Lo que está en A **o** en B | Todos los huéspedes de web y OTA |
| Intersección A ∩ B | Lo común | Quien compró producto X **y** Y |
| Diferencia A − B | En A y no en B | Reservas **sin** cobro |
| Producto cartesiano A × B | Todos los pares | Rara vez lo quieres entero: explota |

Ejemplo:

```python
A = {"Ana", "Juan", "Marta", "Luis"}       # compraron X
B = {"Marta", "Luis", "Sofía", "Pedro"}    # compraron Y

print("unión:", A | B)
print("intersección:", A & B)
print("solo X:", A - B)
print("todos los pares:", {(a, b) for a in A for b in B})
```

### Las mismas operaciones, en tablas de datos

En el análisis real, esas "bolsas de nombres" suelen ser **tablas** con más columnas (importe, fecha, cliente…), y combinarlas es el pan de cada día. La correspondencia exacta es esta:

- Un **inner join** (`merge(..., how="inner")`) equivale a una **intersección por clave**: se quedan solo las filas cuyo valor de clave (por ejemplo, el `cliente`) aparece **en las dos tablas**. *Reservas que ya tienen su cobro.*
- Un **outer join** (`how="outer"`) equivale a una **unión con nulos**: entran las filas de ambas tablas, y donde alguien no tiene pareja en la otra tabla, las columnas de esa tabla quedan vacías (`NaN`). *Todos los huéspedes, vengan de la web o de la OTA, aunque falte algún dato.*
- Filtrar **"reservas sin cobro"** equivale a una **diferencia**: los de una tabla que **no** están en la otra. En pandas no existe el operador `-` entre tablas: se hace un *left join* y se conservan las filas cuya columna de la otra tabla quedó en `NaN`.

Así que no tienes que memorizar los JOIN como una lista arbitraria de opciones de pandas: **inner es intersección, outer es unión, quedarse con los que no tienen pareja es diferencia** — y ya conoces esas tres operaciones.

### El producto cartesiano: útil, pero explosivo

El producto cartesiano A × B combina **cada** elemento de A con **todos** los de B. Su tamaño se calcula multiplicando: si `|A| = 4` y `|B| = 4`, entonces `|A × B| = 16` pares.

Con conjuntos pequeños es una herramienta útil (generar todos los menús posibles, todas las parejas cliente-producto). Pero multiplicar es traicionero a escala: **con dos tablas de un millón de filas, el producto cartesiano genera 10¹² pares** (un billón: ni te cabe en memoria ni te da tiempo a procesarlo). Ese cruce total es lo que en SQL se llama `CROSS JOIN`. Los joins reales cruzan **por clave** precisamente para no pagar ese precio: nunca hagas un `CROSS JOIN` por accidente.

## Relaciones, funciones y lógica

### Relaciones

Una **relación** conecta elementos: *Juan es amigo de Ana*; *esta reserva pertenece a este hotel*. Se representa con **pares ordenados**: `(Juan, Ana)` significa que Juan apunta a Ana, y no es lo mismo que `(Ana, Juan)`.

Formalmente, una relación entre A y B es un **subconjunto de A × B**. Traducción: de todos los pares posibles que podrías formar, la relación **elige algunos**. Que sea subconjunto significa justo eso: *no todos los pares tienen por qué estar conectados* — Ana puede ser amiga de Juan sin que todo el grupo sea amigo entre sí.

En datos, una relación es cualquier tabla de pares: `amigos.csv` con columnas `persona1, persona2`, o `reservas` con `cliente, hotel`.

### Funciones

Una **función** es una relación con una regla extra: asigna a **cada** entrada **una sola** salida. `f(usuario) → edad`:

- el **dominio** son las entradas posibles (los usuarios registrados);
- el **codominio**, las salidas posibles (las edades);
- distintos usuarios pueden tener la misma edad (dos entradas, la misma salida: **permitido**); lo que no puede haber es un usuario con dos edades distintas en la misma función (una entrada, dos salidas: **prohibido**).

En Python, un diccionario `{"Ana": 26, "Juan": 31}` se comporta exactamente como una función: claves = dominio, valores = salida. Cuando en [preproceso](preproceso.md) recodifiques una variable (agrupar edades en tramos, convertir euros a céntimos, calcular un *score*), estarás aplicando una función a cada fila.

### Lógica

La **lógica** filtra. Una **proposición** es un enunciado que es verdadero o falso, sin término medio: *Ana es mayor de edad*, *este pedido supera 50 kg*. Los operadores combinan proposiciones:

- **AND (∧):** las dos a la vez. *Es mayor de edad **y** ha comprado más de 5 veces.*
- **OR (∨):** al menos una. *Es de Santander **o** de Torrelavega.*
- **NOT (¬):** lo contrario. **No* es menor de edad.*

```text
P: edad > 18
Q: compras > 5
VIP = P ∧ Q
```

La tabla de verdad resume el funcionamiento de los tres operadores. **Se lee por filas**: cada fila es una combinación posible de P y Q (por ejemplo, la segunda fila: P falso y Q verdadero), y las columnas de la derecha dicen qué resulta de cada operador en ese caso:

| P | Q | P ∧ Q | P ∨ Q | ¬P |
| --- | --- | --- | --- | --- |
| F | F | F | F | V |
| F | V | F | V | V |
| V | F | F | V | F |
| V | V | V | V | F |

Fíjate en la diferencia clave: P ∧ Q solo es verdadero en **un** caso de los cuatro (cuando ambas son verdaderas); P ∨ Q es verdadero en **tres**. Por eso el AND filtra mucho más que el OR.

En pandas, un filtro es literalmente esta lógica aplicada columna a columna:

```python
df[(df["ciudad"] == "Madrid") & (df["edad"] > 30)]
```

Esta línea se lee por partes: `df["ciudad"] == "Madrid"` produce, para cada fila, un verdadero o falso; el `&` combina esa columna de verdictos con la de `edad > 30`; y los corchetes seleccionan las filas cuyo verdicto combinado es verdadero. Esa línea **es** lógica algorítmica aplicada al dato.

!!! warning "Paréntesis en pandas"
    Python usa `&`, `|` y `~` con Series (columnas). Cada comparación va entre paréntesis:

    ```python
    premium = df[(df["edad"] > 25) & (df["compras"] > 10)]
    ```

    No uses `and` / `or` con Series: `and` y `or` quieren un único verdadero-o-falso, y una columna son millones de ellos — pandas no sabe reducirlos a uno y lanza error.

## Grafos

### Qué es un grafo

Un grafo es la estructura matemática que modela *"cosas conectadas entre sí"*. Se escribe `G = (V, E)`:

- `V` (*vertices*): los **nodos**, las cosas — personas, ciudades, productos;
- `E` (*edges*): las **aristas**, las conexiones entre pares de nodos — amistades, carreteras, "se compró junto a".

Una red de amistades es un grafo: personas (nodos) unidas por amistades (aristas). Lo mismo que un mapa de carreteras (ciudades y conexiones) o un catálogo ("clientes que compraron X también compraron Y").

Encaja cuando la pregunta es *quién se conecta con quién*: comunidades en redes, rutas logísticas y productos que se compran juntos.

| Tipo de grafo | Pregunta | Ejemplo |
| --- | --- | --- |
| No dirigido | ¿Existe relación mutua? | Ana — Juan son amigos |
| Dirigido | ¿Quién apunta a quién? | Ana → Juan lo sigue |
| Ponderado | ¿Cuánto cuesta la conexión? | Santander → Bilbao: 102 km |

```mermaid
graph LR
  A[Ana] --- J[Juan]
  A --> M[Marta]
  M --> L[Luis]
  J --> L
```

### La lista de adyacencia

Podrías guardar el grafo como una bolsa de pares, pero para responder *"¿a quién conoce Ana?"* tendrías que revolver la bolsa entera. La **lista de adyacencia** reorganiza la información **por nodo**: un diccionario donde cada clave es un nodo y su valor, el conjunto de sus vecinos. Consultar los vecinos de Ana pasa a ser inmediato:

```python
red = {
    "Ana": {"Juan", "Marta"},
    "Juan": {"Ana", "Luis"},
    "Marta": {"Luis"},
    "Luis": set(),
}

vecinos_de_ana = red["Ana"]
```

No hace falta Gephi (una herramienta visual especializada en grafos) en esta UT. Sí reconocer dos cosas: que una tabla de aristas con columnas (`origen`, `destino`, `peso`) — como una tabla de tramos de carretera — representa un grafo; y que un *join* muchos-a-muchos entre dos tablas puede generar muchas conexiones (cada fila de una empareja con muchas de la otra).

## Lógica algorítmica

Un **algoritmo** es una receta: una secuencia de pasos con cuatro propiedades. Cada una excluye un defecto concreto:

- **ordenada** — hay un primer paso y se sabe cuál viene después (no es una lista de consejos sueltos);
- **finita** — termina en algún momento (un bucle infinito no es un algoritmo);
- **no ambigua** — cada paso se puede ejecutar sin interpretaciones ("remueve bien" no vale; "remueve 30 segundos" sí);
- **con entradas y salidas** — recibe datos y produce un resultado.

```text
Inicio
  Leer lista de importes
  Sumar
  Dividir entre el número de elementos
  Mostrar media
Fin
```

Una traducción segura a Python:

```python
def media(numeros):
    if not numeros:
        raise ValueError("No se puede calcular la media de una lista vacía")

    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)
```

Eso también puede escribirse `df["importe"].mean()`. La llamada de pandas es más corta, pero el motor todavía tiene que recorrer los valores: la función no ha desaparecido, solo está escondida.

!!! note "«Determinista», con precisión"
    Para iniciarse, significa que cada paso está claramente definido y la misma entrada produce siempre el mismo camino. En informática también existen **algoritmos aleatorizados** (que usan el azar deliberadamente); siguen siendo algoritmos aunque la misma entrada pueda recorrer caminos distintos.

## Complejidad (Big-O)

### La idea: no cuánto tarda, sino cómo crece

Dos soluciones igual de correctas pueden tardar cantidades de tiempo absurdamente distintas. La **complejidad** mide **tiempo o memoria** en función del tamaño de entrada `n` (filas, nodos, eventos).

No medimos los segundos concretos de tu portátil —dependen del hardware y la implementación—, sino **cómo crece el trabajo** cuando `n` crece. La pregunta clave es siempre la misma: *si duplico los datos, ¿qué le pasa al trabajo?* ¿Se duplica? ¿Se cuadruplica? ¿Ni se inmuta?

| Orden | Nombre | Intuición | Ejemplo |
| --- | --- | --- | --- |
| O(1) | Constante | El coste no crece con n | Acceder por clave en un `dict`, **en promedio** |
| O(log n) | Logarítmico | Partes por la mitad | Búsqueda binaria (lista **ordenada**) |
| O(n) | Lineal | Un pase | Recorrer el CSV |
| O(n log n) | Casi lineal | Divide y combina | Ordenación eficiente |
| O(n²) | Cuadrático | Cada uno con todos | Comparar cada reserva con todas las demás |

```mermaid
flowchart LR
  A["O(1)"] --> B["O(log n)"]
  B --> C["O(n)"]
  C --> D["O(n log n)"]
  D --> E["O(n²)"]
```

La cadena anterior va **de mejor a peor escalado**: O(1) es una raya plana. O(log n) crece muy despacio. O(n) sube proporcionalmente. O(n²) se vuelve inviable.

### De dónde salen las cifras

Con 1 000 000 de elementos:

- **Lineal** son ~10⁶ pasos: un pase, un paso por elemento.
- **Binaria** son ~20 pasos: cada paso descarta la mitad (10⁶ → 5·10⁵ → 2,5·10⁵ → …) y como 2²⁰ ≈ 1 048 576, unas 20 mitades bastan.
- **`n log₂ n`** son ~20 millones (10⁶ × 20).
- **Cuadrática** son ~10¹²: cada elemento contra todos los demás (10⁶ × 10⁶).

Por eso un doble bucle "para detectar duplicados" **no** es el plan en Big Data. Las alternativas que usarás: `drop_duplicates` de pandas, una **tabla hash** (un diccionario grande que "recuerda" los elementos ya vistos y permite comprobar si algo está en O(1) esperado) o una **ventana** (funciones de ventana: agrupar filas y comparar dentro de cada grupo ordenado, en lugar de contra toda la tabla).

### Lineal frente a binaria

```python
def busqueda_lineal(datos, objetivo):
    for posicion, valor in enumerate(datos):
        if valor == objetivo:
            return posicion
    return -1


def busqueda_binaria(datos_ordenados, objetivo):
    izquierda, derecha = 0, len(datos_ordenados) - 1
    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if datos_ordenados[centro] == objetivo:
            return centro
        if datos_ordenados[centro] < objetivo:
            izquierda = centro + 1
        else:
            derecha = centro - 1
    return -1
```

Para 16 elementos, binaria necesita como máximo unas 4 comparaciones (2⁴ = 16); para un millón, unas 20.

!!! warning "La búsqueda binaria no ordena gratis"
    Exige una colección **ya ordenada**. Si primero ordenas, pagas O(n log n). Para **una sola búsqueda**, recorrer O(n) puede ser más barato; para miles de consultas sobre la misma colección, ordenar o indexar sí compensa.

!!! note "Tabla hash: O(1) esperado"
    `set` y `dict` suelen buscar en O(1), pero no garantizan literalmente un paso ni O(1) en el peor caso: hay colisiones, redimensionados y coste de calcular el *hash*. El coste constante es una intuición útil del caso promedio, no una garantía absoluta.

### Cuadernos de complejidad

- [Big-O: teoría y curvas de crecimiento](https://colab.research.google.com/drive/1InYuv7O8DWM0g4mFHRIpw3-LGPrfYlxu?usp=sharing): explicación de Big-O y curvas teóricas. La curva cuadrática está dividida por 100 y el eje vertical limitado a 100; el gráfico ilustra tendencias, no segundos medidos.
- [Búsquedas en listas, conjuntos y diccionarios](https://colab.research.google.com/drive/1mZfjK-IH2qmyKHnUe2LU6kiarKepmveX?usp=sharing): búsqueda lineal y binaria en lista ordenada, seguida de búsquedas en `set` y `dict`.
- [Búsquedas, memoria y alternativa con Dask](https://colab.research.google.com/drive/1QMJKYknyyv_-pyOQ5WaNdqCZZ2u8KyPS?usp=sharing): amplía la comparación con un caso de agotamiento de RAM, una versión que libera cada colección antes de crear la siguiente y un ejemplo con Dask. La parte sobre PySpark es explicativa; no contiene un laboratorio ejecutable de Spark.

!!! warning "Ajusta el tamaño antes de ejecutar"
    El cuaderno de listas empieza con `n = 200_000_000`; su segundo ejemplo usa `200_000_00`, que son **20 millones**, aunque el comentario dice 200 millones. El de memoria utiliza 100 y 80 millones. En tu copia, cambia **cada asignación de `n`** a `100_000` para la primera prueba. En el ejemplo Dask, reduce también `CHUNK_SIZE` a `10_000`. Ejecuta por bloques y aumenta el tamaño solo después de observar el consumo de memoria.

En el ejemplo Dask, el acceso por índice no es una búsqueda hash. La llamada a `np.searchsorted` tampoco constituye por sí sola una medición comparable de búsqueda binaria distribuida. Utiliza las funciones explícitas sobre listas para comparar algoritmos, y el bloque Dask para observar el procesamiento por bloques.

!!! failure "Trampa de aula"
    «Como pandas es rápido, la complejidad da igual.» pandas **esconde** el bucle. Si tu idea es O(n²), el clúster también pagará shuffle y tiempo. El criterio a) es elegir la operación, no el logo.

## Combinatoria (visión aplicada)

La combinatoria estudia **cuántas formas** hay de ordenar o elegir elementos. Antes de las fórmulas, una notación: `n!` (*factorial de n*) es el producto de todos los enteros desde n hasta 1: `4! = 4·3·2·1 = 24`. Es, por ejemplo, el número de formas de ordenar 4 personas en una fila.

Los cuatro conceptos, cada uno con su pregunta característica:

- **Producto cartesiano:** todos los pares entre conjuntos; `|A × B| = |A| · |B|`. *¿Cuántos menús puedo formar con un entrante y un plato?*
- **Permutaciones:** ordenar **todos** los elementos; `n!`. *¿De cuántas formas ordeno la cola completa?*
- **Variaciones:** elegir y ordenar `k` de `n`; `n! / (n-k)!`. *¿Cuántos podios (1º, 2º, 3º) hay con 8 corredores?*
- **Combinaciones:** elegir `k` de `n` **sin importar el orden**; `n! / (k!(n-k)!)`. *¿Cuántos equipos de 3 salen de 8 personas?*

El detalle que distingue los dos últimos: ¿importa el orden? ¿Código PIN `123` y `321` cuentan distinto? **Sí**: importa el orden (variaciones). ¿Un comité formado por Ana, Luis y Marta cambia por escribir Marta, Ana y Luis? **No**: es la misma combinación.

```python
from itertools import combinations, permutations, product

entrantes = ["Sopa", "Ensalada", "Gazpacho", "Croquetas"]
platos = ["Pollo", "Pescado", "Pasta"]

menus = list(product(entrantes, platos))      # 4 · 3 = 12
ordenes = list(permutations(["A", "B", "C"])) # 3! = 6
parejas = list(combinations(["A", "B", "C"], 2))
```

Aplicación: escenarios, optimización, "clientes que compraron A también compraron B". Cuaderno: [combinatoria](https://colab.research.google.com/drive/1lOe3pA0-L7iGGNWAmDtZwt1ZxXv4L-zO?usp=sharing).

### Teoría de grupos (solo reconocimiento)

Este concepto aparece en algunos temarios, así que conviene haberlo oído. Un **grupo** es un conjunto con una operación que cumple cuatro propiedades: operar dos elementos da otro elemento del mismo conjunto (*cierre*); el orden de agrupar no cambia el resultado (*asociatividad*); hay un elemento que no altera nada — como el 0 en la suma (*neutro*); y cada elemento tiene otro que lo deshace — como −x deshace +x (*inverso*). Los números enteros con la suma forman un grupo.

La teoría formal es avanzada y aparece en cifrado y simetrías; **no** la aplicarás en esta UT. Y una precisión que evita un error típico: **vectores y matrices no son, por sí solos, teoría de grupos** (eso es álgebra lineal, otra cosa). Basta con reconocer el concepto.

## Representar la información

Un **dataset** es un conjunto organizado de datos. En una tabla, cada fila es una observación (cliente, compra, sensor en un instante) y cada columna, un atributo (edad, precio, fecha). No todo dataset tiene que ser tabular: una colección de imágenes etiquetadas también lo es.

En Big Data puede contener millones o miles de millones de observaciones: por eso la estructura elegida afecta a memoria, recorrido y búsqueda.

| Estructura | Idea | Ejemplo |
| --- | --- | --- |
| Vector | Secuencia ordenada | Temperaturas `[20, 21, 23, 22]` |
| Matriz | Tabla filas × columnas | Usuario × producto en un recomendador |
| Tabla de decisión | Reglas en forma tabular | Edad>18 ∧ compras>5 → VIP |
| Árbol | Jerarquía | Categorías de Amazon |
| Grafo | Relaciones | Red social, rutas |
| Tabla hash | Búsqueda ~O(1) | `dict` de Python |

Cuaderno: [vectores, matrices y estructuras](https://colab.research.google.com/drive/1W1yXeDfUYtK2BtPVmWIHRrnu7oD1EihK?usp=sharing).

### Vector y matriz en Python

```python
import numpy as np

temperaturas = np.array([20, 21, 23, 22])
print("media:", temperaturas.mean())

compras = np.array(
    [
        [2, 1, 3],  # Ana
        [0, 2, 1],  # Juan
        [3, 0, 2],  # Marta
        [1, 1, 4],  # Luis
    ]
)

print("total por cliente:", compras.sum(axis=1))
print("total por producto:", compras.sum(axis=0))
```

`axis=1` suma a lo largo de las columnas (una cifra por fila/cliente). `axis=0` baja por las filas (una cifra por columna/producto).

### Tabla de decisión

| Edad > 18 | Compras > 5 | VIP |
| --- | --- | --- |
| Sí | Sí | Sí |
| Sí | No | No |
| No | Sí o no | No |

Es la misma regla que `edad > 18 AND compras > 5`, expresada para que negocio pueda revisarla sin leer Python: cada fila de la tabla es un caso, y la última columna dice qué decide la regla.

!!! example "En voz alta"
    Tienes 5 millones de logs y quieres las visitas de una IP. ¿Recorres el fichero cada vez (O(n) por consulta) o indexas/particionas por IP?

## Actividades (hacer en Colab)

**1. Conjuntos y lógica.** Objetivo: practicar operaciones con conjuntos y aplicar una regla lógica a clientes. A = {Ana, Juan, Marta, Luis} compraron X; B = {Marta, Luis, Sofía, Pedro} compraron Y. Calcula A ∪ B, A ∩ B, A − B.

Premium si edad > 25 **y** compras > 10:

| Cliente | Edad | Compras |
| --- | --- | --- |
| Ana | 28 | 12 |
| Juan | 22 | 15 |
| Marta | 30 | 8 |
| Luis | 35 | 20 |
| Sofía | 24 | 5 |

**2. Matriz** (Móvil / Portátil / Auriculares). Objetivo: representar datos bidimensionales y extraer totales por fila y columna:

| | Móvil | Portátil | Auriculares |
| --- | --- | --- | --- |
| Ana | 2 | 1 | 3 |
| Juan | 0 | 2 | 1 |
| Marta | 3 | 0 | 2 |
| Luis | 1 | 1 | 4 |

¿Quién compró más en total? ¿Qué producto es el más popular?

**3. Combinatoria.** Objetivo: contar y enumerar posibilidades en un caso real. Entrantes {Sopa, Ensalada, Gazpacho, Croquetas} × platos {Pollo, Pescado, Pasta}. Primero calcula cuántos menús pueden formarse y después escribe **todas** las combinaciones (1+1). Solución esperada: **12**.

**4. Árbol.** Objetivo: representar una regla de negocio como árbol de decisión. Dibuja las dos decisiones y sus ramas. Si edad > 25 y compras > 5 → descuento. Aplícalo a Ana 28/12, Juan 22/3, Marta 19/6, Luis 35/4.

??? check "Autocorrección: abre después de intentarlo"
    **Actividad 1**

    - `A ∪ B = {Ana, Juan, Marta, Luis, Sofía, Pedro}`.
    - `A ∩ B = {Marta, Luis}`.
    - `A − B = {Ana, Juan}`.
    - Premium (`edad > 25` **y** `compras > 10`): **Ana y Luis**.

    **Actividad 2**

    - Total por cliente: Ana 6, Juan 3, Marta 5, Luis 6. Máximo: **empate entre Ana y Luis**.
    - Total por producto: móvil 6, portátil 4, auriculares 10. Más popular: **auriculares**.

    **Actividad 3**

    - `4 entrantes × 3 platos = 12 menús`.

    **Actividad 4**

    - Solo **Ana** recibe descuento: Luis supera la edad, pero no `compras > 5`; Marta supera compras, pero no edad. Es AND, no OR.

### Plantilla de entrega

En una sola celda Markdown, antes del código:

```markdown
## Problema
(Qué se pregunta)

## Representación elegida
(conjunto, matriz, tabla, árbol o grafo; por qué)

## Algoritmo
(pasos o pseudocódigo)

## Complejidad
(orden Big-O y qué significa cuando crece n)

## Resultado
(valor obtenido y una comprobación)
```

El cuaderno de **tipos de datos y fundamentos** repasa tipos, mutabilidad y serialización JSON; después desarrolla conjuntos, lógica, grafos, matrices, combinatoria y búsquedas. Termina con **tres actividades distintas** de las cuatro anteriores: conjuntos de tiendas, matriz de recomendaciones 4×4 y suma de números pares con análisis de complejidad. El árbol de clasificación con scikit-learn es una ampliación. Enlace: [Tipos de datos y fundamentos en Python](https://colab.research.google.com/drive/1zLLp2cZTXoTCLczo8ibElVPZX7eIZEPx?usp=sharing).

## Miniproyecto de compras

El [Miniproyecto de compras y relaciones entre productos](https://colab.research.google.com/drive/1YYxgnXcdUw0_qgwGdYeGwvOjxh-dLlsj?usp=sharing) repite primero los ejemplos de matemática discreta y después presenta **«Mini-proyecto integrador: de transacciones a conocimiento»**. El código ya está resuelto: genera 5.000 cestas simuladas para 200 clientes y 12 productos, analiza intersecciones de clientes, construye un grafo de co-compra, calcula clientes VIP y representa ventas y productos.

Una fila representa un producto de una cesta, por lo que habrá más de 5.000 filas. Para relacionar productos, el código agrupa por **cliente y fecha**, no por un identificador único de ticket. El criterio VIP utiliza gasto y número de **líneas** por encima del percentil 80. Ejecuta los bloques, modifica un parámetro y explica cómo afecta al resultado.

## Estudio de logística

Completa las celdas `# --- TU CÓDIGO AQUÍ ---` del cuaderno de conjuntos, relaciones, funciones, lógica y grafos:

[Logística: cuaderno de actividades](https://colab.research.google.com/drive/1cWbe73qRxhDEDg5FCM-Fdwj8GvIVLj58?usp=sharing)

No conviertas el cuaderno en cinco ejercicios aislados. Cuenta una historia:

1. **Conjuntos:** pedidos atendidos por cada centro y operaciones entre ellos.
2. **Relaciones:** asignación de camiones a rutas y propiedades de esa relación.
3. **Funciones:** peso, coste y tarifa de los pedidos, con recargos.
4. **Lógica:** pedidos urgentes, pesados, peligrosos y orden de prioridad.
5. **Grafos:** centros conectados por carreteras y centralidad de grado; el grafo base no asigna pesos a las aristas.

Evidencia:

- [ ] Todas las celdas `TU CÓDIGO AQUÍ` están completadas.
- [ ] Cada salida tiene una frase que la interpreta.
- [ ] La estructura elegida está justificada.
- [ ] Hay al menos una comprobación del resultado.
- [ ] Se explica la complejidad de una búsqueda o recorrido.

## Solución de referencia (profesorado)

- Las cuatro actividades de esta página (conjuntos, matriz, menús y descuento), resueltas: [Cuatro actividades resueltas de fundamentos](https://colab.research.google.com/drive/14PapYsQgCl1E8a2Nm1mKHrGNOTQ14dVd?usp=sharing).
- Logística resuelta: [Logística: tareas resueltas](https://colab.research.google.com/drive/1H0_0yrT77FVNvCoxepL4bRy-dHlhf6ij?usp=sharing).

En la matriz de compras hay empate entre **Ana y Luis** (6 unidades). El cuaderno resuelto muestra un solo nombre con `idxmax()`; la respuesta completa debe mencionar a ambos.

Úsalas **después** de intentar el problema. Una solución que se ejecuta pero que no puedes explicar no demuestra el criterio **a)**.

Índice de todos los cuadernos: [Cuadernos Colab](cuadernos.md).

## Correcciones y precisiones

1. **Permutación frente a variación.** Si se eligen `k` de `n` y el orden importa, son **variaciones**; una permutación ordena los `n` elementos.
2. **Tabla hash O(1).** Es coste esperado o promedio, no una garantía absoluta.
3. **Búsqueda binaria.** Los ~20 pasos para un millón presuponen una lista **ordenada**; ordenar desde cero cuesta O(n log n).
4. **Algoritmo determinista.** Es una propiedad útil para iniciarse, pero existen algoritmos aleatorizados. El requisito general es que los pasos estén definidos.
5. **Teoría de grupos.** La operación debe cumplir el **cierre**; además, álgebra lineal no es sinónimo de teoría de grupos.
6. **Dataset.** Un dataset no se limita a filas y columnas. Una colección de imágenes o grafos también puede ser un dataset.
7. **Gráfico de complejidad.** La curva O(n²) está dividida por 100 y el eje vertical corta las curvas al llegar a 100. Sirve como intuición, pero no para comparar valores reales; por eso aquí se dan órdenes y cifras explícitas.
8. En la actividad de matriz, "quién compró más productos" significa **más unidades en total**, no más categorías distintas.

## Referencias para consultar

Para implementar los ejemplos:

- [Python — conjuntos](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Python — `itertools`](https://docs.python.org/3/library/itertools.html)
- [Python — complejidad temporal de estructuras](https://wiki.python.org/moin/TimeComplexity)
- [NumPy — introducción y creación de arrays](https://numpy.org/doc/stable/user/absolute_beginners.html)

## Resumen del tema

- Matemática discreta (conjuntos, relaciones, combinatoria, grafos) modela el dato.
- Un algoritmo es una secuencia finita de pasos con entradas y salidas.
- La complejidad dice si el paso escala.
- Estructuras: vectores, matrices, grafos, árboles, tablas de decisión.
- El modelado sigue en [modelado](modelado.md); extraer, en [1.3](extraccion.md).

!!! success "Al terminar 1.2"
    Ante un problema sabes elegir una representación, escribir una regla o algoritmo, estimar cómo crece su coste y comprobar el resultado. Eso es aplicar matemática discreta y lógica algorítmica al dato, no memorizar símbolos.
