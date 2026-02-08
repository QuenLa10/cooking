from pathlib import Path
from datetime import timedelta

# Donne le chemin absolu de la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Création d'un objet blueprint pour stocker des paramètres
class Config:
    SECRET_KEY = "63i@i!7tj6d9!LYq"
    DATABASE = BASE_DIR / "app" / "db" / "cooking.db"
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
