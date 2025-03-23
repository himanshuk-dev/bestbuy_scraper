# Initialize Flask app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from .routes import api_bp

# Load .env variables
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Set config from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(api_bp)

    return app