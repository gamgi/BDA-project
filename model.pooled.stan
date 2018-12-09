data {
  int<lower=0> N;           // num. samples
  vector[N] y;              // exam means
}
parameters {
  real mu;             // school means
  real<lower=0> sigma; // school variances
}
model {
  y ~ normal(mu, sigma);
}

generated quantities {
    vector[N] log_lik;
    for (i in 1:N)
        log_lik[i] = normal_lpdf(y[i] | mu, sigma);
}
