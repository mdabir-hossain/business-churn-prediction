# Business Churn Prediction Phase 4 Leakage And Validation Report

Phase: Leakage and validation hardening  
Date: 2026-05-14  
Scope: documentation-first leakage and validation design before controlled model evaluation.

## Summary

Phase 4 strengthened the project's leakage and validation design. The work documented a proposed prediction setup, created a field-by-field availability review, clarified known leakage risks, and added a validation strategy for later controlled evaluation.

No notebook cells were executed, no models were trained, and no metrics were generated or reported.

## Files Created

- `docs/validation_strategy.md`
- `BUSINESS_CHURN_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`

## Files Updated

- `docs/leakage_review.md`
- `src/churn_model/config.py`
- `README.md`

## Key Leakage Decisions

- `Churn` is the target and must never enter features.
- `customerID` is an identifier and should be excluded from modelling and public row-level outputs.
- Full-dataset `pd.qcut` before train/test split is a leakage risk.
- `TotalCharges` and `tenure` may be valid only if known at the scoring moment.
- The notebook's `CLTV = MonthlyCharges * tenure` should be described as observed revenue-to-date, not true future customer lifetime value.
- Learned transformations should be fitted only on training data or training folds.
- Demographic fields such as `gender` and `SeniorCitizen` require responsible-use review before final modelling.

## Validation Design Decisions

- The proposed prediction moment is scoring active customers at the end of a billing cycle before the future churn outcome.
- The proposed prediction window is the next billing period or near-term retention window.
- The current single stratified train/test split is treated as an early baseline, not a complete validation strategy.
- Stratification remains useful because churn is imbalanced.
- Stratified cross-validation may be added for more stable model comparison.
- Temporal validation would be more realistic if event dates become available.
- Accuracy alone is not sufficient for churn modelling.
- Future metrics should include ROC-AUC, PR-AUC, churn-class precision/recall/F1, confusion matrix, lift/gains, calibration, and threshold/cost analysis.
- Threshold selection should be business-aware and reflect retention capacity, intervention cost, customer fatigue, and false-positive/false-negative trade-offs.

## Source Updates

Small safe constants were added to `src/churn_model/config.py`:

- `EXCLUDED_IDENTIFIER_COLUMNS`
- `SAFE_FEATURE_EXCLUSIONS`
- `PROPOSED_PREDICTION_MOMENT`
- `PROPOSED_PREDICTION_WINDOW`

These constants document intended exclusions and proposed validation assumptions. They do not execute modelling.

## Tests Added Or Not Added

No new tests were added in Phase 4. Phase 3 already added synthetic-data tests covering target and identifier exclusion logic. Test execution is still pending because the current shell does not have `python`, `py`, or `pytest` available.

## Checks Performed

- Read `SKILL.md`.
- Read `BUSINESS_CHURN_PROJECT_AUDIT.md`.
- Read `BUSINESS_CHURN_PHASE_1_REPORT.md`.
- Read `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`.
- Read `BUSINESS_CHURN_PHASE_3_SOURCE_REPORT.md`.
- Inspected current docs and `src/churn_model/` files.
- Verified that changes remained documentation-first and did not require the real customer CSV.

## Checks Not Performed

- No package installation was performed.
- No tests were executed.
- No notebook execution was performed.
- No model training was performed.
- No model evaluation was performed.
- No metrics were generated or reported.
- No Git commands were used to initialise, commit, or push.

## Remaining Risks

- Leakage is not fully solved until the design is implemented in the training/evaluation pipeline.
- Prediction moment and prediction window remain proposed assumptions, not confirmed business truth.
- Dataset provenance and licence remain unverified.
- The existing notebook still contains the original full-dataset feature engineering pattern.
- The existing notebook still contains the saved data-path `FileNotFoundError`.
- The project does not yet have a controlled model evaluation pipeline.
- Tests still need to be executed in a configured Python environment.

## Recommended Phase 5 Next Step

Phase 5 should build a controlled model/evaluation pipeline that implements the leakage and validation decisions documented here. It should fit preprocessing only on training data, avoid full-dataset learned transformations, save metrics with provenance, and include threshold-aware evaluation. Metrics should be reported only after a controlled run creates saved artifacts under `reports/metrics/`.

