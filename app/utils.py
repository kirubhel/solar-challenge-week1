import pandas as pd

def load_data(country):
    path = f"data/{country.lower()}_clean.csv"
    return pd.read_csv(path)

def compute_z_scores(df, columns):
    from scipy.stats import zscore
    return df[columns].apply(zscore)
