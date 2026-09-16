---
title: 1.6 Planificación con GitHub Projects
tags:
  - SBD
  - RA1
---

# 1.6. Planificar el análisis (GitHub Projects)

El criterio **e)** no pregunta “¿sabes Scrum de memoria?”. Pregunta si **cierras un trabajo de datos a tiempo**: objetivo, prioridades, orden y reloj.

En un proyecto de análisis siempre hay más ideas que sesiones. Si no priorizas, el cuaderno queda a medias y el resumen —lo único que el cliente usa— no existe.

## Por qué planificar

Limpiar `clientes_actividad.csv` parece “una tarde”. Sin plan: tres personas pican el mismo `replace`, nadie genera el recuento por ciudad y el gráfico se come el tiempo. Con plan: el grupo sabe qué es **imprescindible** y qué es **ornamento**.

## Ciclo mínimo

1. **Objetivo.** Una frase que se puede dar por hecha o no. *“Dataset limpio y clientes por ciudad.”*
2. **Tareas.** Cargar, deduplicar, unificar ciudades, fechas, resumen, gráfico, comentarios.
3. **Prioridad.** Esencial vs deseable.
4. **Secuencia.** No grafiques antes de limpiar: el gráfico de `Madird` miente.
5. **Tiempo.** Un mini-sprint (1–2 sesiones). Al final: qué está hecho, qué no, por qué.

## Objetivos que se pueden comprobar

Mal: “trabajar los datos”.  
Bien: “dejar el CSV sin duplicados, ciudades unificadas y una tabla de clientes por ciudad”.

Eso es el *definition of done* del sprint de aula.

## Esencial frente a deseable

Objetivo principal: limpiar [clientes_actividad.csv](../assets/practicas/clientes_actividad.csv) y resumir por ciudad.

| Esencial (sin esto no hay práctica) | Deseable (si sobra tiempo) |
| --- | --- |
| Cargar el CSV | Gráfico de barras |
| Eliminar duplicados | Comentarios largos en cada celda |
| Corregir `ciudad` | Informe muy maquetado |
| Unificar fechas | Extra de API meteorológica |
| Recuento por ciudad | |

Si el reloj llega a cero, las esenciales tienen que estar **hechas**. Eisenhower, en una frase: importante y urgente primero; bonito y no urgente, después.

## Mini-sprints

Un *sprint* profesional dura 1–4 semanas. En clase usamos **mini-sprints** (una o dos sesiones):

- Al inicio: objetivo + lista priorizada.
- Durante: el tablero se mueve.
- Al final: revisión (qué, qué no, qué cambia mañana).

Tres columnas bastan:

```text
POR HACER          EN PROGRESO         HECHO
- Cargar datos     - Limpiar ciudades  - Importar pandas
- Crear gráfico
- Documentar
```

## Issues y GitHub Projects

Cuando el trabajo vive en un repositorio:

1. Un **issue** por tarea (“Unificar ciudades”, no “el trabajo”).
2. Un **Project** (tablero) con *Por hacer / En progreso / Hecho*.
3. Mover la tarjeta, no reescribir el enunciado en un chat.

Así el criterio e) deja rastro: se ve el objetivo, el orden y el tiempo. No hace falta la API GraphQL de Projects; el tablero de la clase vale.

!!! tip "Enlace con 1.3"
    La actividad de limpieza de clientes **se planifica aquí** y se ejecuta en pandas. Entrega típica: enlace al Project (o captura del tablero) + notebook o script + CSV limpio + recuento.

!!! success "Al terminar 1.6"
    Eres capaz de decir, en un minuto: objetivo, tres tareas esenciales, una deseable y en qué orden las harías esta semana.
