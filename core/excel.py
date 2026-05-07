import pandas as pd


def load_excel(path):

    df = pd.read_excel(path)

    # remove espaços invisíveis
    df.columns = df.columns.str.strip()

    return df.to_dict(orient="records")