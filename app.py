from flask import Flask, jsonify, request
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Wirer"}
]




@app.route("/usuarios", methods=['POST'])
def criar_usuario():
    novo = request.json
    novo['id'] = len(usuarios) + 1
    usuarios.append(novo)
    return jsonify(novo), 201
