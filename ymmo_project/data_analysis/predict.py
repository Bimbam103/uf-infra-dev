import pandas as pd
from sklearn.linear_model import LinearRegression


def entrainer_modele(df: pd.DataFrame, features, target):
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model


if __name__ == '__main__':
    print('Prédiction IA prête.')
