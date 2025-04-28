from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def create_db():
    con = sqlite3.connect("./studenti.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS studenti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cognome TEXT NOT NULL,
            eta INTEGER NOT NULL
        )
    ''')
    con.commit()
    con.close()

create_db()

def get_all_students():
    con = sqlite3.connect("./studenti.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studenti")
    studenti = cur.fetchall()
    con.close()
    print("Studenti", studenti)

    # Assicuriamoci che i dati siano restituiti correttamente
    studenti_dict = {row[0]: {"nome": row[1], "cognome": row[2], "eta": row[3]} for row in studenti}
    print("Studenti dal DB:", studenti_dict)  # Debug: stampa i dati nel terminale
    return studenti_dict

@app.route("/studenti", methods=["POST"])
def create_studente():
    dati = request.json
    con = sqlite3.connect("./studenti.db")
    cur = con.cursor()
    cur.execute("INSERT INTO studenti (nome, cognome, eta) VALUES (?, ?, ?)", 
                (dati.get("nome"), dati.get("cognome"), dati.get("eta")))
    con.commit()
    new_id = cur.lastrowid
    con.close()
    return jsonify({"messaggio": "Studente aggiunto", "id": new_id}), 201

@app.route("/studenti", methods=["GET"])
def get_studenti():
    studenti = get_all_students()
    print("Studenti trovati:", studenti)  # Aggiunto per debug
    return jsonify(studenti)

@app.route("/studenti/<int:id>", methods=["GET"])
def get_studente(id):
    con = sqlite3.connect("./studenti.db")
    cur = con.cursor()
    cur.execute("SELECT nome, cognome, eta FROM studenti WHERE id = ?", (id,))
    studente = cur.fetchone()
    con.close()
    if studente:
        return jsonify({"nome": studente[0], "cognome": studente[1], "eta": studente[2]})
    return jsonify({"errore": "Studente non trovato"}), 404

@app.route("/studenti/<int:id>", methods=["PUT"])
def update_studente(id):
    dati = request.json
    con = sqlite3.connect("./studenti.db")
    cur = con.cursor()
    cur.execute("UPDATE studenti SET nome = ?, cognome = ?, eta = ? WHERE id = ?", 
                (dati.get("nome"), dati.get("cognome"), dati.get("eta"), id))
    con.commit()
    con.close()
    return jsonify({"messaggio": "Studente aggiornato"})

@app.route("/studenti/<int:id>", methods=["DELETE"])
def delete_studente(id):
    con = sqlite3.connect("./studenti.db")
    cur = con.cursor()
    cur.execute("DELETE FROM studenti WHERE id = ?", (id,))
    con.commit()
    con.close()
    return jsonify({"messaggio": "Studente eliminato"})

if __name__ == "__main__":
    app.run(debug=True)
