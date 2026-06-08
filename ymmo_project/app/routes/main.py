from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # C'est ici qu'on affichera les biens immobiliers populaires plus tard
    return render_template('index.html')