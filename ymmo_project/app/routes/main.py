from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import BienImmobilier
from data_analysis.clean_data import generer_et_analyser_donnees, predire_prix

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # On récupère les filtres saisis par l'utilisateur s'ils existent
    ville_recherche = request.args.get('ville', '').strip()
    type_recherche = request.args.get('type_bien', '')

    # Requête de base : on prend tous les biens
    query = BienImmobilier.query

    # Si l'utilisateur a écrit une ville, on filtre (sans distinction de majuscules)
    if ville_recherche:
        query = query.filter(BienImmobilier.ville.ilike(f"%{ville_recherche}%"))
    
    # Si l'utilisateur a choisi un type spécifique
    if type_recherche:
        query = query.filter_by(type_bien=type_recherche)

    liste_biens = query.all()
    return render_template('index.html', biens=liste_biens, ville_recherche=ville_recherche, type_recherche=type_recherche)

@main_bp.route('/stats', methods=['GET', 'POST'])
def stats():
    stats_ville, stats_type = generer_et_analyser_donnees()
    prix_estime = None
    surface_saisie = None
    ville_saisie = None
    
    if request.method == 'POST':
        surface_saisie = int(request.form.get('surface', 0))
        ville_saisie = request.form.get('ville', 'Aix-en-Provence')
        if surface_saisie > 0:
            prix_estime = predire_prix(surface_saisie, ville_saisie)
            
    return render_template(
        'stats.html', 
        stats_ville=stats_ville, 
        stats_type=stats_type,
        prix_estime=prix_estime,
        surface_saisie=surface_saisie,
        ville_saisie=ville_saisie
    )

@main_bp.route('/ajouter-bien', methods=['GET', 'POST'])
def ajouter_bien():
    if request.method == 'POST':
        # Extraction des données du formulaire HTML
        nouveau_bien = BienImmobilier(
            titre=request.form.get('titre'),
            type_bien=request.form.get('type_bien'),
            statut="A vendre",
            prix=int(request.form.get('prix')),
            surface_m2=int(request.form.get('surface')),
            ville=request.form.get('ville'),
            id_commercial=1 # Lié temporairement à Jean Dupont (ID 1)
        )
        
        # Sauvegarde dans la base de données SQL
        db.session.add(nouveau_bien)
        db.session.commit()
        
        # Retour à l'accueil pour voir le résultat
        return redirect(url_for('main.index'))
        
    return render_template('ajouter_bien.html')

@main_bp.route('/acheter-louer')
def acheter_louer():
    # Page catalogue qui récupère tous les biens de la base
    ville_recherche = request.args.get('ville', '').strip()
    type_recherche = request.args.get('type_bien', '')

    query = BienImmobilier.query

    if ville_recherche:
        query = query.filter(BienImmobilier.ville.ilike(f"%{ville_recherche}%"))
    if type_recherche:
        query = query.filter_by(type_bien=type_recherche)

    liste_biens = query.all()
    return render_template('acheter_louer.html', biens=liste_biens, ville_recherche=ville_recherche, type_recherche=type_recherche)

@main_bp.route('/bien/<int:id_bien>')
def voir_bien(id_bien):
    # Récupère le bien spécifique ou renvoie une erreur 404 si l'ID n'existe pas
    bien = BienImmobilier.query.get_or_404(id_bien)
    return render_template('voir_bien.html', bien=bien)