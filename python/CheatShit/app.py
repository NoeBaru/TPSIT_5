from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Creazione dell'istanza dell'app Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessario per usare flash messages (per notifiche agli utenti)
DATABASE = 'database.db'  # Nome del database SQLite

# Funzione per ottenere una connessione sempre attiva al database
def db_connection():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)  # Permette connessioni da più thread
    conn.row_factory = sqlite3.Row  # Consente di accedere ai risultati con nomi di colonna
    return conn, conn.cursor()  # Restituisce la connessione e il cursore

# Rotta per la pagina iniziale con il form di login
@app.route('/')
def index():
    return render_template('index.html')  # Mostra la pagina principale con il form di login

# Rotta per gestire il login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']  # Recupera l'username dal form
    password = request.form['password']  # Recupera la password dal form

    conn, cursor = db_connection()  # Connessione al database
    cursor.execute("SELECT TipoUtente, soldiCaricati FROM Utenti WHERE Username = ? AND Password = ?", (username, password))
    user = cursor.fetchone()  # Recupera un solo risultato
    conn.close()  # Chiude la connessione

    if user:  # Se l'utente esiste, controlla il suo tipo
        user_type = user["TipoUtente"]  # Ottiene il tipo di utente
        if user_type == 'admin': return redirect(url_for('admin_page'))  # Reindirizza alla pagina admin
        elif user_type == 'user': return redirect(url_for('user_page', username=username))  # Reindirizza alla pagina utente

    return "Login fallito. Controlla le credenziali."  # Messaggio di errore se le credenziali sono errate

# Rotta per la pagina admin
@app.route('/admin')
def admin_page():
    return render_template('admin.html')  # Mostra la pagina admin con i prodotti

# Rotta per la pagina utente
@app.route('/user')
def user_page():
    return render_template('user.html')  # Mostra la pagina utente

# Avvio dell'app Flask in modalità debug
if __name__ == '__main__':
    app.run(debug=True)
