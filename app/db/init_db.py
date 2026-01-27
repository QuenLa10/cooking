import sqlite3
from pathlib import Path

# __file__ contient le chemin du fichier en cours d'exécution
db = Path(__file__).parent / "cooking.db"

# On crée toutes les tables
def create_tables():

    # Crée le fichier .db q'il n'existe pas
    con = sqlite3.connect(db)

    # On execute le fichier qui contient toutes les commandes pour créer les tables
    with open("schema.sql") as f:
        con.executescript(f.read())

    con.commit()
    con.close()

def fill_tables():

    con = sqlite3.connect(db)

    # On execute le fichier qui contient toutes les commandes pour remplir les tables
    with open("seed.sql") as f:
        con.executescript(f.read())

    con.commit()
    con.close()

if __name__ == "__main__":
    create_tables()
    print('La base de données a été initialisée.')
    fill_tables()
    print('La base de données a été remplie avec les données test.')