from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user

from application.churches.models import Church
from application import db, app


def churces_to_table():
    file = open('kirkot.txt')
    Lines = file.readlines()

    print("MOIMOIMOIMOIOIMOI \n MOIMOIMOIMOI")

    for line in Lines:
        print(line)
