from data import Data
import config
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")


df_income, df_results = Data.load()
print(df_results.head())
print(df_income.head())

df_all = pd.merge(df_income, df_results, on="municipality_code")
exit(0)

print(df_all.head())
