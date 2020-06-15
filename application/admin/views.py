from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required

from application.auth.models import User
from application.churches.models import Church
from application.admin.models import Tourguide, Visitors

from application.admin.forms import VisitorForm

from datetime import datetime


@app.route("/admin/users/", methods=["GET"])
@login_required(role="ADMIN")
def admin_users():

    return render_template("admin/userlist.html", users=Tourguide.guide_list())


@app.route("/admin/users/tourguide/<user_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def add_tourguide(user_id):

    return render_template("admin/addtourguide.html", user=User.query.filter(User.id == user_id).first(), guide_churches=Tourguide.church_list(user_id))


@app.route("/admin/users/tourguide/<user_id>/addchurch", methods=["GET", "POST"])
@login_required(role="ADMIN")
def tourguide_church(user_id):

    church_name = request.form.get("church")
    church = Church.query.filter(Church.church == church_name).first()

    if church is None:
        return render_template("admin/addtourguide.html", user=User.query.filter(User.id==user_id).first(), no_data_error="Kirkkoa ei tietokannassa")
    if Tourguide.query.filter(Tourguide.church_id==church.id, Tourguide.user_id==user_id).first() is not None:
        return render_template("admin/addtourguide.html", user=User.query.filter(User.id==user_id).first(), in_table_error="Oppaalle on jo lisätty tämä kirkko")

    church_id = church.id

    tg = Tourguide(user_id, church_id)
    db.session().add(tg)
    db.session().commit()

    return render_template("admin/userlist.html", users=User.query.filter(User.id!=1))

@app.route("/admin/guide/", methods=["GET", "POST"])
@login_required(role="GUIDE")
def guide_churches():

    return render_template("admin/guidechurches.html", churches=Church.tourguide_churches(current_user.id))

@app.route("/admin/guide/visitors/<church_id>", methods=["GET", "POST"])
@login_required(role="GUIDE")
def guide_addvisitors(church_id):
    date = datetime.today().strftime('%Y-%m-%d')

    return render_template("admin/addvisitors.html", church=Church.query.filter(Church.id==church_id).first(), form=VisitorForm(), date=date)


@app.route("/admin/guide/visitors/<church_id>/addvisitors", methods=["GET", "POST"])
@login_required(role="GUIDE")
def guide_create_stat(church_id):
    date = datetime.today().strftime('%Y-%m-%d')

    form = VisitorForm(request.form)

    if not form.validate():
        return render_template("admin/addvisitors.html", church=Church.query.filter(Church.id==church_id).first(), form=form, date=date)
    if Visitors.query.filter(Visitors.church_id==church_id and Visitors.date==date).first() is not None:
        nbm = Visitors.query.filter(Visitors.church_id==church_id and Visitors.date==date).first().visitors
        return render_template("admin/addvisitors.html", church=Church.query.filter(Church.id==church_id).first(), form=form, date=date, in_table_error="Päivän kävijät on jo merkattu: " + str(nbm) + " kävijää")
    
    date = datetime.today().strftime('%Y-%m-%d')
    v = Visitors(church_id, form.visitors.data, date)

    db.session().add(v)
    db.session().commit()

    return redirect(url_for("guide_churches"))

@app.route("/admin/guide/stats", methods=["GET", "POST"])
@login_required(role="GUIDE")   
def guide_view_stats():

    return render_template("admin/stats.html", visitor_sum=Visitors.sum(current_user.id), stats=Visitors.stats(current_user.id))

@app.route("/admin/<church>/", methods=["GET", "POST"])
@login_required
def church_admin_view(church):
    return render_template("churches/church.html", comments=Church.church_comments(church), church=Church.query.filter(Church.church==church).first())
    
 