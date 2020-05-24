from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user

from application.visits.models import Visit
from application.visits.forms import VisitForm
from application import db, app


@app.route("/visits/new/")
@login_required
def visits_form():
    return render_template("visits/new.html", form=VisitForm())


@app.route("/visits/", methods=["POST"])
@login_required
def visits_create():
    form = VisitForm(request.form)

    if not form.validate():
        return render_template("visits/new.html", form=form)

    v = Visit(form.church.data, form.comment.data)
    v.tourguide = form.tourguide.data
    v.account_id = current_user.id

    db.session().add(v)
    db.session().commit()

    return redirect(url_for("visits_index"))


@app.route("/visit", methods=["GET"])
@login_required
def visits_index():
    return render_template("visits/list.html", visits=Visit.query.filter(Visit.account_id == current_user.id))


@app.route("/visits/<visit_id>/", methods=["POST"])
@login_required
def tourguide_set_present(visit_id):

    v = Visit.query.get(visit_id)
    v.tourguide = True
    db.session().commit()

    return redirect(url_for("visits_index"))


@app.route("/visits/edit/<visit_id>/", methods=["GET", "POST"])
@login_required
def visit_edit(visit_id):

    return render_template("visits/edit.html", visit=Visit.query.filter(Visit.id == visit_id))


@app.route("/visits/", methods=["POST"])
@login_required
def visits_editEntry(visit_id):
    form = EditForm(request.form)

    if not form.validate():
        return render_template("visits/new.html", form=form)

    v = Visit(form.church.data, form.comment.data)
    v.tourguide = form.tourguide.data
    v.account_id = current_user.id

    db.session().add(v)
    db.session().commit()

    return redirect(url_for("visits_index"))
