# Business Summary

This summary is generated from aggregate Phase 5B evaluation artifacts. It does not include row-level customer predictions and does not claim causal business impact or ROI.

## Controlled Run Context

- Dataset path: `data/telco_churn.csv`
- Rows after cleaning: 7,032
- Non-churn after cleaning: 5,163
- Churn after cleaning: 1,869
- Split: stratified train/test split
- Test size: 0.2
- Random seed: 42

## Model Comparison

Metrics are rounded to 3 decimals.

| Model | ROC-AUC | PR-AUC | Precision | Recall | F1 | Top-Decile Capture |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.836 | 0.622 | 0.492 | 0.797 | 0.608 | 0.262 |
| Random Forest | 0.817 | 0.599 | 0.621 | 0.487 | 0.546 | 0.267 |
| HistGradientBoosting | 0.825 | 0.631 | 0.592 | 0.508 | 0.547 | 0.283 |

Logistic Regression is strongest for ROC-AUC and recall. HistGradientBoosting is strongest for PR-AUC and top-decile capture. Random Forest has the highest precision at the default threshold.

## Business Interpretation

The preferred model depends on the retention strategy:

- Use a higher-recall approach when missing churners is the bigger concern.
- Use a higher-precision or top-decile approach when outreach capacity is limited.
- Review threshold results before deciding how many customers to contact.

## Threshold Trade-Off

Lower thresholds identify more potential churners but increase false positives. Higher thresholds improve precision but may miss more churners.

Threshold selection should consider outreach capacity, intervention cost, customer fatigue, and tolerance for missed churners. No threshold here is final or deployment-ready.

## False Positives And False Negatives

- False positives: customers contacted as likely churners who would not churn. These may create unnecessary cost or customer fatigue.
- False negatives: likely churners missed by the model. These may represent missed retention opportunities.

## Responsible Limitations

The model identifies predictive associations, not causal drivers. Retention actions should be tested carefully before rollout. This project does not claim deployment readiness, assured retention improvement, or validated financial return.
