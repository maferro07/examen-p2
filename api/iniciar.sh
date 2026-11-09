#!/bin/sh
set -e

echo "Iniciando carga de resultados..."

python /app/scripts/cargar_resultados.py

echo "Iniciando API Flask..."

exec python /app/app.py