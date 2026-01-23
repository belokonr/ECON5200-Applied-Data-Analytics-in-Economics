Lab 2: The Illusion of Growth & The Composition Effect
Objective
Built a Python pipeline to ingest live economic data from the Federal Reserve Economic Data (FRED) API to analyze wage stagnation in the United States and correct for statistical biases that obscure real economic trends. This project demonstrates how seemingly positive wage growth can be a statistical illusion created by compositional shifts in the labor force.
Methodology
Data Collection & Processing
API Integration:

Utilized the fredapi Python library to programmatically fetch real-time economic data from the Federal Reserve
Retrieved AHETPI (Average Hourly Earnings of Production and Nonsupervisory Employees) as the primary nominal wage measure
Fetched CPI (Consumer Price Index) data to adjust for inflation

Real Wage Calculation:

Computed real wages by deflating nominal earnings with the CPI: Real_Wage = (Nominal_Wage / CPI) × 100
Rebased historical series to enable direct comparison across decades
Created time-series visualizations contrasting nominal versus real purchasing power from 1964 to present

Detecting and Correcting the Composition Effect
Statistical Anomaly Detection:

Identified an unusual spike in average wages during the 2020 pandemic period
Recognized this as a potential statistical artifact rather than genuine wage growth

ECI Correction Method:

Fetched Employment Cost Index (ECIWAG) data, which controls for changes in workforce composition
The ECI tracks wages for fixed job positions, eliminating bias from worker mix changes
Rebased both standard wage data and ECI to 100 (2015 baseline) for direct comparison
Isolated the divergence between biased and composition-adjusted measures during 2020

Key Findings
The Money Illusion (1964-Present)
Visualized the stark contrast between nominal and real wage growth over 50+ years:

Nominal wages show consistent upward trajectory, creating an illusion of prosperity
Real wages (adjusted for inflation) reveal near-flat purchasing power since the 1970s
Workers are earning more dollars but buying approximately the same amount of goods and services

The Pandemic Paradox: A Statistical Artifact
The 2020 wage data revealed a critical lesson in economic measurement:
The Apparent Boom:

Standard wage statistics showed a sharp spike in average hourly earnings during March-May 2020
Superficially suggested workers were suddenly earning significantly more

The Hidden Reality:

The Employment Cost Index (ECI) showed stable, modest growth during the same period
The divergence proved the spike was an artificial statistical effect, not real wage increases

Root Cause - The Composition Effect:

Low-wage service workers (retail, hospitality, food service) were disproportionately laid off during lockdowns
The remaining workforce was compositionally skewed toward higher-wage positions
Average wages rose not because anyone got raises, but because the denominator changed
This is analogous to a classroom's average test score rising after struggling students drop the class

Economic Implications:

Demonstrates why composition-controlled indices like the ECI are essential for policy decisions
Reveals how headline statistics can mislead during structural economic shocks
Highlights the importance of understanding measurement methodology when interpreting economic data

Technical Stack

Python: Core programming language
fredapi: Federal Reserve API client
pandas: Time-series data manipulation and analysis
matplotlib: Statistical visualization and annotation

Visualizations

Time-series comparison of nominal vs. real wages (1964-present)
Annotated 2020 pandemic spike showing the composition effect
Dual-axis comparison of standard wages vs. Employment Cost Index (2015-present)
