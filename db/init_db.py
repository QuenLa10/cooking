import sqlite3
from pathlib import Path

# __file__ contient le chemin du fichier en cours d'exécution
db = Path(__file__).parent / "cooking.db"

def create_connection():
    con = sqlite3.connect(db)
    
    #Permet de faire bien fonctionner les relations (notamment les FK)
    con.execute("PRAGMA foreign_keys = ON;")
    return con

# On crée toutes les tables
def create_tables(con):
    cursor = con.cursor()

    # Table UTILISATEURS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        mdp_hash TEXT NOT NULL,
        xp INTEGER DEFAULT 0,
        niveau INTEGER DEFAULT 1,
        est_admin BOOLEAN DEFAULT 0,
        est_banned BOOLEAN DEFAULT 0,
        date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Table SAISONS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saisons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL
    );
    """)

    # Table INGREDIENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL,
        id_saison INT,
        FOREIGN KEY (id_saison) REFERENCES saisons(id)
    );
    """)

    # Table DIFFICULTES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS difficultes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL
    );
    """)

    # Table RECETTES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recettes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT,
        temps TIME,
        id_difficulte INT,
        id_auteur INT,
        recompense_xp INT,
        date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_auteur) REFERENCES utilisateurs(id),
        FOREIGN KEY (id_difficulte) REFERENCES difficultes(id)
    );
    """)

    # Table RECETTES_INGREDIENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recettes_ingredients (
        id_recette INT,
        id_ingredient INT,
        quantite TEXT,
        PRIMARY KEY (id_recette, id_ingredient),
        FOREIGN KEY (id_recette) REFERENCES recettes(id),
        FOREIGN KEY (id_ingredient) REFERENCES ingredients(id)
    );
    """)

    # Table UTILISATEURS_RECETTES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs_recettes (
        id_utilisateur INT,
        id_recette INT,
        date_cuisine TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id_utilisateur, id_recette, date_cuisine),
        FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id),
        FOREIGN KEY (id_recette) REFERENCES recettes(id)
    );
    """)

    # Table ETAPES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS etapes ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INT NOT NULL,
        description TEXT,
        id_recette int,
        FOREIGN KEY (id_recette) REFERENCES recettes(id)                   
    );
    """)

    # Table USTENSILES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ustensiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,               
    nom VARCHAR(255) UNIQUE NOT NULL               
    );
    """)

    # Table USTENSILES_RECETTES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ustensiles_recettes (
    id_ustensile INT,
    id_recette INT,  
    PRIMARY KEY (id_ustensile, id_recette),
    FOREIGN KEY (id_ustensile) REFERENCES ustensiles(id),
    FOREIGN KEY (id_recette) REFERENCES recettes(id)             
    );
    """)

    con.commit()

def main():
    con = create_connection()
    create_tables(con)
    con.close()
    print("Base de données initialisée avec succès")

if __name__ == "__main__":
    main()
