from application import db
from application.models import Base

class Visit(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)
    tourguide = db.Column(db.Boolean, nullable=False)
    comment = db.Column(db.String(144), nullable=False)

    def __init__(self, church_id, comment):
        self.church_id = church_id
        self.comment = comment
        self.tourguide = False
