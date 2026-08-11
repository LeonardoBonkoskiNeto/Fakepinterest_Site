
from flask import render_template, url_for
from Fakepinterest import app, database, bcrypt
from Fakepinterest.models import Usuario, foto
from flask_login import login_required
from Fakepinterest.forms import FormLogin, FormCriarConta

print("ID do app em routes:", id(app))

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        #bcrypt codifica a senha e da mais segurança
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, senha=senha, email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<browser>")
@login_required

def perfil(browser):
    return render_template("perfil.html", browser=browser, idade=25)

print(app.url_map)