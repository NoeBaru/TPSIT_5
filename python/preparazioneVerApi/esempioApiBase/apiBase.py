from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) 

# Dizionario di studenti
studenti = {
    1: {"nome": "Mario", "cognome": "Rossi", "eta": 18},
    2: {"nome": "Luca", "cognome": "Bianchi", "eta": 19},
    3: {"nome": "Giulia", "cognome": "Verdi", "eta": 17}
}

class Studenti(Resource):
    def get(self): #usata per restituire un dato
        return studenti
   
    def post(self): #usata per aggiungere/inserire dati
        dati = request.json #prendo i dati del front-end/json/db
       
        nuovo_id = max(studenti.keys(), default=0) + 1
        studenti[nuovo_id] = {
            "nome": dati.get("nome"),
            "cognome": dati.get("cognome"),
            "eta": dati.get("eta")
        }
        return {"messaggio": "Studente aggiunto", "id": nuovo_id, "studente": studenti[nuovo_id]}, 201
   
    def head(self):
        return "", 200
   
    def options(self):
        return {
            "allow": "GET, POST, OPTIONS, HEAD"
        }, 200, {
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS, HEAD",
            "Access-Control-Allow-Origin": "*"
        }

class Studente(Resource):
    def get(self, id): #usata per restituire un dato
            studente = studenti.get(id)
            if studente:
                return studente
            return {"errore": "Studente non trovato"}, 404

    def patch(self, id): #usato per aggiornare i dati (come update, ma per una risorsa sola/parziale)
        if id in studenti:
            dati = request.json
            studenti[id].update(dati)
            return jsonify({"messaggio": "Studente aggiornato", "studente": studenti[id]})
        return {"errore": "Studente non trovato"}, 404
   
    def put(self, id):
        if id in studenti:
            dati = request.json
            # Controllo campi obbligatori (nome, cognome, eta)
            if not all(k in dati for k in ("nome", "cognome", "eta")):
                return {"errore": "Campi mancanti. Servono: nome, cognome, eta"}, 400

            # Sovrascrive completamente la risorsa esistente
            studenti[id] = {
                "nome": dati["nome"],
                "cognome": dati["cognome"],
                "eta": dati["eta"]
            }
            return {"messaggio": "Studente aggiornato (completo)", "studente": studenti[id]}
        return {"errore": "Studente non trovato"}, 404
           

    def delete(self,id): #usata per rimuovere qualche risorsa/dato
        if id in studenti:
            del studenti[id]
            return jsonify({"messaggio": "Studente eliminato"})
        return {"errore": "Studente non trovato"}, 404
   
    def head(self, id): #usata come la get, ma restituisce solo i codici, come fosse una sorta di test
        if id in studenti:
            return "", 200
        return "", 404

    def options(self, id):
        return {
            "allow": "GET, PUT, PATCH, DELETE, OPTIONS, HEAD"
        }, 200, {
            "Access-Control-Allow-Methods": "GET, PUT, PATCH, DELETE, OPTIONS, HEAD",
            "Access-Control-Allow-Origin": "*"
        }

#per gestire l'end-point
api.add_resource(Studenti, "/studenti") #localhost:porta/studenti
api.add_resource(Studente, "/studenti/<int:id>") #localhost:porta/studenti/1

if __name__ == "__main__":
   
    app.run(debug=True)

"""
    In Flask puro, usi jsonify() per restituire una risposta JSON formattata correttamente,
    con intestazioni HTTP (header Content-Type: application/json) e serializzazione.
    In Flask-RESTful, questa parte è già automatizzata dal framework.
   
    Quando tu ritorni un dizionario Python, ci pensa lui a:
    convertirlo in JSON con json.dumps(...)
    impostare l'header Content-Type: application/json
    creare l'oggetto Response
"""
"""
    POST → Crea una nuova risorsa
        Usi POST quando inserisci un nuovo studente.
        Non conosci a priori l'ID (viene generato dal server).
        È non idempotente: se invii due volte lo stesso POST, crea due risorse.
"""

"""
    PUT → Aggiorna (o crea) una risorsa specifica
        Usi PUT quando modifichi uno studente con ID noto.
        Il client fornisce l'id nella URL.
        È idempotente: inviare più volte lo stesso PUT dà lo stesso risultato.
"""

"""
    PATCH → Modifica parziale di una risorsa
        Usi PATCH quando vuoi aggiornare solo alcuni campi di uno studente.
        È idempotente: inviare più volte la stessa richiesta PATCH produce lo stesso risultato.
"""

"""
    GET → Legge le informazioni
        Cosa fa   Recupera dati dal server (senza modificarli)
        Quando usarlo   Per leggere una o più risorse
        È sicuro
        È idempotente (chiamate ripetute non cambiano niente)
"""

"""
    DELETE → Cancella una risorsa
        Cosa fa   Rimuove una risorsa dal server
        Quando usarlo   Per cancellare una risorsa con ID noto
        Non è sicuro
        È idempotente (una volta cancellata, le richieste successive non cambiano nulla)
"""

"""
    HEAD → Come GET ma senza corpo
        Cosa fa   Verifica se la risorsa esiste, senza restituire il contenuto
        Quando usarlo   Per controlli leggeri sull'esistenza di una risorsa
        È sicuro
        È idempotente
"""

"""
    OPTIONS → Scopri quali metodi sono disponibili
        Cosa fa   Restituisce l'elenco dei metodi supportati dall'endpoint
        Quando usarlo   Per capire come interagire con una risorsa (utile per CORS)
        È sicuro
        È idempotente
"""