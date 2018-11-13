import pandas as pd
import numpy as np

import config


def load_data():
    df_income = pd.read_csv(config.FILES['income'], encoding="ISO-8859-1", skiprows=1)
    print(df_income.head())

    df_muni = pd.read_csv(
        config.FILES['muni'],
        encoding="utf-8",
        skiprows=1,
        header=None,
        names=[
            "Code",
            "Municipality"])
    print(df_muni.head())


load_data()
