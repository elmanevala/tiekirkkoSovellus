from application import db, app
from flask import redirect, url_for, render_template, request
from application.visits.models import Visit

@app.route("/visits/new/")
def visits_form():
    return render_template("visits/new.html")

@app.route("/visits/", methods=["POST"])
def visits_create():
    v = Visit(request.form.get("church"), request.form.get("comment"))

    db.session().add(v)
    db.session().commit()
  
    return redirect(url_for("visits_index"))

@app.route("/visit", methods=["GET"])
def visits_index():
    return render_template("visits/list.html", visits = Visit.query.all())

@app.route("/visits/<visit_id>/", methods=["POST"])
def tourguide_set_present(visit_id):

    v = Visit.query.get(visit_id)
    v.tourguide = True
    db.session().commit()
  
    return redirect(url_for("visits_index"))