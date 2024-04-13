from flask import Blueprint, request, jsonify
from authors_app.models.companies import Companies, db  
from authors_app.extensions import db
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy  # Add this import

company = Blueprint('company', __name__, url_prefix='/acompanypi/v1/')

@company.route('/register', methods=['POST'])
def register():
    company_name = request.json.get('company_name')
    description = request.json.get('description')
    email = request.json.get('email')
    origin = request.json.get('origin')
    title = request.json.get('title')
    user_id = request.json.get('user_id')
    
    if not company_name or not origin or not title or not description or not email:
        return jsonify({"error": "All fields are required"}), 400
    
    try:
        company = Companies(company_name=company_name, origin=origin, email=email, description=description, title=title, user_id=user_id,)
        db.session.add(company)
        db.session.commit()
        return jsonify({'message': 'Company registration successful'}), 201
    except sqlalchemy.exc.IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Company already exists"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
  # DELETE END POINT
  
@company.route('/delete/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    try:
        company = Companies.query.get(company_id)
        if not company:
            return jsonify({"error": "Company not found"}), 404

        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': f"Company with id {company_id} has been deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

