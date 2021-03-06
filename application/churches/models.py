from application import db
from sqlalchemy.sql import text

import os


class Church(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    church = db.Column(db.String(144), nullable=False, index=True)
    town = db.Column(db.String(144), nullable=False)

    visits = db.relationship("Visit", backref='Church', lazy=True)
    tourguides = db.relationship("Tourguide", backref='Church', lazy=True)
    visitors = db.relationship("Visitors", backref='Church', lazy=True)

    def __init__(self, church, town):
        self.church = church
        self.town = town

    def get_id(self):
        return self.id

    @staticmethod
    def town_churches_visits():

        stmt = text("SELECT DISTINCT A.town AS town, "
                    "(SELECT COUNT(*) FROM Church B WHERE B.town=A.town) AS churches, "
                    "(SELECT COUNT(V.comment) FROM Church C LEFT JOIN Visit V ON C.id=V.church_id AND C.town=A.town) AS visits"
                    " FROM Church A")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(
                {"town": row[0], "churches": row[1], "visits": row[2]})

        return response

    @staticmethod
    def churches_in_town(town):

        stmt = text("SELECT church FROM Church WHERE town=:town").params(
            town=town)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"church": row[0]})

        return response

    @staticmethod
    def church_comments(church):

        stmt = text("SELECT V.comment, V.date_created,"
        "(SELECT U.username FROM Account U WHERE U.id=V.account_id)"
        " FROM Church C JOIN Visit V ON C.id=V.church_id AND C.church=:church").params(
            church=church)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            if os.environ.get("HEROKU"):
                date = row[1].strftime("%x")
            else:
                date = str(row[1][:-9])
                
            response.append({"comment": row[0], "date_created": date, "user": row[2]})
            
        return response

    @staticmethod
    def tourguide_churches(guide_id):

        stmt = text("SELECT DISTINCT C.church, C.id FROM Church C JOIN Tourguide T ON C.id=T.church_id AND T.user_id=:guide_id").params(
            guide_id=guide_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"church": row[0], "id": row[1]})
            
        return response

    
