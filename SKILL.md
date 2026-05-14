---
name: business-churn-portfolio
description: Use this skill every time Codex or an AI agent is asked to review, audit, improve, restructure, document, make public-safe, or prepare the Business Churn Prediction project for GitHub, job applications, interviews, demos, or portfolio presentation. Applies to repository hygiene, data safety, reproducibility, leakage-aware ML validation, churn modelling, business interpretation, recruiter-friendly documentation, and phased project upgrades.
---

# Business Churn Portfolio Skill

## What This Skill Is For

Use this skill whenever working on the Business Churn Prediction portfolio project. It guides reviews, audits, improvements, restructuring, documentation, GitHub preparation, interview preparation, and demo preparation.

Operate as a senior data scientist, machine learning engineer, business analytics reviewer, technical writer, and GitHub portfolio maintainer. Keep the work professional, reproducible, recruiter-friendly, technically credible, business-focused, and public-safe.

## What This Project Is

This is a customer churn prediction portfolio project. It should demonstrate:

- machine learning modelling
- leakage-aware validation
- responsible feature engineering
- explainability
- threshold and cost trade-off thinking
- business interpretation for retention decisions
- reproducible engineering practices
- public-safe GitHub presentation

This is not a production retention system. Do not describe it as production-ready unless a future implementation genuinely supports that claim.

## Current Project State

The completed audit is saved as `BUSINESS_CHURN_PROJECT_AUDIT.md`. Read it before major work.

Audit findings:

- The project currently has one raw-looking CSV: `data/telco_churn.csv`.
- The project currently has one notebook: `notebooks/01_eda_modeling.ipynb`.
- The folder is not currently a Git repository.
- There is no README.
- There is no `.gitignore`.
- There are no requirements or environment files.
- There are no saved metric artifacts.
- There are no saved figures or reports beyond the audit report.
- There is no source package.
- There are no tests.
- The notebook has a saved `FileNotFoundError` for `../data/telco_churn.csv`.
- The workflow is notebook-only.
- Raw customer-level data is present and needs provenance/licence review before public release.

The notebook appears to contain EDA, feature engineering, stratified train/test split, logistic regression, random forest, histogram gradient boosting, ROC-AUC code, classification report code, confusion matrix code, and SHAP code. Do not report any metric values unless they exist in saved outputs or are generated in a controlled approved phase.

## Non-Negotiable Safety Rules

- Do not publish raw customer-level data unless licence and provenance are confirmed.
- Treat `customerID` carefully, even if the dataset is public or synthetic.
- Do not commit private, sensitive, customer-level, credential, or secret data.
- Do not invent metrics.
- Do not invent ROI, revenue impact, retention impact, or business impact.
- Do not overclaim causal effects from predictive models.
- Do not silently include target, post-outcome, cancellation-derived, or scoring-time-unavailable fields.
- Do not initialise Git, commit, push, delete, move, or destructively overwrite files unless the user explicitly asks.
- Work phase by phase.
- Preserve user work and existing files.
- Make uncertainty explicit.
- Label all metrics with provenance.
- Keep recommendations evidence-linked and responsibly worded.

## Public-Safety And Data Rules

Treat these as private or ignored by default unless the user explicitly approves publication and provenance is clear:

- `data/raw/`
- `data/interim/`
- `data/processed/`
- full customer-level CSV files
- row-level prediction dumps
- trained model artifacts unless intentionally released
- `.env` files
- API keys, credentials, and service account files
- cache folders
- virtual environments
- local notebook checkpoints

Prefer a public-safe strategy:

- Keep raw data out of Git until licence/provenance is verified.
- Add `data/README.md` explaining source, licence, schema, and access.
- Use `data/sample/` for public-safe sample or synthetic data.
- Remove or transform `customerID` from any published row-level derived files.
- Avoid publishing row-level predictions unless anonymised, sampled, and documented.

## Recommended Project Identity

Suggested public repository names:

- `business-churn-prediction`
- `customer-churn-ml`
- `telecom-churn-prediction`

Suggested tagline:

> Customer churn prediction with leakage-aware validation, explainability, and business-focused threshold analysis.

Suggested portfolio pitch:

> A reproducible churn prediction ML project that connects model evaluation with retention strategy, threshold trade-offs, and responsible business interpretation.

## Target Folder Structure

```text
business-churn-prediction/
|-- README.md
|-- LICENSE
|-- .gitignore
|-- pyproject.toml
|-- requirements.txt
|-- requirements-dev.txt
|-- configs/
|   `-- train_config.yaml
|-- data/
|   |-- README.md
|   |-- raw/
|   |-- interim/
|   |-- processed/
|   `-- sample/
|-- docs/
|   |-- data_card.md
|   |-- model_card.md
|   |-- leakage_review.md
|   |-- business_context.md
|   `-- reproducibility.md
|-- notebooks/
|   |-- 01_eda.ipynb
|   `-- 02_model_review.ipynb
|-- src/
|   `-- churn_model/
|       |-- __init__.py
|       |-- data.py
|       |-- features.py
|       |-- split.py
|       |-- train.py
|       |-- evaluate.py
|       |-- explain.py
|       `-- inference.py
|-- scripts/
|   |-- train_model.py
|   |-- evaluate_model.py
|   `-- make_sample_data.py
|-- models/
|-- reports/
|   |-- figures/
|   |-- metrics/
|   `-- business_summary.md
`-- tests/
    |-- test_data.py
    |-- test_features.py
    `-- test_split.py
```

## Files Usually Safe To Publish

Usually safe after review:

- `README.md`
- `LICENSE`
- `.gitignore`
- `docs/`
- source code under `src/`
- scripts under `scripts/`
- tests under `tests/`
- configs that do not contain secrets
- public-safe sample data
- curated aggregate metrics and figures if generated from approved data and clearly labelled

## Files/Folders To Ignore

Recommended `.gitignore` baseline:

```gitignore
# Raw/private/generated data
data/raw/
data/interim/
data/processed/
data/**/*.csv
!data/sample/
!data/sample/**
!data/README.md

# Prediction outputs and artifacts
predictions/
reports/predictions/
models/
*.pkl
*.pickle
*.joblib
*.onnx

# Local secrets
.env
.env.*
*.pem
*.key
*serviceAccount*.json

# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/

# Virtual environments
.venv/
venv/
env/

# Jupyter
.ipynb_checkpoints/

# OS/editor
.DS_Store
Thumbs.db
.vscode/
.idea/
```

Adjust the CSV rule if the user explicitly approves publishing a licensed public dataset.

## Existing Metrics

- No saved metrics were found in the audit.
- The notebook contains code to compute ROC-AUC, classification report, and confusion matrix.
- The notebook output does not preserve those metric values.
- Future metrics must only be reported after controlled rerun or saved artifact creation.
- Metrics must be labelled with provenance, including dataset version, split method, model, threshold, date generated, and command/notebook used.
- Never improve, round up, infer, or fabricate metrics.

## Validation Standards

- Use stratified split at minimum.
- Consider cross-validation for more stable model comparison.
- Define the prediction moment and prediction window before final evaluation.
- Avoid train/test leakage.
- Fit preprocessing only on training folds.
- Put preprocessing inside scikit-learn pipelines where possible.
- Move learned transformations such as `pd.qcut` into train-only transformers or avoid them.
- Document whether a temporal split is needed.
- Include threshold and cost-aware evaluation when possible.
- Keep random seeds deterministic and documented.

## Leakage Standards

- `Churn` must never enter features.
- `customerID` should not be a model input.
- Exclude post-outcome, cancellation-derived, or scoring-time-unavailable fields.
- Treat `pd.qcut` on the full dataset before split as a leakage risk.
- Document field availability at scoring time.
- Justify derived features such as `CLTV`, `tenure`, and `TotalCharges` in business-time terms.
- Distinguish observed revenue-to-date from true future customer lifetime value.
- Create or maintain `docs/leakage_review.md` before claiming results are credible.

## Business Framing Standards

The project documentation must define:

- churn meaning
- churn window
- prediction window
- scoring population
- stakeholder
- prediction use case
- model output and decision workflow
- false-positive and false-negative implications
- retention action examples
- threshold, cost, retention capacity, or ROI assumptions where possible

Avoid causal claims from predictive models. Frame recommendations as hypotheses, prioritisation ideas, or risk-segment insights unless causal evidence exists.

Examples:

- Prefer: "Customers with month-to-month contracts are associated with higher predicted churn risk."
- Avoid: "Month-to-month contracts cause churn."

## Recommended Metrics

Use metrics appropriate for imbalanced churn modelling:

- ROC-AUC
- PR-AUC
- precision for the churn class
- recall for the churn class
- F1 for the churn class
- confusion matrix
- lift/gains/top-decile capture
- calibration if using probabilities
- threshold/cost curve
- business summary metrics such as contacted population size, expected false positives, expected missed churners, and intervention-cost sensitivity

## Documentation Standards

`README.md` must include:

- one-sentence pitch
- business problem
- dataset source/provenance
- data safety note
- workflow
- validation strategy
- metrics with provenance
- business interpretation
- limitations
- setup/reproducibility commands
- folder structure
- next steps

`docs/model_card.md` must include:

- intended use
- non-intended use
- dataset summary
- features overview
- model families
- validation method
- metrics
- explainability
- limitations
- business and ethical considerations

`docs/data_card.md` must include:

- source
- licence/provenance
- schema
- target definition
- missingness
- privacy/publication constraints

`docs/business_context.md` must include:

- stakeholders
- use case
- decision workflow
- intervention examples
- cost/benefit assumptions
- responsible interpretation

## Code Quality Standards

- Prefer modular source code over notebook-only logic.
- Use tiny test fixtures.
- Use deterministic seeds.
- Avoid hardcoded local paths.
- Provide clear CLI entry points and configs.
- Avoid hidden state.
- Avoid silent overwrites.
- Preserve user edits.
- Keep notebooks for exploration and communication, not as the only execution path.
- Use structured configs for paths, model parameters, and evaluation settings.
- Write focused tests for data loading, feature engineering, split logic, and evaluation utilities.

## Recommended Command Interface

Target commands:

```bash
python scripts/train_model.py --config configs/train_config.yaml
python scripts/evaluate_model.py --config configs/train_config.yaml
python scripts/make_sample_data.py
pytest
```

Commands should be reproducible, documented, and safe by default. They should not overwrite artifacts unless explicitly configured to do so.

## Phase-By-Phase Roadmap

### Phase 1: Repository Hygiene And Public Safety

Tasks:

- Inspect project structure.
- Add `.gitignore`.
- Create safe folder skeleton without moving or deleting raw data.
- Add `data/README.md`.
- Draft README without invented metrics.
- Add initial `docs/leakage_review.md`.
- Decide what data is safe to publish.

Deliverable:

- `BUSINESS_CHURN_PHASE_1_REPORT.md`

### Phase 2: Environment Setup

Tasks:

- Add `requirements.txt`, `requirements-dev.txt`, or `pyproject.toml`.
- Document setup commands.
- Pin or constrain key packages.
- Verify imports if approved.

Deliverable:

- `BUSINESS_CHURN_PHASE_2_ENV_REPORT.md`

### Phase 3: Source Package Skeleton

Tasks:

- Create `src/churn_model/`.
- Add modules for data, features, split, train, evaluate, explain, and inference.
- Add script entry points.
- Preserve notebook logic while moving reusable pieces into source files.

Deliverable:

- `BUSINESS_CHURN_PHASE_3_SOURCE_REPORT.md`

### Phase 4: Leakage And Validation Hardening

Tasks:

- Define prediction moment/window.
- Review all fields for scoring-time availability.
- Move learned transformations into train-only pipelines.
- Add validation or cross-validation design.
- Document leakage decisions.

Deliverable:

- `BUSINESS_CHURN_PHASE_4_LEAKAGE_VALIDATION_REPORT.md`

### Phase 5: Model/Evaluation Pipeline

Tasks:

- Build repeatable train/evaluate scripts.
- Save metrics with provenance.
- Save safe figures.
- Add PR-AUC, class-specific metrics, lift/gains, calibration, and threshold/cost analysis where possible.
- Do not invent or backfill results.

Deliverable:

- `BUSINESS_CHURN_PHASE_5_MODEL_EVAL_REPORT.md`

### Phase 6: Business/Recruiter Documentation

Tasks:

- Finalise README.
- Add data card, model card, business context, reproducibility documentation, and business summary.
- Make the project readable within 60 seconds.
- Keep limitations visible.

Deliverable:

- `BUSINESS_CHURN_PHASE_6_PORTFOLIO_REPORT.md`

### Phase 7: Optional Demo/Dashboard

Tasks:

- Add Streamlit, static dashboard, notebook demo, or lightweight app only after core reproducibility is solid.
- Use sample or synthetic public-safe data.
- Show score distribution, threshold controls, confusion matrix, and retention segment examples.
- Do not expose full customer-level data.

Deliverable:

- `BUSINESS_CHURN_PHASE_7_DEMO_REPORT.md`

## Review Checklist

Public safety:

- Is raw/customer-level data excluded unless provenance/licence is confirmed?
- Is `customerID` excluded from modelling and public row-level outputs?
- Are secrets, local paths, and private artifacts ignored?

Reproducibility:

- Can a fresh user install dependencies?
- Are commands documented?
- Are paths portable?
- Are random seeds set?
- Are metrics saved with provenance?

Leakage and validation:

- Is `Churn` excluded from features?
- Are post-outcome fields excluded?
- Is preprocessing fitted only on training folds?
- Is full-dataset `qcut` avoided or fixed?
- Is prediction timing documented?

Business usefulness:

- Is churn defined?
- Are stakeholders named?
- Are false positives and false negatives explained?
- Is threshold/cost thinking present?
- Are recommendations responsible and non-causal?

Portfolio quality:

- Can a recruiter understand the project in 60 seconds?
- Are headline results present only when verified?
- Are limitations clear?
- Is the folder structure professional?
- Is the work credible for ML Engineer, Data Scientist, and Business Data Analyst roles?

## Change Safety Rules

Before any change, ask:

- Could this expose customer-level data?
- Could this introduce leakage?
- Could this invent or exaggerate results?
- Could this make unsupported causal or business claims?
- Could this break reproducibility?
- Could this make the project less professional?

If the answer is yes or unclear, pause, document the risk, and choose the safer path.

## First Codex Prompt For A Fresh Folder

Use this prompt to start Phase 1:

```text
Read SKILL.md and BUSINESS_CHURN_PROJECT_AUDIT.md first.

Start Phase 1 for this Business Churn Prediction portfolio project.

Rules:
- Do not move or delete raw data.
- Do not initialise Git.
- Do not commit or push.
- Do not train or rerun models.
- Do not invent metrics.
- Do not expose customer-level data.

Tasks:
1. Inspect the current structure.
2. Add a public-safety-focused .gitignore.
3. Create a safe folder skeleton.
4. Add data/README.md describing provenance/licence status as unverified unless confirmed.
5. Draft README.md without invented metrics.
6. Add docs/leakage_review.md with field availability and known leakage risks.
7. Save BUSINESS_CHURN_PHASE_1_REPORT.md summarising exactly what changed, what was not changed, and remaining risks.
```

