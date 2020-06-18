from flask import render_template
from application import app, db

from application.churches.models import Church
from application.visits.models import Visit
from application.admin.models import Visitors

@app.route("/")
def index():

    return render_template("index.html", visit_total=Visit.comments_in_total(), visitor_total=Visitors.visitors_in_total())


@app.context_processor
def context_processor():
    allData = Church.query.all()

    churches = []
    for church in allData:
        churches.append(church.church)

    return dict(churches=churches)
