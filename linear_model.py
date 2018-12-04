from sys import exit
import pystan
import numpy as np
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
# df = df_all[(df_all['season'] == 'K')]
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

model_utils.plot_model(data, samples)
