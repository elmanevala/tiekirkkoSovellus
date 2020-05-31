from application import db
from sqlalchemy.sql import text


class Church(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    church = db.Column(db.String(144), nullable=False)
    town = db.Column(db.String(144), nullable=False)


    visits = db.relationship("Visit", backref='Church', lazy=True)

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
            response.append({"town":row[0], "churches":row[1], "visits":row[2]})

        return response

