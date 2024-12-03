from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Preference, User

user_bp = Blueprint('user', __name__)

@user_bp.route('/preferences', methods=['POST'])
@jwt_required()
def set_preferences():
    data = request.get_json()
    favorite_genre = data['favorite_genre']
    
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    preference = Preference(favorite_genre=favorite_genre, user_id=user.id)
    db.session.add(preference)
    db.session.commit()

    return jsonify({"message": "Preferences updated successfully"}), 200
