from flask_wtf import FlaskForm
from wtforms import validators, IntegerField


class VisitorForm(FlaskForm):
    visitors = IntegerField("Vieralijoita", render_kw={"placeholder": "Vierailijoita"})

    class Meta:
        csrf = False