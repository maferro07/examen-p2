FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
docker compose up -d --build api
COPY iniciar.sh /app/iniciar.sh

RUN chmod +x /app/iniciar.sh

CMD ["/app/iniciar.sh"]