from flask import Blueprint, render_template
from app.routes.decorator import login_required

index_bp = Blueprint("index", __name__)

@index_bp.route("/")
@login_required
def index():
    return render_template("index.html")