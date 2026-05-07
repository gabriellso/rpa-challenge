import pandas as pd


def load_excel(path):

    df = pd.read_excel(path)

    df.columns = df.columns.str.strip()

    return df.to_dict(orient="records")