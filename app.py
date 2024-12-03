from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config
from models import db
from routes.auth import auth_bp
from routes.anime import anime_bp
from routes.user import user_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database and JWT
db.init_app(app)
jwt = JWTManager(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(anime_bp, url_prefix='/anime')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
