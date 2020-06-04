from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/login.html", form=form,
                               error="Käyttäjää ei löydy")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/registration", )
def auth_register():
    return render_template("auth/registration.html", form=RegistrationForm())


@app.route("/auth/", methods=["POST"])
def auth_newUser():

    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registration.html", form=form)

    u = User(form.name.data, form.username.data, form.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/myinfo/", methods=["POST", "GET"])
@login_required
def myinfo():

    return render_template("auth/myinfo.html", form=RegistrationForm(), user=User.query.filter(User.id == current_user.id).first())


@app.route("/auth/myinfo/<name>", methods=["POST", "GET"])
@login_required
def update_name(name):

    ## Koska yksittäisiin muutoksii ei voi käyttä wtf-kaavaketta, teen tässä myöhemmin oman validoinnin
    u = User.query.filter(User.id == current_user.id).first()
    u.name = request.form.get("name")

    print("!!!!!!!!!!")
    print("uusi nimi: " + u.name)
    print("!!!!!!!!!!")

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("myinfo"))
