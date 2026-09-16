---
title: 1.1 Integrar, procesar y analizar
tags:
  - SBD
  - RA1
---

# 1.1. Integrar, procesar y analizar

!!! warning "Inicio con Python (antes de seguir)"
    Consulta este cuaderno antes de las prácticas:

    **[Inicio con Python](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)** · [página del cuaderno](inicio-python.md)

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

## Actividad práctica (nivel inicial) — ETL en Colab

El cuaderno *Inicio con Python* prepara las herramientas básicas para las prácticas de análisis y fundamentos.

Vídeo de aula (Educantabria / SharePoint): [técnicas de análisis y ETL en Colab](https://educantabria-my.sharepoint.com/:v:/g/personal/jose_martin_educantabria_es/EeKBcqViPHZMn0uMthdtUJkBkyb1SHk3crRjD2Rrd8gEPQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=b1SA87).

Tenéis que desarrollar, en Google Colab, un ETL mínimo:

1. Se genera un CSV de clientes con errores (fechas en distintos formatos, duplicados, valores faltantes).
2. **Extracción:** abrir y leer el fichero (Excel o Python).
3. **Transformación:** unificar fechas, eliminar duplicados, corregir erratas.
4. **Carga:** guardar el resultado limpio en un CSV nuevo.
5. Un recuento sencillo: clientes por ciudad y edad media.

Eso convierte dato bruto en información útil. La evidencia no es “haber abierto Colab”: es el fichero limpio y el resumen.

Crea un cuaderno nuevo en Colab para resolver esta actividad. El curso básico de Python sirve como preparación; el cuaderno resuelto de ETL permite contrastar tu trabajo.

- Preparación: Python básico — [Inicio con Python](https://colab.research.google.com/drive/14JeRxBG1KoCPKAJGbQyWnSoG_NuiLkxJ?usp=sharing)
- Solución de referencia (profesorado): [ETL de clientes resuelto](https://colab.research.google.com/drive/1wm6x06U3FGy7VEgpXbaTIcTo3-Q4mp2r?usp=sharing)

El cuaderno resuelto simula la extracción creando un diccionario y un DataFrame; no lee un CSV de entrada. Para cumplir el enunciado de esta actividad, añade la creación y lectura del CSV antes de aplicar la limpieza. La exportación con `to_csv` guarda el resultado en la sesión de Colab; descárgalo desde el panel de archivos para entregarlo.

El listado completo de cuadernos de la unidad está en [Cuadernos Colab](cuadernos.md).

## Procesamiento: el reloj

| Modalidad | Idea | Pregunta | Familia (nombres, no despliegue) |
| --- | --- | --- | --- |
| **Batch** (lotes) | Procesas un bloque al cabo de un periodo | *¿Qué pasó ayer?* | Hadoop, Spark en lote, un script pandas, un job nocturno |
| **Streaming** (flujo) | Procesas a medida que llega | *¿Qué está pasando ahora?* | Kafka, Flink, Spark Streaming |

El lote encaja con el cierre de cobros del hotel. El flujo, con el fraude de una tarjeta o el semáforo de habitación libre. Streaming **no** es latencia cero: tiene un plazo objetivo.

Estas son cuatro arquitecturas habituales (visión general, sin desplegarlas):

| Receta | Idea |
| --- | --- |
| Data warehouse | Dato estructurado, listo para informe |
| Data lake | Cualquier tipo, como llegó |
| **Lambda** | Un camino batch y un camino streaming **en paralelo** |
| **Kappa** | Casi todo entra por streaming; el histórico se reprocesa con el mismo flujo |

El detalle de warehouse y lake está en el [marco](marco-big-data.md). Aquí eliges el **reloj de tu consulta**.

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

## Resumen del tema

- Los **datos** por sí solos no son útiles: hay que integrarlos, procesarlos y analizarlos.
- La **integración** se hace con procesos como **ETL**.
- El **procesamiento** puede ser en **lotes** (batch) o en **tiempo real** (streaming).
- El **análisis** puede ser descriptivo, predictivo o prescriptivo.
- El mismo ciclo se aplica en banca, entretenimiento, industria, etc.

!!! success "Al terminar 1.1"
    Di, con un caso, las tres frases: qué fuentes unes, si el proceso es lote o flujo, y si el resultado describe, predice o prescribe. Después extraes de verdad en [1.3](extraccion.md).
