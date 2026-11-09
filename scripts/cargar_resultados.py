import os
import psycopg2

# Configuración de PostgreSQL
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "datamart")
DB_USER = os.getenv("POSTGRES_USER", "datamart_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Archivo con los resultados de Hadoop
ARCHIVO = "/app/resultado_hadoop.txt"

def cargar_resultados():
    conexion = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados_ventas (
            id SERIAL PRIMARY KEY,
            metodo_pago VARCHAR(50) NOT NULL,
            dia_semana VARCHAR(20) NOT NULL,
            unidades_vendidas BIGINT NOT NULL,
            UNIQUE (metodo_pago, dia_semana)
        )
    """)

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            clave, total = linea.strip().split("\t")

            metodo_pago, dia_semana = clave.split("|")

            cursor.execute("""
                INSERT INTO resultados_ventas
                (metodo_pago, dia_semana, unidades_vendidas)
                VALUES (%s, %s, %s)
                ON CONFLICT (metodo_pago, dia_semana)
                DO UPDATE SET unidades_vendidas = EXCLUDED.unidades_vendidas
            """, (metodo_pago, dia_semana, int(total)))

    conexion.commit()

    cursor.close()
    conexion.close()

    print("Resultados cargados correctamente en PostgreSQL.")

if __name__ == "__main__":
    cargar_resultados()