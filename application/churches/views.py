from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user

from application.churches.models import Church
from application import db, app


@app.route("/churches", methods=["GET"])
@login_required
def towns_index():
    return render_template("churches/townlist.html", towns=Church.town_churches_visits())


@app.route("/churches/<town_name>/", methods=["GET", "POST"])
@login_required
def town_churchview(town_name):
    return render_template("churches/churches.html", comments=Church.churches_in_town(town_name), town=town_name)
