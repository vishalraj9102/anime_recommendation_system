import requests
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import User

anime_bp = Blueprint('anime', __name__)

ANI_LIST_URL = "https://graphql.anilist.co"

def fetch_anime(query, variables=None):
    headers = {"Content-Type": "application/json"}
    response = requests.post(ANI_LIST_URL, json={"query": query, "variables": variables}, headers=headers)
    return response.json()

@anime_bp.route('/search', methods=['GET'])
def search_anime():
    name = request.args.get('name')
    genre = request.args.get('genre')
    
    query = """
    query ($search: String) {
        Media(search: $search, type: ANIME) {
            id
            title {
                romaji
                english
            }
            genres
        }
    }
    """
    variables = {"search": name or genre}
    data = fetch_anime(query, variables)
    
    return jsonify(data)

@anime_bp.route('/recommendations', methods=['GET'])
@jwt_required()
def recommendations():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    preferences = user.preferences.first()

    if preferences:
        favorite_genre = preferences.favorite_genre
        query = """
        query ($genre: String) {
            Page {
                media(genre: $genre, type: ANIME) {
                    title {
                        romaji
                        english
                    }
                }
            }
        }
        """
        variables = {"genre": favorite_genre}
        data = fetch_anime(query, variables)
        
        return jsonify(data)
    return jsonify({"message": "No preferences set"}), 400
