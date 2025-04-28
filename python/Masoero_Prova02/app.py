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
    conn, cursor = db_connection()  # Connessione al database
    cursor.execute("SELECT * FROM Prodotti")  # Recupera tutti i prodotti
    prodotti = cursor.fetchall()
    conn.close()  # Chiude la connessione
    return render_template('admin.html', prodotti=prodotti)  # Mostra la pagina admin con i prodotti

# Rotta per eliminare un prodotto
@app.route('/elimina/<int:id_prodotto>', methods=['POST'])
def elimina(id_prodotto):
    conn, cursor = db_connection()  # Connessione al database
    cursor.execute("DELETE FROM Prodotti WHERE Idprodotto = ?", (id_prodotto,))  # Elimina il prodotto
    conn.commit()  # Conferma la modifica
    conn.close()  # Chiude la connessione
    flash("Prodotto eliminato con successo!", "success")  # Messaggio di conferma
    return redirect(url_for('admin_page'))  # Ritorna alla pagina admin

# Rotta per modificare il prezzo di un prodotto
@app.route('/modifica/<int:id_prodotto>', methods=['POST'])
def modifica_prodotto(id_prodotto):
    nuovo_costo = request.form['nuovo_costo']  # Recupera il nuovo prezzo
    conn, cursor = db_connection()  # Connessione al database
    cursor.execute("UPDATE Prodotti SET Costo = ? WHERE Idprodotto = ?", (nuovo_costo, id_prodotto))  # Aggiorna il prezzo
    conn.commit()  # Conferma la modifica
    conn.close()  # Chiude la connessione
    flash("Prezzo modificato con successo!", "success")  # Messaggio di conferma
    return redirect(url_for('admin_page'))  # Torna alla pagina admin

# Rotta per aggiungere un nuovo prodotto
@app.route('/aggiungi', methods=['POST'])
def aggiungi_prodotto():
    nome = request.form['nome']  # Recupera i dati dal form
    peso = request.form['peso']
    costo = request.form['costo']

    conn, cursor = db_connection()  # Connessione al database
    cursor.execute("INSERT INTO Prodotti (Nome, Peso, Costo) VALUES (?, ?, ?)", (nome, peso, costo))  # Inserisce il prodotto
    conn.commit()  # Conferma la modifica
    conn.close()  # Chiude la connessione
    flash("Prodotto aggiunto con successo!", "success")  # Messaggio di conferma
    return redirect(url_for('admin_page'))  # Torna alla pagina admin

# Rotta per la pagina utente
@app.route('/user')
def user_page():
    username = request.args.get('username')  # Recupera l'username dai parametri della richiesta
    conn, cursor = db_connection()  # Connessione al database

    cursor.execute("SELECT * FROM Prodotti")  # Recupera tutti i prodotti
    prodotti = cursor.fetchall()

    cursor.execute("SELECT soldiCaricati FROM Utenti WHERE Username = ?", (username,))  # Recupera il saldo utente
    user_data = cursor.fetchone()
    conn.close()  # Chiude la connessione

    return render_template('user.html', prodotti=prodotti, username=username, soldiCaricati=user_data["soldiCaricati"])  # Mostra la pagina utente

# Rotta per l'acquisto di un prodotto
@app.route('/compra/<int:id_prodotto>/<username>')
def compra_prodotto(id_prodotto, username):
    conn, cursor = db_connection()  # Connessione al database

    cursor.execute("SELECT Costo FROM Prodotti WHERE Idprodotto = ?", (id_prodotto,))  # Recupera il costo del prodotto
    prodotto = cursor.fetchone()

    cursor.execute("SELECT soldiCaricati FROM Utenti WHERE Username = ?", (username,))  # Recupera il saldo utente
    user_data = cursor.fetchone()

    if prodotto and user_data:  # Controlla se il prodotto e l'utente esistono
        costo = prodotto["Costo"]
        saldo = user_data["soldiCaricati"]

        if saldo >= costo:  # Verifica se l'utente ha abbastanza soldi
            nuovo_saldo = saldo - costo
            cursor.execute("UPDATE Utenti SET soldiCaricati = ? WHERE Username = ?", (nuovo_saldo, username))  # Aggiorna il saldo
            conn.commit()  # Conferma l'acquisto
            flash("Acquisto effettuato con successo!", "success")  # Messaggio di conferma
        else:
            flash("Saldo insufficiente per l'acquisto!", "error")  # Messaggio di errore
            
    conn.close()  # Chiude la connessione
    return redirect(url_for('user_page', username=username))  # Torna alla pagina utente

# Avvio dell'app Flask in modalità debug
if __name__ == '__main__':
    app.run(debug=True)
