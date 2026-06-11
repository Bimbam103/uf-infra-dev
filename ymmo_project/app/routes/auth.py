from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import Utilisateur

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Requête SQL via l'ORM pour trouver l'utilisateur
        user = Utilisateur.query.filter_by(email=email).first()
        
        # Vérification simple (pour l'instant sans hachage pour tester)
        if user and user.mot_de_passe == password:
            return f"Bienvenue {user.prenom} ! Tu es connecté en tant que {user.role}."
        else:
            return "Identifiants incorrects, essaie encore !"
            
    return render_template('login.html')