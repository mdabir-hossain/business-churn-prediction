# Business Churn Prediction Public GitHub Review

Review date: 2026-05-14  
Project path: `F:\Business churn prediction`  
Scope: final public-safety Git review before any manual Git initialisation or GitHub publication.

## Executive Verdict

Verdict: **Yes, conditionally ready for public GitHub review**.

The project is safe to initialise and publish **only if the existing `.gitignore` is kept in place and ignored/private files are not force-added**. The raw customer-level dataset remains present locally at `data/telco_churn.csv`, but it is covered by the current ignore rules and should not be committed unless dataset provenance, licence, and redistribution rights are confirmed.

No Git repository was initialised during this review. No files were committed or pushed.

## Project Structure Inspected

Public-facing project files now include:

- `README.md`
- `SKILL.md`
- `.gitignore`
- `requirements.txt`
- `requirements-dev.txt`
- `configs/train_config.yaml`
- `data/README.md`
- `data/sample/.gitkeep`
- `docs/`
- `notebooks/01_eda_modeling.ipynb`
- `reports/business_summary.md`
- `reports/figures/`
- `reports/metrics/`
- `scripts/`
- `src/churn_model/`
- `tests/`
- phase and audit reports

Local/private or generated files also exist:

- `data/telco_churn.csv`
- `.venv/`
- `.pytest_cache/`
- `src/churn_model/__pycache__/`
- `tests/__pycache__/`

These local/generated items are covered by `.gitignore` patterns and should remain untracked.

## Safe-To-Publish Files And Folders

Safe to publish after final manual staging review:

- `.gitignore`
- `README.md`
- `SKILL.md`
- `requirements.txt`
- `requirements-dev.txt`
- `configs/train_config.yaml`
- `data/README.md`
- `data/sample/.gitkeep`
- `docs/`
- `notebooks/01_eda_modeling.ipynb`
- `reports/business_summary.md`
- `reports/metrics/model_metrics.json`
- `reports/metrics/model_comparison.csv`
- `reports/metrics/threshold_metrics.csv`
- `reports/figures/roc_auc_comparison.png`
- `reports/figures/pr_auc_comparison.png`
- `reports/figures/recall_churn_class_comparison.png`
- `scripts/`
- `src/churn_model/`
- `tests/`
- `BUSINESS_CHURN_PROJECT_AUDIT.md`
- `BUSINESS_CHURN_PHASE_1_REPORT.md`
- `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`
- `BUSINESS_CHURN_PHASE_3_SOURCE_REPORT.md`
- `BUSINESS_CHURN_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`
- `BUSINESS_CHURN_PHASE_5_MODEL_EVAL_REPORT.md`
- `BUSINESS_CHURN_PHASE_5B_EXECUTION_REPORT.md`
- `BUSINESS_CHURN_PHASE_6_PORTFOLIO_REPORT.md`
- `BUSINESS_CHURN_PUBLIC_GITHUB_REVIEW.md`

The saved metrics and figures are aggregate artifacts only. They do not contain row-level predictions or customer-level records, so they are suitable for public portfolio documentation.

## Files And Folders That Must Remain Private Or Ignored

Must not be committed unless explicitly reviewed and approved:

- `data/telco_churn.csv`
- any future full customer-level CSV files
- `data/raw/`
- `data/interim/`
- `data/processed/`
- prediction dumps such as `predictions/` or `reports/predictions/`
- trained model artifacts under `models/`
- `*.pkl`, `*.pickle`, `*.joblib`, `*.onnx`
- `.env` and `.env.*`
- credential files, keys, PEM files, or service account JSON files
- `.venv/`, `venv/`, `env/`
- `.pytest_cache/`
- `__pycache__/`
- `.ipynb_checkpoints/`
- editor and OS files such as `.vscode/`, `.idea/`, `.DS_Store`, and `Thumbs.db`

## `.gitignore` Verdict

Verdict: **fit for public-safety use**.

The current `.gitignore` includes the important protections:

- `data/*.csv`
- `data/**/*.csv`
- `data/raw/`
- `data/interim/`
- `data/processed/`
- prediction outputs
- model artifacts
- local secrets
- Python caches
- virtual environments
- notebook checkpoints
- OS/editor files

`data/telco_churn.csv` would be ignored by the `data/*.csv` rule after Git is initialised. `git check-ignore` could not be run live because this folder is intentionally not currently a Git repository, but the pattern match is direct and unambiguous.

Important staging warning: do not use `git add -f` on `data/telco_churn.csv` or any ignored private artifact.

## Unsafe File Scan

Findings:

- Raw CSV found: `data/telco_churn.csv`
- Row-level prediction files found: none
- Model artifact files found outside `.venv/`: none
- `.env` files found outside `.venv/`: none
- credential/key/service account files found outside `.venv/`: none
- notebook checkpoint folders found: none
- virtual environment folder found: `.venv/`
- cache folders found: `.pytest_cache/`, `src/churn_model/__pycache__/`, `tests/__pycache__/`

The raw CSV, virtual environment, and caches should remain local-only and ignored.

## Documentation Claim Review

Reviewed documentation and reports for unsupported phrases:

- `production-ready`
- `proven ROI`
- `causes churn`
- `guaranteed retention`
- `automated customer decisioning`
- `real-time deployment`

No unsupported matches were found in the reviewed public-facing documentation.

The documentation remains appropriately cautious:

- dataset provenance/licence are still marked as to be confirmed
- prediction timing and prediction window are described as proposed assumptions
- results are described as coming from one controlled stratified train/test split
- causal claims are avoided
- ROI and revenue impact are not claimed
- no row-level predictions are published
- raw customer-level data is described as local-only unless publication rights are confirmed

## Generated Metrics And Figures Review

Safe aggregate metrics:

- `reports/metrics/model_metrics.json`
- `reports/metrics/model_comparison.csv`
- `reports/metrics/threshold_metrics.csv`

Safe aggregate figures:

- `reports/figures/roc_auc_comparison.png`
- `reports/figures/pr_auc_comparison.png`
- `reports/figures/recall_churn_class_comparison.png`

These files are suitable for public GitHub publication because they contain aggregate model evaluation outputs, not row-level customer data or prediction dumps.

## Remaining Risks

- Dataset provenance and licence remain unverified.
- `data/telco_churn.csv` is still physically present in the local project folder, so manual staging must be checked carefully.
- The notebook is publishable as an exploratory artifact, but it still contains an earlier saved path error from the initial project state.
- Results are based on one controlled stratified split, not cross-validation or temporal validation.
- Prediction timing and prediction window remain proposed assumptions.
- A `LICENSE` file is not currently present; add one before public release if you want clear reuse terms.
- Public-safe sample data has not yet been created.

## Recommended Manual Git Commands

Run these manually only when ready. These commands are recommendations; they were not run during this review.

```powershell
git init
```

Check ignored files before staging:

```powershell
git status --short --ignored
git check-ignore -v data/telco_churn.csv
git check-ignore -v .venv/pyvenv.cfg
git check-ignore -v .pytest_cache/
```

Stage only safe project files:

```powershell
git add .gitignore README.md SKILL.md requirements.txt requirements-dev.txt
git add configs/train_config.yaml
git add data/README.md data/sample/.gitkeep
git add docs
git add notebooks/01_eda_modeling.ipynb
git add reports/business_summary.md reports/metrics reports/figures
git add scripts src tests
git add BUSINESS_CHURN_PROJECT_AUDIT.md
git add BUSINESS_CHURN_PHASE_1_REPORT.md BUSINESS_CHURN_PHASE_2_ENV_REPORT.md BUSINESS_CHURN_PHASE_3_SOURCE_REPORT.md
git add BUSINESS_CHURN_PHASE_4_LEAKAGE_VALIDATION_REPORT.md BUSINESS_CHURN_PHASE_5_MODEL_EVAL_REPORT.md
git add BUSINESS_CHURN_PHASE_5B_EXECUTION_REPORT.md BUSINESS_CHURN_PHASE_6_PORTFOLIO_REPORT.md
git add BUSINESS_CHURN_PUBLIC_GITHUB_REVIEW.md
```

Review what would be committed:

```powershell
git status --short
git diff --cached --stat
git diff --cached --name-only
```

Confirm raw/private files are not staged:

```powershell
git status --short --ignored
```

Only after confirming no raw data, cache folders, virtual environments, secrets, model artifacts, or row-level predictions are staged:

```powershell
git commit -m "Prepare public-safe churn prediction portfolio"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Final Verdict

Final verdict: **Yes, conditionally safe to publish**.

The repository is public-safe from a documentation, source-code, aggregate-metrics, and `.gitignore` perspective. The main condition is strict: **do not commit `data/telco_churn.csv` or any other customer-level/raw data until provenance, licence, and redistribution rights are confirmed**.

Before pushing to GitHub, perform a manual staging review with `git status --short --ignored` and `git diff --cached --name-only`.
