from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Lista de livros (simulando um banco de dados)
livros = [
    {
        "id": 1,
        "titulo": "kaiju n8",
        "autor": "naoya matsumoto",
        "data": "2020"   
    },
    {
        "id": 2,
        "titulo": "Drácula",
        "autor": "Bram Stoker",
        "data": "1897"
    },
    {
        "id": 3,
        "titulo": "Frankstayn",
        "autor": "Mary sheille",
        "data": "1818"
    },
    {
        "id": 4,
        "titulo": "Saboroso cadaver",
        "autor": "darkside",
        "data": "2018"   
    },
    {
        "id": 5,
        "titulo": "o chamado de cuthulu",
        "autor": "lovecraft",
        "data": ""   
    },
    {
        "id": 6,
        "titulo": "o médico e o monstro",
        "autor": "albert lois",
        "data": "1886"   
    },
    {
        "id": 7,
        "titulo": "o rei de amarelo",
        "autor": "robert w",
        "data": "1881"   
    },
    {
        "id": 8,
        "titulo": "o corvo",
        "autor": "edgar allan",
        "data": "1845"   
    },
]


@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)



@app.route("/livros", methods=["POST"])
def criar_livro():
    dados = request.json


    if not dados or not dados.get("titulo") or not dados.get("autor"):
        return {"erro": "Título e autor são obrigatórios"}, 400


    for livro in livros:
        if livro["titulo"].lower() == dados["titulo"].lower():
            return {"erro": "Usuario já cadastrado"}, 400

    novo = {
        "id": len(livros) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "data": dados.get("data", None)
    }

    livros.append(novo)
    return jsonify(novo), 201



@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    for livro in livros:
        if livro["id"] == id:
            dados = request.json

            livro["titulo"] = dados.get("titulo", livro["titulo"])
            livro["autor"] = dados.get("autor", livro["autor"])
            livro["data"] = dados.get("data", livro["data"])

            return jsonify(livro)

    return {"erro": "livro não encontrado"}, 404



@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    for livro in livros:
        if livro["id"] == id:
            livro.remove(livros)
            return {"mensagem": "livro removido"}

    return {"erro": "livro não encontrado"}, 404



if __name__ == "__main__":
    app.run(debug=True)
