import pandas as pd


def load_data():
    countries = ["ethiopia", "kenya", "sudan", "tanzania", "nigeria"]
    dfs = []

    for country in countries:
        df = pd.read_csv(f"data/{country}_clean.csv")
        df["Country"] = country.capitalize()
        df["DATE"] = pd.to_datetime(df["DATE"])
        dfs.append(df)

    return pd.concat(dfs)
