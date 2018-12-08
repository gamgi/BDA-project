import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_pareto_ks(y, label):
    print("Plotting pareto k for {}".format(label))
    x = list(range(1, len(y) + 1))
    plt.figure(figsize=(10, 4))
    plt.style.use(settings.gray_background)
    plt.axhline(y=0.7, linewidth=2, color='r', alpha=0.5, zorder=1)
    plt.axhline(y=1.0, linewidth=2, color='r', zorder=1)
    plt.scatter(x, y, marker="o", zorder=10)
    plt.yticks(np.arange(0.0, 1.1, 0.1))
    # plt.xlabel(label)
    plt.ylabel(r"$k$")
    plt.xlabel(r"pareto $k$ index ({})".format(label))
    plt.xticks(x)
    # plt.gca().axes.yaxis.set_visible(False)
    plt.show()


def plot_pareto_ks2(y):
    N = len(y)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(range(1, N + 1), y, 100, marker='x')
    ax.set_ylim(-0.1, 1.1)
    for l in [0.5, 0.7]:
        ax.axhline(l, alpha=0.4, color='red', linestyle='--')
    ax.set_xlabel('Observation left out')
    ax.set_ylabel('Pareto k')
    plt.show()


def plot_data(
        df,
        x_variable="taxable income, median",
        y_variable="mean",
        xlabel='median income for municipality',
        ylabel='exam mean for school',
        min_n=1,
        selected_classes=None,
        class_variable='municipality'):
    return
    """Plot scatterplot hilighting certain selected_classes"""

    if selected_classes is None:
        df_sorted_unique = df_all.drop_duplicates(
            subset="municipality").nlargest(
            20, "taxable income, median")
        # Apply min_n condition
        df_sorted_unique = df_sorted_unique[(df_sorted_unique['pass'] >= min_n)]
        selected_classes = np.unique(df_sorted_unique[[class_variable]].values.flatten())
    fig, ax = plt.subplots(figsize=(15, 8))

    # Plot rest
    # Filter non-selected variables, with n_min conditon
    d = df[(~df[class_variable].isin(selected_classes)) & (df['pass'] >= min_n)]
    x = d.loc[:, x_variable].values
    y = d.loc[:, y_variable].values
    ax.scatter(x, y, 10, marker=',', label='rest', c='lightgray')

    # Plot selected
    for i, c in enumerate(selected_classes):
        # Filter selected variables, with n_min conditon
        d = df.loc[(df[class_variable] == c) & (df['pass'] >= min_n)]
        x = d.loc[:, x_variable].values
        y = d.loc[:, y_variable].values
        ax.scatter(x, y, 10, marker=',', label=c)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.legend(loc=1, prop={'size': 8})
    plt.show()
