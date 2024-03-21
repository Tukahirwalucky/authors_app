from flask import Blueprint, request, jsonify
from authors_app.models.books import Books
from authors_app.models.users import Users
from authors_app.models.companies import Companies
from authors_app.extensions import db
from datetime import datetime

book_bp = Blueprint('book', __name__, url_prefix='/api/v1/book')

@book_bp.route('/register', methods=['POST'])
def register_book():
    try:
        data = request.get_json()

        # Print out the data received from the request for debugging
        print("Received Data:", data)

        # Extract data from the request
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        price_unit = data.get('price_unit')
        pages = data.get('pages')
        publication_date = data.get('publication_date')
        isbn = data.get('isbn')
        genre = data.get('genre')
        user_id = data.get('user_id')
        company_id = data.get('company_id')

        # Validate required fields
        required_fields = ['title', 'description', 'price', 'price_unit', 'pages', 'publication_date', 'isbn', 'genre', 'user_id', 'company_id']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Convert publication_date to a Date object
        try:
            publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid publication date format. Please use YYYY-MM-DD"}), 400

        # Check if user and company exist
        user = Users.query.get(user_id)
        if not user:
            return jsonify({"error": f"User with ID {user_id} not found"}), 404

        company = Companies.query.get(company_id)
        if not company:
            return jsonify({"error": f"Company with ID {company_id} not found"}), 404

        # Create a new book instance with retrieved objects
        new_book = Books(title=title, description=description, price=price, price_unit=price_unit,
                        pages=pages, user_id=user_id, company_id=company_id,
                        publication_date=publication_date, isbn=isbn, genre=genre)

        # Add the book to the database session and commit changes
        db.session.add(new_book)
        db.session.commit()

        return jsonify({"message": f"Book '{title}' has been uploaded"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500
