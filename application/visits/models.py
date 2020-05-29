from application import db
from application.models import Base


from sqlalchemy.sql import text


class Visit(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    church_id = db.Column(db.Integer, db.ForeignKey(
        'church.id'), nullable=False)
    tourguide = db.Column(db.Boolean, nullable=False)
    comment = db.Column(db.String(144), nullable=False)

    def __init__(self, church_id, comment):
        self.church_id = church_id
        self.comment = comment
        self.tourguide = False

    @staticmethod
    def name_comment_tourguide(visit_id):
        stmt = text("SELECT Church.church, Visit.comment, Visit.tourguide FROM Visit"
                    " LEFT JOIN Church ON Visit.church_id = Church.id"
                    " WHERE (Visit.id IS visit_id)")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])
            response.append(row[1])
            response.append(row[2])

        return response


