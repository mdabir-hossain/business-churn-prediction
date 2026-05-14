# Business Churn Prediction Phase 1 Report

Phase: Repository hygiene and public safety  
Date: 2026-05-14  
Scope: public-safety scaffold, initial documentation, and folder structure only.

## Summary

Phase 1 created a safer project scaffold for a UK job-ready churn prediction portfolio project. The existing notebook and CSV were preserved exactly as requested. No Git repository was initialised, no commits were made, and no models were trained or rerun.

## Files Created

- `.gitignore`
- `README.md`
- `data/README.md`
- `docs/leakage_review.md`
- `BUSINESS_CHURN_PHASE_1_REPORT.md`
- `configs/.gitkeep`
- `data/sample/.gitkeep`
- `reports/figures/.gitkeep`
- `reports/metrics/.gitkeep`
- `scripts/.gitkeep`
- `src/churn_model/.gitkeep`
- `tests/.gitkeep`

## Folders Created

- `configs/`
- `docs/`
- `reports/`
- `reports/figures/`
- `reports/metrics/`
- `src/`
- `src/churn_model/`
- `scripts/`
- `tests/`
- `data/sample/`

## Files Intentionally Not Changed

- `data/telco_churn.csv`
- `notebooks/01_eda_modeling.ipynb`
- `BUSINESS_CHURN_PROJECT_AUDIT.md`
- `SKILL.md`

## Public-Safety Decisions

- Raw customer-level CSV files are ignored by default in `.gitignore`.
- `data/telco_churn.csv` is treated as local-only until dataset provenance and licence are confirmed.
- `customerID` is flagged as an identifier that should be handled carefully.
- `data/sample/` is reserved for future public-safe sample or synthetic data.
- Model artifacts, prediction outputs, local secrets, virtual environments, Python caches, and notebook checkpoints are ignored by default.
- README language avoids model performance claims because no saved metrics were found in the audit.

## Remaining Risks

- Dataset provenance and licence are still unverified.
- The project still has no verified dependency file.
- The notebook still contains a saved data-path `FileNotFoundError`.
- No model metrics have been generated or saved in a controlled reproducible run.
- Prediction timing and prediction window are still to be confirmed.
- Full-dataset `pd.qcut` remains a known leakage risk in the existing notebook.
- The project is still notebook-first and has no source package implementation yet.
- Tests have not been implemented yet.

## Recommended Phase 2 Next Step

Phase 2 should focus on environment setup:

1. Add `requirements.txt`, `requirements-dev.txt`, or `pyproject.toml`.
2. Pin or constrain core dependencies.
3. Document setup commands for a fresh local environment.
4. Verify imports only if the user approves running environment checks.
5. Save findings in `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`.

