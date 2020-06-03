from flask import render_template
from application import app, db

from application.churches.models import Church


@app.route("/")
def index():

    allData = Church.query.all()

    churches = []
    for church in allData:
        churches.append(church.church)


    return render_template("index.html", churches=churches)
