data {
  int<lower=0> N;          // num. samples
  vector[N] x;             // income median
  vector[N] y;             // exam mean
  real sigma0;             // beta prior std.
  real sigma1;             // alpha prior std.
  real mu1;                // alpha prior mu.
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
  alpha ~ normal(mu1, sigma1);  // Alpha prior
  beta ~ normal(0, sigma0);     // Beta prior
  y ~ normal(mu, sigma);
}
