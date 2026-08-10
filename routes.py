
from flask import render_template, url_for
from Fakepinterest import app
from flask import login_required

print("ID do app em routes:", id(app))

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<browser>")
@login_required
def perfil(browser):
    return render_template("perfil.html", browser=browser, idade=25)

print(app.url_map)