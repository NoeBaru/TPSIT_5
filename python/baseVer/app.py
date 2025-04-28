from flask import Flask, render_template, request, redirect, make_response
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "mia_chiave_super_segreta"

# Homepage con form per il nome
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")

        # Creazione di un token JWT
        token = jwt.encode({"nome": nome, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm="HS256")

        # Creazione di un cookie con il token
        resp = make_response(redirect("/home"))
        resp.set_cookie("user_token", token, max_age=1800)  # Cookie valido 30 minuti
        return resp

    return render_template("index.html")

# Pagina privata accessibile solo con token
@app.route("/home")
def home():
    token = request.cookies.get("user_token")

    if not token:
        return redirect("/")  # Se non c'è token, torna alla homepage

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        nome = decoded["nome"]
        return f"<h1>Ciao, {nome}! Benvenuto nella tua area riservata.</h1>"
    except jwt.ExpiredSignatureError:
        return "Sessione scaduta. Torna alla <a href='/'>homepage</a>"
    except jwt.InvalidTokenError:
        return "Token non valido. Torna alla <a href='/'>homepage</a>"

if __name__ == "__main__":
    app.run(debug=True)
