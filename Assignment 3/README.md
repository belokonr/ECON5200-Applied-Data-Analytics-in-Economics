# The Causal Architecture

**Module 3: Bootstrapping, Permutation, & Causal Inference**
**Role:** Senior Data Economist — SwiftCart Logistics
**Platform:** Google Colab

---

## Overview

This project tackles three core challenges facing SwiftCart Logistics, a multinational on-demand delivery platform: driver compensation equity, A/B testing of a new routing algorithm, and ROI evaluation of a premium subscription service. The analysis replaces fragile parametric assumptions with computation-heavy, non-parametric methods to build empirical evidence and isolate causality from correlation.

---

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Phase 1 — Bootstrapping Non-Parametric Uncertainty](#phase-1--bootstrapping-non-parametric-uncertainty)
3. [Phase 2 — Permutation Testing for A/B Experiments](#phase-2--permutation-testing-for-ab-experiments)
4. [Phase 3 — Causal Inference via Propensity Score Matching](#phase-3--causal-inference-via-propensity-score-matching)
5. [Phase 4 — AI-Assisted Visualization](#phase-4--ai-assisted-visualization)
6. [Data](#data)
7. [Academic Integrity Protocol](#academic-integrity-protocol)
8. [Dependencies](#dependencies)

---

## Environment Setup

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook titled: `Econ_5200_Assignment_3_Causal`.
3. Import the required libraries:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
```

---

## Phase 1 — Bootstrapping Non-Parametric Uncertainty

**Business Context:** A labor union is challenging SwiftCart's public claim about median driver compensation. Tip data is zero-inflated and right-skewed, rendering the Central Limit Theorem unreliable for small-sample audits.

### Step 1.1 — Data Generation

Simulate an audit sample of 250 driver tips: 100 zero-tips concatenated with 150 tips drawn from an Exponential distribution (`scale=5.0`).

```python
np.random.seed(42)
zeros = np.zeros(100)
tips = np.random.exponential(scale=5.0, size=150)
driver_tips = np.concatenate([zeros, tips])
```

### Step 1.2 — Manual Bootstrap Engine

- Resample `driver_tips` **with replacement** for **10,000 iterations**.
- Compute the **median** of each resample.
- Extract the **95% confidence interval** (2.5th and 97.5th percentiles) using `np.percentile`.
- Discuss the asymmetry of the bootstrap interval versus a standard parametric CI.

> **Constraint:** Manual `for` loop required — `scipy.stats.bootstrap` is **prohibited**.

---

## Phase 2 — Permutation Testing for A/B Experiments

**Business Context:** Engineering claims a new "Batch Routing" algorithm reduces delivery times. However, treatment-group outliers from software crash loops violate the homoscedasticity assumption of a standard T-test.

### Step 2.1 — Synthetic A/B Data

- **Control** (n=500): Normal distribution (`mean=35, sd=5`)
- **Treatment** (n=500): Log-Normal distribution (`mean=3.4, sigma=0.4`)
- Compute the **observed difference in means** (Control − Treatment).

### Step 2.2 — Manual Permutation Test

- Concatenate all 1,000 observations into a single array.
- Run **5,000 iterations**: shuffle, split into two groups of 500, compute the difference in means.
- Calculate the **empirical p-value**: proportion of permuted differences ≥ the observed difference.

> **Constraint:** Manual `for` loop required — `scipy.stats.permutation_test` is **prohibited**.

---

## Phase 3 — Causal Inference via Propensity Score Matching

**Business Context:** Marketing claims SwiftPass subscribers spend 300% more per month, but high-volume "power users" self-select into the program — a textbook case of selection bias.

### Step 3.1 — Naive Estimate

- Load `swiftcart_loyalty.csv`.
- Calculate the **Simple Difference in Means (SDO)** for post-treatment spending between subscribers (`D=1`) and non-subscribers (`D=0`).

### Step 3.2 — Propensity Score Matching (PSM)

1. **Estimate propensity scores** using `LogisticRegression` on pre-treatment covariates (order volume, account age, support tickets).
2. **Match** each subscriber to the nearest non-subscriber by propensity score using `NearestNeighbors`.
3. **Compute the ATT** (Average Treatment Effect on the Treated) from the matched sample.
4. **Compare** the causal ATT to the naive SDO with a written analysis.

---

## Phase 4 — AI-Assisted Visualization

**Status:** LLM usage **authorized and required**.

Using the P.R.I.M.E. Framework, prompt an LLM to generate a **Love Plot** (Standardized Mean Differences) that visualizes covariate balance before and after matching. The plot should provide visual evidence that selection bias was successfully mitigated.

---

## Data

| File | Description |
|---|---|
| `swiftcart_loyalty.csv` | Observational dataset with pre-treatment covariates and post-treatment spending for SwiftPass subscribers and non-subscribers. |

Synthetic datasets for Phases 1 and 2 are generated in-notebook using the seed `np.random.seed(42)`.

---

## Academic Integrity Protocol

- **Phases 1 & 2:** All bootstrap and permutation engines must be written manually with native NumPy. High-level statistical libraries (`scipy.stats.bootstrap`, `scipy.stats.permutation_test`) are strictly prohibited.
- **Phase 4:** LLM assistance is authorized exclusively for visualization expansion.

---

## Dependencies

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

All dependencies are pre-installed in Google Colab.
