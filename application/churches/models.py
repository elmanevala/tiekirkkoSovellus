from application import db


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

