from application import db, app
from flask import render_template, request
from application.visits.models import Visit

@app.route("/visits/new/")
def visits_form():
    return render_template("visits/new.html")

@app.route("/visits/", methods=["POST"])
def visits_create():
    v = Visit(request.form.get("church"), request.form.get("comment"))

    db.session().add(v)
    db.session().commit()
  
    return "hello world!"