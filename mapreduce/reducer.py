import sys

clave_actual = None
total = 0

for linea in sys.stdin:
    try:
        clave, cantidad = linea.strip().split("\t", 1)
        cantidad = int(cantidad)

        if clave == clave_actual:
            total += cantidad
        else:
            if clave_actual is not None:
                print(f"{clave_actual}\t{total}")

            clave_actual = clave
            total = cantidad

    except ValueError:
        continue

if clave_actual is not None:
    print(f"{clave_actual}\t{total}")