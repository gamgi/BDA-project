import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from data import Data
import config


df_income, df_results = Data.load()
print("resultss shape:", df_results.shape)
print(df_results.sort_values(by="municipality_code").head())
print("All income shape:", df_income.shape)
print(df_income.sort_values(by="municipality_code").head())

df_all = pd.merge(df_results, df_income, on=["municipality_code", "year"], how='inner')

print("All records shape:", df_all.shape)
print(df_all.sort_values(by=["municipality_code", "year"]).head(n=20))

sample = df_all.sample(frac=1)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
years = np.unique(df_all[['year']].values.flatten())
for i, year in enumerate(years):
    df = sample.loc[sample['year'] == year]
    x = df.loc[:, "taxable income, median"].values
    y = df.loc[:, "mean"].values
    ax.scatter(x, y, 10, marker=',', label=year)
ax.set_xlabel('median income for municipality')
ax.set_ylabel('exam mean for school')
plt.legend()
plt.show()
