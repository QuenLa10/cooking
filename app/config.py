from pathlib import Path

# Donne le chemin absolu de la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Création d'un objet blueprint pour stocker des paramètres
class Config:
    SECRET_KEY = "dev-secret-key"
    DATABASE = BASE_DIR / "app" / "db" / "cooking.db"
    DEBUG = True
