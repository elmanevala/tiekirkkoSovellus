from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    name = StringField("Nimi")
    password = PasswordField("Salasana")
    passwordcheck = PasswordField("Salasana uudestaan")

    class Meta:
        csrf = False
