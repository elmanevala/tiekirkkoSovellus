from application import db

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    church = db.Column(db.String(144), nullable=False)
    tourguide = db.Column(db.Boolean, nullable=False)
    comment = db.Column(db.String(144), nullable=False)

    def __init__(self, church, comment):
        self.church = church
        self.comment = comment
        self.tourguide = False