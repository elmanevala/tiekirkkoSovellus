from application import db
from application.models import Base

from flask_login import current_user

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
    def name_comment_tourguide():

        stmt = text("SELECT Church.church, Visit.comment, Visit.tourguide, Visit.id FROM Visit"
                    " JOIN Church ON Visit.church_id = Church.id AND Visit.account_id = :user").params(user=current_user.id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(
                {"church": row[0], "comment": row[1], "tourguide": row[2], "id": row[3]})

        return response

    @staticmethod
    def comments_in_total():

        stmt = text("SELECT COUNT(visit) FROM Visit")

        res = db.engine.execute(stmt)

        for row in res:
            response= row[0]

        return response

