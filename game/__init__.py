from flask import Flask
from flask_cors import CORS
from .controllers import BoardView


def create_app(mode_config=None):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    if mode_config == "test":
        app.config.from_object('config.TestConfig')
    else:
        app.config.from_object('config.Config')

    CORS(app)
    BoardView.register(app)

    with app.app_context():
        # Register Blueprints
        pass

        return app
