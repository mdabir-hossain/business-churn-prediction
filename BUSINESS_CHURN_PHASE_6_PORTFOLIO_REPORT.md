# Business Churn Prediction Phase 6 Portfolio Report

Phase: Business and recruiter documentation  
Date: 2026-05-14  
Scope: GitHub-ready documentation using saved controlled metrics only.

## Files Created

- `docs/model_card.md`
- `docs/data_card.md`
- `docs/business_context.md`
- `BUSINESS_CHURN_PHASE_6_PORTFOLIO_REPORT.md`

## Files Updated

- `README.md`
- `docs/reproducibility.md`
- `reports/business_summary.md`

## Metrics Surfaced

Only saved Phase 5B artifacts from `reports/metrics/` were used.

Surfaced rounded metrics:

- Logistic Regression: ROC-AUC 0.836, PR-AUC 0.622, precision 0.492, recall 0.797, F1 0.608, top-decile capture 0.262
- Random Forest: ROC-AUC 0.817, PR-AUC 0.599, precision 0.621, recall 0.487, F1 0.546, top-decile capture 0.267
- HistGradientBoosting: ROC-AUC 0.825, PR-AUC 0.631, precision 0.592, recall 0.508, F1 0.547, top-decile capture 0.283

No invented metrics were added.

## Figures Referenced

- `reports/figures/roc_auc_comparison.png`
- `reports/figures/pr_auc_comparison.png`
- `reports/figures/recall_churn_class_comparison.png`

No figures were regenerated in Phase 6.

## Documentation Improvements

- Rewrote the README for recruiter readability and GitHub review.
- Added a model card covering intended use, non-intended use, validation, metrics, threshold trade-offs, and responsible-use notes.
- Added a data card covering provenance status, schema, target definition, identifier handling, and public-safety constraints.
- Added business context documentation covering stakeholders, workflow, false positives/false negatives, and threshold decisions.
- Updated reproducibility instructions with the successful Phase 5B commands and generated artifact paths.
- Updated business summary with concise saved metrics and non-causal interpretation.

## Public-Safety Decisions

- Raw/customer-level data remains local-only until provenance and licence are confirmed.
- `customerID` is treated as an identifier and excluded from features.
- No row-level predictions are published.
- Documentation points to aggregate metrics only.
- Customer-level CSV files remain ignored by default.

## Remaining Risks

- Dataset provenance and licence remain unverified.
- Prediction timing and prediction window remain proposed assumptions.
- Results are based on one controlled stratified train/test split.
- Temporal validation is not available without date fields.
- No causal or ROI claims are supported.
- The exploratory notebook still contains a saved path error.

## Public GitHub Review Readiness

The project is ready for public GitHub review from a documentation and aggregate-results perspective, provided the raw customer-level CSV is not committed publicly until provenance and licence are confirmed.

Recommended before publishing:

- verify `.gitignore` behaviour before adding files
- confirm whether `data/telco_churn.csv` can be redistributed
- consider adding a public-safe sample dataset if full data cannot be shared
- review README rendering on GitHub

## Recommended Next Step

Proceed to a public-safety Git review: inspect ignored files, decide whether the raw CSV should remain local-only, and prepare a clean commit only after confirming no customer-level data or private artifacts are staged.

