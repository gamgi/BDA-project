import random
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def plot_2018_results(df_res_2018, school_means, var):
    test_schools = random.sample(list(school_means.items()), 4)

    def school_info(school_number):
        return (
            df_res_2018[df_res_2018['school_number'] == school_number]['mean'].values[0],
            df_res_2018[df_res_2018['school_number'] == school_number]['school_name'].values[0]
        )
        
    fig, axes = plt.subplots(2, 2, figsize=(10,6))
    x = np.linspace(1.5, 6.5, 100)
    for i, (school_number, mean) in enumerate(test_schools):
        mean_2018, school_name = school_info(school_number)
        axes[i%2][i//2].plot(x, stats.norm.pdf(x, loc=mean, scale=var))
        axes[i%2][i//2].axvline(x=mean_2018, linewidth=2, color='r', alpha=0.5, zorder=1)
        axes[i%2][i//2].set_title(school_name)
    
    plt.tight_layout()
    plt.show()
