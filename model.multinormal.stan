data {
  int<lower=0> N;          // num. samples
  vector[2] y[N];          // [income', mean']
  real sigma0;             // income std.
  real sigma1;             // exam mean std.
  vector[2] mu0;           // prior mu.
  cov_matrix[2] tau;       // prior mu cov matrix.
}
parameters {
  real<lower=-1, upper=1> rho;
  vector[2] mu;
}
transformed parameters {
  cov_matrix[2] sigma;
  sigma[1,1] = sigma0 * sigma0;
  sigma[1,2] = sigma0 * sigma1 * rho;
  sigma[2,1] = sigma0 * sigma1 * rho;
  sigma[2,2] = sigma1 * sigma1;
}
model {
  mu ~ multi_normal(mu0, tau);      // prior
  for (n in 1:N) {
    y[n] ~ multi_normal(mu, sigma);
  }
}
