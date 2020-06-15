from application import db
from sqlalchemy.sql import text

import os


class Tourguide(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    church_id = db.Column(db.Integer, db.ForeignKey(
        'church.id'), nullable=False)

    def __init__(self, user_id, church_id):
        self.user_id = user_id
        self.church_id = church_id


    @staticmethod
    def church_list(user_id):

        stmt = text("SELECT C.church, C.town FROM Church C JOIN Tourguide T ON C.id=T.church_id AND T.user_id=:user_id").params(
            user_id=user_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"church": row[0], "town": row[1]})

        return response


    @staticmethod
    def guide_list():

        stmt = text("SELECT U.username, U.date_created,"
        "(SELECT COUNT(*) FROM Tourguide WHERE Tourguide.user_id=U.id) AS nbm, U.id"
        " FROM Account U WHERE U.id!=1 ORDER BY nbm DESC")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            if os.environ.get("HEROKU"):
                date = row[1].strftime("%x")
            else:
                date = str(row[1][:-9])
            
            response.append({"username": row[0], "date_created": date, "church_nbm": row[2], "id": row[3]})

        return response



class Visitors(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    church_id = db.Column(db.Integer, db.ForeignKey(
        'church.id'), nullable=False)
    visitors = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(144), nullable=False)

    def __init__(self, church_id, visitors, date):
        self.church_id = church_id
        self.visitors = visitors
        self.date = date

    @staticmethod
    def sum(user_id):

        stmt = text("SELECT SUM(A.visitors) AS sum FROM Visitors A JOIN Tourguide T ON A.church_id=T.church_id AND T.user_id=:user_id").params(
            user_id=user_id)

        res = db.engine.execute(stmt)

        for row in res:
            response= row[0]

        return response

    @staticmethod
    def stats(user_id):

        stmt = text("SELECT C.church AS church, "
        "(SELECT SUM(V.visitors) FROM Visitors V WHERE church_id = C.id) AS sum, "
        "(SELECT AVG(V.visitors) FROM Visitors V WHERE church_id = C.id) AS avg, "
        "(SELECT COUNT(comment) FROM Visit WHERE Visit.church_id=C.id) AS comment_sum, "
        "C.id, C.town "
        "FROM Church C JOIN Tourguide T ON T.church_id=C.id AND T.user_id=:user_id").params(
            user_id=user_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(
                {"church": row[0], "sum": row[1], "avg": row[2], "comment_sum": row[3], "church_id": row[4], "town": row[5]})

        return response
