from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from VendingMachine import VendingMachine
import sqlite3
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
SECRET_KEY = "mysecretkey"
vm = VendingMachine()

# Inizializzazione database utenti e prodotti
def initialize_db():
    con = sqlite3.connect('./distributoreAutomatico.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('user', 'admin')),
            balance REAL DEFAULT 5.0
        )
    ''')
    con.commit()
    con.close()

initialize_db()  # Avvia la creazione delle tabelle


# --- FUNZIONI DI AUTENTICAZIONE ---
def get_user_data():
    con = sqlite3.connect('./distributoreAutomatico.db')
    cur = con.cursor()
    cur.execute("SELECT username, password, role, balance FROM utenti")
    users = {row[0]: {"password": row[1], "role": row[2], "balance": row[3]} for row in cur.fetchall()}
    con.close()
    return users

def check_account(username, password):
    users = get_user_data()
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]  # Restituisce ruolo e saldo
    return None

def add_user(username, password, role="user"):
    if role not in ["user", "admin"]:
        return False
    hashed_password = generate_password_hash(password)
    users = get_user_data()
    if username not in users:
        con = sqlite3.connect('./distributoreAutomatico.db')
        cur = con.cursor()
        cur.execute("INSERT INTO utenti (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
        con.commit()
        con.close()
        return True
    return False

# --- ROUTE DI AUTENTICAZIONE ---
@app.route("/")
def index():
    user_token = request.cookies.get("username")
    if user_token:
        decoded_token = jwt.decode(user_token, SECRET_KEY, algorithms=["HS256"])
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = check_account(username, password)

        if user:
            expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
            token = jwt.encode({"username": username, "role": user["role"]}, SECRET_KEY, algorithm="HS256")
            response = make_response(redirect(url_for('home')))
            response.set_cookie("username", token, httponly=True, samesite="Strict", max_age=60*60*24)
            return response
        else:
            return render_template("login.html", alert="Credenziali errate")
    return render_template("login.html")

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie("username")
    return response

# --- HOME PAGE DIFFERENZIATA ---
@app.route("/home")
def home():
    user_token = request.cookies.get("username")
    if not user_token:
        return redirect(url_for('login'))

    decoded_token = jwt.decode(user_token, SECRET_KEY, algorithms=["HS256"])
    role = decoded_token["role"]

    if role == "admin":
        return redirect(url_for('admin_panel'))
    return redirect(url_for('user_panel'))

# --- PAGINA UTENTE ---
@app.route("/user")
def user_panel():
    user_token = request.cookies.get("username")
    if not user_token:
        return redirect(url_for('login'))
    
    decoded_token = jwt.decode(user_token, SECRET_KEY, algorithms=["HS256"])
    username = decoded_token["username"]
    
    con = sqlite3.connect('./distributoreAutomatico.db')
    cur = con.cursor()
    cur.execute("SELECT balance FROM utenti WHERE username = ?", (username,))
    balance = cur.fetchone()[0]
    con.close()

    return render_template("products.html", products=vm.products, balance=balance)

@app.route("/buy", methods=['POST'])
def buy():
    user_token = request.cookies.get("username")
    if not user_token:
        return redirect(url_for('login'))
    
    decoded_token = jwt.decode(user_token, SECRET_KEY, algorithms=["HS256"])
    username = decoded_token["username"]

    product_id = int(request.form["product_id"])
    con = sqlite3.connect('./distributoreAutomatico.db')
    cur = con.cursor()
    cur.execute("SELECT balance FROM utenti WHERE username = ?", (username,))
    balance = cur.fetchone()[0]

    if product_id in vm.products and balance >= vm.products[product_id]['price']:
        vm.vend(product_id, vm.products[product_id]['price'])
        new_balance = balance - vm.products[product_id]['price']
        cur.execute("UPDATE utenti SET balance = ? WHERE username = ?", (new_balance, username))
        con.commit()
        con.close()
        return redirect(url_for('user_panel'))
    else:
        con.close()
        return "Saldo insufficiente o prodotto non disponibile", 400

# --- PAGINA ADMIN ---
@app.route("/admin")
def admin_panel():
    user_token = request.cookies.get("username")
    if not user_token:
        return redirect(url_for('login'))

    decoded_token = jwt.decode(user_token, SECRET_KEY, algorithms=["HS256"])
    if decoded_token["role"] != "admin":
        return "Accesso negato", 403

    return render_template("admin.html", products=vm.products)

@app.route("/admin/add_product", methods=['POST'])
def add_product():
    product_id = int(request.form["product_id"])
    name = request.form["name"]
    price = float(request.form["price"])
    stock = int(request.form["stock"])

    if product_id not in vm.products:
        vm.add_product(product_id, name, price, stock)
        return redirect(url_for('admin_panel'))
    else:
        return "ID prodotto già esistente", 400

@app.route("/admin/remove_product", methods=['POST'])
def remove_product():
    product_id = int(request.form["product_id"])
    if product_id in vm.products:
        vm.remove_product(product_id)
        return redirect(url_for('admin_panel'))
    else:
        return "Prodotto non esistente", 400

@app.route("/admin/update_stock", methods=['POST'])
def update_stock():
    product_id = int(request.form["product_id"])
    stock = int(request.form["stock"])

    if product_id in vm.products:
        vm.restock(product_id, stock)
        return redirect(url_for('admin_panel'))
    else:
        return "Prodotto non esistente", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
