from init_db import create_connection

con = create_connection()
cur = con.cursor()

# saisons
cur.executemany("INSERT INTO saisons(nom) VALUES (?)", [
("Printemps",),
("Été",),
("Automne",),
("Hiver",)                
])

# difficultes
cur.executemany("""
INSERT INTO difficultes(nom) VALUES (?)"  
""")