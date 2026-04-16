from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de livros (simulando um banco de dados)
usuarios = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899
    },
    {
        "id": 2,
        "titulo": "Saboroso Cadaver",
        "autor": "Darkside",
        "ano": 2022
    },
    {
        "id": 3,
        "titulo": "Kaiju n8",
        "autor": "Matsumoto",
        "ano": 2019
    },
]


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)



@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json


    if not dados or not dados.get("titulo") or not dados.get("autor"):
        return {"erro": "Título e autor são obrigatórios"}, 400

    if dados.get("ano", 0) < 0:
        return {"erro": "Ano inválido"}, 400

    for livro in usuarios:
        if livro["titulo"].lower() == dados["titulo"].lower():
            return {"erro": "Livro já cadastrado"}, 400

    novo = {
        "id": len(usuarios) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "ano": dados.get("ano", None)
    }

    usuarios.append(novo)
    return jsonify(novo), 201



@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            dados = request.json

            usuario["titulo"] = dados.get("titulo", usuario["titulo"])
            usuario["autor"] = dados.get("autor", usuario["autor"])
            usuario["ano"] = dados.get("ano", usuario["ano"])

            return jsonify(usuario)

    return {"erro": "Livro não encontrado"}, 404



@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Livro removido"}

    return {"erro": "Livro não encontrado"}, 404



if __name__ == "__main__":
    app.run(debug=True)