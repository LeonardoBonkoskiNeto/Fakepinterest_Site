
from flask import render_template, url_for, redirect
from Fakepinterest import app, database, bcrypt
from Fakepinterest.models import Usuario, foto
from flask_login import login_required, login_user, logout_user, current_user
from Fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename

print("ID do app em routes:", id(app))


#######DEFINIR METODOS#########
@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))

    return render_template("homepage.html", form=form_login)

#######CRIAR CONTA#########
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

#######CRIAR PERFIL#########
@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required

def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        #usuario vendo o proprio perfil
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            #salvar o arquivo na pasta fotos_post
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                app.config["UPLOAD_FOLDER"],  nome_seguro)
            arquivo.save(caminho)
            #registrar esse caminho no banco de dados
            Foto = foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(Foto)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:     
          usuario = Usuario.query.get(int(id_usuario))
          return render_template("perfil.html", usuario=usuario, form=None)
    
#######CRIAR LOGOUT#########
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

print(app.url_map)

#######CRIAR FEED#########
@app.route("/feed")
@login_required
def feed():
    fotos = foto.query.order_by(foto.data_criacao.desc()).all()
    return render_template("feed.html", fotos=fotos)