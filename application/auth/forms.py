from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from wtforms.validators import EqualTo

class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", render_kw={"placeholder": "käyttäjänimi"})
    password = PasswordField("Salasana",  render_kw={"placeholder": "salasana"})

    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=3, max=20, message='Käyttäjäimi 3-20 merkkiä')], render_kw={"placeholder": "käyttäjänimi"})
    name = StringField("Nimi", [validators.Length(min=3, max=50, message='Nimi 3-50 merkkiä')], render_kw={"placeholder": "nimi"})
    password = PasswordField("Salasana", [validators.Length(min=8, max=20, message='Salasanassa oltava 8-20 merkkiä'), EqualTo('passwordcheck', message='Salasanat eivät täsmää')], render_kw={"placeholder": "salasana"}, )
    passwordcheck = PasswordField("Salasana uudestaan",render_kw={"placeholder": "salasana uudestaan"})

    class Meta:
        csrf = False

class PasswordForm(FlaskForm):
    password = PasswordField("Salasana", [validators.Length(min=8, max=20, message='Salasanassa oltava 8-20 merkkiä'), EqualTo('passwordcheck', message='Salasanat eivät täsmää')], render_kw={"placeholder": "salasana"}, )
    passwordcheck = PasswordField("Salasana uudestaan",render_kw={"placeholder": "salasana uudestaan"})

    class Meta:
        csrf = False