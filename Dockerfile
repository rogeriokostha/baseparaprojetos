# Usar uma imagem oficial e leve (slim) do Python 3.12
FROM python:3.12-slim

# Evitar que o Python gere arquivos .pyc e garanta stdout não "bufado" (ideal para logs docker)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependências de sistema necessárias para compilação e pro PostgreSQL (libpq)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir a pasta de trabalho (o diretório no container onde o app viverá)
WORKDIR /app

# Copiar APENAS o requirements.txt primeiro para otimizar o Cache de camadas do Docker
COPY requirements.txt /app/

# Instalar pacotes pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todo o resto da aplicação
COPY . /app/

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
