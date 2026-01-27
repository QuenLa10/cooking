INSERT OR IGNORE INTO Saisons(nom) 
VALUES [("Printemps",),
        ("Été",),
        ("Automne",),
        ("Hiver",)];

INSERT OR IGNORE INTO Difficultes(nom)
VALUES [("Très Facile",),
        ("Facile",),
        ("Intermédiaire",),
        ("Avancé",),
        ("Très Difficile",)];

INSERT OR IGNORE INTO Utilisateurs(nom, email, mdp_hash, xp, niveau, est_admin, est_banni)
VALUES [("Quentin","quentin.dazy@telecomnancy.net","hash1",500,2,1,0),
        ("Léonie","leonie.ferrier@telecomnancy.net","hash2",350,1,1,0)];
