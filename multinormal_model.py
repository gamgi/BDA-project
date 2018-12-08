from sys import exit
import pystan
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import pandas as pd
import logging
import warnings
from data import Data

import model_utils
from model_utils import Model
# Disable unnecessary logging and warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
logging.getLogger("pystan").setLevel(logging.WARNING)


# Load income and examination result data
df_income, df_results = Data.load()
df_all = pd.merge(df_results, df_income, on=["municipality_code", "year"], how='inner')

# Sample
print("Using a sample for calculations")
excluded_munis = ['Helsinki', 'Espoo', 'Kauniainen']
df = df_all[(~df_all['municipality'].isin(excluded_munis)) & (df_all['season'] == 'K')]
sample = df.sample(frac=0.33, random_state=1)

# Prepare data
N, d = sample.shape
y = sample['mean']
x = sample['taxable income, median']
xy = list(zip(x, y))

data = dict(
    N=N,
    y=xy,
    # sigma0=100,
    sigma1=1,
    tau=np.array([[100, 0], [0, 1]]),
    mu0=[22500, 4.5]
)

# https://stackoverflow.com/questions/41597177/get-aspect-ratio-of-axes
from operator import sub


def get_aspect(ax):
    # Total figure size
    figW, figH = ax.get_figure().get_size_inches()
    # Axis size on figure
    _, _, w, h = ax.get_position().bounds
    # Ratio of display units
    disp_ratio = (figH * h) / (figW * w)
    # Ratio of data units
    # Negative over negative because of the order of subtraction
    data_ratio = sub(*ax.get_ylim()) / sub(*ax.get_xlim())

    return disp_ratio / data_ratio


def plot_model(data, samples):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 10))
    x, y = zip(*data['y'])

    ax1.set_xlabel("median income")
    ax1.set_ylabel("mean exam score")
    ax1.set_xlim((15000, 35000))
    ax1.set_ylim((1, 7))

    mu_ = samples['mu'].T
    mu = np.mean(mu_, axis=1)
    sigma = np.mean(samples['sigma'], axis=0).flatten()

    # Scatterplot with cov ellipsis
    #aspect = (max(x) - min(x)) / (max(y) - min(y))
    aspec = (35000 - 15000) / (7 - 1)
    angle = np.rad2deg(np.arctan(sigma[1]))

    for j in [1]:  # range(1, 4):
        ell = Ellipse(xy=(mu[0], mu[1]),
                      width=sigma[0] * j * 2, height=sigma[3] * j * 2,
                      angle=angle / aspect)
        ell.set_facecolor('none')
        ell.set_edgecolor('b')
        ax1.add_artist(ell)
    ax1.scatter(x, y, s=0.5)
    ax1.plot(mu[0], mu[1], marker='x', color='b')

    # Histograms
    ax2.hist(samples['rho'], 50)
    ax2.set_xlabel("rho")
    ax3.hist(mu_[0], 50)
    ax3.set_xlabel("mu_x")
    ax4.hist(mu_[1], 50)
    ax4.set_xlabel("mu_y")
    plt.show()


# Prepare stan
print("Compiling model...")
model = Model('model.multinormal.stan')
print("Fitting data to model...")
fit = model.sample(data=data)  # , iter=3500)
samples = fit.extract(permuted=True)
print(samples.keys())
print("Fitted...")

print(fit)

plot_model(data, samples)
