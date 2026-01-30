# Imagem base leve e segura (Python Slim)
#FROM python:3.13-slim

# Cria usuário não-root (Prática de Segurança: nunca rode como root!)
#RUN useradd -m appuser
#WORKDIR /app

# Instala dependências
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
#COPY app.py .

# Define permissões
#RUN chown -R appuser:appuser /app
#USER appuser

# Expõe a porta e roda
#EXPOSE 5000
#CMD ["python", "app.py"]
FROM python:3.13-slim

# Atualiza os pacotes do SO para corrigir CVEs conhecidas (como a do OpenSSL)
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# ... restante do seu Dockerfile (useradd, WORKDIR, etc)
RUN useradd -m appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
