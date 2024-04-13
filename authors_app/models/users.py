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
    password_hash = db.Column(db.String(255), nullable=False)  # Changed from Text to String

    biography = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    # Define relationship to books authored by the user
    books_authored = db.relationship('Book', backref='author', lazy=True)
    
    # Define relationship to companies associated with the user
    associated_companies = db.relationship('Company', backref='associated_user', lazy=True, foreign_keys='Company.user_id')
    
    #company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    
    def _init_(self, first_name, last_name, email, contact, password, biography, user_type, company_id, image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password_hash = password  # Assign the hashed password directly
        self.biography = biography
        self.user_type = user_type
        self.company_id = company_id  # Set the company_id attribute
        self.image = image
        self.image = image
        
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"