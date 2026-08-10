#criar formularios    
from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Fakepinterest import Usuario

class FormLogin():
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("senha", validators=[DataRequired()])
    botao_confirmaçao = SubmitField("fazer login")

class FormCriarConta():
     email = StringField("E-mail", validators=[DataRequired(), Email()])
     username = StringField("senha", validators=[DataRequired()])
     senha = PasswordField("senha", validators=[DataRequired(), Length(6, 20)])
     confirmacao_senha = PasswordField("senha", validators=[DataRequired(), EqualTo("senha")])
     botao_confirmaçao = SubmitField("criar conta")

     def validate_email(self, email):
          usuario = Usuario.query.filyer_by(email=email.data).first()

          if usuario:
               return ValidationError("email ja cadastrado, faça log in para continuar")