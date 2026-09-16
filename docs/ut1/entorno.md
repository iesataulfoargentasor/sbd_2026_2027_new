---
title: "Preparar el entorno y descargar el laboratorio"
tags: [SBD, RA1]
---

# Preparar el entorno y descargar el laboratorio

## Un paquete para toda la unidad

Descarga [sbd-ut1-hotel.zip](../assets/practicas/sbd-ut1-hotel.zip), descomprímelo y abre una terminal en la carpeta `sbd-ut1-hotel`. Incluye datos, generador, análisis PySpark, ensayo de streaming y comprobaciones. No necesitas contratar servicios cloud.

Entorno de referencia: **Python 3.11, Java 17 y PySpark 3.5.6**. Es una versión fijada para reproducir la práctica, no una afirmación de que sea la última disponible. La [documentación de instalación de Spark](https://spark.apache.org/docs/3.5.6/api/python/getting_started/install.html) describe los requisitos.

Comprueba `python --version` y `java -version`. Si falta Java, utiliza el entorno que prepare el profesor antes de continuar.

```bash
python -m venv .venv
```

Activa el entorno en macOS/Linux con `source .venv/bin/activate`; en PowerShell con `.venv\Scripts\Activate.ps1`. Después:

```bash
python -m pip install -r requirements.txt
python generar.py --salida datos --copias 1
python referencia.py datos
python analizar.py --entrada datos --salida resultados
python verificar.py resultados
```

Cada salida debe ser nueva: el programa evita sobrescribir trabajos anteriores. Para repetir elige `resultados_02`. El cálculo se ejecuta con dos hilos locales por defecto; no representa dos servidores.

## Qué obtendrás

| Ruta | Contenido |
| --- | --- |
| `datos/reservas.csv` | Reservas sintéticas con identificadores únicos |
| `datos/hoteles.csv` | Catálogo de dos hoteles |
| `datos/eventos.jsonl` | Eventos de confirmación/cancelación |
| `resultados/integrado/` | Una fila por reserva, en Parquet |
| `resultados/resumen/` | Indicadores por hotel y canal, en CSV |
| `resultados/metricas.json` | Volumen, tiempo y controles |

Spark escribe **directorios con ficheros `part-*`**, no un único archivo con el nombre de la carpeta. No edites esos fragmentos a mano.

## Si falla

- Java no encontrado: revisa Java 17 y `JAVA_HOME` con el profesor.
- Módulo `pyspark` no encontrado: comprueba que has activado el entorno.
- `PYTHON_VERSION_MISMATCH`: los procesos de Spark deben usar la misma versión de Python. Activa el entorno antes de abrir PySpark; si persiste, configura `PYSPARK_PYTHON` con la ruta al Python de ese entorno antes de iniciar la sesión.
- Ruta existente: elige otra salida.
- Un control de calidad detiene el proceso: lee el mensaje; no elimines el control para conseguir una salida.
- Falta de memoria: reduce `--copias` y registra el límite. No lleves todas las filas al programa con `collect()`.

Los [fundamentos](fundamentos.md) y `referencia.py` pueden trabajarse con Python estándar. El ensayo completo requiere Java y PySpark.

## Apoyo auxiliar: Docker en una página

**CE:** apoyo instrumental a la ejecución; Docker no es contenido curricular evaluable de RA1. **Al terminar:** podrás abrir y detener el entorno que proporcione el profesor e identificar sus componentes.

| Concepto | Significado práctico |
| --- | --- |
| Imagen | Plantilla con programas y dependencias |
| Contenedor | Instancia ejecutándose a partir de una imagen |
| Servicio | Componente declarado en el archivo Compose |
| Volumen | Datos persistentes asociados al entorno |
| Red | Comunicación entre componentes |

Esta chuleta requiere un archivo `compose.yml` facilitado por el aula. El paquete actual utiliza Python/Java local y no incluye Compose: no ejecutes estos comandos esperando que creen un entorno por sí solos. Desde la carpeta del Compose docente:

```bash
docker compose up -d
docker compose ps
docker compose logs --tail=50
docker compose exec NOMBRE_SERVICIO sh
docker compose down
```

Sustituye `NOMBRE_SERVICIO` por el que muestre `ps`. `up -d` inicia en segundo plano; `ps` muestra servicios; `logs` ayuda a leer una incidencia; `exec` abre una shell dentro del servicio; `down` retira los contenedores y redes del proyecto. No añadas `-v` si quieres conservar los volúmenes. Para contenedores individuales existen `docker ps`, `docker logs NOMBRE_CONTENEDOR` y `docker exec -it NOMBRE_CONTENEDOR sh`.

La configuración de Hadoop, HDFS/YARN, replicación y monitorización queda en BDA. Consulta la [referencia de Docker Compose](https://docs.docker.com/reference/cli/docker/compose/) cuando necesites interpretar una opción.

!!! example "Comprobación de entorno"
    Si usas Docker, identifica el servicio donde ejecutarías Python y la ruta persistente de trabajo del Compose docente. Comprueba que los resultados siguen accesibles tras detenerlo. Si trabajas localmente, registra versiones y ejecuta la muestra: no necesitas instalar Docker para acreditar RA1.

Para las introducciones con pandas se necesita también pandas en el entorno Python (`python -m pip install pandas`); registra la versión utilizada. Los ejemplos nuevos de ventanas, opiniones y AWS están en sus páginas y no modifican el ZIP original.
