import pandas as pd


def nettoyer_donnees(chemin_fichier: str) -> pd.DataFrame:
    df = pd.read_csv(chemin_fichier)
    df = df.dropna()
    return df


if __name__ == '__main__':
    print('Nettoyage des données...')
