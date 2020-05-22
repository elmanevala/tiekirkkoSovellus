from flask_wtf import FlaskForm
from wtforms import StringField

class VisitForm(FlaskForm):
    church = StringField("Kirkko")
    comment = StringField("Kommentti")
    class Meta:
        csrf = False