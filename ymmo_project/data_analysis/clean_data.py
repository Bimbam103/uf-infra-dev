import pandas as pd
import random

def generer_et_analyser_donnees():
    # 1. Simulation d'un historique de transactions (Faux jeu de données)
    villes = ['Aix-en-Provence', 'Marseille', 'Paris', 'Lyon', 'Nice']
    types = ['Résidentiel', 'Professionnel']
    
    donnees = []
    for _ in range(100):
        ville = random.choice(villes)
        type_b = random.choice(types)
        surface = random.randint(30, 200)
        
        # Le prix dépend de la surface et de la ville (ex: Paris plus cher)
        prix_metre = random.randint(3000, 5000)
        if ville == 'Paris':
            prix_metre += 4000
        elif ville == 'Aix-en-Provence' or ville == 'Nice':
            prix_metre += 1500
            
        prix = surface * prix_metre
        donnees.append({'ville': ville, 'type_bien': type_b, 'surface_m2': surface, 'prix': prix})
    
    # 2. Transformation en DataFrame Pandas (Nettoyage/Analyse)
    df = pd.DataFrame(donnees)
    
    # Calcul du prix au m² pour chaque vente
    df['prix_m2'] = df['prix'] / df['surface_m2']
    
    # Statistiques clés : Prix moyen au m² par ville
    stats_ville = df.groupby('ville')['prix_m2'].mean().round(2).to_dict()
    
    # Statistiques clés : Nombre de ventes par type de bien
    stats_type = df['type_bien'].value_counts().to_dict()
    
    return stats_ville, stats_type

def predire_prix(surface, ville):
    # Un mini-algorithme de prédiction linéaire basique basé sur la surface et la ville
    prix_m2_moyen = 4500
    if ville.lower() == 'paris':
        prix_m2_moyen = 8500
    elif ville.lower() in ['aix-en-Provence', 'aix en provence', 'nice']:
        prix_m2_moyen = 6000
        
    return int(surface * prix_m2_moyen)