
from flask import render_template, url_for
from Fakepinterest import app
from flask_login import login_required
from Fakepinterest.forms import FormLogin, FormCriarConta

print("ID do app em routes:", id(app))

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<browser>")
@login_required
def perfil(browser):
    return render_template("perfil.html", browser=browser, idade=25)

print(app.url_map)