data {
  int<lower=0> N;           // num. samples
  int<lower=0> K;           // num. schools
  int<lower=1,upper=K> x[N];// school indicator
  vector[N] y;              // exam means
}
parameters {
  vector[K] mu;             // school means
  real<lower=0> sigma;      // common std
  real omega;               // school mean mean
  real<lower=0> tau2;       // school mean variance
}
model {
  mu ~ normal(omega, tau2);
  y ~ normal(mu[x], sigma);
}

generated quantities {
    vector[N] log_lik;
    for (i in 1:N)
        log_lik[i] = normal_lpdf(y[i] | mu[x[i]], sigma);
}
