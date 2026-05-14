from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)

# Lista de livros (simulando um banco de dados)
usuarios = [
    {
        "id": 1,
        "nome": "mairene",
        "email": "mairene202@gmail.com",
        "telefone": "9999999"   
    },
    {
        "id": 2,
        "nome": "mario",
        "email": "super.mario@gmail.com",
        "telefone": "88888888"
    },
    {
        "id": 3,
        "nome": "luidi",
        "email": "luidi.manfiel@gmail.com",
        "telefone": "77777777"
    },
    {
        "id": 4,
        "nome": "pity",
        "email": "princesa.pity@gmail.com",
        "telefone": "55555555"   
    },
    {
        "id": 5,
        "nome": "daise",
        "email": "supermario.bros@gmail.com",
        "telefone": "44444444"   
    },
    {
        "id": 6,
        "nome": "bowser",
        "email": "bowser.castle@gmail.com",
        "telefone": "333333333"   
    },
    {
        "id": 7,
        "nome": "rosalina",
        "email": "rosalina.292@gmail.com",
        "telefone": "2222222222"   
    },
    {
        "id": 8,
        "nome": "soshiro",
        "email": "hoshina.2@gmail.com",
        "telefone": "1111111111"   
    },
]


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)



@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json


    if not dados or not dados.get("nome") or not dados.get("id"):
        return {"erro": "Título e autor são obrigatórios"}, 400


    for pessoa in usuarios:
        if pessoa["nome"].lower() == dados["nome"].lower():
            return {"erro": "Usuario já cadastrado"}, 400

    novo = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"],
        "email": dados["email"],
        "telefone": dados.get("telefone", None)
    }

    usuarios.append(novo)
    return jsonify(novo), 201



@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            dados = request.json

            usuario["nome"] = dados.get("nome", usuario["nome"])
            usuario["email"] = dados.get("email", usuario["email"])
            usuario["telefone"] = dados.get("telefone", usuario["telefone"])

            return jsonify(usuario)

    return {"erro": "Pessoa não encontrado"}, 404



@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Pessoa removido"}

    return {"erro": "Usuario não encontrado"}, 404



if __name__ == "__main__":
    app.run(debug=True)