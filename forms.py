#criar formularios    
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("fazer login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("username", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField(
        "senha",
        validators=[DataRequired(), EqualTo("senha")]  )
    botao_confirmacao = SubmitField("criar conta")

    def validate_email(self, email):
     usuario = Usuario.query.filter_by(email=email.data).first()

     if usuario:
         raise ValidationError("email já cadastrado, faça login para continuar")