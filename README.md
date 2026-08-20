# Week 05 Thursday — Integration Assignment: Full EDA Pipeline on an Orders Dataset

Self-contained exploratory data analysis notebook: generate a dataset with planted problems, diagnose every issue, clean with justified decisions, visualize with Matplotlib, and explain every finding in writing.

## Files

| File | Description |
|------|-------------|
| `week5_thursday_eda.ipynb` | Complete EDA notebook — generation, diagnosis, cleaning, 5 visualizations, findings, technical summary |
| `.venv/` | Python virtual environment with numpy, pandas, matplotlib, scipy, jupyter |
| `01_histogram_price_distribution.png` | Histogram: unit price spread |
| `02_bar_category_revenue.png` | Bar chart: total revenue per category |
| `03_scatter_price_vs_quantity.png` | Scatter plot: unit price vs quantity |
| `04_line_daily_orders.png` | Line chart: daily order volume over time |
| `05_bar_region_distribution.png` | Horizontal bar: region distribution |

## Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install numpy pandas matplotlib scipy jupyter nbconvert

# Launch JupyterLab
jupyter lab
```

Open `week5_thursday_eda.ipynb` and run **Kernel → Restart Kernel and Run All Cells** to verify, or run headlessly:

```bash
python -m jupyter nbconvert --to notebook --execute week5_thursday_eda.ipynb
```

## What the Notebook Covers

### 6 Phases (all completed)

| Phase | What Happens |
|-------|-------------|
| **1. Generation** | Dataset built from the exact assignment spec — 5,000 orders, 6 planted problems |
| **2. Diagnosis** | Full diagnostic sweep — `.head()`, `.info()`, `.describe()`, `.isna().sum()`, `.value_counts()`, plus IQR outlier detection and scipy distribution shape analysis |
| **3. Cleaning** | Per-column, per-issue fixes — each with a one-sentence justification, plus post-cleaning verification |
| **4. Visualization** | 5 charts via `fig, ax = plt.subplots()` — distribution, category comparison, relationship, time series, geographic breakdown |
| **5. Findings** | 3 full-sentence findings, each backed by a specific chart or number |
| **6. Technical Summary** | Plain-language write-up for a non-technical reader, with honest limitations |

### 6 Data-Quality Issues Found and Fixed

| # | Issue | Column | Detection | Fix |
|---|-------|--------|-----------|-----|
| 1 | Missing values | `customer_id` | `.isna().sum()` | Dropped ~150 rows (justified: cannot fabricate customer IDs) |
| 2 | Missing values | `region` | `.isna().sum()` | Filled with "Unknown" (justified: preserves rows, gap visible) |
| 3 | Inconsistent casing | `product_category` | `.value_counts()` | `.str.title()` normalized (justified: merges split categories) |
| 4 | Negative quantities | `quantity` | `.describe()` min | `.abs()` converted (justified: sign is data-entry error) |
| 5 | Outlier prices | `unit_price` | IQR fence detection | Median replacement (justified: preserves row without distortion) |
| 6 | Duplicate rows | all | `.duplicated()` | `drop_duplicates()` (justified: inflates counts) |

### 5 Visualizations

| Chart | Type | Question Answered |
|-------|------|-------------------|
| 01 | Histogram | What is the distribution of unit prices? |
| 02 | Bar chart | Which product category generates the most revenue? |
| 03 | Scatter plot | Is there a relationship between price and quantity? |
| 04 | Line chart | Is there a temporal pattern in order volume? |
| 05 | Horizontal bar | How are orders distributed across regions? |

### Extra Features Beyond Requirements

- IQR-based outlier detection with fence calculations
- Scipy distribution shape analysis (skewness + kurtosis)
- Revenue column computed for category-level analysis
- Post-cleaning verification block confirming all fixes
- Pearson correlation computed for scatter plot
- 7-day rolling average on time series chart
- Professional color palette, clean spines, formatted axis labels

## Requirements

- Python 3.10+
- numpy 2.2+, pandas 2.3+, matplotlib 3.10+, scipy 1.15+
- JupyterLab
