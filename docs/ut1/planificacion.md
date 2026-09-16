---
title: "1.3. Planificación del proyecto de análisis"
tags: [SBD, RA1]
---

# 1.3. Planificación del proyecto de análisis

**CE que se trabajan:** e. Consulta el [texto oficial](ra1.md).

**Al terminar:** convertir preguntas en tareas priorizadas con dependencias, estimaciones y seguimiento real.

## Un objetivo que se pueda cerrar

«Analizar reservas» no permite saber cuándo hemos terminado. Un objetivo útil es: «obtener reservas y cancelaciones por hotel y canal para septiembre de 2026, verificadas con la muestra y con un ensayo de volumen documentado». El resultado esperado incluye corrección y límites, no solo un fichero.

Separa lo imprescindible (claves válidas, indicador correcto, ejecución repetible) de lo deseable (una segunda fuente opcional o una presentación más elaborada). Si falta tiempo, protege primero la respuesta verificable.

| Tarea | Prioridad | Dependencia | Estimación inicial | Criterio de cierre |
| --- | --- | --- | ---: | --- |
| Definir indicadores | Alta | Encargo | 30 min | Fichas con población y denominador |
| Inventariar fuentes | Alta | Indicadores | 45 min | Diccionario con claves y unidades |
| Preparar y validar | Alta | Inventario | 90 min | Rechazos explicados y copia original |
| Integrar | Alta | Validación | 90 min | Recuentos e importes conservados |
| Calcular y contrastar | Alta | Integración | 60 min | Resultado manual y automático coinciden |
| Ensayar escala | Alta | Resultado correcto | 60 min | Filas, bytes, tiempo y entorno registrados |
| Ampliar preguntas | Media | Resultado correcto | 45 min | Nuevo indicador con límites |
| Defender | Alta | Mediciones | 30 min | Conclusión y revisión del plan |

Son estimaciones para organizar el trabajo del equipo, no duración oficial ni reparto de toda la UT. Añade margen para incidencias y registra después el tiempo real.

## GitHub Issues y Projects como evidencia

1. Crea un Project del equipo y vincula el repositorio de la práctica.
2. Usa un tablero con «Por hacer», «En progreso», «Bloqueado» y «Hecho».
3. Crea una Issue por resultado verificable. Añade responsable, prioridad, estimación y enlace a las tareas de las que depende.
4. Usa campos de fecha o iteración para situar el trabajo. Si el centro emplea otra configuración de Projects, conserva la misma información.
5. Vincula la Issue con el código, informe o resultado que demuestra su cierre. Mover una tarjeta no sustituye la evidencia.

Ejemplo de contenido de una Issue:

```text
Título: Integrar reservas con el catálogo sin multiplicar filas
Objetivo: una fila por id_reserva con hotel y localidad.
Depende de: validación de claves del catálogo.
Prioridad: alta. Responsable: integrante asignado. Estimación: 90 min.
Aceptación:
- Cero claves huérfanas y catálogo único por id_hotel.
- Mismo número de reservas y mismo importe antes/después.
- Ejecución y controles enlazados.
```

Consulta las [funciones de Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). El CE e se evidencia con las decisiones y el seguimiento; no depende de automatizaciones avanzadas de GitHub.

## Mini-sprints y revisión

Un mini-sprint es un intervalo corto de trabajo con un resultado concreto. Primero cierra una muestra correcta; después, integración y análisis; por último, escala y defensa. Al comenzar cada sesión revisa bloqueos. Al terminar, actualiza tiempo real y siguiente paso.

Si el catálogo tiene claves duplicadas, registra la incidencia, quién debe resolverla y qué tareas quedan bloqueadas. Puedes avanzar el diccionario o el contraste manual mientras se aclara la fuente. Evita mantener todas las tareas «En progreso».

!!! example "Práctica y comprobación"
    Crea al menos seis Issues con dependencias y criterios de cierre, y conserva una vista inicial y otra final del tablero. Introduce una incidencia real o simulada y explica qué tarea reprogramaste y por qué. Un tablero creado al final con todo en «Hecho» no demuestra seguimiento.

Para la [práctica integradora](practica.md), entrega el enlace al tablero y una comparación de tres estimaciones con sus tiempos reales. Explica una desviación sin modificar retrospectivamente el plan inicial.
