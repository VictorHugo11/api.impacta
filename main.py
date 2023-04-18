from flask import Flask, jsonify

app = Flask(__name__)

filmes = [
    {"Nome": "Velozes e Furiosos", "Ano": 2001},
    {"Nome": "+ Velozes + Furiosos", "Ano": 2003},
    {"Nome": "Velozes e Furiosos: Desafio em Toquio", "Ano": 2006},
    {"Nome": "Velozes e Furiosos 4", "Ano": 2009},
    {"Nome": "Velozes e Furiosos 5: Operação Rio", "Ano": 2011},
    {"Nome": "Velozes e Furiosos 6", "Ano": 2013},
    {"Nome": "Velozes & Furiosos 7", "Ano": 2015},
    {"Nome": "Velozes e Furiosos 8", "Ano": 2017},
    {"Nome": "Velozes e Furiosos 9", "Ano": 2021}
]

# Rota para consultar filmes por ano de lançamento
@app.route('/filmes/<int:ano>', methods=['GET'])
def buscar_filmes_por_ano(ano):
    if ano >= 1980 and ano <= 2021:
        # Filtra os filmes pelo ano de lançamento
        filmes_encontrados = [filme for filme in filmes if filme['Ano'] == ano]
        if filmes_encontrados:
            return jsonify({"filmes": filmes_encontrados}), 200
        else:
            return jsonify({"mensagem": "Nenhum filme encontrado para o ano de lancamento informado"}, 'codigo da solitacao 404')
    else:
        return jsonify({"mensagem": "Ano de lancamento invalido"}, 'codigo da solitacao 400')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
