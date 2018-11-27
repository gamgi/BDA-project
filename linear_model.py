from sys import exit
import pystan
import numpy as np
import pandas as pd
import logging
import warnings
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
# Local
import stan_utility
from data import Data
# Disable unnecessary logging and warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
logging.getLogger("pystan").setLevel(logging.WARNING)


class Model:
    def __init__(self, filename, seed=1):
        self.seed = seed
        self.stan_file = filename
        self.stan_model = stan_utility.compile_model(self.stan_file)

    def sample(self, data, **kwargs):
        self.fit = self.stan_model.sampling(data=data, seed=self.seed, **kwargs)
        return self.fit


def plot_model(data, samples):
    x = data['x']
    y = data['y']
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
    ax1.scatter(x, y, 5)

    ax1.set_xlabel("median income")
    ax1.set_ylabel("mean exam score")
    ax1.set_xlim((15000, 35000))
    # Error range
    for p in np.arange(5, 95, 5):
        ax1.plot(
            x,
            np.percentile(samples["mu"], p, axis=0),
            alpha=0.1,
            linewidth=10,
            color='gray'
        )
    # Mean
    ax1.plot(
        x,
        np.percentile(samples["mu"], 50, axis=0),
    )
    ax2.hist(samples["beta"], 50)
    ax2.set_xlabel("beta")
    ax3.hist(samples["alpha"], 50)
    ax3.set_xlabel("alpha")
    plt.show()


# Load income and examination result data
df_income, df_results = Data.load()
df_all = pd.merge(df_results, df_income, on=["municipality_code", "year"], how='inner')

# Sample
print("Using a sample for calculations")
df = df_all[(df_all['season'] == 'K')]
sample = df.sample(frac=0.2, random_state=1)

# Prepare data
N, d = sample.shape
y = sample['mean']
x = sample['taxable income, median']

data = dict(
    N=N,
    x=x,
    y=y,
    sigma0=4.0
)

# Prepare stan
print("Compiling model...")
model = Model('model.linear.stan')
print("Fitting data to model...")
fit = model.sample(data=data)
samples = fit.extract(permuted=True)
print("Fitted...")

print(fit)

plot_model(data, samples)
