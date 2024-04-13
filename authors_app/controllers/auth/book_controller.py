from flask import Blueprint, request, jsonify
from authors_app.models.books import Books
from authors_app.extensions import db

book_bp = Blueprint('book', __name__, url_prefix='/api/v1/book')

@book_bp.route('/register', methods=['POST'])
def register_book():
    title = request.json.get('title')
    description = request.json.get('description')
    image = request.json.get('image')
    price = request.json.get('price')
    price_unit = request.json.get('price_unit')
    pages = request.json.get('pages')
    publication_date = request.json.get('publication_date')
    genre = request.json.get('genre')
    isbn = request.json.get('isbn')
    user_id = request.json.get('user_id')
    
    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    if not description:
        return jsonify({"error": "Description is required"}), 400
    
    if not image:
        return jsonify({"error": "Image is required"}), 400
    
    if not price:
        return jsonify({"error": "Price is required"}), 400
    
    if not price_unit:
        return jsonify({"error": "Price unit is required"}), 400
    
    if not pages:
        return jsonify({"error": "Pages is required"}), 400
    
    if not publication_date:
        return jsonify({"error": "Publication date is required"}), 400
    
    if not genre:
        return jsonify({"error": "Genre is required"}), 400
    
    if not isbn:
        return jsonify({"error": "ISBN is required"}), 400
    
    if not user_id:
        return jsonify({"error": "User_id is required"}), 400

    new_book = Books(title=title, description=description, image=image, price=price, price_unit=price_unit, 
                pages=pages, publication_date=publication_date, genre=genre, isbn=isbn, user_id=user_id)
    
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify({'message': 'Book registered successfully'}), 201

@book_bp.route('/books', methods=['GET'])
def get_books():
    books = Books.query.all()
    return jsonify([book.serialize() for book in books]), 200

@book_bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Books.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.serialize()), 200

@book_bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Books.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.json
    for field in ['title', 'description', 'image', 'price', 'price_unit', 'pages', 'publication_date', 'genre', 'isbn', 'user_id']:
        if field in data:
            setattr(book, field, data[field])

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'}), 200

@book_bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200
