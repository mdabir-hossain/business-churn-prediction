# Reproducibility

## Status

Phase 5B successfully ran tests and the controlled training/evaluation command in a local virtual environment. The project now saves aggregate metrics and figures, but it is still a portfolio project and not a deployed system.

## Environment Setup

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Windows PowerShell activation is:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by execution policy, use an approved local development workflow and document it before running the pipeline.

## Test Command

```powershell
pytest
```

Phase 5B result:

```text
10 passed, 1 warning
```

The warning related to pytest cache writing and did not affect test results.

## Controlled Training Command

```powershell
python scripts/train_model.py --config configs/train_config.yaml
```

This command:

- loads the local CSV
- applies safe deterministic feature helpers
- excludes `customerID` and `Churn` from features
- fits preprocessing inside model pipelines
- evaluates candidate models
- saves aggregate metrics only

## Generated Artifacts

Metrics:

- `reports/metrics/model_metrics.json`
- `reports/metrics/model_comparison.csv`
- `reports/metrics/threshold_metrics.csv`

Figures:

- `reports/figures/roc_auc_comparison.png`
- `reports/figures/pr_auc_comparison.png`
- `reports/figures/recall_churn_class_comparison.png`

Business summary:

- `reports/business_summary.md`

## Data Path Expectations

The controlled pipeline expects:

```text
data/telco_churn.csv
```

The raw dataset should remain local unless provenance and licence are confirmed.

## Current Reproducibility Limitations

- Dataset provenance and licence remain to be confirmed.
- The original notebook still contains a saved path error and should be treated as exploratory.
- Metrics are from one controlled stratified train/test split.
- Temporal validation is not available without date fields.
- No lock file is currently provided.

