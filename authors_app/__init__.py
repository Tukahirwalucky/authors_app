from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from authors_app.controllers.auth.auth_controller import auth
from authors_app.controllers.auth.book_controller import book_bp
from authors_app.controllers.auth.company_controller import company
from authors_app.extensions import db
from authors_app.controllers.auth.auth_controller import auth

# Import your database model classes here
from authors_app.models.users import Users
from authors_app.models.companies import Companies
from authors_app.models.books import Books

#registering blueprints
#app.register_blueprint(auth)

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
   
    # Initialize the Flask application with SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    # Register blueprints or routes here
    app.register_blueprint(auth)
    app.register_blueprint(book_bp)
    app.register_blueprint(company)

    @app.route('/')
    def home():
        return "AUTHORS API project set up 1"

    return app
