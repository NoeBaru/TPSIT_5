from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
import sqlite3
from random import randint

app = Flask(__name__)

#crea la tabella del db se non esiste già
def inizializeDb():
    con = sqlite3.connect("./socialNetworkDB.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            idUtente INT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            PRIMARY KEY("idUtente")
        )
    ''')
    con.commit()
    con.close()

inizializeDb()

#prende i dati del login
def getUserData():
    con = sqlite3.connect("./socialNetworkDB.db")
    cur = con.cursor()
    cur.execute("SELECT idUtente, username, password FROM utenti")
    users = {row[0]: {"username": row[1], "password": row[2]} for row in cur.fetchall()}
    con.close()
    return users

def checkAccount(username, password): # controlla che l'account esista
    users = getUserData()
    if username in users and  password:
        return users[username]
    else:
        return None
    
@app.route("/")
def index():
    user = request.cookies.get("username")
    if user: # se l'utente è loggato mostra la pagina index, altrimenti rimanda a quella di login
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = checkAccount(username, password)
        
        if user:
            response = make_response(redirect(url_for('home')))
            response.set_cookie("username", httponly=True, samesite="Strict", max_age=60*60*24)
            return response
        else:
            return render_template("login.html", alert = "Credenziali errate")
    return render_template("login.html")

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie("username")
    return response

@app.route("/index")
def home():
    user = request.cookies.get("username")
    if not user:
        return redirect(url_for('login'))
    
@app.route("/index", methods=['POST'])
def nuovoStato():
    con = sqlite3.connect("./socialNetworkDB.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS stati (idStato INT PRIMARY KEY, stato TEXT NOT NULL, idUtente INT, FOREIGN KEY(idUtente) REFERENCES "stati"("idUtente"))''')
    stati = []
    stato = int(request.form["stato"])
    username = request.form["username"]
    idUtente = request.form["idUtente"]

    con.close()
    if stato not in stati:
        stato.append(stati)
        nuovoStato(stato, username, idUtente)
        return redirect(url_for('idex'))
    else:
        return "Stato già esistente"

@app.route("/index", methods=['POST'])    
def visualizzaStatoRandom():
    nRandom = randint() #generare un numero casuale tra 1 e il numero di stati presenti nel db

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')