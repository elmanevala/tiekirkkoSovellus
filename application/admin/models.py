from application import db

class Tourguide(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)


    def __init__(self, user_id, church_id):
        self.user_id = user_id
        self.church_id = church_id


class Visitors(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)
    visitors = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(144), nullable=False)

    def __init__(self, church_id, visitors, date):
        self.church_id = church_id
        self.visitors = visitors
        self.date = date
        

