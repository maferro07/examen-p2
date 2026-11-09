# Examen P2 — Procesamiento de ventas con Hadoop

## 1. Descripción del proyecto

Este proyecto tiene como objetivo analizar un conjunto de datos de 5 millones de registros de ventas utilizando Hadoop MapReduce.

El análisis responde a la siguiente pregunta:

**¿Cuántas unidades se vendieron por método de pago y día de la semana?**

Los resultados se almacenan en PostgreSQL y se pueden consultar mediante una API desarrollada con Flask.

## 2. Tecnologías utilizadas

- **Python:** generación y procesamiento de datos.
- **Hadoop MapReduce:** procesamiento de grandes cantidades de información.
- **PostgreSQL:** almacenamiento de resultados.
- **Flask:** creación de la API.
- **Docker Compose:** administración de los contenedores.

## 3. Funcionamiento del proyecto

El proyecto se desarrolla en cinco etapas:

1. Generar un dataset de 5 millones de ventas.
2. Procesar los registros mediante Hadoop MapReduce.
3. Realizar el mismo análisis con Python secuencial.
4. Guardar los resultados en PostgreSQL.
5. Consultar la información mediante una API Flask.

## 4. Resultados obtenidos

El procesamiento generó 28 combinaciones de métodos de pago y días de la semana.

Los tiempos registrados fueron:

| Procesamiento | Tiempo |
|---|---|
| Hadoop MapReduce | 151.41 segundos |
| Python secuencial | 125.45 segundos |

Ambos métodos produjeron los mismos resultados.

En esta ejecución, Python secuencial fue más rápido porque Hadoop se utilizó en un entorno local.

## 5. API

La API permite consultar los resultados almacenados en PostgreSQL.

**Consultar todos los resultados:**

`http://localhost:5050/resultados`

**Consultar los resultados de un método de pago:**

`http://localhost:5050/resultados/Tarjeta`

**Comprobar el funcionamiento de la API:**

`http://localhost:5050/salud`

## 6. Evidencias

La carpeta `evidencias` contiene los resultados obtenidos durante el procesamiento de los datos.

Estos archivos permiten comparar los resultados de Hadoop MapReduce y Python secuencial.

## 7. Instrucciones de ejecución

### Requisitos

Para ejecutar el proyecto es necesario tener instalados:

- Docker
- Docker Compose
- Git

### Descargar el proyecto

Clonar el repositorio desde GitHub y entrar a la carpeta del proyecto.

### Configurar las variables de entorno

Crear el archivo `.env` utilizando como referencia `.env.example` y configurar las credenciales de PostgreSQL.

### Iniciar los contenedores

Desde la carpeta principal del proyecto, ejecutar:

```bash
docker compose up -d --build
```

Este comando construye las imágenes necesarias e inicia los servicios de Hadoop, PostgreSQL y Flask.

### Consultar la API

Una vez que los servicios estén funcionando y los resultados se hayan cargado correctamente, abrir:

`http://localhost:5050/resultados`

La API mostrará las unidades vendidas por método de pago y día de la semana.

### Nota importante

El dataset original no está incluido en GitHub debido a su tamaño. Se proporciona el archivo `generar_dataset.py` para generarlo.

El procesamiento con Hadoop debe ejecutarse antes de cargar sus resultados en una instalación nueva. Las instrucciones completas para realizar este proceso están pendientes de documentarse.