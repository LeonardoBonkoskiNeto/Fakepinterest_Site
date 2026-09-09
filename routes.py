
from flask import render_template, url_for, redirect
from Fakepinterest import app, database, bcrypt
from Fakepinterest.models import Usuario, foto
from flask_login import login_required, login_user, logout_user, current_user
from Fakepinterest.forms import FormLogin, FormCriarConta

print("ID do app em routes:", id(app))

@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))

    return render_template("homepage.html", form=form_login)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        #bcrypt codifica a senha e da mais segurança
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, senha=senha, email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<id_usuario>")
@login_required

def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        #usuario vendo o proprio perfil
        return render_template("perfil.html", usuario=current_user, idade=25)
    else:     
          usuario = Usuario.query.get(int(id_usuario))
          return render_template("perfil.html", usuario=usuario, idade=25)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

print(app.url_map)