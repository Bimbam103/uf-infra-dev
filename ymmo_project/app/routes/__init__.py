from .auth import auth_bp
from .main import main_bp

# Ce package expose les blueprints disponibles sans les enregistrer.
# L'enregistrement se fait dans create_app() pour éviter les dépendances circulaires.
