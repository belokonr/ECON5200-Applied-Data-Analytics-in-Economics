# Replication: Minimum Wages and Employment in the Fast-Food Industry

A replication of Card and Krueger's (1994) landmark study on the employment effects of New Jersey's 1992 minimum wage increase on the fast-food industry.

## Original Study

**Card, D., & Krueger, A. B. (1994).** Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania. *The American Economic Review*, 84(4), 772–793.

The original paper exploits the April 1, 1992 increase in New Jersey's minimum wage from $4.25 to $5.05 per hour, using fast-food restaurants in eastern Pennsylvania (where the minimum wage remained at $4.25) as a control group. The authors surveyed 410 Burger King, KFC, Wendy's, and Roy Rogers restaurants in two waves — before (February–March 1992) and after (November–December 1992) the policy change — and found no evidence that the higher minimum wage reduced employment.

## Project Overview

This project replicates the core empirical results of Card and Krueger (1994), including:

- **Difference-in-differences estimates** of the effect of the minimum wage on full-time-equivalent (FTE) employment (Table 3)
- **Reduced-form regression models** for employment changes using the New Jersey dummy and the initial wage gap variable (Table 4)
- **Specification tests and robustness checks** across alternative employment measures and sample restrictions (Table 5)
- **Price effect analysis** estimating the pass-through of higher labor costs to meal prices (Table 7)

## Repository Structure

```
├── README.md
├── data/
│   ├── raw/                 # Original survey data
│   └── cleaned/             # Processed analysis-ready datasets
├── code/
│   ├── 01_clean_data.R      # Data cleaning and variable construction
│   ├── 02_summary_stats.R   # Replication of Tables 1 and 2
│   ├── 03_employment.R      # Difference-in-differences and regression models (Tables 3–5)
│   ├── 04_other_outcomes.R  # Nonwage offsets and other outcomes (Table 6)
│   ├── 05_prices.R          # Price effect models (Table 7)
│   └── utils.R              # Helper functions
├── output/
│   ├── tables/              # Replicated tables
│   └── figures/             # Replicated figures (e.g., wage distributions)
└── docs/
    └── replication_notes.md # Notes on methodology and any deviations
```

## Data

The dataset used in this replication is sourced from Card and Krueger's original survey of 410 fast-food restaurants. The public-use dataset is available through the [Card and Krueger data archive](https://data.nber.org/minimum-wage/) hosted by the National Bureau of Economic Research (NBER).

### Key Variables

| Variable | Description |
|---|---|
| `state` | 1 = New Jersey, 0 = Pennsylvania |
| `chain` | Restaurant chain (Burger King, KFC, Roy Rogers, Wendy's) |
| `co_owned` | 1 = company-owned, 0 = franchisee-owned |
| `fte_before` | FTE employment in wave 1 (full-time + 0.5 × part-time) |
| `fte_after` | FTE employment in wave 2 |
| `wage_before` | Starting wage in wave 1 |
| `wage_after` | Starting wage in wave 2 |
| `gap` | Proportional wage increase needed to reach $5.05 (0 for PA stores) |
| `price_before` | Price of a full meal in wave 1 |
| `price_after` | Price of a full meal in wave 2 |
| `closed` | 1 = store permanently closed by wave 2 |

## Methodology

The primary identification strategy is a **difference-in-differences** design comparing employment changes at New Jersey restaurants (treatment) to Pennsylvania restaurants (control) before and after the minimum wage increase. An alternative within-state comparison uses the **initial wage gap** — the proportional raise required for a store to comply with the $5.05 minimum — as a continuous treatment intensity measure. Stores already paying at or above $5.00 serve as an internal control group within New Jersey.

FTE employment is defined as: `FTE = full-time workers (including managers) + 0.5 × part-time workers`. Employment at permanently closed stores is set to zero; temporarily closed stores are treated as missing in the baseline specification.

## Requirements

- R ≥ 4.0 (or Python ≥ 3.8, depending on implementation)
- Key packages: `tidyverse`, `fixest`, `modelsummary`, `haven`

Install R dependencies:

```r
install.packages(c("tidyverse", "fixest", "modelsummary", "haven"))
```

## How to Run

```bash
# Clone the repository
git clone https://github.com/username/card-krueger-replication.git
cd card-krueger-replication

# Run the full analysis pipeline
Rscript code/01_clean_data.R
Rscript code/02_summary_stats.R
Rscript code/03_employment.R
Rscript code/04_other_outcomes.R
Rscript code/05_prices.R
```

## References

- Card, D., & Krueger, A. B. (1994). Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania. *The American Economic Review*, 84(4), 772–793.
- Card, D., & Krueger, A. B. (1993). Minimum Wages and Employment: A Case Study of the Fast Food Industry in New Jersey and Pennsylvania. NBER Working Paper No. 4509.
- Katz, L. F., & Krueger, A. B. (1992). The Effect of the Minimum Wage on the Fast Food Industry. *Industrial and Labor Relations Review*, 46(1), 6–21.

## License

This project is for educational purposes only. The original data and study are the intellectual property of the original authors.
