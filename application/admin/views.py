from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User


@app.route("/admin/users/", methods=["GET"])
@login_required(role="ADMIN")
def admin_users():

    return render_template("admin/userlist.html", users=User.query.all())