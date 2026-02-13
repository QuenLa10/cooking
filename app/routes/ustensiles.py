from flask import Blueprint, render_template, session
from app.routes.decorator import login_required, admin_required
from app.database import get_db

ustensiles_bp = Blueprint("ustensiles", __name__)