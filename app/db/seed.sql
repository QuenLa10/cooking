INSERT OR IGNORE INTO utilisateurs(nom, email, mdp_hash, xp, niveau, est_admin, est_banni)
VALUES  ("Quentin","quentin.dazy@telecomnancy.net","hash1",500,2,1,0),
        ("Léonie","leonie.ferrier@telecomnancy.net","hash2",350,1,1,0);


INSERT OR IGNORE INTO saisons(nom) 
VALUES  ("Printemps"),
        ("Été"),
        ("Automne"),
        ("Hiver"),
        ("Toute saison");

INSERT OR IGNORE INTO ingredients(nom, id_saison) 
VALUES  ("Pomme",(SELECT id_saison FROM saisons WHERE nom = "Automne")),
        ("Poire",(SELECT id_saison FROM saisons WHERE nom = "Automne")),
        ("Banane",(SELECT id_saison FROM saisons WHERE nom = "Toute saison")),
        ("Kiwi vert",(SELECT id_saison FROM saisons pommeWHERE nom = "Toute saison")),
        ("Orange",(SELECT id_saison FROM saisons WHERE nom = "Hiver")),
        ("Pamplemousse",(SELECT id_saison FROM saisons WHERE nom = "Hiver")),
        ("Pastèque",(SELECT id_saison FROM saisons WHERE nom = "Été")),
        ("Melon",(SELECT id_saison FROM saisons WHERE nom = "Été"));

INSERT OR IGNORE INTO difficultes(nom)
VALUES  ("Très Facile"),
        ("Facile"),
        ("Intermédiaire"),
        ("Avancé"),
        ("Très Difficile");

INSERT OR IGNORE INTO recettes(titre, temps, id_difficulte, id_auteur, recompense_xp)
VALUES  ("Lasagnes","2","hash1",500,2,1,0),
        ("Léonie","leonie.ferrier@telecomnancy.net","hash2",350,1,1,0);

