# Bayesian Data Analysis Project
Project

# Getting started
```
python -m venv venv
source venv
pip install -r requirements.txt
python test.py
```

# Development
## Linting
`./lint.sh`

# Fetching data
In project root, run `bin/download_data.sh`.
This requires [jq](https://stedolan.github.io/jq/).

# Data Sources
* https://www.ylioppilastutkinto.fi/tietopalvelut/tilastot/koulukohtaisia-tunnuslukuja
* http://pxnet2.stat.fi/PXWeb/pxweb/fi/StatFin/StatFin__tul__tvt/?tablelist=true (nr 12)

# Sources
* https://github.com/betanalpha/jupyter_case_studies/blob/master/pystan_workflow/stan_utility.py
