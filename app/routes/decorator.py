from functools import wraps
from flask import session, redirect, url_for, flash
from app.database import get_db

# Pour vérifier que l'utilisateur est connecté et qu'il n'est pas banni
def login_required(f):
    @wraps(f)
    def fonction_decore(*args, **kwargs):
        # Vérifie que l'utilisateur est connecté
        identifiant = session.get('identifiant')
        if not identifiant:
            flash("Vous devez être connecté pour accéder à cette page.")
            return redirect(url_for('auth.login'))
        
        # Vérifie qu'il n'est pas banni (en récupérant l'info depuis la db)
        base = get_db()
        cur = base.cursor()
        cur.execute("SELECT est_banni FROM utilisateurs WHERE identifiant = ?", (identifiant,))
        banni = cur.fetchone()[0]
        if banni == 1:
            flash("Vous avez été banni de certaines pages du site.")
            return redirect(url_for('index.index'))

        return f(*args, **kwargs)

    return fonction_decore

# Pour vérifier que l'utilisateur est connecté et qu'il a le role d'admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Vérifie que l'utilisateur est connecté
        identifiant = session.get('identifiant')
        if not identifiant:
            flash("Vous devez être connecté pour accéder à cette page.")
            return redirect(url_for('auth.login'))

        # Vérifie que l'utilisateur est admin (en récuperant l'info depuis la db)
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT est_admin FROM utilisateurs WHERE identifiant = ?", (identifiant,))
        admin = cur.fetchone()[0]

        if admin == 0:
            flash("Vous n'avez pas les droits nécessaires pour accéder à cette page.")
            return redirect(url_for('index.index'))

        return f(*args, **kwargs)
    
    return decorated_function