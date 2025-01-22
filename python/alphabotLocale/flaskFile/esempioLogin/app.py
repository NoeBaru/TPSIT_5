from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = 'account.db'

def get_db_connection():
    return sqlite3.connect(DB_NAME)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['e-mail']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM account WHERE utente = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

@app.route('/createAccount', methods=['GET', 'POST'])
def create_account():
    error = None
    if request.method == 'POST':
        username = request.form['e-mail']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO account (utente, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            error = 'Username already exists'
        finally:
            conn.close()

    return render_template('createAccount.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
