# Self-Review Checklist — Week 5 Thursday EDA

## Data Loading & Inspection

- [x] Dataset loaded from CSV via `pd.read_csv()`
- [x] Shape confirmed (5,015 rows, 7 columns)
- [x] `.head()` inspected — first 10 rows displayed
- [x] `.info()` run — column types and missing counts reviewed
- [x] `.describe()` run — min/max/mean/std examined for impossible values
- [x] `.isna().sum()` run — exact missing counts computed with percentages
- [x] `.value_counts()` run — category labels checked for inconsistencies

## Cleaning Decisions (per-issue justified)

- [x] Missing `customer_id` (150 rows) — dropped rows
- [x] Missing `region` (~4%, 193 rows) — filled with "Unknown"
- [x] Inconsistent category casing ("electronics" → "Electronics") — title case
- [x] Negative `quantity` (30 rows) — `.abs()` (treated as sign error per assignment framing; see notebook section 2.5 and 3.3 for returns consideration)
- [x] Negative `unit_price` (63 rows) — `.abs()` (natural byproduct of Normal(45,20) distribution)
- [x] Outlier `unit_price` = 4999.99 (20 rows) — replaced with median of non-outlier prices
- [x] Duplicate rows (15 rows) — `drop_duplicates()`
- [x] Each cleaning decision justified with reasoning per column/issue

## Visualization

- [x] 9 charts built via `fig, ax = plt.subplots()` pattern (required: 3+)
- [x] All charts labeled with titles, axis labels, and legends
- [x] Misleading chart comparison (truncated y-axis) included
- [x] 2×2 subplots grid included (4 views in one figure)
- [x] Statistical annotations on charts (mean, median, skewness, Pearson r)

## Automated Quality Checks

- [x] 22 automated post-cleaning quality checks — all passing

## Summary & Documentation

- [x] Before/after comparison table showing cleaning impact
- [x] 4 findings stated as full sentences backed by specific charts/numbers
- [x] Technical summary written for non-technical reader with honest limitations
- [x] README updated with all 18 files and 22 checks

## Execution

- [x] Notebook survives Restart Kernel and Run All without errors
- [x] Feature branch (`feature/week5-eda`) with incremental commits

## Issues Found During Review

1. **Date range:** January–May corrected to January–July (data runs through 2024-07-27)
2. **Planted issue count:** "seven intentional" corrected to "six deliberately introduced + one discovered"
3. **Duplicate explanation:** "5 unique rows × 3 copies" corrected to "15 unique rows × 1 copy"
4. **IQR section:** Clarified 45 rows flagged by IQR vs 20 planted outlier values
5. **Negative unit_price origin:** Clarified as natural distribution byproduct, not deliberate injection
6. **Returns consideration:** Added explicit "why not treat as returns" paragraph to cleaning section 3.3

## Self-Assessment

**Strengths:**
- 9 charts (3× required), 22 automated checks, 7 issues found and fixed
- Per-column justified decisions, not blanket `dropna()`/`fillna()`
- Diagnosis before cleaning (Phase 2 before Phase 3)
- Bonus catch: negative unit_price not in spec but genuinely present

**Limitations acknowledged:**
- Negative quantities treated as sign errors; a return-aware system would net these against revenue
- `is_return` flag created from original quantity sign before `.abs()`; available for downstream segmentation
- `Unknown` region is a placeholder, not a real geographic region
- Outlier replacement uses median — sensitive to distribution shape
