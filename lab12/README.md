# Architecting the Prediction Engine

## Objective

Engineer a multivariate OLS prediction framework to forecast residential real estate valuations using cross-sectional market data, and rigorously evaluate out-of-sample generalization performance through dollar-denominated loss minimization.

## Data

**Zillow ZHVI 2026 Micro Dataset** — A cross-sectional snapshot of modern U.S. residential market valuations sourced from Zillow's Home Value Index.

## Tech Stack

Python · pandas · NumPy · statsmodels (Patsy Formula API)

## Methodology

- Ingested and preprocessed the Zillow ZHVI cross-sectional dataset, performing exploratory diagnostics to identify candidate regressors and assess distributional properties.
- Specified a multivariate OLS regression model via the statsmodels Patsy Formula API, selecting predictors grounded in economic intuition and empirical signal strength.
- Partitioned the dataset into training and holdout samples to enforce a strict separation between in-sample estimation and out-of-sample evaluation.
- Generated point forecasts on the holdout set and computed Root Mean Squared Error (RMSE) in nominal U.S. dollars, translating statistical loss into an interpretable financial error margin.
- Benchmarked model performance against baseline heuristics to quantify the marginal predictive value of the multivariate specification.

## Key Findings

The project marked a deliberate transition from classical inferential modeling — where the objective is parameter interpretation and hypothesis testing — to predictive engineering, where the objective is minimizing forecast error on unseen observations. By denominating the RMSE in actual U.S. dollars rather than abstract statistical units, the framework produces a directly actionable measure of algorithmic business risk: a single number that quantifies, in financial terms, the expected magnitude of valuation error the model introduces into any downstream decision pipeline.
