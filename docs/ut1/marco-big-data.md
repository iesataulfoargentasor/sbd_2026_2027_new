---
title: 1.0 Marco Big Data
tags:
  - SBD
  - RA1
---

# 1.0. Marco: qué es Big Data (paquete de introducción)

Este apartado incorpora el paquete eXe *UT1 Introducción a Big Data SBD*. En BDA ya diseñaste el almacén; aquí el marco sirve para **situar el análisis**: de dónde sale el valor, quién lo extrae y en qué tipo de almacén consultas.

Los datos son el “petróleo del siglo XXI” (Clive Humby, 2006), pero en los 2020 **almacenar no basta**: hay que comprenderlos y gestionarlos. *Big* implica volúmenes que un solo equipo no sostiene: hace falta computación distribuida o nube. Aun así, mucho problema de empresa local se resuelve con *small data*; las técnicas de esta UT también sirven a esa escala.

## Las V (de 3 a 7)

Al principio bastaban **3 V** para reconocer un problema Big Data:

| V | Qué mira |
| --- | --- |
| **Variedad** | Fuentes y tipos: estructurado (tablas), semiestructurado (JSON), no estructurado (correo, imagen, audio) |
| **Volumen** | Cantidad; a menudo no cabe en la RAM de un sistema clásico (TB o más) |
| **Velocidad** | Ritmo de captura y proceso, a veces casi en tiempo real |

Luego se añadieron **valor** (el dato tiene que mejorar una decisión) y **veracidad** (fiabilidad; sin exploración el análisis miente). Otras dos completan un mapa de **7 V**: **viabilidad** (qué datos hacen falta de verdad) y **visualización** (KPI y gráficos comprensibles). El RA2 de SBD profundiza en cuadros de mando; aquí reconoces por qué existen.

## Ciencia de datos (pasos, no un producto)

1. Definir el objetivo con quien decide.
2. Recopilar internos y externos (bruto).
3. Preparar: limpiar, transformar, combinar.
4. Explorar: patrones y correlaciones.
5. Modelar (a menudo con IA) si la pregunta lo pide.
6. Presentar y, si cambia el dato, iterar.

Eso es el mismo ciclo que planificarás en [1.6](planificacion.md) y ejecutarás en [1.3](extraccion.md)–[1.4](preproceso.md).

## Analítica y BI

Las aplicaciones Big Data **recogen** de muchas fuentes. La inteligencia de negocio (**BI**) se pregunta **cómo usa** la empresa esos datos.

- Descriptiva: ¿qué sucedió?
- Diagnóstica: ¿por qué?
- Con Big Data e IA: **predictiva** (¿qué pasará?) y **prescriptiva** (¿qué debería ocurrir / cómo evitarlo?).

El detalle de los tres tipos (más el reloj lote/flujo) está en [1.1](ciclo-analisis.md).

## Data warehouse y data lake

El **warehouse** centraliza analítica **OLAP** sobre dato **estructurado**, *schema-on-write*, de solo lectura (el CRUD vive en OLTP). Sale de ETL: extraer, limpiar, transformar, cargar. Sirve a informes e histórico.

El **data lake** guarda el **bruto** (JSON, imagen, PDF, log) y transforma después. Necesita almacén distribuido que crezca: HDFS on-prem o, cada vez más, **S3** / Blob. Eso es el destino del [laboratorio AWS](laboratorio-aws.md).

No eliges uno “para siempre”: el lake para explorar; el warehouse para el panel del lunes.

## Roles

| Rol | Oficio |
| --- | --- |
| **Analista de datos** | Convierte dato en información de negocio (SQL, visualización) |
| **Científico de datos** | Modelos de IA; base matemática y estadística |
| **Ingeniero de datos** | Diseño y mantenimiento de ETL, cloud y almacenes (el perfil más cercano a FP) |
| **Arquitecto de datos** | Infraestructura, escalabilidad, gobierno, linaje y seguridad |

El arquitecto elige el tablero; el ingeniero mueve el dato; el científico extrae conocimiento. En esta UT1 actúas sobre todo como **ingeniero/analista**.

## Casos de uso

- Industria 4.0: sensores IoT.
- Streaming de vídeo: recomendación a partir del comportamiento.
- Mapas: rutas con histórico y tráfico en vivo.
- Redes sociales: sentimiento sobre un producto o tendencia.

## Actividad de aula (paquete Introducción a Big Data)

**Parte 1 — Reflexión.** ¿Cuál de las V te parece la más importante y por qué? ¿Qué servicio de tu día a día sería difícil de sustituir y qué V le duele?

**Parte 2 — Landscape.** En el [mapa Firstmark](https://mad.firstmark.com/) (vista [card](https://mad.firstmark.com/card)), elige tres herramientas que vayan a salir en el ciclo (por ejemplo Kafka, Spark, Athena). Anota **categoría** y **una alternativa** de la misma fila.

!!! info "No sustituye a BDA"
    Las 5 V y el lake/warehouse se *imparten* como diseño en BDA. Aquí el paquete se recupera para no perder el material de Moodle y para hablar el mismo idioma cuando extraigas y consultes.
