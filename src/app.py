'''Juliana'''
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API VendaMais rodando!"})

@app.route("/produtos")
def produtos():
    return jsonify([
        {"id": 1, "nome": "Produto A"},
        {"id": 2, "nome": "Produto B"}
    ])

if __name__ == "__main__":
    app.run(debug=True)