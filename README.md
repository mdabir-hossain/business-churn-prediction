# Business Churn Prediction

Customer churn prediction with leakage-aware validation, aggregate model evaluation, and business-focused threshold analysis.

## Executive Summary

This portfolio project turns an early churn-modelling notebook into a more reproducible, public-safe machine learning project for UK Machine Learning Engineer, Data Scientist, and Business Data Analyst applications.

The controlled Phase 5B run evaluates three models using aggregate metrics only. No row-level predictions are published. Logistic Regression is strongest for ROC-AUC and churn recall, while HistGradientBoosting is strongest for PR-AUC and top-decile capture. The preferred model depends on the retention strategy: broad churn capture, higher precision outreach, or prioritised high-risk segments.

## Business Problem

Churn prediction can help retention, customer success, and commercial teams prioritise customers who may need outreach before they leave. This project frames model output as decision support, not automatic customer treatment.

The model should support questions such as:

- Which customers are associated with higher churn risk?
- How does threshold choice affect false positives and missed churners?
- Which model is more suitable for outreach capacity and retention priorities?

## Data And Public Safety

The local dataset is a telecom-style customer churn CSV at `data/telco_churn.csv`.

Current public-safety position:

- Dataset provenance/licence: to be confirmed.
- Raw customer-level CSV files are ignored by default until publication rights are clear.
- `customerID` is treated as an identifier and excluded from model features.
- No row-level prediction dumps are published.
- Controlled outputs under `reports/metrics/` are aggregate metrics only.

## Methodology

The controlled pipeline:

1. Loads the local CSV from `data/telco_churn.csv`.
2. Validates expected columns.
3. Converts `TotalCharges` to numeric and drops missing `TotalCharges` rows.
4. Creates deterministic features only, including service count, autopay flag, fibre flag, senior-alone flag, and observed revenue-to-date.
5. Excludes `customerID` and `Churn` from features.
6. Uses a stratified train/test split.
7. Fits preprocessing inside scikit-learn pipelines.
8. Compares Logistic Regression, Random Forest, and HistGradientBoosting.
9. Saves aggregate metrics and figures.

The pipeline intentionally avoids full-dataset `pd.qcut` and does not publish row-level predictions.

## Validation Strategy

Controlled Phase 5B run context:

- Dataset path: `data/telco_churn.csv`
- Rows after cleaning: 7,032
- Target distribution after cleaning: 5,163 non-churn, 1,869 churn
- Split method: stratified train/test split
- Test size: 0.2
- Random seed: 42
- Public safety: aggregate metrics only

Prediction timing and prediction window are proposed assumptions, not confirmed business truth. See `docs/leakage_review.md` and `docs/validation_strategy.md`.

## Controlled Results

Metrics below are from saved Phase 5B artifacts in `reports/metrics/`, rounded to 3 decimals.

| Model | ROC-AUC | PR-AUC | Churn Precision | Churn Recall | Churn F1 | Top-Decile Capture |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.836 | 0.622 | 0.492 | 0.797 | 0.608 | 0.262 |
| Random Forest | 0.817 | 0.599 | 0.621 | 0.487 | 0.546 | 0.267 |
| HistGradientBoosting | 0.825 | 0.631 | 0.592 | 0.508 | 0.547 | 0.283 |

Interpretation:

- Logistic Regression has the strongest ROC-AUC and highest churn recall, making it useful where missing likely churners is costly.
- HistGradientBoosting has the strongest PR-AUC and top-decile capture, making it useful for prioritised high-risk outreach.
- Random Forest has the highest churn precision at the default threshold, but lower recall.

Figures:

- `reports/figures/roc_auc_comparison.png`
- `reports/figures/pr_auc_comparison.png`
- `reports/figures/recall_churn_class_comparison.png`

## Threshold Trade-Offs

The saved `threshold_metrics.csv` shows the expected trade-off:

- Lower thresholds capture more churners but create more false positives.
- Higher thresholds improve precision but miss more churners.
- Threshold choice should depend on retention budget, outreach capacity, intervention cost, customer fatigue, and tolerance for missed churners.

Example from Logistic Regression:

| Threshold | Precision | Recall | F1 |
|---:|---:|---:|---:|
| 0.3 | 0.415 | 0.928 | 0.573 |
| 0.5 | 0.492 | 0.797 | 0.608 |
| 0.7 | 0.613 | 0.623 | 0.618 |

No threshold is presented as final or deployment-ready.

## How To Run

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements-dev.txt
```

Run tests:

```powershell
pytest
```

Run the controlled pipeline:

```powershell
python scripts/train_model.py --config configs/train_config.yaml
```

Expected aggregate outputs:

- `reports/metrics/model_metrics.json`
- `reports/metrics/model_comparison.csv`
- `reports/metrics/threshold_metrics.csv`
- `reports/business_summary.md`
- `reports/figures/*.png`

## Project Structure

```text
business-churn-prediction/
|-- README.md
|-- configs/
|   `-- train_config.yaml
|-- data/
|   |-- README.md
|   |-- sample/
|   `-- telco_churn.csv
|-- docs/
|   |-- business_context.md
|   |-- data_card.md
|   |-- leakage_review.md
|   |-- model_card.md
|   |-- reproducibility.md
|   `-- validation_strategy.md
|-- notebooks/
|   `-- 01_eda_modeling.ipynb
|-- reports/
|   |-- business_summary.md
|   |-- figures/
|   `-- metrics/
|-- scripts/
|   |-- evaluate_model.py
|   `-- train_model.py
|-- src/
|   `-- churn_model/
`-- tests/
```

## Limitations

- Dataset provenance and licence are still to be confirmed.
- Prediction timing and prediction window are proposed assumptions.
- Results are from one stratified train/test split, not temporal validation.
- The project does not claim causal business impact.
- The project does not claim ROI or revenue uplift.
- Raw customer-level data should not be committed publicly until licence/provenance is confirmed.
- Model outputs should support human review, not automatic customer treatment.

## Future Improvements

- Confirm dataset provenance and publication rights.
- Add a data source link or public-safe sample dataset.
- Add cross-validation and, if dates become available, temporal validation.
- Add calibration review for probability outputs.
- Add model card and business documentation updates as assumptions mature.
- Build an optional demo using public-safe sample data only.
