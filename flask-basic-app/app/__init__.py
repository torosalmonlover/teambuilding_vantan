from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # Import and register the blueprint
    from .routes import main
    app.register_blueprint(main)

    return app