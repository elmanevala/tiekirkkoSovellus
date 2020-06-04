from flask import render_template
from application import app, db

from application.churches.models import Church


@app.route("/")
def index():

    return render_template("index.html")


@app.context_processor
def context_processor():
    allData = Church.query.all()

    churches = []
    for church in allData:
        churches.append(church.church)

    return dict(churches=churches)
