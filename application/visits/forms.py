from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class VisitForm(FlaskForm):
    church = StringField("Kirkko",  [validators.Length(min=2)])
    comment = StringField("Kommentti",  [validators.Length(min=2)])
    tourguide = BooleanField("Opas paikalla")
    class Meta:
        csrf = False