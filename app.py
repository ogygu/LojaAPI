from flask import Flask, make_response, request, jsonify
from bd import Itens

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/itens", methods=['GET'])
def getItens():
    return Itens


@app.route("/itens/create", methods=['POST'])
def creatItens():
    iten = request.json
    Itens.append(iten)
    return iten
    # return make_response(jsonify(message="Roupa cadastrada com sucesso", iten=iten))


app.run()
