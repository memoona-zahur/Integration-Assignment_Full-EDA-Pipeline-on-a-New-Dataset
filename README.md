# Week 05 Thursday — Integration Assignment: Full EDA Pipeline on an Orders Dataset

Self-contained exploratory data analysis notebook: generate a dataset with planted problems, diagnose every issue, clean with justified decisions, visualize with Matplotlib, and explain every finding in writing.

## Files

| File | Description |
|------|-------------|
| `week5_thursday_eda.ipynb` | Complete EDA notebook — diagnosis, cleaning, 9 visualizations, 15 automated checks, findings, technical summary |
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

### 8 Phases (all completed)

| Phase | What Happens |
|-------|-------------|
| **1. Loading** | Dataset loaded from `orders_raw.csv` — exact assignment spec |
| **2. Diagnosis** | Full sweep — `.head()`, `.info()`, `.describe()`, `.isna().sum()`, `.value_counts()`, IQR outlier detection, scipy shape analysis |
| **3. Cleaning** | 7 per-column fixes — each with written justification and alternatives considered |
| **4. Verification** | 22 automated quality checks confirming every fix worked |
| **5. Before/After** | Side-by-side comparison table showing cleaning impact |
| **6. Visualization** | 9 charts via `fig, ax = plt.subplots()` — distribution, category, relationship, time, region, subplots grid, misleading comparison, before/after overlay |
| **7. Findings** | 4 full-sentence findings, each backed by a specific chart or number |
| **8. Technical Summary** | Plain-language write-up for non-technical readers, with honest limitations |

### 7 Data-Quality Issues Found and Fixed

| # | Issue | Column | Detection | Fix |
|---|-------|--------|-----------|-----|
| 1 | Missing values | `customer_id` | `.isna().sum()` | Dropped ~150 rows (justified: cannot fabricate customer IDs) |
| 2 | Missing values | `region` | `.isna().sum()` | Filled with "Unknown" (justified: preserves rows, gap visible) |
| 3 | Inconsistent casing | `product_category` | `.value_counts()` | `.str.title()` normalized (justified: merges split categories) |
| 4 | Negative quantities | `quantity` | `.describe()` min | `.abs()` converted (justified: sign is data-entry error) |
| 5 | Negative prices | `unit_price` | `.describe()` min | `.abs()` converted (justified: sign is data-entry error) |
| 6 | Outlier prices | `unit_price` | IQR fence detection | Median replacement (justified: preserves row without distortion) |
| 7 | Duplicate rows | all | `.duplicated()` | `drop_duplicates()` (justified: inflates counts) |

### 9 Visualizations

| Chart | Type | Question Answered |
|-------|------|-------------------|
| 01 | Histogram with annotations | What is the distribution of unit prices? |
| 02 | Bar chart with value labels | Which product category generates the most revenue? |
| 03 | Scatter plot with Pearson r | Is there a relationship between price and quantity? |
| 04 | Line chart with rolling average | Is there a temporal pattern in order volume? |
| 05 | Horizontal bar with percentages | How are orders distributed across regions? |
| 06 | 2x2 subplots grid | Four key views in one figure |
| 07 | Misleading vs honest comparison | How can a truncated y-axis deceive? |
| 08 | Before/after overlaid histograms | How did cleaning change the data's shape? |
| 09 | Category counts bar chart | How many orders per category after normalization? |

### Extra Features Beyond Requirements

- IQR-based outlier detection with fence calculations
- Scipy distribution shape analysis (skewness + kurtosis)
- Negative unit_price detection (7th issue beyond the 6 listed in spec)
- Revenue column computed for category-level analysis
- 15 automated post-cleaning verification checks
- Pearson correlation computed for scatter plot
- 7-day rolling average on time series chart
- Misleading vs honest chart comparison (media literacy)
- Before/after comparison table quantifying cleaning impact
- Professional color palette, clean spines, formatted axis labels

## Requirements

- Python 3.10+
- numpy 2.2+, pandas 2.3+, matplotlib 3.10+, scipy 1.15+
- JupyterLab
