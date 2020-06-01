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
    return render_template("churches/churches.html", churches=Church.churches_in_town(town_name), town=town_name)

@app.route("/churches/<town_name>/<church>/", methods=["GET", "POST"])
@login_required
def church_comment(church, town_name):

    kirkko = Church.query.filter(Church.church==church).first()
    
    return render_template("churches/church.html", comments=Church.church_comments(church), church=Church.query.filter(Church.church==church).first())