from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from app.database import get_db, close_db

recipes_bp = Blueprint("recipes", __name__)

# Afficher la liste des recettes
@recipes_bp.route("/recipes")
def affiche_recettes():
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM recettes")
    recettes = cur.fetchall()
    return render_template("affiche_recettes.html", recettes=recettes)

# Ajouter une recette
@recipes_bp.route("/addrecipes", methods=["GET", "POST"])
def ajout_recettes():

    # On récupère les choix de difficulté possibles (et leurs id)
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM difficultes;")
    difficultes = cur.fetchall()

    # Formulaire pour rentrer les données
    if request.method == "POST":
        titre = request.form["titre"]
        temps = request.form["temps"]
        etapes = request.form.getlist("etapes[]")
        id_difficulte = request.form["id_difficulte"]
        id_auteur = 1
        recompense_xp = request.form["recompense_xp"]
        date_creation = datetime.today().strftime("%Y-%m-%d")

        base = get_db()
        cur = base.cursor()

        # Ajout des données de la recette à la DB
        cur.execute("""INSERT INTO recettes (titre, temps, id_difficulte, id_auteur, recompense_xp, date_creation)
                    VALUES (?, ?, ?, ?, ?, ?)""", (titre, temps, id_difficulte, id_auteur, recompense_xp, date_creation))
        base.commit()

        # Ajout des étapes de la recette à la DB
        id_recette = cur.execute("SELECT id FROM recettes WHERE titre=?", (titre,)).fetchone()[0]
        for i in range(len(etapes)):
            cur.execute("""INSERT INTO etapes (id_recette, n_etape, instructions)
                        VALUES (?, ?, ?);""", (id_recette, i+1, etapes[i]))
        base.commit()
        return redirect("/")

    return render_template("ajout_recette.html", difficultes=difficultes)

@recipes_bp.route("/modif_recipe", methods=["POST", "GET"])
def modif_recette(id_recette):
    # à faire
    return render_template("modif_recette.html")