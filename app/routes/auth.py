from flask import Blueprint

# Création du Blueprint
auth_bp = Blueprint("auth", __name__)

# Page de login
@auth_bp.route("/login")
def login () :
    return "Page login"

# Page de logout
@auth_bp.route("/logout")
def logout() :
    return "Page logout"

# Page de Sign up
@auth_bp.route("/signup")
def signup() :
    return "Page signup"