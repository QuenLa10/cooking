from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime
from app.database import get_db
from app.routes.decorator import login_required, admin_required

recipes_bp = Blueprint("recipes", __name__)

# Afficher la liste des recette
@recipes_bp.route("/recipes")
@login_required
def liste_recettes():
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM recettes")
    recettes = cur.fetchall()
    return render_template('liste_recettes.html', recettes=recettes)
    
# Afficher une recette
@recipes_bp.route("/recipes/<int:id>")
@login_required
def affiche_recette(id):
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM recettes WHERE id = ?", (id,))
    recette = cur.fetchone()
    cur.execute("SELECT * FROM etapes WHERE id_recette = ? ORDER BY numero", (id,))
    etapes = cur.fetchall()
    return render_template("affiche_recette.html", recette=recette, etapes=etapes)

# Ajouter une recette
@recipes_bp.route("/add_recipe", methods=["GET", "POST"])
@admin_required
def ajout_recettes():

    # On récupère les choix de difficulté, d'ingrédients
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM difficultes;")
    difficultes = cur.fetchall()
    cur.execute("SELECT * FROM ingredients")
    ingredients = cur.fecthall()


    # Formulaire pour rentrer les données
    if request.method == "POST":
        titre = request.form["titre"]
        temps = request.form["temps"]
        etapes = request.form.getlist("etapes[]")
        id_difficulte = request.form["id_difficulte"]
        recompense_xp = request.form["recompense_xp"]
        date_creation = datetime.today().strftime("%Y-%m-%d")
        # Pour l'auteur, on va récupérer l'id de la personne connectée
        identifiant = session.get('identifiant')
        cur.execute("SELECT id FROM utilisateurs WHERE identifiant = ?", (identifiant,))
        id_auteur = cur.fetchone()[0]

        # Ajout des données de la recette à la DB
        cur.execute("""INSERT INTO recettes (titre, temps, id_difficulte, id_auteur, recompense_xp, date_creation)
                    VALUES (?, ?, ?, ?, ?, ?)""", (titre, temps, id_difficulte, id_auteur, recompense_xp, date_creation))
        base.commit()

        # Ajout des étapes de la recette à la DB
        id_recette = cur.execute("SELECT id FROM recettes WHERE titre=?", (titre,)).fetchone()[0]
        for i in range(len(etapes)):
            cur.execute("""INSERT INTO etapes (id_recette, numero, description)
                        VALUES (?, ?, ?);""", (id_recette, i+1, etapes[i]))
        base.commit()

        return redirect(url_for("liste_recettes"))

    return render_template("ajout_recette.html", difficultes=difficultes, ingredients=ingredients)

@recipes_bp.route("/update_recipe/<int:id>", methods=["POST", "GET"])
@admin_required
def modif_recette(id):
    # à faire
    return render_template("modif_recette.html")

@recipes_bp.route("/delete_recipe/<int:id>")
@admin_required
def supprime_recette(id):
    base = get_db()
    cur = base.cursor()
    cur.execute("DELETE FROM recettes WHERE id = ?", (id,))
    cur.execute("DELETE FROM recettes_ingredients WHERE id_recette = ?", (id,))
    cur.execute("DELETE FROM etapes WHERE id_recette = ?", (id,))
    cur.execute("DELETE FROM ustensiles_recettes WHERE id_recette = ?", (id,))
    # est-ce qu'on supprime l'historique des utilisateurs qui ont réalisé la recette ?
    base.commit()
    return redirect(url_for("recipes.liste_recettes"))