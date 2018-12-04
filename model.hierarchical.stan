data {
  int<lower=0> N;           // num. samples
  int<lower=0> K;           // num. schools
  int<lower=1,upper=K> x[N];// school indicator
  vector[N] y;              // exam means
  // real sigma0;              // prior std.
  // real mu0;                 // prior mean
}
parameters {
  vector[K] mu;             // school means
  real<lower=0> sigma;      // common std?
  real omega;               // school mean mean
  real<lower=0> tau2;       // school mean variance
}
model {
  // add prior for omega?
  // omega ~ normal(sigma0, mu0);

  mu ~ normal(omega, tau2);
  y ~ normal(mu[x], sigma);
}
