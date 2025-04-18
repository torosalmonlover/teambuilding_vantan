from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # Register blueprints or routes here if needed

    return app