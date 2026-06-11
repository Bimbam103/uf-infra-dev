import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# On instancie SQLAlchemy ici
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config['SECRET_KEY'] = 'une_cle_tres_secrete_ymmo'
    
    # Configuration de la BDD : fichier SQLite dans le dossier instance du package
    basedir = os.path.abspath(os.path.dirname(__file__))
    sqlite_path = os.path.join(os.path.dirname(basedir), 'instance', 'ymmo.db')
    os.makedirs(os.path.dirname(sqlite_path), exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{sqlite_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # On lie la BDD à notre application Flask
    db.init_app(app)
    
    # Import et enregistrement des Blueprints
    from .routes.main import main_bp
    from .routes.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app