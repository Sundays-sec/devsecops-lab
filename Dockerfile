# Imagem base leve e segura (Python Slim)
FROM python:3.11-alpine

# Cria usuário não-root (Prática de Segurança: nunca rode como root!)
RUN useradd -m appuser
WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY app.py .

# Define permissões
RUN chown -R appuser:appuser /app
USER appuser

# Expõe a porta e roda
EXPOSE 5000
CMD ["python", "app.py"]
