import numpy as np
# Local
import stan_utility


class Model:
    def __init__(self, filename, seed=1):
        self.seed = seed
        self.stan_file = filename
        self.stan_model = stan_utility.compile_model(self.stan_file)

    def sample(self, data, **kwargs):
        self.fit = self.stan_model.sampling(data=data, seed=self.seed, **kwargs)
        return self.fit
