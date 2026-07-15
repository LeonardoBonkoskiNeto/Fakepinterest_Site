from main import app  
from flask import render_template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<browser>")
def perfil(browser):
     return render_template("perfil.html", browser=browser, idade=25)


if __name__=="__main__":
    app.run(debug=True)