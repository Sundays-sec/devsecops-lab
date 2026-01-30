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
    
    # ❌ VULNERABILIDADE: Senha fixa no código (Hardcoded Credential)
    # O SonarQube DEVE pegar isso.
    if username == "admin" and password == "123456": 
        return "Acesso Permitido"
    else:
        return "Acesso Negado"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
