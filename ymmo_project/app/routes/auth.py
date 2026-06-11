from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import db
from app.models import Utilisateur

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Utilisateur.query.filter_by(email=email).first()
        
        if user and user.mot_de_passe == password:
            # Enregistrement des informations dans la session Flask
            session['user_id'] = user.id_utilisateur
            session['user_name'] = f"{user.prenom} {user.nom}"
            session['user_role'] = user.role
            
            # Redirection vers la page d'accueil une fois connecté
            return redirect(url_for('main.index'))
        else:
            flash("Identifiants incorrects, veuillez réessayer.", "danger")
            
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # Vérification si l'email existe déjà
        if Utilisateur.query.filter_by(email=email).first():
            flash("Cet email est déjà utilisé !", "danger")
            return redirect(url_for('auth.register'))
            
        nouveau_client = Utilisateur(
            nom=request.form.get('nom'),
            prenom=request.form.get('prenom'),
            email=email,
            mot_de_passe=request.form.get('password'),
            role="Client", # Rôle attribué automatiquement aux inscriptions
            id_agence=1    # Lié par défaut à la première agence
        )
        db.session.add(nouveau_client)
        db.session.commit()
        
        flash("Inscription réussie ! Vous pouvez vous connecter.", "success")
        return redirect(url_for('auth.login'))
        
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    # On vide la session pour déconnecter l'utilisateur
    session.clear()
    return redirect(url_for('main.index'))