# Business Churn Prediction Phase 2 Environment Report

Phase: Environment setup  
Date: 2026-05-14  
Scope: dependency files and reproducibility documentation only.

## Summary

Phase 2 added a preliminary Python environment setup for the current notebook-first churn project. The setup is intentionally honest about what is and is not verified: dependencies are constrained using reasonable ranges, but the original notebook environment was not captured and no model training or notebook rerun was performed.

## Files Created

- `requirements.txt`
- `requirements-dev.txt`
- `docs/reproducibility.md`
- `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`

## Files Updated

- `README.md`

## Dependencies Added

Runtime dependencies in `requirements.txt`:

- `numpy>=1.24,<3.0`
- `pandas>=2.0,<3.0`
- `matplotlib>=3.7,<4.0`
- `seaborn>=0.12,<0.14`
- `scikit-learn>=1.3,<2.0`
- `shap>=0.44,<1.0`
- `jupyterlab>=4.0,<5.0`
- `ipykernel>=6.0,<7.0`

Development dependencies in `requirements-dev.txt`:

- `pytest>=8.0,<9.0`
- `pytest-cov>=5.0,<7.0`
- `ruff>=0.6,<1.0`
- `black>=24.0,<26.0`
- `nbqa>=1.8,<2.0`

## Checks Performed

- Read `SKILL.md`, `BUSINESS_CHURN_PROJECT_AUDIT.md`, and `BUSINESS_CHURN_PHASE_1_REPORT.md`.
- Inspected notebook imports without executing notebook cells.
- Inspected the current project file list.
- Verified that the dependency list matches the imports found in the notebook.

## Checks Not Performed

- No package installation was performed.
- No import smoke test was performed.
- No notebook execution was performed.
- No model training or evaluation was performed.
- No metrics were generated or reported.

## Remaining Reproducibility Risks

- The original package versions are unknown.
- Dataset provenance and licence remain unverified.
- The existing notebook still has brittle relative path handling.
- The saved notebook still contains a `FileNotFoundError`.
- There is no source package or CLI pipeline yet.
- There are no tests yet.
- No metrics or figures have been saved from a controlled reproducible run.
- SHAP can be sensitive to dependency versions, so it may need adjustment once imports are checked in a real environment.

## Recommended Phase 3 Next Step

Phase 3 should create the initial source package skeleton under `src/churn_model/` and begin moving reusable, non-training logic out of the notebook. Start with data loading, schema constants, path helpers, feature definitions, and split utilities, then add small tests with fixture data. Do not train models in Phase 3 unless the user explicitly approves a later modelling phase.

