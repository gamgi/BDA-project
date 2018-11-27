data {
  int<lower=0> N;          // num. samples
  vector[N] x;             // income median
  vector[N] y;             // exam mean
  real sigma0;             // prior std.
}
parameters {
  real alpha;
  real beta;
  real<lower=0> sigma;
}
transformed parameters {
  vector[N] mu;
  mu = alpha + beta * x;
}
model {
  beta ~ normal(0, sigma0);
  y ~ normal(mu, sigma);
}
