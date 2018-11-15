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


def plot_class(
        df,
        class_variable,
        x_variable="taxable income, median",
        y_variable="mean",
        xlabel='median income for municipality',
        ylabel='exam mean for school',
        min_n=1,
        legend=True):
    fig, ax = plt.subplots(figsize=(10, 5))
    classes = np.unique(df[[class_variable]].values.flatten())
    for i, c in enumerate(classes):
        d = df.loc[(df[class_variable] == c) & (df['pass'] >= min_n)]
        x = d.loc[:, x_variable].values
        y = d.loc[:, y_variable].values
        ax.scatter(x, y, 10, marker=',', label=c)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if legend:
        plt.legend(loc=1, prop={'size': 6})
    plt.show()


# Plot
plot_class(sample, 'year')
plot_class(sample, 'season')
plot_class(sample, 'municipality', min_n=50)
