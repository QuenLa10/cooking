from flask import Blueprint, render_template, session
from app.routes.decorator import login_required, admin_required
from app.database import get_db

profile_bp = Blueprint("profile", __name__)

# Afficher les informations personnelle
@profile_bp.route("/profile")
@login_required
def profile(id):
    identifiant = session.get('identifiant')
    base = get_db()
    cur = base.cursor()
    cur.execute("SELECT * FROM utilisateurs WHERE identifiant = ?", (identifiant,))
    info_utilisateur = cur.fetchone()
    return render_template('profile.html', info_utilisateur = info_utilisateur)

# Changer de mot de passe

# Pour les admin : accorder le role admin a d'autres personnes


