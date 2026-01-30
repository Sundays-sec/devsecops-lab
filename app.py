from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao Sistema Seguro!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # ✅ CORREÇÃO: Buscando do Ambiente (Environment Variable)
    # Se a variável não existir, usa None (falha segura)
    safe_password = os.getenv('APP_PASSWORD')
    
    if username == "admin" and password == safe_password:
        return "Acesso Permitido"
    else:
        return "Acesso Negado"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
