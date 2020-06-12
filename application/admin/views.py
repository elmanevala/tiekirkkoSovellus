from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.churches.models import Church
from application.admin.models import Tourguide


@app.route("/admin/users/", methods=["GET"])
@login_required(role="ADMIN")
def admin_users():

    return render_template("admin/userlist.html", users=User.query.filter(User.id!=1))


@app.route("/admin/users/tourguide/<user_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def add_tourguide(user_id):

    return render_template("admin/addtourguide.html", user=User.query.filter(User.id == user_id).first())


@app.route("/admin/users/tourguide/<user_id>/addchurch", methods=["GET", "POST"])
@login_required(role="ADMIN")
def tourguide_church(user_id):

    church_name = request.form.get("church")
    church = Church.query.filter(Church.church == church_name).first()

    if church is None:
        return render_template("admin/addtourguide.html", user=User.query.filter(User.id==user_id).first(), error="Kirkkoa ei tietokannassa")

    church_id = church.id

    tg = Tourguide(user_id, church_id)
    db.session().add(tg)
    db.session().commit()

    return render_template("admin/userlist.html", users=User.query.filter(User.id!=1))

@app.route("/admin/guide/", methods=["GET", "POST"])
@login_required(role="GUIDE")
def guide_churches():

    return render_template("admin/guidechurches.html", churches=Church.tourguide_churches(current_user.id))
