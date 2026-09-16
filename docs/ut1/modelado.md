---
title: Modelado y resolución de problemas
tags:
  - SBD
  - RA1
---

# Modelado, razonamiento y resolución de problemas

El Anexo VI cita *modelado, razonamiento, resolución de problemas*. Aquí se **reconoce** el oficio; el detalle de Dijkstra o de un clúster queda para más adelante.

## Objetivos

- Traducir un problema real a un modelo que un ordenador entienda.
- Usar razonamiento deductivo, inductivo o heurístico.
- Representar con diagramas de flujo, tablas, árboles, grafos o matrices.
- Seguir definir → entradas/salidas → algoritmo → probar.

## De la pregunta al modelo

*¿Cómo recomendar una película en Netflix?* → matriz usuario × película → similitud.

*¿Ruta más corta entre ciudades?* → nodos (ciudades), aristas con peso (km) → Dijkstra.

El modelo tiene que ser simple **y** bastante realista.

| Tipo | Idea | Ejemplo |
| --- | --- | --- |
| Deductivo | Si A implica B y A es cierto, B es cierto | Par ⇒ divisible entre 2 |
| Inductivo | Generalizas desde casos | Quien compra pan suele comprar leche |
| Heurístico | Regla rápida, no óptima | “Coge primero la calle más ancha” |

Flujo par/impar: leer número → `mod 2 = 0` → par; si no, impar.

Algoritmo de la media: sumar notas → dividir entre n → mostrar.

## Ejemplos

- Grafo de amistades: el más conectado es el de **mayor grado**.
- Árbol de tienda: ¿ha comprado antes? → ¿en los últimos 30 días? → complementar / fidelidad / más vendidos.

## Actividades

**1.** Promoción si edad > 18 **y** al menos una compra el último mes. Diagrama de flujo + pseudocódigo.

**2.** Cinco alumnos y sus amistades: dibuja el grafo; quién está más conectado.

**3.** Árbol para recomendar cine: género (comedia/acción) × edad (niño/adulto).

Los grafos y conjuntos de [1.2](fundamentos.md) son el mismo lenguaje.
