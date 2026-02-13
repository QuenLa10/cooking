from flask import Blueprint, render_template, request, redirect
from app.routes.decorator import login_required, admin_required
from app.database import get_db

ingredients_bp = Blueprint("ingredients", __name__)


# Afficher la liste des ingrédients
@ingredients_bp.route("/ingredients")
@login_required
def liste_ingredients():
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM ingredients")
    ingredients = cur.fetchall()
    print(ingredients)
    return render_template('liste_ingredients.html', ingredients=ingredients)

# Ajouter un ingrédient
@ingredients_bp.route("/add_ingredient", methods=["GET", "POST"])
@admin_required
def ajouter_ingredients():
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM saisons")
    saisons = cur.fetchall()

    if request.method == "POST":
        nom = request.form["nom"]
        id_saison = request.form["id_saison"]
        cur.execute("INSERT INTO ingredients (nom, id_saison) VALUES (?, ?)", (nom, id_saison))
        base.commit()
        return redirect('/ingredients')
    
    return render_template('ajout_ingredient.html', saisons=saisons)