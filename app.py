from flask import Flask, jsonify
import os

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
    {"id": 3, "nome": "Carol"}
]

filmes = [
    {"id": 1, "nome": "Circulo_de_fogo"},
    {"id": 2, "nome": "2012"},
    {"id": 3, "nome": "rote_1"}]

jogos = [

{"id":1, "nome": "Minecraft", "plataforma":"PC"},
{"id":2, "nome": "Call_of_duty_ghosts" ,"plataforma":"PlayStation_3"},
{"id":1, "nome": "Minecraft" ,"plataforma":"PC"}


]

livros = [
    {"id": 1, "nome": "Saboroso_cadaver"},
    {"id": 2, "nome": "Harry_potter"},
    {"id": 3, "nome": "matt_imortal"}
    ]

produtos = [
    {"id": 1, "nome": "cadeira"},
    {"id": 2, "nome": "pc"},
    {"id": 3, "nome": "banana"}
    ]

series = [
    {"id": 1, "nome": "Kaiju_n8"},
    {"id": 2, "nome": "Paradise_pd"},
    {"id": 3, "nome": "100"}
    ]





@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

@app.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify(filmes)

@app.route("/jogos", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/series", methods=["GET"])
def listar_series():
    return jsonify(series)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)