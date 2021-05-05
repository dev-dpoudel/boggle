from flask import Flask
from flask_cors import CORS
from .controllers import boggle_bp


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config.from_object('config.Config')

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(boggle_bp)

        return app
