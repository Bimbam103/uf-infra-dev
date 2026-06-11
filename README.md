# uf-infra-dev

Application Flask légère pour la gestion immobilière et quelques scripts d'analyse/prédiction.

## Résumé du contenu

- `ymmo_project/run.py` : point d'entrée principal du package (démarre l'app Flask).
- `ymmo_project/app/__init__.py` : factory `create_app()` et configuration (SQLAlchemy, blueprints).
- `ymmo_project/app/models.py` : modèles SQLAlchemy (`Agence`, `Utilisateur`, `BienImmobilier`).
- `ymmo_project/app/routes/` : blueprints et routes (`main.py`, `auth.py`, `agence.py`, `data_ia.py`).
- `ymmo_project/data_analysis/` : scripts d'analyse et prédiction (`clean_data.py`, `predict.py`).
- `ymmo_project/instance/ymmo.db` : base SQLite locale (données persistantes).
- `requirements.txt` : dépendances Python du projet.

## Commandes pour faire fonctionner le projet

1. Ouvrir un terminal et activer l'environnement virtuel (PowerShell) :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& .\venv\Scripts\Activate.ps1
```

ou (CMD) :

```cmd
.\venv\Scripts\activate
```

2. Installer les dépendances (si nécessaire) :

```powershell
python -m pip install -r requirements.txt
```

3. Lancer l'application depuis la racine du dépôt :

```powershell
.\venv\Scripts\python.exe ymmo_project\run.py
# ou depuis le dossier ymmo_project : ..\venv\Scripts\python.exe run.py
```

4. (Optionnel) Créer les tables SQLite si nécessaire :

```powershell
.\venv\Scripts\python.exe -c "from ymmo_project.app import create_app, db; app=create_app();
with app.app_context(): db.create_all()"
```

## Technologies utilisées (résumé)

- **Python** : langage principal du projet.
- **Flask** : micro-framework web utilisé pour l'application et les routes.
- **Flask-SQLAlchemy** : extension ORM pour gérer la base SQLite via modèles Python.
- **SQLite** : base de données embarquée utilisée pour stocker les données dans `ymmo_project/instance/ymmo.db`.
- **pandas** : manipulation et analyse de données (dans `data_analysis/`).
- **scikit-learn** : utilitaire pour créer/entraîner des modèles (fichier `predict.py`).
- **requests** : pour appels HTTP éventuels depuis des scripts (présent dans `requirements.txt`).

## Descriptions détaillées des technologies et composants utilisés

- Python : langage principal utilisé pour toute la logique serveur et les scripts d'analyse. Les scripts sont exécutés avec l'interpréteur Python du `venv`. Python est utilisé pour la configuration de l'application, la définition des modèles, les routes et les scripts d'IA.

- Flask : micro-framework web léger. Il gère le routage HTTP, la gestion des requêtes/réponses, le rendu des templates Jinja2 et le cycle de vie de l'application. Le projet utilise une factory `create_app()` pour configurer Flask et enregistrer les blueprints.

- Blueprints (Flask) : mécanisme de modularisation des routes et de séparation des responsabilités. `main.py` et `auth.py` sont mis en place comme blueprints pour isoler les routes d'interface publique et d'authentification.

- Flask-SQLAlchemy : extension fournissant un ORM (Object-Relational Mapping). Elle permet de définir des classes Python qui correspondent à des tables SQL, d'exécuter des requêtes via `Model.query` et de gérer la session/base de données via `db.session`.

- SQLite : SGBD embarqué, simple à utiliser en local et sans configuration serveur. Ici la base est située dans `ymmo_project/instance/ymmo.db`. Convient pour du développement et des prototypes, pas pour un usage haute charge en production.

- pandas : bibliothèque pour la manipulation de données tabulaires (DataFrame). Utilisée pour créer, nettoyer et agréger des jeux de données dans `data_analysis/` (calculs de prix au m², statistiques par ville, etc.).

- scikit-learn : bibliothèque ML pour prototypage de modèles. `predict.py` montre un exemple d'entraînement d'une régression linéaire (LinearRegression). Permet d'entraîner, évaluer et sauvegarder des modèles simples.

- requests : bibliothèque HTTP simple pour faire des requêtes vers des APIs externes depuis des scripts ou services.

- Jinja2 (via Flask) : moteur de template utilisé pour générer les pages HTML à partir des templates situés dans `app/templates/`. Injecte des variables et rend du HTML côté serveur.

- Static files (CSS/JS) : répertoire `app/static/` contenant les styles et scripts front-end. Flask sert ces fichiers statiques automatiquement.

- Environment virtual (`venv`) : environnement Python isolé utilisé pour installer et gérer les dépendances du projet (fichiers dans `venv/`). Toujours activer le `venv` avant d'installer ou d'exécuter l'application.

- Debugger & reloader Flask : en mode debug, Flask active un reloader (redémarrage automatique) et le debugger interactif pour faciliter le développement.

- Structure & workflows README :
	- `ymmo_project/app/` : logique serveur (blueprints, modèles, templates, static)
	- `ymmo_project/data_analysis/` : scripts de génération/nettoyage et prototypes ML
	- `ymmo_project/instance/` : fichier SQLite local (`ymmo.db`)

Si tu veux, j'ajoute des exemples de commandes `pandas` ou un mini-tutoriel pour convertir `agence.py` et `data_ia.py` en blueprints. Dis-moi quelle profondeur tu souhaites pour chaque description.

## Installation et dépendances (commandes)

Suivre ces étapes pour préparer l'environnement et démarrer l'application (exemples Windows PowerShell / CMD). Adapte le chemin vers `python` si tu utilises un autre interpréteur.

- Créer et activer un `venv` (PowerShell) :

```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

- Installer les dépendances :

```powershell
pip install -r requirements.txt
```

- Créer la base de données (SQLite) et les tables :

```powershell
.\venv\Scripts\python.exe -c "from ymmo_project.app import create_app, db; app=create_app();
with app.app_context(): db.create_all()"
```

- Lancer l'application (depuis la racine du dépôt) :

```powershell
.\venv\Scripts\python.exe ymmo_project\run.py
# ou depuis le dossier ymmo_project : ..\venv\Scripts\python.exe run.py
```

- Commandes utiles de debug :

```powershell
# Vérifier la version de Python utilisée
python --version

# Lister les paquets installés dans le venv
pip list
```

