from flask import Flask, jsonify, request

"""
autore: Noemi Baruffolo
classe: 5AROB
testo: progettare una web API che riceve un numero intero e risponde se il numero è pari o dispari
"""

app = Flask(__name__)

@app.route('/api/v1/parita', methods=['GET'])
def check_parita():
    # Controlla se il parametro 'num' è presente nella richiesta
    if 'num' not in request.args:
        return jsonify({"errore": "Nessun numero fornito. Specificare un numero"}), 400

    try:
        num = int(request.args['num'])  # Converte il parametro in un intero
    except ValueError:
        return jsonify({"errore": "Numero non valido. Inserire un numero intero"}), 400

    # Determina se il numero è pari o dispari
    parita = "pari" if num % 2 == 0 else "dispari"

    return jsonify({"num": num, "parita": parita})

if __name__ == '__main__':
    app.run(debug=True)