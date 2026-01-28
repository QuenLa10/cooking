import sqlite3
from flask import g, current_app

# g vit le temps d'une requête HTTP, il est vide au début, détruit à la fin
# On peut y stocker ce qu'on veut : g.user = "Quentin"
# current_app est un pointeur vers l'app en cours d'utilisation


# Fonction pour ouvrir 1 seule connexion DB par requête
def get_db() :
    if "db" not in g : # Si la connexion n'existe pas encore
        g.db = sqlite3.connect(current_app.config["DATABASE"]) # Chemin récupéré depuis la config
    return g.db

# Fonction pour fermer la base de données (décorateur pour fermer automatiquement dans __init__.py)
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
