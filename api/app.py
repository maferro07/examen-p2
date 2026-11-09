import os
from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def conectar_bd():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "datamart"),
        user=os.getenv("POSTGRES_USER", "datamart_user"),
        password=os.getenv("POSTGRES_PASSWORD"),
        cursor_factory=RealDictCursor
    )

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API DataMart funcionando"})

@app.route("/salud")
def salud():
    return jsonify({"estado": "activo"})

# Consultar todos los resultados
@app.route("/resultados", methods=["GET"])
def obtener_resultados():
    with conectar_bd() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT metodo_pago, dia_semana, unidades_vendidas
                FROM resultados_ventas
                ORDER BY metodo_pago, dia_semana
            """)
            datos = cursor.fetchall()
    return jsonify(datos)

# Consultar por metodo de pago
@app.route("/resultados/<metodo>", methods=["GET"])
def filtrar_resultados(metodo):
    with conectar_bd() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT metodo_pago, dia_semana, unidades_vendidas
                FROM resultados_ventas
                WHERE LOWER(metodo_pago) = LOWER(%s)
                ORDER BY dia_semana
            """, (metodo,))
            datos = cursor.fetchall()
    return jsonify(datos)

# Agregar o actualizar un resultado
@app.route("/resultados", methods=["POST"])
def agregar_resultado():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "Se requiere un objeto JSON"}), 400

    try:
        metodo = datos["metodo_pago"]
        dia = datos["dia_semana"]
        unidades = datos["unidades_vendidas"]

        if (
            not isinstance(metodo, str)
            or not metodo.strip()
            or not isinstance(dia, str)
            or not dia.strip()
            or type(unidades) is not int
            or unidades < 0
        ):
            return jsonify({"error": "Datos invalidos"}), 400

    except KeyError:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    with conectar_bd() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO resultados_ventas
                (metodo_pago, dia_semana, unidades_vendidas)
                VALUES (%s, %s, %s)
                ON CONFLICT (metodo_pago, dia_semana)
                DO UPDATE SET
                    unidades_vendidas = EXCLUDED.unidades_vendidas
            """, (metodo.strip(), dia.strip(), unidades))

    return jsonify({"mensaje": "Resultado guardado correctamente"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)