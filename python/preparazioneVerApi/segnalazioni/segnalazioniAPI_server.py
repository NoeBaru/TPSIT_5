from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import sqlite3
from datetime import datetime

app = Flask(__name__)
api = Api(app)

DB_PATH = "./segnalazioni.db"

"""
    Author: Noemi Baruffolo
    date: 5/05/2025
    es. preparazioneVerApi 2
    text: server Web API segnalazioni (vedi testo su Classroom)
    """

def getConnection():
    conn = sqlite3.connect(DB_PATH)
    return conn, conn.cursor()

class Quartieri(Resource):
    def get(self):  #p.2 restituisci l’elenco dei quartieri
        conn, cur = getConnection()
        cur.execute("SELECT * FROM quartieri")
        result = cur.fetchall()
        conn.close()
        return [{"id": r[0], "nome": r[1]} for r in result], 200

    def post(self):  #p.3 aggiungi un nuovo quartiere
        data = request.json
        nome = data.get("nome")
        if not nome:
            return {"errore": "Nome del quartiere mancante"}, 400
        try:
            conn, cur = getConnection()
            cur.execute("INSERT INTO quartieri (nome) VALUES (?)", (nome,))
            conn.commit()
            conn.close()
            return {"messaggio": "Quartiere aggiunto"}, 201
        except Exception as e:
            return {"errore": str(e)}, 400

class Segnalazioni(Resource):
    def post(self):  #p.1 registra una nuova segnalazione
        data = request.json
        conn, cur = getConnection()

        try:
            id_quartiere_query = "SELECT id FROM quartieri WHERE nome = ?"
            cur.execute(id_quartiere_query, (data["quartiere"],))
            result = cur.fetchone()
            if not result:
                return {"errore": "Quartiere non esistente"}, 400
            id_quartiere = result[0]

            cur.execute("""
                INSERT INTO segnalazioni (id_quartiere, categoria, descrizione, stato, data_ora)
                VALUES (?, ?, ?, ?, ?)
            """, (
                id_quartiere,
                data["categoria"],
                data["descrizione"],
                data.get("stato", "in attesa"),
                data.get("data_ora", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            ))
            conn.commit()
            conn.close()
            return {"messaggio": "Segnalazione registrata"}, 201
        except Exception as e:
            return {"errore": str(e)}, 400

    def get(self):  #p.5 ritorna elenco filtrato
        stato = request.args.get("stato")
        categoria = request.args.get("categoria")
        quartiere = request.args.get("quartiere")

        query = """
            SELECT s.id, q.nome, s.categoria, s.descrizione, s.stato, s.data_ora
            FROM segnalazioni s
            JOIN quartieri q ON s.id_quartiere = q.id
            WHERE 1=1
        """ # in ogni caso restituisce almeno qualcosa, se true restituisce tutto della select
        params = []
        if stato:
            query += " AND s.stato = ?"
            params.append(stato)
        if categoria:
            query += " AND s.categoria = ?"
            params.append(categoria)
        if quartiere:
            query += " AND q.nome = ?"
            params.append(quartiere)

        conn, cur = getConnection()
        cur.execute(query, params)
        result = cur.fetchall()
        conn.close()
        return [
            {
                "id": r[0],
                "quartiere": r[1],
                "categoria": r[2],
                "descrizione": r[3],
                "stato": r[4],
                "data_ora": r[5]
            } for r in result
        ], 200

class UpdateSegnalazione(Resource):  #p.4 aggiorna stato
    def put(self, id_segnalazione):
        data = request.json
        nuovo_stato = data.get("stato")
        if not nuovo_stato:
            return {"errore": "Stato mancante"}, 400
        conn, cur = getConnection()
        cur.execute("UPDATE segnalazioni SET stato = ? WHERE id = ?", (nuovo_stato, id_segnalazione))
        conn.commit()
        conn.close()
        return {"messaggio": "Stato aggiornato"}, 200

api.add_resource(Quartieri, "/quartieri")
api.add_resource(Segnalazioni, "/segnalazioni")
api.add_resource(UpdateSegnalazione, "/segnalazioni/<int:id_segnalazione>")

if __name__ == "__main__":
    app.run(debug=True)
