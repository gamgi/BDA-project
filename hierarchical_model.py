from sys import exit
import pystan
import numpy as np
import pandas as pd
import logging
import warnings
from data import Data
from scipy import stats
from matplotlib import pyplot as plt

import model_utils
from model_utils import Model
# Disable unnecessary logging and warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
logging.getLogger("pystan").setLevel(logging.WARNING)


# Load income and examination result data
df_income, df_results = Data.load()
df_all = pd.merge(df_results, df_income, on=["municipality_code", "year"], how='inner')


def plot_model(data, school_means, var):
    fig, ax = plt.subplots(figsize=(8, 10))
    x = np.linspace(0, 5, 100)
    print(school_means[0], var)
    for m in school_means:
        ax.plot(x, stats.norm.pdf(x, loc=m, scale=var))
    plt.show()


def predict_muni(muni):
    df = df_all[(df_all['municipality'] == muni) & (df_all['season'] == 'K')]
    
    number_of_schools = 0
    for i, val in enumerate(df['school_id'].unique()):
        number_of_schools += 1
        df.loc[(df['school_id'] == val), 'school_number'] = i+1
    df.school_number = df.school_number.astype(int)
    
    sample = df.sample(frac=1, random_state=1)
    
    # Prepare data
    N, d = sample.shape
    K = number_of_schools
    y = sample['mean'].values.flatten()
    x = sample['school_number'].values.flatten()
    
    data = dict(
        N=N,
        K=K,
        x=x,
        y=y,
    )
    print(data)
    
    # Prepare stan
    print("Compiling model...")
    model = Model('model.hierarchical.stan')
    print("Fitting data to model...")
    fit = model.sample(data=data, iter=4000)
    samples = fit.extract(permuted=True)
    print("Fitted...")
    
    print(fit)
    print("School means:")
    school_means = fit.summary()['summary'][:number_of_schools, 0]
    var = fit.summary()['summary'][number_of_schools, 0]
    
    plot_model(data, school_means, var)


predict_muni('Kauhava')
