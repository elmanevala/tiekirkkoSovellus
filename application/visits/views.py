from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user, LoginManager, login_manager

from application.visits.models import Visit
from application.visits.forms import VisitForm, EditForm
from application.churches.models import Church
from application import db, app


@app.route("/visits/new/")
@login_required
def visits_form():

    return render_template("visits/new.html", form=VisitForm())


@app.route("/visits/", methods=["POST"])
@login_required
def visits_create():
    form = VisitForm(request.form)

    church = request.form.get("church")

    if not form.validate():
        return render_template("visits/new.html", form=form, error="Kirkkoa ei tietokannassa")
    if Church.query.filter(Church.church == church).first() is None:
        allData = Church.query.all()

        churches = []
        for church in allData:
            churches.append(church.church)
        return render_template("visits/new.html", form=form, error="Kirkkoa ei tietokannassa")

    c = Church.query.filter(Church.church == church).first()


    v = Visit(c.id, form.comment.data)
    v.tourguide = form.tourguide.data
    v.account_id = current_user.id

    db.session().add(v)
    db.session().commit()

    return redirect(url_for("visits_index"))


@app.route("/visit", methods=["GET"])
@login_required
def visits_index():

    return render_template("visits/list.html", visits=Visit.name_comment_tourguide())


@app.route("/visits/edit/<visit_id>/tourguide", methods=["POST"])
@login_required
def tourguide_set_present(visit_id):

    v = Visit.query.get(visit_id)

    if v.account_id != current_user.id:
        login_manager = LoginManager()
        return login_manager.unauthorized()

    if v.tourguide == True:
        v.tourguide = False
    else:
        v.tourguide = True

    db.session().commit()

    return redirect(url_for("visit_edit", visit_id=visit_id, form=EditForm()))


@app.route("/visits/edit/<visit_id>/", methods=["GET", "POST"])
@login_required
def visit_edit(visit_id):

    v = Visit.query.filter(Visit.id == visit_id).first()

    if v.account_id != current_user.id:
        login_manager = LoginManager()
        return login_manager.unauthorized()

    visit_church = v.church_id

    return render_template("visits/edit.html", visit=Visit.query.filter(Visit.id == visit_id).first(), form=EditForm(), church=Church.query.filter(Church.id == visit_church).first())


@app.route("/visits/edit/<visit_id>/entry/", methods=["GET", "POST"])
@login_required
def visits_edit_entry(visit_id):
    v1=Visit.query.filter(Visit.id==visit_id).first()
    church_id = v1.church_id
    
    form = EditForm(request.form)

    if not form.validate():
        return render_template("visits/edit.html", visit=Visit.query.filter(Visit.id == visit_id).first(), form=form, church=Church.query.filter(Church.id == church_id).first())
    if v1.account_id != current_user.id:
        login_manager = LoginManager()
        return login_manager.unauthorized()

    v = Visit.query.get(visit_id)
    v.comment = form.comment.data

    db.session().add(v)
    db.session().commit()

    return redirect(url_for("visits_index"))


@app.route("/visits/<visit_id>/delete", methods=["POST"])
@login_required
def visit_delete(visit_id):

    Visit.query.filter(Visit.id == visit_id).delete()
    db.session().commit()

    return redirect(url_for("visits_index"))
