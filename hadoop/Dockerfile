# Imagen base de Debian
FROM debian:bookworm-slim

# Instalar Java, Python, SSH y herramientas necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jdk-headless \
    python3 \
    openssh-server \
    openssh-client \
    curl \
    ca-certificates \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Configurar Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Configurar Hadoop
ENV HADOOP_HOME=/opt/hadoop

# Agregar Hadoop al PATH
ENV PATH="${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${PATH}"

# Descargar Hadoop
RUN curl -fL \
    https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz \
    -o /tmp/hadoop.tar.gz \
    && tar -xzf /tmp/hadoop.tar.gz -C /opt \
    && mv /opt/hadoop-3.3.6 /opt/hadoop \
    && rm /tmp/hadoop.tar.gz

# Crear directorios de trabajo
RUN mkdir -p /data/input /data/output /run/sshd

# Configurar Hadoop para utilizar Java
RUN printf '\nexport JAVA_HOME=%s\n' "$JAVA_HOME" \
    >> "$HADOOP_HOME/etc/hadoop/hadoop-env.sh"

# Directorio de trabajo
WORKDIR /opt/hadoop

# Mantener el contenedor activo y ejecutar SSH
CMD ["/bin/sh", "-c", "/usr/sbin/sshd && exec tail -f /dev/null"]