# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective

This lab constructs a multivariate hedonic pricing model on synthetic California real estate data and manually proves the Frisch-Waugh-Lovell (FWL) theorem, demonstrating how OLS mechanically isolates partial effects by partialling out shared covariance among regressors.

## Data

2026 California residential sale records (Zillow synthetic dataset) comprising three key variables: **Sale_Price**, **Property_Age**, and **Distance_to_Tech_Hub**.

## Tech Stack

Python 3.10+ · pandas · statsmodels.formula.api · matplotlib

## Methodology

- Estimated a **bivariate OLS** regression of Sale_Price on Property_Age alone to establish a naïve baseline coefficient.
- Estimated the **full multivariate OLS** specification, regressing Sale_Price on both Property_Age and Distance_to_Tech_Hub, to obtain the partial effect of property age conditional on tech-hub proximity.
- Executed a manual proof of the **Frisch-Waugh-Lovell theorem** in three stages:
  1. Regressed Property_Age on Distance_to_Tech_Hub and extracted the residuals (i.e., the component of property age orthogonal to tech-hub proximity).
  2. Regressed Sale_Price on Distance_to_Tech_Hub and extracted the residuals (i.e., the component of sale price orthogonal to tech-hub proximity).
  3. Regressed the Sale_Price residuals on the Property_Age residuals. The resulting coefficient was compared against the multivariate partial coefficient.
- Visualized the residual-on-residual relationship to illustrate the partialled-out variance structure.

## Key Findings

- **Omitted Variable Bias (OVB):** The bivariate specification produced a materially inflated coefficient on Property_Age. By excluding Distance_to_Tech_Hub — a variable correlated with both the regressor and the dependent variable — the model falsely attributed the price premium associated with tech-hub proximity to the physical age of the home.
- **FWL Verification:** The manually computed residual-on-residual coefficient matched the multivariate OLS partial coefficient to full machine precision, confirming that OLS achieves *ceteris paribus* interpretation not by assumption, but by algebraic construction — systematically stripping shared covariance from each regressor before estimating its marginal contribution.
- **Implication:** The exercise demonstrates that dimensionality in regression is not merely additive; each additional covariate restructures the entire coefficient vector by reallocating explained variance. The FWL theorem makes this mechanism explicit and verifiable.
