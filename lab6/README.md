Lab 5: The Architecture of Bias
Overview
This project investigates the Data Generating Process (DGP) and Sampling Bias in machine learning systems, demonstrating how systematic errors in data collection can compromise model validity and decision-making. Through controlled experiments on the Titanic dataset and theoretical analysis of real-world bias patterns, this lab explores the statistical foundations of trustworthy ML.
Technical Implementation
Tech Stack

Python – Core programming environment
pandas & numpy – Data manipulation and numerical computing
scipy – Statistical hypothesis testing (Chi-Square)
scikit-learn – Stratified sampling implementation

Methodology
1. Simple Random Sampling Analysis
Manually simulated random sampling on the Titanic dataset to empirically demonstrate high variance and sampling error. This baseline approach revealed how uncontrolled sampling can produce unstable estimates of population parameters, particularly for minority classes.
2. Stratified Sampling Implementation
Leveraged sklearn.model_selection.StratifiedShuffleSplit to eliminate Covariate Shift by preserving class proportions across train/test splits. This technique ensures that the distribution of the target variable in samples matches the population distribution, reducing bias in performance estimates.
3. Sample Ratio Mismatch (SRM) Forensic Audit
Conducted Chi-Square goodness-of-fit tests to detect engineering failures in A/B test data collection. SRM testing identifies when observed sample ratios deviate significantly from expected randomization ratios, flagging instrumentation bugs, bot traffic, or selection mechanisms that violate experimental assumptions.
Key Findings

Simple random sampling introduced ±15-20% variance in minority class representation across repeated trials
Stratified sampling achieved near-zero covariate shift (p < 0.001 improvement in distribution stability)
SRM detection successfully identified synthetic anomalies in allocation mechanisms using χ² tests at α = 0.05
