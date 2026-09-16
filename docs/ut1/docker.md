---
title: Entorno Docker
tags:
  - SBD
---

# Entorno Docker (apoyo) y clúster Hadoop

Docker **no** es un criterio propio del RA1. El paquete de Moodle *Manual para Docker en Big Data* es un **laboratorio de Hadoop en contenedores**: NameNode, YARN, DataNodes y un MapReduce de ejemplo. Sirve para **reproducir** un entorno y para el criterio **f)** (elegir e integrar sistemas) cuando el profesor lo pide.

El ZIP y el PDF del aula (`Hadoop_cluster_profesor.zip`, `Hadoop_con_Docker.pdf`) **no** se copian a git; se descargan desde Moodle. Aquí queda la chuleta, el vídeo y el enunciado.

## Qué problema resuelve

Instalar pandas, Java, Hadoop y tres versiones de Python en el sistema del centro termina en conflictos. Un **contenedor** empaqueta la receta. Un **Compose** levanta varias piezas (el clúster) con un fichero.

| Concepto | En una frase |
| --- | --- |
| Imagen | Receta inmutable (`ubuntu`, `python:3.12-slim`) |
| Contenedor | Esa receta **en marcha** |
| Dockerfile | Instrucciones `FROM` / `RUN` / `COPY` / `CMD` |
| Volumen | Dato **fuera** del contenedor (tus CSV o HDFS local) |
| Puerto | Cómo entras desde el navegador (HDFS `9870`, YARN `8088`) |
| Compose | Varios servicios descritos juntos |
| Red | Cómo se hablan NameNode, Resource Manager y workers |

No guardes secretos (claves AWS) en la imagen ni en el `compose` que subes a Moodle.

## Chuleta (del eXe)

```sh
docker --version
docker pull ubuntu
docker images
docker run -it ubuntu /bin/bash
docker ps
docker ps -a
docker stop <id>
docker rm <id>
docker exec -it <id> /bin/bash
docker logs <id>
docker stats
docker build -t mi-imagen .
docker compose up -d
docker compose down
docker network create mi-red
```

Ejemplo de Dockerfile del eXe:

```dockerfile
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
COPY ./app /usr/src/app
CMD [ "python3", "/usr/src/app/app.py" ]
```

Para pandas y el generador de logs de [1.7](laboratorio-aws.md), un venv local basta. Usa Docker cuando toque el clúster o un `compose.yaml` de aula.

```sh
python -m venv .venv
source .venv/bin/activate
pip install pandas pyarrow faker
```

## Vídeo de ayuda

[Instalación de Apache Hadoop con Docker](https://youtu.be/f6FJ91f-qpA) (Tomás Fernández Pena). Resume NameNode, DataNodes, YARN, Compose y una prueba MapReduce (cálculo de π).

## Actividad — Montaje de un clúster Hadoop con Docker

**Requisito:** ~8 GB de RAM y Docker Desktop (o Docker en Linux).

1. Comprueba `docker --version`.
2. Dockerfile sobre Ubuntu que instale Hadoop; configura **NameNode** y **Resource Manager (YARN)**.
3. `docker-compose.yml` con NameNode, Resource Manager, DataNodes y NodeManagers, en una red Docker. Expón las UIs.
4. Directorios HDFS; abre HDFS en `localhost:9870`.
5. Workers que reciban tareas YARN y almacenen bloques.
6. Prueba:

```sh
hadoop jar /path/to/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples.jar pi 16 10000
```

7. YARN: `localhost:8088`. Comprueba que los DataNodes participan.

**Entrega (Moodle):** capturas HDFS y YARN, breve descripción, `Dockerfile`, `docker-compose.yml` y el resultado de π.

!!! tip "Criterio f), sin marear"
    Elegir S3 + Glue + Athena **es** integrar sistemas en el laboratorio de logs. Elegir Docker+Hadoop es **otro** sistema, el del manual. No los mezcles en la misma frase de examen como si fueran el mismo oficio.
