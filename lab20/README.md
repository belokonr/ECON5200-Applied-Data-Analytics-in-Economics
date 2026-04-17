# Time Series Diagnostics & Advanced Decomposition

**Objective:** This lab develops a robust diagnostic and decomposition framework for time series analysis, addressing common specification errors in seasonal-trend decomposition and stationarity testing while extending standard methods to handle multi-seasonal patterns, structural breaks, and trend uncertainty quantification.

**Methodology:**

- Diagnosed a misspecified STL decomposition where an additive model was applied to multiplicative data; resolved via log-transformation to stabilize variance and restore valid residual structure.
- Corrected an ADF test configuration by adjusting the regression parameter (constant vs. constant + trend) to match the data-generating process, ensuring valid inference on unit root behavior.
- Applied MSTL (Multiple Seasonal-Trend decomposition using LOESS) to hourly electricity demand data, capturing both diurnal (24h) and weekly (168h) seasonal cycles in a single decomposition pass.
- Implemented a moving block bootstrap over the STL trend component of GDP data to construct nonparametric confidence bands, quantifying trend uncertainty without distributional assumptions.
- Deployed the PELT (Pruned Exact Linear Time) algorithm for structural break detection in GDP, then ran per-regime ADF tests to assess whether stationarity properties shift across identified break points.
- Consolidated all methods into a reusable `decompose.py` module exposing three core functions: `run_stl()`, `test_stationarity()`, and `detect_breaks()`.

**Key Findings:**

- The GDP series exhibits I(1) behavior globally, with PELT-identified structural breaks near [YOUR DATES] delineating regimes with distinct trend dynamics.
- Per-regime stationarity tests confirm that the unit root persists within individual regimes, suggesting the breaks reflect shifts in drift or trend slope rather than transitions between stationary and non-stationary behavior.
- Electricity demand decomposes cleanly under MSTL, with the daily cycle dominating variance and the weekly cycle capturing workday/weekend load differentials.
- Bootstrap-derived confidence bands on the GDP trend reveal meaningful uncertainty during recessionary periods, underscoring the limitations of point-estimate trend extraction.

