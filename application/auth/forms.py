from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", render_kw={"placeholder": "käyttäjänimi"})
    password = PasswordField("Salasana",  render_kw={"placeholder": "salasana"})

    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=3, message='Käyttäjäimi vähintään kolme merkkiä pitkä')], render_kw={"placeholder": "käyttäjänimi"})
    name = StringField("Nimi", [validators.Length(min=3, message='Nimi vähintään kolme merkkiä pitkä')], render_kw={"placeholder": "nimi"})
    password = PasswordField("Salasana", [validators.EqualTo('passwordcheck', message='Salasanat eivät täsmää')], render_kw={"placeholder": "salasana"}, )
    passwordcheck = PasswordField("Salasana uudestaan",render_kw={"placeholder": "salasana uudestaan"})

    class Meta:
        csrf = False

class PasswordForm(FlaskForm):
    password = PasswordField("Salasana", [validators.EqualTo('passwordcheck', message='Salasanat eivät täsmää')], render_kw={"placeholder": "salasana"}, )
    passwordcheck = PasswordField("Salasana uudestaan",render_kw={"placeholder": "salasana uudestaan"})
    
    class Meta:
        csrf = False