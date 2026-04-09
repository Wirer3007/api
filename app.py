from flask import Flask, jsonify, request
import os

app = Flask(__name__)

usuarios = [
    {   "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899
        },

    {   "id": 2,
        "titulo": "Saboroso Cadaver",
        "autor": "Darkside",
        "ano": 2022
        },

    {   "id": 3,
        "titulo": "Kaiju n8",
        "autor": "Matsumoto",
        "ano": 2019
        },
]




@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)
    


@app.route("/usuarios", methods=['POST'])
def criar_usuario():
 if not usuarios.get('titulo') or not usuarios.get('autor'):
    if usuarios['ano'] < 0: return {"erro": "Ano inválido"}, 400
    for l in usuarios:
      if l['titulo'] == usuarios['titulo']:
       return {"erro": "Livro já cadastrado"}, 400
    novo = request.json
    novo['id'] = len(usuarios) + 1
    usuarios.append(novo)
    return jsonify(novo), 201
 return {
    "mensagem": "Livro cadastrado com sucesso",
     "livro": novo
    }, 201
 return {"erro": "Título e autor são obrigatórios"}, 400

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            dados = request.json
            usuario['nome'] = dados.get('nome', usuario['nome'])
            return jsonify(usuario)
    return {"erro": "Usuário não encontrado"}, 404


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário removido"}
    return {"erro": "Usuário não encontrado"}, 404




if __name__ == "__main__":
    app.run (debug = True)