from flask import Flask
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///visits.db"    
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

from application import views

from application.visits import models
from application.visits import views

from application.auth import models
from application.auth import views

from application.churches import models
from application.churches import views

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try: 
    db.create_all()
except:
    pass

# Reading the file kirkot.txt to churches table.
from application.churches.models import Church
if Church.query.first() is None:
    file = open('kirkot.txt')
    Lines = file.readlines()
    for line in Lines:
        town_church = line.split(", ")
        c = Church(town_church[1][:-1], town_church[0])
        db.session().add(c)
        db.session().commit()