---
title: Autoevaluación UT1
---

# Autoevaluación de la UT1

Quince preguntas, una respuesta correcta en cada una. Al corregir verás la explicación y un enlace para repasar. No puntúan en Moodle ni sustituyen las evidencias de la práctica.

<div class="dwec-quiz" data-dwec-quiz data-src="../../assets/quizzes/ut1.json"></div>

## Repaso de los nuevos bloques

**CE que se trabajan:** a–g. **Al terminar:** podrás localizar qué explicación o evidencia necesitas reforzar. Conservamos las quince preguntas interactivas anteriores y añadimos estas comprobaciones razonadas.

### 1. Planificación (CE e)

Una tarea «integrar» pasa a bloqueada porque el catálogo repite claves. ¿Qué debe quedar en Projects?

??? success "Respuesta orientativa"
    Incidencia, dependencia, responsable, nueva previsión y trabajo que sí puede continuar. Conserva estimación original y real; no reconstruyas el plan al final. Repasa [1.3](planificacion.md).

### 2. Preparación (CE b, d, g)

Falta un importe y aparece una estancia de 40 noches. ¿Debes poner cero y eliminar el extremo?

??? success "Respuesta orientativa"
    No sin una regla justificada. El importe ausente se separa o declara con cobertura; el extremo se revisa antes de decidir. Repasa [1.5](preproceso.md).

### 3. Integración (CE c, d)

Tres reservas de un hotel encuentran dos filas de catálogo. ¿Cuántos pares produce el join?

??? success "Respuesta orientativa"
    Seis. Un left join conserva correspondencias, pero puede multiplicar filas. Valida claves y cardinalidad antes de sumar. Repasa [1.6](integracion.md).

### 4. Escala (CE a, g)

¿`dropDuplicates(["id_reserva"])` garantiza conservar la última versión?

??? success "Respuesta orientativa"
    No. Hace falta una ventana ordenada por versión/fecha y desempate válido, o detener el proceso si existe conflicto. Repasa [1.8](transformaciones-escala.md).

### 5. Flujo (CE b, f)

Un evento de 10:02 llega después de otro de 10:05. ¿A qué ventana de cinco minutos pertenece?

??? success "Respuesta orientativa"
    A [10:00, 10:05) según su tiempo de evento. El ensayo sin watermark actualiza esa ventana; una política de tardíos podría cambiar su tratamiento. Repasa [1.10](streaming.md).

### 6. Sistemas (CE f)

El crawler creó una tabla con columnas genéricas y la consulta cuenta 1 001 filas en vez de 1 000. ¿Qué revisas?

??? success "Respuesta orientativa"
    Cabecera, clasificador, propiedad de omisión de cabecera, esquema y prefijo. Contrasta los registros y no declares correcta la integración solo porque SQL se ejecuta. Repasa [1.12](aws-s3-glue-athena.md).

### 7. Coste (CE g)

Has convertido CSV a Parquet y la segunda consulta es más rápida. ¿Es suficiente para recomendarlo?

??? success "Respuesta orientativa"
    Comprueba igualdad de resultados, bytes, repetición/caché y coste de conversión. Valora consultas futuras y mínimos cloud. Repasa [1.11](coste-calidad.md).

### 8. Fundamentos y análisis (CE a, b)

¿Por qué buscar en un diccionario y por qué no interpretar una mención a «atención» como sentimiento positivo?

??? success "Respuesta orientativa"
    El diccionario reduce trabajo esperado bajo supuestos de unicidad y memoria; una regla textual solo reconoce el patrón definido, no su significado completo. Repasa [1.2](fundamentos.md) y [1.9](analisis.md).

Cierra el repaso señalando una evidencia pendiente para cada CE en tu [proyecto](practica.md).
