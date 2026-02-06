PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS ustensiles_recettes ;
DROP TABLE IF EXISTS ustensiles ;
DROP TABLE IF EXISTS etapes ;
DROP TABLE IF EXISTS utilisateurs_recettes ;
DROP TABLE IF EXISTS recettes_ingredients ;
DROP TABLE IF EXISTS recettes ;
DROP TABLE IF EXISTS difficultes ;
DROP TABLE IF EXISTS ingredients ;
DROP TABLE IF EXISTS saisons ;
DROP TABLE IF EXISTS utilisateurs ;



-- Table UTILISATEURS
CREATE TABLE utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        mdp_hash TEXT NOT NULL,
        xp INTEGER DEFAULT 0,
        niveau INTEGER DEFAULT 1,
        est_admin BOOLEAN DEFAULT 0,
        est_banni BOOLEAN DEFAULT 0,
        date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

--  Table SAISONS
CREATE TABLE saisons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL
    );

--  Table INGREDIENTS
CREATE TABLE ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL,
        id_saison INT,
        FOREIGN KEY (id_saison) REFERENCES saisons(id)
    );

--  Table DIFFICULTES
CREATE TABLE difficultes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL
    );

--  Table RECETTES
CREATE TABLE recettes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        temps TIME,
        id_difficulte INT,
        id_auteur INT,
        recompense_xp INT,
        date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_auteur) REFERENCES utilisateurs(id),
        FOREIGN KEY (id_difficulte) REFERENCES difficultes(id)
    );


-- Table RECETTES_INGREDIENTS
CREATE TABLE recettes_ingredients (
        id_recette INT,
        id_ingredient INT,
        quantite TEXT,
        PRIMARY KEY (id_recette, id_ingredient),
        FOREIGN KEY (id_recette) REFERENCES recettes(id),
        FOREIGN KEY (id_ingredient) REFERENCES ingredients(id)
    );

--  Table UTILISATEURS_RECETTES
CREATE TABLE utilisateurs_recettes (
        id_utilisateur INT,
        id_recette INT,
        date_cuisine TEXT,
        PRIMARY KEY (id_utilisateur, id_recette, date_cuisine),
        FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id),
        FOREIGN KEY (id_recette) REFERENCES recettes(id)
    );

--  Table ETAPES
CREATE TABLE etapes ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INT NOT NULL,
        description TEXT,
        id_recette INT,
        FOREIGN KEY (id_recette) REFERENCES recettes(id)                   
    );

--  Table USTENSILES
CREATE TABLE ustensiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(255) UNIQUE NOT NULL           
    );


--  Table USTENSILES_RECETTES
CREATE TABLE ustensiles_recettes (
        id_ustensile INT,
        id_recette INT,  
        PRIMARY KEY (id_ustensile, id_recette),
        FOREIGN KEY (id_ustensile) REFERENCES ustensiles(id),
        FOREIGN KEY (id_recette) REFERENCES recettes(id)             
    );