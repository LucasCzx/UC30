from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "123"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "LG" and senha == "12345":
            session["usuario"] = usuario
            return redirect("/dashboard")

        return "Login errado"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect("/login")

    return render_template("dashboard.html", usuario=session["usuario"])

@app.route("/rotalogin")
def rotalogin():
    return "Esta é a rota login"

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/login")

app.run(debug=True)

