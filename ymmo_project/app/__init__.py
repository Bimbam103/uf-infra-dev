from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Configuration de base (à lier plus tard avec la BDD de ton binôme)
    app.config['SECRET_KEY'] = 'une_cle_tres_secrete_ymmo'
    
    # Import et enregistrement des Blueprints (les morceaux de ton site)
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    return app