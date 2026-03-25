# High-Dimensional GDP Growth Forecasting with Regularized Regression

## Objective

This project forecasts 5-year average GDP per capita growth across 120+ countries using 50+ World Development Indicators, illustrating how OLS breaks down in high-dimensional settings and how Ridge and Lasso regularization recover reliable out-of-sample predictive performance.

## Methodology

- **Data acquisition.** Retrieved 35+ indicators from the World Bank's World Development Indicators (WDI) database via the `wbgapi` Python API, covering trade openness, macroeconomic aggregates, educational attainment, infrastructure, health outcomes, financial development, natural resource rents, agricultural productivity, and governance quality for the 2013–2019 period.
- **Feature engineering and preprocessing.** Constructed a cross-sectional design matrix of country-level averages, standardized all predictors using `StandardScaler` to ensure coefficient comparability and well-conditioned optimization across regularization methods.
- **Model estimation.** Estimated three linear models — unrestricted OLS, Ridge (`RidgeCV`), and Lasso (`LassoCV`) — with regularization hyperparameters selected via built-in cross-validation over a grid of candidate λ values.
- **Evaluation.** Assessed in-sample versus out-of-sample fit using `train_test_split`, comparing training and test R² to diagnose overfitting and quantify regularization gains.
- **Coefficient path analysis.** Visualized the full Lasso regularization path (`lasso_path`) to trace how individual predictor coefficients shrink toward zero as the penalty increases, clarifying which indicators survive selection at the optimal λ.

## Key Findings

- **OLS overfitting.** The unrestricted OLS model achieved a high training R² but produced poor — and in some splits negative — test R², confirming that fitting a large number of predictors to a moderate cross-section of countries captures noise rather than signal.
- **Regularization gains.** Both Ridge and Lasso substantially improved out-of-sample accuracy, demonstrating the practical payoff of the bias-variance tradeoff: accepting a small amount of in-sample bias in exchange for a large reduction in prediction variance.
- **Sparsity and interpretability.** Lasso matched Ridge's test R² while driving the majority of coefficients to exactly zero, selecting a compact subset of economically meaningful predictors. This underscores a key distinction: predictors excluded by Lasso are not necessarily irrelevant to growth — they are redundant *conditional on the retained set*, a point that matters for policy interpretation.

## Tech Stack

Python · pandas · NumPy · scikit-learn · matplotlib · wbgapi
