"""Genera logs.csv de ejemplo para el laboratorio S3 + Glue + Athena."""

from datetime import datetime, timedelta, timezone
import csv
import random

from faker import Faker

fake = Faker()

URLS = [
    "/",
    "/home",
    "/productos",
    "/productos/categoria1",
    "/productos/categoria2",
    "/carrito",
    "/checkout",
    "/contacto",
    "/login",
    "/registro",
]

COUNTRIES = ["ES", "FR", "DE", "IT", "PT", "UK", "US"]


def generar_timestamp_ultimos_dias(dias=7):
    ahora = datetime.now(timezone.utc)
    delta = timedelta(
        days=random.randint(0, dias),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return (ahora - delta).isoformat()


def generar_logs(num_filas=500, nombre_fichero="logs.csv"):
    with open(nombre_fichero, mode="w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["timestamp", "ip", "url", "country", "user_agent"])
        for _ in range(num_filas):
            writer.writerow(
                [
                    generar_timestamp_ultimos_dias(),
                    fake.ipv4_public(),
                    random.choice(URLS),
                    random.choice(COUNTRIES),
                    fake.user_agent(),
                ]
            )
    print(f"Fichero '{nombre_fichero}' generado con {num_filas} filas.")


if __name__ == "__main__":
    generar_logs()
