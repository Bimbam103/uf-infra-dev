from flask import Blueprint, render_template, request
from app.models import BienImmobilier
# On importe nos fonctions d'analyse
from data_analysis.clean_data import generer_et_analyser_donnees, predire_prix

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    liste_biens = BienImmobilier.query.all()
    return render_template('index.html', biens=liste_biens)

@main_bp.route('/stats', methods=['GET', 'POST'])
def stats():
    # On génère les analyses Pandas en temps réel
    stats_ville, stats_type = generer_et_analyser_donnees()
    
    prix_estime = None
    surface_saisie = None
    ville_saisie = None
    
    # Si l'utilisateur utilise le formulaire de prédiction d'IA
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