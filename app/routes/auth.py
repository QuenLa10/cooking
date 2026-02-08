from flask import Blueprint, flash, session, redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.database import get_db

# Création du Blueprint
auth_bp = Blueprint("auth", __name__)

# Page de login
@auth_bp.route("/login", methods=['GET', 'POST'])
def login() :
    if request.method == 'POST':
        identifiant = request.form['identifiant']
        mdp = request.form["mdp"]
        base = get_db()
        cur = base.cursor()
        cur.execute("SELECT identifiant, mdp_hash FROM utilisateurs WHERE identifiant = ?", (identifiant,))
        login_user = cur.fetchone()

        # On vérifie si l'identifiant existe
        if login_user is None:
            flash("Identifiant ou mot de passe incorrect")
            return redirect(url_for('auth.login'))
        
        # On vérifie si le mdp est correct
        if check_password_hash(login_user[1], mdp):
            session.permanent = True
            session['identifiant'] = identifiant
            return redirect(url_for('index.index'))
        
        else:
            flash("Identifiant ou mot de passe incorrect")
            return redirect(url_for('auth.login'))
        
    return render_template('login.html')

# Page de logout
@auth_bp.route("/logout")
def logout() :
    session.pop('identifiant', None)
    return redirect(url_for('auth.login'))

# Page de Sign up
@auth_bp.route("/signup", methods=['POST', 'GET'])
def signup() :
    if request.method == 'POST':
        identifiant = request.form["identifiant"]
        email = request.form["email"]
        mdp = request.form["mdp"]
        mdp_hash = generate_password_hash(mdp)

        base = get_db()
        cur = base.cursor()
        cur.execute("SELECT identifiant FROM utilisateurs WHERE identifiant = ?", (identifiant,))
        cur.execute("SELECT email FROM utilisateurs WHERE email = ?", (email,))
        autre_identifiant = cur.fetchone()
        autre_email = cur.fetchone()

        # si l'identifiant existe déjà
        if autre_identifiant != None:
            flash("Cet identifiant existe déjà")
            return redirect(url_for('auth.signup'))
        
        # si l'email existe déjà
        elif autre_email != None:
            flash("Cet email est déjà utilisé")
            return redirect(url_for('auth.signup'))
        
        else:
            cur.execute("INSERT INTO utilisateurs (identifiant, mdp_hash, email) VALUES (?, ?, ?)", (identifiant, mdp_hash, email))
            base.commit()
        
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')

# A FAIRE : fct pour changer de mdp