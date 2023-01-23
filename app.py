
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def get_root():
    return render_template("index.html")

@app.post("/")
def post_root():
    email = request.form.get("email")
    password = request.form.get("password")

    # result = funcao(email, password)

    name = "Bruno"
    lastname = "Jucá"
    email = "brunojuca@ice.ufjf.br"
    phone = "40028922"

    return render_template("result.html", name=name, lastname=lastname, email=email, phone=phone)