from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

livros = [
    {
        "id": 1,
        "titulo": "Kaiju Nº 8",
        "autor": "Naoya Matsumoto",
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
        "titulo": "Frankenstein",
        "autor": "Mary Shelley",
        "data": "1818"
    },
    {
        "id": 4,
        "titulo": "Saboroso Cadáver",
        "autor": "DarkSide",
        "data": "2018"
    },
    {
        "id": 5,
        "titulo": "O Chamado de Cthulhu",
        "autor": "H. P. Lovecraft",
        "data": "1926"
    },
    {
        "id": 6,
        "titulo": "O Médico e o Monstro",
        "autor": "Robert Louis Stevenson",
        "data": "1886"
    },
    {
        "id": 7,
        "titulo": "O Rei de Amarelo",
        "autor": "Robert W. Chambers",
        "data": "1895"
    },
    {
        "id": 8,
        "titulo": "O Corvo",
        "autor": "Edgar Allan Poe",
        "data": "1845"
    }
]



@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)



@app.route("/livros", methods=["POST"])
def criar_livro():
    dados = request.get_json()

    if not dados:
        return {"erro": "Dados não enviados"}, 400

    if not dados.get("titulo") or not dados.get("autor"):
        return {"erro": "Título e autor são obrigatórios"}, 400


    for livro in livros:
        if livro["titulo"].lower() == dados["titulo"].lower():
            return {"erro": "Livro já cadastrado"}, 400


    novo_id = max([livro["id"] for livro in livros], default=0) + 1

    novo = {
        "id": novo_id,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "data": dados.get("data", None)
    }

    livros.append(novo)

    return jsonify(novo), 201



@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    for livro in livros:
        if livro["id"] == id:

            dados = request.get_json()

            if not dados:
                return {"erro": "Dados não enviados"}, 400

            if "titulo" in dados and not dados["titulo"]:
                return {"erro": "O título não pode estar vazio"}, 400

            if "autor" in dados and not dados["autor"]:
                return {"erro": "O autor não pode estar vazio"}, 400

          
            if "titulo" in dados:
                for outro_livro in livros:
                    if (
                        outro_livro["id"] != id
                        and outro_livro["titulo"].lower() == dados["titulo"].lower()
                    ):
                        return {"erro": "Já existe outro livro com esse título"}, 400

            livro["titulo"] = dados.get("titulo", livro["titulo"])
            livro["autor"] = dados.get("autor", livro["autor"])
            livro["data"] = dados.get("data", livro["data"])

            return jsonify(livro)

    return {"erro": "Livro não encontrado"}, 404



@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)

            return {
                "mensagem": "Livro removido com sucesso"
            }

    return {"erro": "Livro não encontrado"}, 404



if __name__ == "__main__":
    app.run(debug=True)
