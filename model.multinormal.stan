data {
  int<lower=0> N;          // num. samples
  vector[2] y[N];          // [income', mean']
  real sigma_mean;         // exam mean std.
  vector[2] mu0;           // prior mu mean
  cov_matrix[2] tau;       // prior mu cov matrix.
}
parameters {
  real<lower=-1, upper=1> rho;
  vector[2] mu;
  real<lower=0> sigma_income;
}
transformed parameters {
  cov_matrix[2] sigma;
  sigma[1,1] = sigma_income * sigma_income;
  sigma[1,2] = sigma_income * sigma_mean * rho;
  sigma[2,1] = sigma_income * sigma_mean * rho;
  sigma[2,2] = sigma_mean * sigma_mean;
}
model {
  mu ~ multi_normal(mu0, tau);      // prior
  for (n in 1:N) {
    y[n] ~ multi_normal(mu, sigma); // posterior
  }
}
generated quantities {
  vector[N] log_lik;
  for (i in 1:N)
    log_lik[i] = multi_normal_lpdf(y[i] | mu, sigma);
}
