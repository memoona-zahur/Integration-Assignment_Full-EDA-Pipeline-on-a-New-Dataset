# Technical Summary — Orders Dataset EDA
**Date:** Week 05, Thursday

---

## What the Dataset Contains

This dataset represents **5,000 hourly orders** placed throughout January–May 2024, each with an order ID, date, customer ID, product category (Electronics, Home Goods, Apparel, or Books), quantity, unit price, and geographic region (North, South, East, or West). The data was generated synthetically with several intentional quality issues to simulate the kinds of problems found in real-world data systems.

**Final cleaned shape:** ~4,850 rows × 8 columns (after removing 15 duplicates, ~150 rows with missing customer IDs, and adding a computed revenue column).

---

## What Was Wrong (and What We Fixed)

| Issue | Rows Affected | Resolution | Justification |
|-------|--------------|------------|---------------|
| Missing `customer_id` | ~150 (3%) | Dropped rows | Cannot fabricate customer IDs; 3% loss is acceptable |
| Missing `region` | ~200 (4%) | Filled with "Unknown" | Preserves rows; gap remains visible in reports |
| Inconsistent category casing | ~2,500 (~50%) | Normalized to title case | "Electronics"/"electronics" merged into one category |
| Negative quantities | 30 | Converted to absolute values | Sign was a data-entry error; magnitude is meaningful |
| Implausible unit prices ($4,999.99) | 20 | Replaced with median ($44.15) | Outlier distorted all price-based statistics |
| Duplicate rows | 15 | Removed exact duplicates | Would inflate counts and revenue totals |

---

## Top Findings

1. **Electronics is the dominant revenue category**, generating the highest total revenue across all orders. This result only emerges after merging the duplicated "Electronics"/"electronics" labels — the casing inconsistency was the single most impactful data quality issue in the dataset, one that would silently halve the apparent revenue for the largest product line.

2. **Order quantity is independent of unit price.** The correlation between these two variables is near zero, and the scatter plot trend line is flat. Revenue variation across orders is driven by price differences, not by how many items customers buy at once. This suggests pricing strategy, not volume bundling, is the primary revenue lever in this dataset.

3. **4% of orders lack geographic data.** After filling missing regions with "Unknown," the gap remains visible in all reports. Any regional revenue comparison must acknowledge that roughly 1 in 25 orders is excluded from region-specific conclusions.

---

## Honest Limitations

**The most significant limitation** is that ~150 orders (3%) with missing `customer_id` values were dropped entirely. This means their revenue is excluded from all totals and averages. If those missing IDs follow a pattern — for example, if a particular region or product category is disproportionately affected — the totals in this report could be biased in a way that is invisible from the cleaned data alone.

A second limitation is that **outlier unit prices ($4,999.99) were replaced with the column median** rather than investigated further. In a real business context, it would be worth checking whether those high prices represent genuine (but rare) premium transactions or are truly data-entry errors. The median replacement is conservative but assumes the latter without proof.

Finally, this is **synthetic data** — the patterns observed (uniform daily orders, flat price-quantity relationship) are artifacts of the generation process. Real-world data would likely show seasonality, customer behavior patterns, and price sensitivity that this dataset cannot capture.

---

*Generated as part of the Week 05 Integration Assignment — Full EDA Pipeline.*
