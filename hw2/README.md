# Audit 02: Deconstructing Statistical Lies

A forensic investigation into the statistical mechanisms that produce misleading conclusions in data science and machine learning — from biased data generation to flawed experimental design.

## Objective

This project examines how the **Data Generating Process (DGP)** and **Sampling Bias** can silently corrupt machine learning pipelines and statistical analyses. Through hands-on simulations and audits, it exposes common failure modes that lead practitioners to draw confident but incorrect conclusions from data.

## Tech Stack

- **Python 3**
- **pandas** — data manipulation and analysis
- **NumPy** — numerical simulation and computation
- **Matplotlib** — statistical visualization

## Methodology

### 1. Data Generating Process Simulation — Latency Skew

Manually simulated a skewed data generating process to demonstrate how summary statistics can misrepresent underlying system behavior. Compared **Median Absolute Deviation (MAD)** against **Standard Deviation (SD)** to illustrate the fragility of variance metrics under non-normal distributions.

### 2. Bayesian Probability Audit — False Positive Erosion

Implemented a Bayesian probability framework to quantify how **false positive rates escalate** as the baseline probability of a true positive decreases. This audit demonstrates why high-accuracy classifiers can still produce predominantly incorrect positive predictions in rare-event scenarios.

### 3. Sample Ratio Mismatch (SRM) Forensic Audit

Applied **Chi-Square goodness-of-fit tests** to detect Sample Ratio Mismatch in A/B testing environments. SRM is a critical diagnostic for identifying upstream engineering failures — such as broken randomization or biased assignment — that silently invalidate experimental results.

### 4. Survivorship Bias Visualization — Crypto Markets

Visualized survivorship bias in cryptocurrency market data to show how analyzing only surviving assets produces a systematically distorted picture of expected returns, concealing the full distribution of outcomes including failures.

## Key Takeaways

- Summary statistics without distributional context are unreliable decision inputs.
- Bayesian reasoning is essential when evaluating classifiers on imbalanced populations.
- A/B tests require SRM checks as a prerequisite to any inference.
- Survivorship bias is not a theoretical concern — it is a measurable distortion in real market data.

