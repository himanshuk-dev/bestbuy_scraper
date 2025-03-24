# Initialize Flask app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from routes import api_bp
from db import db

# Load .env variables
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    # Use testing config if provided
    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(api_bp)

    return app