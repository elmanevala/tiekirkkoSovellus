from application import db
from application.models import Base

from application.admin.models import Tourguide

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), index=True, nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    visits = db.relationship("Visit", backref='account', lazy=True)
    tourguides = db.relationship("Tourguide", backref='account', lazy=True)

    def __init__(self, name, username, password, admin):
        self.name = name
        self.username = username
        self.password = password
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_tourguide(self):
        if Tourguide.query.filter(Tourguide.user_id==self.id).first() is None:
            return False
        else:
            return True

    def roles(self):
        if (self.admin == True):
            return ["ADMIN"]
        elif (User.is_tourguide(self)):
            return["GUIDE"]
        else:
            return ["ANY"]