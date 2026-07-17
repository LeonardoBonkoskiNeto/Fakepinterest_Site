
from flask import render_template, url_for
from Fakepinterest import app

print("ID do app em routes:", id(app))

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<browser>")
def perfil(browser):
    return render_template("perfil.html", browser=browser, idade=25)

print(app.url_map)