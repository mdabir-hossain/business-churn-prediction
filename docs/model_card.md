# Model Card

## Model Overview

This model card documents the controlled Phase 5B churn evaluation for a portfolio project. It is not a production retention system.

Model candidates evaluated:

- Logistic Regression
- Random Forest
- HistGradientBoostingClassifier

All results are from saved aggregate artifacts in `reports/metrics/`.

## Intended Use

The project is intended to demonstrate leakage-aware churn modelling, validation design, model comparison, threshold trade-off thinking, and responsible business interpretation.

Suitable uses:

- portfolio review
- technical interview discussion
- model evaluation walkthrough
- retention decision-support prototype discussion

## Non-Intended Use

Do not use this project for:

- automatic customer treatment
- live customer decisioning
- production retention targeting
- causal claims about why customers churn
- ROI or revenue-impact claims without explicit assumptions and validation

## Dataset Summary

Controlled Phase 5B run:

- Dataset path: `data/telco_churn.csv`
- Rows after cleaning: 7,032
- Non-churn after cleaning: 5,163
- Churn after cleaning: 1,869
- Target column: `Churn`
- Identifier column: `customerID`

Dataset provenance and licence remain to be confirmed.

## Proposed Prediction Setup

The current setup assumes customers are scored at the end of a billing cycle using information available before a future churn outcome. The prediction window is assumed to be the next billing period or near-term retention window.

These are proposed assumptions, not confirmed business truth.

## Validation Method

The controlled run used:

- stratified train/test split
- test size 0.2
- random seed 42
- preprocessing fitted inside model pipelines
- aggregate metrics only

No row-level predictions were published.

## Saved Metrics Summary

Metrics are rounded to 3 decimals.

| Model | ROC-AUC | PR-AUC | Precision | Recall | F1 | Top-Decile Capture |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.836 | 0.622 | 0.492 | 0.797 | 0.608 | 0.262 |
| Random Forest | 0.817 | 0.599 | 0.621 | 0.487 | 0.546 | 0.267 |
| HistGradientBoosting | 0.825 | 0.631 | 0.592 | 0.508 | 0.547 | 0.283 |

Logistic Regression is strongest for ROC-AUC and churn recall. HistGradientBoosting is strongest for PR-AUC and top-decile capture. Random Forest has the highest default-threshold precision. The preferred model depends on retention strategy.

## Threshold Considerations

Threshold selection should reflect:

- retention budget
- outreach capacity
- intervention cost
- customer fatigue
- tolerance for false positives
- tolerance for missed churners

Lower thresholds generally improve recall and increase false positives. Higher thresholds generally improve precision and miss more churners.

## False Positives And False Negatives

False positives are customers contacted as likely churners who would not churn. They may create unnecessary cost or customer fatigue.

False negatives are likely churners missed by the model. They may represent missed retention opportunities.

## Explainability Status

The original notebook includes SHAP exploration for a logistic model, but Phase 5B did not regenerate explainability artifacts. Current controlled outputs focus on aggregate model metrics and threshold analysis.

Future work should add saved, public-safe explainability summaries and avoid causal interpretation.

## Limitations

- Dataset provenance/licence is unconfirmed.
- Prediction timing and window are proposed assumptions.
- Evaluation uses a stratified random split, not temporal validation.
- Metrics come from one controlled run.
- No calibration analysis is currently surfaced.
- No row-level predictions are published.
- Model outputs should support human decision-making only.

## Responsible-Use Notes

Recommendations should be framed as prioritisation ideas. Do not claim that any feature is the reason customers churn. Any retention intervention should be reviewed, tested, and monitored before business rollout.
