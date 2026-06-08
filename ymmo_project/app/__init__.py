from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# On instancie SQLAlchemy ici
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config['SECRET_KEY'] = 'une_cle_tres_secrete_ymmo'
    
    # Configuration de la BDD : on indique le chemin du fichier SQLite local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../ymmo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # On lie la BDD à notre application Flask
    db.init_app(app)
    
    # Import et enregistrement des Blueprints
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    return app