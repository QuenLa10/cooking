import flask
from flask import Flask
from .config import Config
from .database import close_db

def create_app():

    # On crée l'app, qui contient les routes, configuration etc
    app = Flask(__name__)


    # config car une app a besoin du mode debug, clé secrète, chemin bd etc
    # Flask stocke ceci dans app.config
    # Ici, Flask lit la classe et copie ses variables dedans
    app.config.from_object(Config)

    # Flask va appeler close_db() automatiquement à la fin de chaque requête
    app.teardown_appcontext(close_db)


    # blueprints, chaque chose qu'on importe permet d'importer toutes les fonctions
    from .routes.index import index_bp
    from .routes.auth import auth_bp
    from .routes.recipes import recipes_bp
    from .routes.profile import profile_bp
    
    # ajoute les routes à l'app
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(profile_bp)


    return app