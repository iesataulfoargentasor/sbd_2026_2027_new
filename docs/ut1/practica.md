---
title: "1.13. Práctica integradora RA1"
tags: [SBD, RA1]
---

# 1.13. Práctica integradora RA1

**CE que se trabajan:** a–g. Consulta el [texto oficial](ra1.md).

**Al terminar:** entregar y defender un análisis reproducible con evidencias de los siete criterios.

## Encargo

Dirección solicita reservas y cancelaciones por hotel y canal en el periodo de la muestra. Debes construir una respuesta reproducible, explicar sus límites y comprobar que sigue funcionando con más datos.

## Secuencia

1. Redacta tres preguntas y define población, periodo y unidad.
2. Planifica tareas, dependencias, prioridades y tiempos.
3. Genera datos y conserva las fuentes; documenta el diccionario.
4. Introduce un error en una copia y acredita su detección.
5. Integra fuentes sin multiplicar reservas.
6. Calcula y contrasta la muestra con la tabla de referencia.
7. Amplía el volumen según el equipo y registra ejecución y límites.
8. Ejecuta el ensayo incremental e interpreta sus dos estados.
9. Revisa el plan y entrega conclusiones comprensibles.

El laboratorio resuelto es apoyo. Para tu entrega añade el análisis por canal, explica cada comprobación y trabaja la variación que asigne el profesor; ejecutar el script sin comprenderlo no acredita todos los criterios.

## Evidencias y criterios

| CE | Entrega |
| --- | --- |
| a | Comparación de algoritmos y explicación de predicados y relaciones |
| b | Código ejecutado, volumen ampliado y resultados comprobados |
| c | Inventario de fuentes y combinación efectiva |
| d | Diagrama de relaciones, granularidad y controles de joins |
| e | Plan inicial, seguimiento y revisión |
| f | Justificación de sistemas y recorrido de entrada a salida; integración MongoDB si la asigna el profesor |
| g | Calidad, tiempos, recursos y valoración de coste |

Las ponderaciones, fechas y modalidad de entrega se publican en Moodle. El cuestionario de la web es formativo.

## Qué entregar

- Informe breve del problema, plan y conclusiones.
- Diccionario y esquema de relaciones.
- Código, versiones y pasos para reproducir.
- Datos sintéticos o parámetros de generación.
- Resultados y controles; fichero de métricas y evidencias del flujo.

No incluyas contraseñas. No basta una captura del resultado: debe poder repetirse. Evita afirmaciones causales y declara que el importe es nominal y la cancelación se define por existencia de evento.

## Revisión final

¿Se conservan las reservas al unir? ¿El denominador es correcto? ¿El resultado cambia si repites un evento? ¿Has medido realmente el volumen declarado? ¿Puede otra persona explicar por qué tu conclusión se sostiene?

## Proyecto ampliado: reservas, catálogo, opiniones y eventos

Mantén la referencia original para comprobar los totales y añade `opiniones.json` siguiendo [integración](integracion.md). La nueva salida tendrá una fila por reserva con atributos de hotel, cancelación y contexto de opiniones. No cambies los totales originales al añadir contexto. Si amplías datos, genera identificadores y relaciones coherentes; no uses la repetición de claves como simulación de volumen válida.

El ensayo mínimo combina CSV y JSON/JSONL. Añade además una extracción desde SQL, API o MongoDB suministrada por el profesor y documenta su integración efectiva. El [laboratorio AWS](aws-s3-glue-athena.md) aporta otra evidencia de selección de sistemas cuando esté disponible. Justifica la alternativa con requisitos de acceso, volumen, latencia, reproducibilidad y coste.

### Hitos y criterios de aceptación

| Hito | Evidencia verificable | CE |
| --- | --- | --- |
| Pregunta y plan | Issues/Project con objetivos, prioridades, dependencias, tiempos y revisiones | e |
| Razonamiento | Conjuntos, predicado, grafo y comparación ejecutada de dos algoritmos | a |
| Fuentes | Diccionario con tipos, unidades, origen, claves, periodo y extracción repetible | c, f |
| Preparación | Reglas, originales, recuentos de aceptados/rechazados y decisiones sobre nulos/outliers | b, d, g |
| Integración | Reservas + hoteles + opiniones resumidas + cancelaciones; controles de cardinalidad | c, d |
| Spark y análisis | DataFrames/SQL, indicadores definidos y contraste de muestra | a, b |
| Escala y flujo | Volumen ampliado medido y evolución de un flujo con ventanas | b, f, g |
| Decisión final | Comparación equivalente, calidad y justificación de sistemas y costes | f, g |

### Organización de la entrega

```text
README.md                 Pasos, versiones, parámetros y limitaciones
plan/                     Plan inicial, seguimiento y revisión; enlace a Projects
diccionario.md            Fuentes, granularidad, claves, unidades y reglas
codigo/                   Extracción, preparación, integración y análisis
evidencias/               Controles, resultados pequeños y métricas
informe.md                Preguntas, resultados, decisiones y límites
```

Mantén datos sintéticos pequeños o un generador; no subas grandes datasets ni secretos. Distingue el script base resuelto de tus extensiones. En el ensayo ampliado declara cuántas filas y bytes has procesado realmente: 60 000 reservas son un escalón de prueba, no una definición de Big Data. El profesor concretará el volumen y entorno para CE b, y la evidencia debe reflejar lo ejecutado.

### Defensa individual

Prepara respuestas con el código y datos delante:

1. ¿Qué predicado decide aceptar una reserva y qué hace con nulos?
2. ¿Por qué el join no duplica importes? Demuéstralo con un caso conflictivo.
3. ¿Por qué la media de opiniones del hotel no describe a cada huésped?
4. ¿Qué tarea cambió durante el proyecto y cómo alteró la secuencia?
5. ¿Qué transformación requiere intercambio y qué has medido realmente?
6. ¿Qué sistema sustituirías si cambia el volumen o no hay acceso cloud?
7. ¿Qué conclusión sería injustificada con estas fuentes?

!!! success "Revisión de cierre"
    Otra persona debe poder repetir el análisis de la muestra y obtener seis reservas, 15 noches, 1 660 euros nominales y dos canceladas. Las opiniones no cambian esos totales. La entrega ampliada debe incluir al menos un fallo detectado y una decisión corregida, junto con evidencias de los siete CE; Docker no se evalúa como competencia RA1.
