from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user

from application.churches.models import Church
from application import db, app


@app.route("/towns", methods=["GET"])
@login_required
def towns_index():



    return render_template("churches/townlist.html", towns=Church.town_churches_visits())


@app.route("/towns", methods=["GET"])
@login_required
def town_churchview():

    return render_template("churches/townlist.html", towns=Church.town_churches_visits)
