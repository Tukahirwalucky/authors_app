from authors_app.extensions import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.Integer, nullable=False)
    user_type = db.Column(db.String(50), nullable=False)
    image = db.Column(db.BLOB, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, first_name, last_name, email, contact, user_type, image, password, biography):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.user_type = user_type
        self.image = image
        self.password = password
        self.biography = biography

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def __repr__(self):
        return f'User(id={self.id}, email={self.email})'