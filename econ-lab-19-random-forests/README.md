**Project Title:** Tree-Based Models — Random Forests

**Objective:** This project evaluates the predictive performance and interpretability of tree-based ensemble methods against linear benchmarks on the California Housing dataset, with emphasis on hyperparameter optimization, feature importance diagnostics, and classification performance.

**Methodology:**

- Benchmarked Decision Tree, Ridge Regression, and Random Forest regressors on 20,640 observations across 8 housing features, using cross-validated RMSE and R² as primary evaluation metrics.
- Conducted systematic hyperparameter tuning of the Random Forest via GridSearchCV over `n_estimators`, `max_depth`, and `max_features`, selecting the configuration that minimized out-of-sample error.
- Extracted Mean Decrease in Impurity (MDI) and permutation-based feature importances to assess variable contributions under both model-intrinsic and model-agnostic frameworks.
- Constructed a Random Forest classifier for a binarized price outcome and compared ROC-AUC against a logistic regression baseline.
- Developed an interactive Plotly + ipywidgets dashboard for real-time exploration of model predictions, residual diagnostics, and feature importance rankings.

**Key Findings:**

- The tuned Random Forest substantially outperformed Ridge Regression (R² = 0.8051 vs. R² = 0.5759), confirming the presence of meaningful nonlinearities and interaction effects in the housing data.
- MDI and permutation importance rankings diverged for correlated features — median income dominated under both methods, while geographic coordinates showed greater sensitivity to the importance estimation approach.
- The RF classifier achieved a higher AUC than logistic regression, reinforcing the advantage of flexible, nonparametric decision boundaries for this prediction task.

