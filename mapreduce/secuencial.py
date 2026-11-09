import csv
import time
from datetime import datetime
from collections import defaultdict

inicio = time.time()

archivo = "data/ventas_125053905.csv"

resultados = defaultdict(int)

with open(archivo, "r") as f:
    lector = csv.DictReader(f)

    for fila in lector:
        try:
            fecha = datetime.strptime(
                fila["fecha_hora"],
                "%Y-%m-%d %H:%M:%S"
            )

            dia = fecha.strftime("%A")
            metodo = fila["metodo_pago"]
            cantidad = int(fila["cantidad"])

            clave = f"{metodo}|{dia}"

            resultados[clave] += cantidad

        except (ValueError, KeyError):
            continue

for clave, total in sorted(resultados.items()):
    print(f"{clave}\t{total}")

fin = time.time()

print(f"\nTiempo secuencial: {fin - inicio:.2f} segundos")