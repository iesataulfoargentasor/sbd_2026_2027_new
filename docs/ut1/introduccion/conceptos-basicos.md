---
title: "2. Conceptos básicos"
---

# 2. Conceptos básicos

### 2.1 Integración de datos

**Definición**: proceso de **combinar datos de diferentes fuentes** (bases de datos, sensores, archivos, redes sociales, etc.) para obtener una visión unificada y coherente.

**Ejemplo sencillo:**

Una empresa de logística puede tener:

- Base de datos de clientes.
- Sensores GPS de camiones.
- Registros de almacén.
- Integrar esos datos permite ver **qué cliente recibió un pedido, por qué ruta pasó y cuánto tardó**.

**El proceso ETL**

El método más común para integrar datos es el **proceso ETL**:

1. **Extract (Extracción)**:

    - Se obtienen los datos desde sus fuentes originales.
    - Ejemplo: descargar registros de ventas de una base de datos SQL y comentarios de clientes de Twitter.

2. **Transform (Transformación)**:

    - Se limpian, normalizan y adaptan los datos para que tengan un formato uniforme.
    - Ejemplo: convertir todas las fechas a un mismo formato (dd/mm/aaaa), eliminar duplicados, corregir errores tipográficos.

3. **Load (Carga):**

    - Los datos ya transformados se cargan en un sistema de almacenamiento central (como un Data Warehouse o un Data Lake).
    - Ejemplo: guardar todos los registros limpios en una base de datos para consultas posteriores.


Resultado: un único conjunto de datos coherente que combina múltiples fuentes.

### 2.2 Procesamiento de datos

**Definición**: conjunto de operaciones que transforman los datos en bruto en información útil.

Existen dos grandes tipos:

**a) Procesamiento por lotes (Batch Processing)**

- Los datos se recogen durante un periodo de tiempo y se procesan juntos en **bloques grandes**.
- Características:

    - Adecuado para grandes volúmenes de datos históricos.
    - No es inmediato: hay un **retraso** entre la recogida y el resultado.
    - Herramientas: **Hadoop, Spark batch**.

- Ejemplo: calcular todas las ventas de un supermercado al final del día.

**b) Procesamiento en tiempo real (Stream Processing)**

- Los datos se procesan **a medida que llegan**, en cuestión de segundos o milisegundos.
- Características:

    - Respuesta casi instantánea.
    - Útil cuando la rapidez es crítica.
    - Herramientas: **Apache Kafka, Flink, Spark Streaming**.

- Ejemplo: detección de fraude en una tarjeta de crédito en el momento de la transacción.

Diferencia clave:

- **Batch**: precisión y volumen (¿qué pasó ayer?).
- **Streaming**: inmediatez y reacción (¿qué está pasando ahora?).

### 2.3 Análisis de la información

**Definición**: aplicar métodos matemáticos, estadísticos y computacionales para **extraer conocimiento de los datos**.

**Tipos de análisis**

1. **Análisis descriptivo** → Explica lo que ya pasó.

    - Ejemplo: "El 30% de clientes compraron online el mes pasado."

2. **Análisis predictivo** → Intenta anticipar lo que pasará.

    - Ejemplo: "Se espera un aumento de ventas de un 10% en Navidad."

3. **Análisis prescriptivo** → Propone acciones a tomar.

    - Ejemplo: "Para aumentar ventas, invertir más en publicidad en redes sociales."


Lo importante: el análisis convierte **datos** → en **información** → en **decisiones**.

[← 1. Introducción: el valor de los datos](valor-datos.md) · [3. Arquitecturas de sistemas de datos (visión general) →](arquitecturas.md)

---

Material docente original aportado por el profesor, procedente de eXeLearning. Se conserva la licencia [Creative Commons Reconocimiento–CompartirIgual 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Adaptación de formato para estos apuntes.
