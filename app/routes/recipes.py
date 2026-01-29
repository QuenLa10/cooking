from flask import Blueprint, render_template, request
from datetime import datetime
from app.database import get_db, close_db
from pathlib import Path # provisoire
import sqlite3 # provisoire

recipes_bp = Blueprint("recipes", __name__)

chemin_db = Path(__file__).resolve().parent.parent / "db" / "cooking.db" #c'est provisoire car les fonction get_db() et close_db() ne fonctionnent pas

@recipes_bp.route("/AjoutRecette")
def ajout_recettes():
    #base = get_db() #ça ne marche pas je sais pas pourquoi
    base = sqlite3.connect(chemin_db) # provisoire
    cur = base.cursor()
    cur.execute("SELECT * FROM difficultes;")
    difficultes = cur.fetchall()
    base.close() # provisoire
    #close_db()

    print(difficultes)

    if request.method == "POST":
        titre = request.form["titre"]
        temps = request.form["temps"]
        id_difficulte = request.form["id_difficulte"]
        id_auteur = 1
        recompense_xp = request.form["recompense_xp"]
        date_creation = datetime.today().strftime("%Y-%m-%d")

        #base = get_db() #ça ne marche pas je sais pas pourquoi
        base = sqlite3.connect(chemin_db) # provisoire
        cur = base.cursor()
        cur.execute("")
        base.close() # provisoire
        #close_db()

    return render_template("ajout_recette.html", difficultes=difficultes)