from . import db
from datetime import datetime

class Agence(db.Model):
    __tablename__ = 'agence'
    id_agence = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    
    # Relation POO : pour récupérer les utilisateurs d'une agence
    utilisateurs = db.relationship('Utilisateur', backref='agence', lazy=True)

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False) # 'Commercial', 'Direction', etc. [cite: 75]
    id_agence = db.Column(db.Integer, db.ForeignKey('agence.id_agence'), nullable=False)
    
    # Relation POO : pour récupérer les biens gérés par ce commercial
    biens = db.relationship('BienImmobilier', backref='commercial', lazy=True)

class BienImmobilier(db.Model):
    __tablename__ = 'bien_immobilier'
    id_bien = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    type_bien = db.Column(db.String(50), nullable=False) # 'Résidentiel' ou 'Professionnel' [cite: 63]
    statut = db.Column(db.String(50), nullable=False)     # 'A vendre' ou 'A acheter' [cite: 64]
    prix = db.Column(db.Integer, nullable=False)
    surface_m2 = db.Column(db.Integer, nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    id_commercial = db.Column(db.Integer, db.ForeignKey('utilisateur.id_utilisateur'), nullable=False)