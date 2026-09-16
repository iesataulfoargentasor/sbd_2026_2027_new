# UT1 de Sistemas de Big Data

## Alcance

Orden EDU/48/2024, Anexo VI. Módulo 5074: 135 horas, 6 ECTS. La UT1 desarrolla RA1 y sus siete criterios; las 40 horas son orientativas. Se publican 15 páginas de unidad, una portada, cuestionario de 15 preguntas y laboratorio descargable.

## Correspondencia

- a: conjuntos, relaciones, lógica y complejidad temporal/espacial con ejemplos del hotel.
- b: extracción automática con PySpark, referencia mínima y generación ampliable; el docente debe concretar el ensayo a escala del centro.
- c/d: CSV, catálogo y eventos JSON anidados; claves, granularidad y conjunto integrado.
- e: planificación desde el encargo, seguimiento y revisión.
- f: selección de sistemas, integración de fuentes y puente opcional con MongoDB mediante exportación programática.
- g: controles de calidad, tiempo, bytes y recursos; criterios de eficacia y eficiencia.

Incluye introducción práctica a análisis incremental. Se reservan cuadros de mando, visualización extensa y gestión avanzada para los siguientes RA. Se mantiene la continuidad con BDA sin reasignar todas las competencias por tecnología.

## Procedencia

Texto, datos y laboratorio redactados para este proyecto. Se consultan y enlazan materiales de Aitor Medrano como referencia, sin copiar sus páginas, recursos gráficos ni ejercicios. CSS, motor del cuestionario y logotipo se reutilizan del repositorio BDA del titular. Las atribuciones y licencias de dependencias y recursos ajenos se conservan.

## Validación

MkDocs se construye en modo estricto. GitHub Actions ejecuta el análisis PySpark, compara sus resultados con expectativas independientes, prueba rechazo de claves duplicadas y referencias huérfanas y ejecuta el ensayo Structured Streaming con dos llegadas. Se prueban una y dos copias del conjunto de referencia.

Estas comprobaciones verifican funcionamiento local en el entorno de integración continua, no rendimiento distribuido ni grandes volúmenes. La conexión a MongoDB requiere un servidor del aula y no se considera validada contra un servidor real en esta entrega. El equipo local de autoría no dispone de Java; las pruebas PySpark se ejecutan en Actions con Java 17. Los resultados del ensayo a escala y las métricas de memoria corresponden a la práctica posterior del centro.
