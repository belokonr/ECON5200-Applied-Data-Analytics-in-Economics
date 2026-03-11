# Data Wrangling & Engineering Pipeline

## Objective

Design and execute a reproducible feature-engineering and imputation pipeline to transform a chaotic human-resources economics dataset into an analysis-ready frame suitable for causal inference and predictive econometric modeling.

## Data

- **Source file:** `messy_hr_economics.csv`

## Tech Stack

- **Language:** Python
- **Core libraries:** pandas, statsmodels, missingno, category_encoders

## Methodology

- **Missingness diagnostics** — Profiled the dataset with `missingno` visualizations (matrix, heatmap, dendrogram) to classify missing-data mechanisms. Confirmed that the dominant pattern was **Missing at Random (MAR)**, meaning missingness was conditionally dependent on observed covariates rather than on the missing values themselves.
- **Conditional imputation** — Applied imputation strategies aligned with each variable's distributional properties and missingness mechanism, preserving the joint distribution of the data to avoid biasing downstream coefficient estimates.
- **Dummy-variable encoding with reference-class exclusion** — Converted categorical regressors into binary indicator columns while deliberately dropping one reference category per factor. This step prevents the **Dummy Variable Trap** (perfect multicollinearity), which would otherwise render OLS estimation infeasible due to a singular design matrix.
- **Target Encoding for high-cardinality features** — Replaced high-cardinality geographic identifiers with their conditional mean of the target variable using `category_encoders.TargetEncoder`. This compresses the feature space from potentially hundreds of sparse dummies into a single, information-dense continuous regressor while mitigating overfitting risk through built-in regularization.
- **Post-pipeline validation** — Verified the cleaned frame for remaining nulls, multicollinearity diagnostics (VIF), and dtype consistency to confirm readiness for econometric specification.

## Key Findings

- **MAR confirmation** allowed the use of principled, conditionally-driven imputation rather than costly listwise deletion, preserving sample size and statistical power.
- **Reference-class exclusion** resolved perfect multicollinearity, ensuring that all coefficient estimates are uniquely identified and interpretable relative to a clearly defined baseline group.
- **Target Encoding** successfully compressed high-cardinality geographic data into a single continuous feature, substantially reducing dimensionality without discarding the geographic signal embedded in the outcome variable.
- The final pipeline produced a clean, fully populated, and econometrically well-conditioned dataset ready for OLS, IV, or panel-data estimation.
