# Business Churn Prediction Phase 3 Source Report

Phase: Source package skeleton  
Date: 2026-05-14  
Scope: safe reusable helpers, initial package structure, and synthetic-data tests.

## Summary

Phase 3 created the initial `src/churn_model/` Python package skeleton and added small tests using synthetic fixture data only. The work extracted safe reusable logic from the existing notebook, including data loading, schema checks, feature helpers, path helpers, and stratified splitting. No notebook cells were executed, no model training was performed, and no metrics were generated.

## Files Created

- `src/churn_model/__init__.py`
- `src/churn_model/config.py`
- `src/churn_model/data.py`
- `src/churn_model/features.py`
- `src/churn_model/split.py`
- `src/churn_model/evaluate.py`
- `src/churn_model/paths.py`
- `tests/test_data.py`
- `tests/test_features.py`
- `tests/test_split.py`
- `BUSINESS_CHURN_PHASE_3_SOURCE_REPORT.md`

## Files Updated

- `README.md`
- `docs/reproducibility.md`

## Files Removed

- `src/churn_model/.gitkeep`
- `tests/.gitkeep`

These placeholder files were replaced by real package and test files.

## Logic Extracted

Safe reusable logic added:

- project constants for target, identifier, data paths, service columns, and random state
- portable project-root path helpers
- local CSV loading helper that does not download data or print records
- required-column validation helpers
- `TotalCharges` numeric cleaning
- service-count feature helper
- autopay flag helper
- fibre service flag helper
- senior-alone flag helper
- observed revenue-to-date helper, avoiding misleading future CLTV language
- target/features splitting that excludes target and identifier columns
- stratified train/test split helper
- lightweight evaluation helper functions for future controlled evaluation phases

The full-dataset `pd.qcut` pattern from the notebook was not made a default safe transformation. It is included only as an explicitly experimental helper with leakage-warning documentation.

## Tests Added

The new tests use small synthetic data only. They verify:

- required columns can be detected
- missing required columns raise a clear error
- `TotalCharges` cleaning converts invalid values to missing
- feature helpers do not require the real customer CSV
- target and identifier columns are excluded from features
- stratified split returns expected shapes and preserves classes

## Checks Performed

- Read `SKILL.md`, `BUSINESS_CHURN_PROJECT_AUDIT.md`, `BUSINESS_CHURN_PHASE_1_REPORT.md`, and `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`.
- Inspected the existing notebook logic without executing notebook cells.
- Inspected the current project structure.
- Created package files and tests with synthetic fixtures only.
- Attempted to run `pytest`, but the command was not available in the current shell.
- Attempted to run `python -m pytest`, but `python` was not available in the current shell.
- Checked for `python`, `py`, and `pytest` commands; none were found on PATH.

## Checks Not Performed

- No model training was performed.
- No model evaluation was performed.
- No metrics were generated or reported.
- No notebook execution was performed.
- No package installation was performed.
- Tests were not executed because Python/pytest were not available in the current shell.

## Remaining Risks

- The source package is still a skeleton, not a complete modelling pipeline.
- The notebook remains the main end-to-end workflow for now.
- Dataset provenance and licence remain unverified.
- Prediction timing and prediction window remain to be confirmed.
- Leakage hardening is not complete.
- The real CSV path issue in the notebook has not been changed.
- Tests currently cover helper behaviour only, using synthetic fixtures.
- Test execution still needs to be performed after a Phase 2 environment is created and activated.

## Recommended Phase 4 Next Step

Phase 4 should focus on leakage and validation hardening. Define the prediction moment and prediction window, classify each field by scoring-time availability, decide how to handle `TotalCharges`, `tenure`, and observed revenue-to-date, and move learned transformations into train-only pipelines or avoid them. Save the findings in `BUSINESS_CHURN_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`.
