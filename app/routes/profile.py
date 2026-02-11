from flask import Blueprint, render_template
from app.routes.decorator import login_required, admin_required

profile_bp = Blueprint("profile", __name__)

# Afficher les informations personnelle
@profile_bp.route("/profile/<int:id>")
@login_required
def profile(id):
    return render_template('profile.html')
