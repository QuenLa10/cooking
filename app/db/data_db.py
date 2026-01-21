from init_db import create_connection
import sqlite3,datetime

con = create_connection()
cur = con.cursor()

# saisons
cur.executemany("INSERT OR IGNORE INTO saisons(nom) VALUES (?)", [
("Printemps",),
("Été",),
("Automne",),
("Hiver",)                
])

# difficultes
cur.executemany("INSERT OR IGNORE INTO difficultes(nom) VALUES (?)", [
("Très Facile",),
("Facile",),
("Intermédiaire",),
("Avancé",),
("Très Difficile",)                 
])

# utilisateurs
cur.executemany("INSERT OR IGNORE INTO utilisateurs(nom, email, mdp_hash, xp, niveau, est_admin, est_banni) VALUES (?,?,?,?,?,?,?)", [
("Quentin","quentin.dazy@telecomnancy.net","hash1",500,2,1,0)
])
con.commit()