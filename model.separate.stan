data {
  int<lower=0> N;           // num. samples
  int<lower=0> K;           // num. schools
  int<lower=1,upper=K> x[N];// school indicator
  vector[N] y;              // exam means
}
parameters {
  vector[K] mu;             // school means
  vector<lower=0>[K] sigma; // school variances
}
model {
  y ~ normal(mu[x], sigma[x]);
}

generated quantities {
    vector[N] log_lik;
    for (i in 1:N)
        log_lik[i] = normal_lpdf(y[i] | mu[x[i]], sigma[x[i]]);
}
