# Business Churn Prediction Phase 5 Model Evaluation Report

Phase: Controlled model/evaluation pipeline  
Date: 2026-05-14  
Scope: pipeline implementation, metrics artifact design, and attempted controlled execution.

## Summary

Phase 5 created a controlled model/evaluation pipeline that implements the Phase 4 leakage and validation decisions in source code. The pipeline is designed to load the local dataset safely, clean `TotalCharges`, create deterministic leakage-safe features, split data with stratification, fit preprocessing only inside model pipelines, compare candidate models, and save aggregate metrics with provenance.

The controlled run could not complete in the current shell because the available Python runtime is missing required dependencies. No metrics were generated or reported.

## Files Created

- `configs/train_config.yaml`
- `src/churn_model/train.py`
- `scripts/train_model.py`
- `scripts/evaluate_model.py`
- `tests/test_evaluate.py`
- `tests/test_train.py`
- `BUSINESS_CHURN_PHASE_5_MODEL_EVAL_REPORT.md`

## Files Updated

- `requirements.txt`
- `src/churn_model/data.py`
- `src/churn_model/evaluate.py`
- `README.md`

## Files Removed

- `configs/.gitkeep`
- `scripts/.gitkeep`

These placeholder files were replaced by real config and script files.

## Pipeline Design

The Phase 5 pipeline is configured through `configs/train_config.yaml` and can be run with:

```bash
python scripts/train_model.py --config configs/train_config.yaml
```

Design choices:

- load only the local CSV specified in the config
- validate expected raw columns
- clean `TotalCharges`
- drop rows with missing `TotalCharges` when configured
- create deterministic row-level features only
- use observed revenue-to-date wording instead of true future CLTV
- exclude `customerID` and `Churn` from model features
- avoid full-dataset `pd.qcut`
- use stratified train/test split
- fit one-hot encoding inside each scikit-learn pipeline
- save aggregate metrics only
- avoid row-level prediction dumps

## Models Configured For Evaluation

The pipeline compares:

- Logistic Regression baseline
- Random Forest
- HistGradientBoostingClassifier

Model quality should not be overclaimed. Final interpretation should consider multiple metrics and threshold trade-offs, not only a single headline score.

## Metrics Designed For Output

When the controlled run succeeds, the pipeline is designed to save:

- `reports/metrics/model_metrics.json`
- `reports/metrics/threshold_metrics.csv`
- `reports/metrics/model_comparison.csv`

The metrics JSON includes provenance:

- run date/time
- dataset path
- row count after cleaning
- target distribution after cleaning
- split method
- test size
- random seed
- model names
- selected threshold policy
- command used
- public-safety note

## Figures Designed For Output

When the controlled run succeeds, the pipeline is designed to save aggregate comparison figures under `reports/figures/`:

- ROC-AUC comparison
- PR-AUC comparison
- churn-class recall comparison

No figures were generated in this Phase 5 run attempt because execution failed before training.

## Tests Added

Added synthetic-data tests for:

- threshold prediction helpers
- threshold metrics
- probability evaluation helpers
- top-fraction capture
- pipeline construction
- target and identifier exclusion before modelling

Tests do not require the real customer CSV.

## Checks Performed

- Read `SKILL.md`.
- Read `BUSINESS_CHURN_PROJECT_AUDIT.md`.
- Read `BUSINESS_CHURN_PHASE_1_REPORT.md`.
- Read `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`.
- Read `BUSINESS_CHURN_PHASE_3_SOURCE_REPORT.md`.
- Read `BUSINESS_CHURN_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`.
- Inspected current source package, docs, tests, config, scripts, and reports folders.
- Used the bundled Python runtime path provided by the workspace.
- Attempted to run `python -m pytest` with the bundled Python runtime.
- Attempted to run `python scripts/train_model.py --config configs/train_config.yaml` with the bundled Python runtime.
- Checked core imports with the bundled Python runtime.

## Checks Not Performed

- No model training completed.
- No model evaluation completed.
- No metrics were generated.
- No figures were generated.
- No row-level predictions were saved.
- No notebook execution was performed.
- No package installation was performed.
- No Git initialisation, commit, or push was performed.

## Execution Results

Test execution did not run because `pytest` is not installed in the bundled Python runtime:

```text
No module named pytest
```

The controlled training command did not run because `PyYAML` is not installed:

```text
ModuleNotFoundError: No module named 'yaml'
```

A core import check also showed that `scikit-learn` is not installed:

```text
ModuleNotFoundError: No module named 'sklearn'
```

Because the environment is missing required dependencies, no Phase 5 metric artifacts were created. This is intentional: metrics must only be reported after a controlled run succeeds and saves artifacts under `reports/metrics/`.

## Metrics Generated And Saved

None.

Expected future output paths after dependencies are installed:

- `reports/metrics/model_metrics.json`
- `reports/metrics/threshold_metrics.csv`
- `reports/metrics/model_comparison.csv`

## Figures Generated And Saved

None.

Expected future output paths after dependencies are installed:

- `reports/figures/roc_auc_comparison.png`
- `reports/figures/pr_auc_comparison.png`
- `reports/figures/recall_churn_class_comparison.png`

## Remaining Risks

- The controlled pipeline has not yet been executed successfully.
- Tests have not been executed in a fully configured environment.
- Dataset provenance and licence remain unverified.
- Prediction moment and prediction window remain proposed assumptions.
- The existing notebook still contains the saved path error and notebook-only modelling code.
- The pipeline needs a dependency-installed Python environment before metrics can be generated.
- Future metrics must be reviewed for leakage, threshold policy, and business interpretation before being presented prominently.

## Recommended Phase 6 Next Step

Before Phase 6 portfolio documentation, install dependencies in a project virtual environment and run:

```bash
python -m pip install -r requirements-dev.txt
pytest
python scripts/train_model.py --config configs/train_config.yaml
```

Only after the controlled run succeeds should Phase 6 update the README, model card, and business summary with saved metrics from `reports/metrics/`. If execution remains blocked, Phase 6 should focus on documentation structure and clearly state that metrics are pending.

