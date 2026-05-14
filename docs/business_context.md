# Business Context

## Stakeholders

Potential stakeholders for this churn project:

- retention marketing
- customer success
- commercial leadership
- finance or revenue operations
- product/service teams

The model is designed for decision support, not automatic customer treatment.

## Churn Definition And Prediction Setup

The project uses `Churn` as the supervised target. The exact business definition is to be confirmed.

Proposed setup:

- Prediction moment: end of billing cycle before future churn outcome
- Prediction window: next billing period or near-term retention window
- Scoring population: active customers with account, service, and billing data available before the outcome

These are assumptions for portfolio development and should be updated if business documentation becomes available.

## Retention Decision Workflow

A safe decision-support workflow could be:

1. Score active customers using the controlled pipeline.
2. Review aggregate model performance and threshold trade-offs.
3. Select an outreach threshold based on retention capacity and acceptable false-positive volume.
4. Prioritise customers for human-reviewed retention outreach.
5. Track intervention outcomes separately before making business-impact claims.

No row-level prediction outputs are published in this repository.

## Model Trade-Offs

Phase 5B controlled results show:

- Logistic Regression is strongest for ROC-AUC and churn recall.
- HistGradientBoosting is strongest for PR-AUC and top-decile capture.
- Random Forest has the highest default-threshold precision.

The preferred model depends on the strategy. A team focused on broad churn capture may prefer higher recall. A team with limited outreach capacity may prefer stronger precision or top-decile ranking.

## False Positives And False Negatives

False positives:

- customers flagged as likely churners who would not churn
- may create unnecessary outreach cost, discount leakage, or fatigue

False negatives:

- likely churners missed by the model
- may represent missed retention opportunities

## Threshold And Cost Trade-Offs

Lower thresholds usually capture more churners but increase false positives. Higher thresholds usually improve precision but miss more churners.

Threshold choice should depend on:

- retention budget
- outreach capacity
- intervention cost
- customer fatigue risk
- customer value
- tolerance for missed churners

No threshold in this project is final or deployment-ready.

## Responsible Recommendations

Safe wording:

- "Customers in this segment are associated with higher churn risk."
- "This segment may be useful for prioritising retention outreach."
- "This pattern should be tested before rollout."

Avoid:

- "This feature is the reason customers leave."
- "This intervention will reduce churn."
- "This model proves ROI."

## Business Limitations

- No causal experiment has been run.
- No ROI model is included.
- Dataset provenance is not confirmed.
- Prediction timing remains an assumption.
- Metrics come from one controlled train/test split.
- Retention actions should be tested before rollout.
