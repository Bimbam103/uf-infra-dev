from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Agence(db.Model):
    __tablename__ = 'agence'
    id_agence = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    
    # Relation POO : Permet d'accéder aux commerciaux d'une agence facilement (agence.commerciaux)
    commerciaux = db.relationship('Utilisateur', backref='agence', lazy=True)

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    id_agence = db.Column(db.Integer, db.ForeignKey('agence.id_agence'), nullable=False)
    
    biens = db.relationship('BienImmobilier', backref='commercial', lazy=True)

class BienImmobilier(db.Model):
    __tablename__ = 'bien_immobilier'
    id_bien = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    type_bien = db.Column(db.String(50), nullable=False) # Résidentiel / Professionnel
    prix = db.Column(db.Integer, nullable=False)
    surface_m2 = db.Column(db.Integer, nullable=False)
    id_commercial = db.Column(db.Integer, db.ForeignKey('utilisateur.id_utilisateur'), nullable=False)