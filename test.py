from data import Data
import config
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df_income, df_results = Data.load()
#print(df_results.head())
#print(df_income.head())

df_all = pd.merge(df_income, df_results, on="municipality_code")

print(df_all.head())

sample = df_all.sample(frac=0.1)

# Plot
x = sample.loc[: , "taxable income, median"].values
y = sample.loc[: , "mean"].values
fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(x, y, 10, marker=',')
ax.set_xlabel('median income')
ax.set_ylabel('exam mean')
plt.show()
