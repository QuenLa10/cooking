import flask
from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)

    # config
    app.config.from_object(Config)


    # blueprints
    from .routes.auth import auth_bp
    from .routes.recipes import recipes_bp
    from .routes.profile import profile_bp
    
    # ajoute les routes à l'app
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(profile_bp)

    # route pour tester (temporaire)
    @app.route("/")
    def accueil() :
        return "Projet Cooking !!!"

    return app