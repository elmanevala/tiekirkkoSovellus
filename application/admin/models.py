from application import db

class Tourguide(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)


    def __init__(self, user_id, church_id):
        self.user_id = user_id
        self.church_id = church_id

