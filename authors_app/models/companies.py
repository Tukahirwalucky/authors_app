from authors_app.extensions import db
from datetime import datetime

class Companies(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', backref='companies')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, name, description, price, origin, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.origin = origin
        self.user_id = user_id

    def __repr__(self):
        return f'{self.name} {self.origin}'


