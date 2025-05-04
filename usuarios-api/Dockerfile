# Etapa 1: Imagem base
FROM python:3.11-slim

# Etapa 2: Definindo o diretório de trabalho
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Etapa 3: Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential

# Etapa 4: Cria diretório de trabalho
WORKDIR /app

# Etapa 5: Copia arquivos
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

# Etapa 6: Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

