import sys
import csv
from datetime import datetime

for linea in sys.stdin:
    try:
        datos = next(csv.reader([linea]))

        # Ignorar encabezado y registros incompletos
        if len(datos) != 8 or datos[0] == "id":
            continue

        fecha = datos[1]
        cantidad = int(datos[5])
        metodo_pago = datos[7]

        # Obtener día de la semana
        dia = datetime.strptime(
            fecha, "%Y-%m-%d %H:%M:%S"
        ).strftime("%A")

        # Enviar clave y cantidad
        print(f"{metodo_pago}|{dia}\t{cantidad}")

    except (ValueError, IndexError, csv.Error):
        continue