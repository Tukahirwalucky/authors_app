from flask import Flask
from authors_app.extensions import migrate, db
from flask_sqlalchemy import SQLAlchemy
from authors_app.controllers.auth.auth_controller import auth
from authors_app.controllers.auth.book_controller import book_bp
from authors_app.controllers.auth.company_controller import company_bp  # Corrected import statement

# Import your database model classes here


def create_app():
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object('config.Config')
   
    # Initialize the Flask application with SQLAlchemy
    db.init_app(app)

    # Initialize Flask-Migrate for handling database migrations
    migrate.init_app(app, db)

    # Register blueprints or routes here
    
    
    from authors_app.models.users import Users
    from authors_app.models.companies import Companies
    from authors_app.models.books import Books

    app.register_blueprint(auth)
    app.register_blueprint(book_bp)
    app.register_blueprint(company_bp)  # Register the company blueprint
    
    
    
    @app.route('/')
    def home():
        return "AUTHORS API project set up 1"

    return app