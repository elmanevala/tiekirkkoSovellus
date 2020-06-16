from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class VisitForm(FlaskForm):
    church = StringField("Kirkko",  [validators.Length(min=2, max=50)], render_kw={"placeholder": "kirkko"})
    comment = StringField("Kommentti",  [validators.Length(min=2, max=500, message='Kommentin oltava 3-500 merkkiä')], render_kw={"placeholder": "kommentti"})
    tourguide = BooleanField("Opas paikalla")
    class Meta:
        csrf = False


class EditForm(FlaskForm):
    comment = StringField("Uusi kommentti",  [validators.Length(min=2, max=500, message='Kommentin oltava 3-500 merkkiä')], render_kw={"placeholder": "kommentti"})

    class Meta:
        csrf = False