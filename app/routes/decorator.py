from functools import wraps
from flask import session, redirect, url_for

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        # Si l'utilisateur n'est pas connecté
        if 'identifiant' not in session:
            return redirect(url_for('auth.login'))
        
        # Sinon on continue normalement
        return view(*args, **kwargs)

    return wrapped_view
