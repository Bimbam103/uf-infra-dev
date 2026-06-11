# uf-infra-dev

Application Flask pour la gestion immobilière et l'analyse de données.

## Structure du projet

- `run.py` : point d'entrée principal du projet
- `ymmo_project/` : package Python principal
- `ymmo_project/app/` : application Flask, blueprints et modèles
- `ymmo_project/data_analysis/` : scripts de traitement et de prédiction
- `instance/` : données locales gérées par Flask (base SQLite)
- `requirements.txt` : dépendances Python

## Exécution

1. Active le `venv`
2. Lance l'application depuis le dossier racine :

```powershell
python run.py
```
