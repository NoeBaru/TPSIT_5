from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app) 

DB_PATH = "./meteo_db.db"

"""
    Author: Noemi Baruffolo
    date: 02/05/2025
    es. preparazioneVerApi
    text: server Web API metereologica (vedi testo su Classroom)
"""

def getConnection():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    return conn, cur

class Grandezza(Resource):
    def get(self, nome): #1.a
        conn, cur = getConnection()
        query = "SELECT id_misura FROM grandezze WHERE grandezza_misurata = ?"
        cur.execute(query, (nome,))
        result = cur.fetchone()
        conn.commit()
        conn.close()
        if result:
            return {"id_misura" : result[0]}, 200
        else:
            return "Il nome della grandezza ricercata non esiste", 404

       
class Stazione(Resource):
    def get(self, nome): #1.b
        conn, cur = getConnection()
        query = "SELECT id_stazione FROM stazioni WHERE nome = ?"
        cur.execute(query, (nome,))
        result = cur.fetchone()
        conn.commit()
        conn.close()
        if result:
            return {"id_stazione" : result[0]}, 200
        else:
            return "Il nome della stazione ricercata non esiste", 404

class Misurazione(Resource):
    def post(self): #1.c
        dati = request.json
        conn, cur = getConnection()
        try: #per controllare che non dia errori
            query = "INSERT INTO misurazioni VALUES (NULL, ?, ?, ?, ?)"
            cur.execute(query, (dati["id_stazione"], dati["id_grandezza"], dati["data_ora"], dati["valore"]))
            conn.commit()
            conn.close()
            return "Misurazione inserita con successo", 201 #201 creazione
        except Exception as e:
            return f"Errore {str(e)}", 400

class Statistiche(Resource):  # 1.d
    def get(self, id_stazione, id_grandezza):
        conn, cur = getConnection()
        query = """
            SELECT AVG(valore), MAX(valore), MIN(valore)
            FROM misurazioni
            WHERE id_stazione = ? AND id_grandezza = ?
        """
        cur.execute(query, (id_stazione, id_grandezza))
        result = cur.fetchone()
        conn.close()
        if result and all(val is not None for val in result):
            return {
                "media": result[0],
                "massimo": result[1],
                "minimo": result[2]
            }, 200
        else:
            return "Nessun dato disponibile per la combinazione fornita", 404

api.add_resource(Grandezza, "/grandezza/<string:nome>")
api.add_resource(Stazione, "/stazione/<string:nome>")
api.add_resource(Misurazione, "/misurazione")
api.add_resource(Statistiche, "/statistiche/<int:id_stazione>/<int:id_grandezza>")

if __name__ == "__main__":
    app.run(debug=True)
