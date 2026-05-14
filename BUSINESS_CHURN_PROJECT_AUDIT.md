# Business Churn Prediction Project Audit

Audit date: 2026-05-14  
Project path: `F:\Business churn prediction`  
Audit scope: structure, Git status, data/public-safety risk, ML correctness, workflow, reproducibility, business usefulness, and portfolio readiness.  
Important note: no models were trained or retrained during this audit. Existing metrics were not independently rerun.

## Executive Summary

This is currently a very small notebook-first churn project consisting of:

- one raw-looking CSV file: `data/telco_churn.csv`
- one notebook: `notebooks/01_eda_modeling.ipynb`
- no Git repository metadata in this folder
- no README, requirements file, source package, tests, saved figures, model artifacts, or reports

The notebook contains a reasonable early-stage workflow: load data, clean `TotalCharges`, perform EDA, engineer features, train/test split with stratification, train three classifiers, evaluate ROC-AUC, and run SHAP for a logistic model. However, the saved notebook does not contain model metric outputs. The first saved cell output is a `FileNotFoundError`, suggesting the notebook was run from a working directory where `../data/telco_churn.csv` did not resolve.

For a UK job-ready Machine Learning Engineer / Data Scientist / Business Data Analyst portfolio project, the main gaps are repository hygiene, reproducibility, public-safe data handling, saved and documented metrics, leakage review, business framing, and recruiter-facing documentation.

## Current Project Structure

Observed structure:

```text
F:\Business churn prediction/
├── data/
│   └── telco_churn.csv
└── notebooks/
    └── 01_eda_modeling.ipynb
```

File sizes observed:

| Path | Type | Size |
|---|---:|---:|
| `data/telco_churn.csv` | CSV data | 977,501 bytes |
| `notebooks/01_eda_modeling.ipynb` | Jupyter notebook | 23,622 bytes |

No hidden project files, `.gitignore`, README, dependency files, source package, tests, saved reports, saved metrics, saved figures, or deployment/demo files were found.

## Git Repository Status

`git status --short --branch` returned:

```text
fatal: not a git repository (or any of the parent directories): .git
```

Conclusion:

- This folder is not currently a Git repository.
- `git remote -v` was not run because the folder is not a Git repository.
- No branch or remote information is available.
- Git was not initialised during this audit.

## File Inventory

### Notebooks

- `notebooks/01_eda_modeling.ipynb`
  - Contains EDA, feature engineering, model training code, model comparison code, SHAP code, and a short business recommendations markdown cell.
  - Saved outputs are mostly absent.
  - The first saved output is a `FileNotFoundError` for `../data/telco_churn.csv`.

### Scripts

No standalone scripts were found.

### Source Code

No `src/` package or reusable Python modules were found.

### Data Files

- `data/telco_churn.csv`
  - 7,043 rows
  - 21 columns
  - Columns:
    - `customerID`
    - `gender`
    - `SeniorCitizen`
    - `Partner`
    - `Dependents`
    - `tenure`
    - `PhoneService`
    - `MultipleLines`
    - `InternetService`
    - `OnlineSecurity`
    - `OnlineBackup`
    - `DeviceProtection`
    - `TechSupport`
    - `StreamingTV`
    - `StreamingMovies`
    - `Contract`
    - `PaperlessBilling`
    - `PaymentMethod`
    - `MonthlyCharges`
    - `TotalCharges`
    - `Churn`
  - Target distribution in the CSV:
    - `No`: 5,174
    - `Yes`: 1,869

### Model Artifacts

No saved model artifacts were found.

### Reports and Figures

No saved report files or figure exports were found.

### Requirements / Environment Files

No `requirements.txt`, `requirements-dev.txt`, `environment.yml`, `pyproject.toml`, `setup.py`, or equivalent environment file was found.

### README / Docs

No README or docs files were found.

### Config Files

No project configuration files were found.

### Tests

No tests were found.

### Deployment / Demo Files

No deployment, API, dashboard, Streamlit, Gradio, notebook demo, Docker, or CI files were found.

## Existing Workflow

The likely intended workflow in `notebooks/01_eda_modeling.ipynb` is:

1. Load CSV from `../data/telco_churn.csv`.
2. Inspect shape, dtypes, and churn distribution.
3. Convert `TotalCharges` to numeric with `errors="coerce"`.
4. Drop rows where `TotalCharges` becomes missing.
5. Standardise column names by stripping spaces and replacing spaces with underscores.
6. Perform EDA:
   - churn distribution
   - churn by contract type
   - tenure distribution by churn
   - monthly charges by churn
   - internet service by churn
   - numeric correlation heatmap
7. Engineer features:
   - `ServiceCount`
   - `TenureGroup`
   - `ChargesTier`
   - `IsFiber`
   - `IsAutoPay`
   - `SeniorAlone`
   - `CLTV`
8. Drop `customerID`.
9. Encode `Churn` as 1 for yes and 0 for no.
10. Split data using `train_test_split`:
    - `test_size=0.2`
    - `random_state=42`
    - `stratify=y`
11. Identify numeric and categorical features.
12. Build a `ColumnTransformer`:
    - one-hot encode categorical features
    - pass numeric features through unchanged
13. Train:
    - Logistic Regression with `class_weight="balanced"`
    - Random Forest with `class_weight="balanced"`
    - HistGradientBoostingClassifier
14. Evaluate with:
    - ROC-AUC
    - classification report for logistic regression
    - confusion matrix for logistic regression
    - ROC-AUC comparison table
15. Run SHAP using a separately fitted logistic regression on preprocessed training data.
16. Add high-level business recommendations.

## Existing Metrics Found

No saved model metric values were found in the project files.

The notebook contains code intended to compute:

- Logistic Regression ROC-AUC
- Logistic Regression classification report
- Logistic Regression confusion matrix
- Random Forest ROC-AUC
- HistGradientBoosting ROC-AUC
- A three-model ROC-AUC comparison table

However, the metric outputs are not saved in the notebook, reports, CSV files, JSON files, or other artifacts. The metrics were not independently rerun during this audit, in line with the instruction not to train or retrain models.

## Data/Public Safety Review

### Raw Data Files

`data/telco_churn.csv` appears to be the raw dataset used directly by the notebook.

### Processed / Generated Feature Files

No processed, interim, or generated feature files were found.

### Prediction Dumps

No prediction dumps were found.

### Potential Customer / Personally Identifiable Fields

The dataset contains `customerID`. Even if this is a synthetic or public sample identifier, it should be treated carefully in a public portfolio project.

Visible fields do not include obvious direct contact details such as name, email, phone number, address, postcode, or payment card details. However, the combination of service attributes, charges, tenure, demographic flags, and customer identifiers should still be handled as customer-level data.

### Files That Should Not Be Committed Publicly Without Review

Before making this public, review whether the CSV is licensed for redistribution. Do not commit it unless provenance and licence are clear.

Candidate files/directories to exclude or handle carefully:

- `data/raw/`
- full customer-level datasets
- prediction outputs containing row-level customer risk
- trained model files if they encode sensitive information
- local notebooks with private paths or unsanitised outputs
- any future credentials, API keys, environment files, or service-account files

### `.gitignore`

No `.gitignore` was found.

Recommended `.gitignore` should exclude at least:

- Python caches
- virtual environments
- notebook checkpoints
- local environment files
- raw/private data
- generated model artifacts unless intentionally released
- temporary outputs

### Public-Safe Data Strategy

Recommended approach:

- Add `data/README.md` explaining dataset source, licence, schema, and how to obtain the data.
- Keep full raw data out of Git unless redistribution is explicitly allowed.
- If public sharing is allowed, still document source and licence clearly.
- If public sharing is uncertain, include only a small synthetic or sampled public-safe dataset in `data/sample/`.
- Keep row-level predictions out of the repository unless anonymised, sampled, and documented.
- Remove or transform `customerID` before publishing any derived row-level files.

## ML Correctness Review

### Split Strategy

The notebook uses a single stratified random train/test split with `test_size=0.2` and `random_state=42`.

Strength:

- Stratification is appropriate because churn is imbalanced.

Limitations:

- No validation set or cross-validation is present.
- No temporal split is considered.
- It is unclear whether the business use case predicts near-future churn at a specific scoring date. Without that definition, the split may not reflect deployment conditions.

### Possible Leakage

Several leakage risks should be reviewed before treating results as portfolio-grade:

- Feature engineering is performed before the train/test split.
- `ChargesTier` uses `pd.qcut` on the full dataset before splitting. This learns bin thresholds from all rows, including the future test set.
- `CLTV = MonthlyCharges * tenure` may be acceptable if both values are known at scoring time, but the name `CLTV` is potentially misleading because it is more like observed lifetime revenue to date, not true future customer lifetime value.
- `TotalCharges`, `tenure`, and `CLTV` may be valid features if known at prediction time, but they should be explicitly justified against the prediction date.
- No explicit leakage review identifies whether any fields are post-churn, cancellation-generated, or unavailable before the churn decision.

### Target Handling

The target `Churn` is encoded and dropped from features correctly in the visible code.

### Preprocessing Fit Scope

The main model pipelines use `ColumnTransformer` inside scikit-learn `Pipeline`, so one-hot encoding is fitted on training data when `clf.fit(X_train, y_train)` is called.

However:

- Full-dataset feature engineering before split should be moved into a train-aware pipeline where needed.
- SHAP code manually calls `preprocess.fit_transform(X_train)`, which is training-only, but it fits a separate preprocessing object/model outside the main pipeline. That makes explainability less directly tied to the exact fitted model artifact.

### Class Imbalance

Class imbalance is partly handled:

- Logistic Regression uses `class_weight="balanced"`.
- Random Forest uses `class_weight="balanced"`.
- HistGradientBoostingClassifier does not include a visible imbalance strategy.

There is no discussion of why a strategy was chosen, how imbalance affects metrics, or how precision/recall trade-offs affect retention actions.

### Metrics

The code uses ROC-AUC and a classification report. These are useful but incomplete for churn.

Recommended additions:

- precision, recall, and F1 for churn class
- confusion matrix interpreted in business terms
- PR-AUC, especially because churn is imbalanced
- lift/gains or top-decile capture
- threshold-specific metrics
- calibration assessment if probabilities drive actions
- cost-based evaluation if retention incentives have known costs

### Probability Calibration and Threshold Selection

No calibration or threshold-selection workflow was found.

The default classifier threshold of 0.5 is likely not business-optimal for churn. A portfolio-grade project should explain threshold choice using retention capacity, intervention cost, expected margin, false-positive cost, or recall target.

### Explainability

SHAP is present for a logistic model. This is promising, but currently:

- no saved SHAP plot was found
- no exact top features were saved as a table
- no model card explains limitations
- no business-safe language warns that explanations are associations, not causal proof

## Leakage Risk Review

Key leakage concerns:

1. `pd.qcut` is fitted on the full dataset before splitting.
2. The project does not define prediction timing, so it is unclear which fields are available at scoring time.
3. `TotalCharges`, `tenure`, and derived `CLTV` may be valid, but they need time-aware justification.
4. Feature engineering currently lives in the notebook rather than a fitted transformer or source module.
5. No leakage checklist or documented field availability review exists.

Recommended fix:

- Create `docs/leakage_review.md`.
- Define the prediction moment, for example: "At the end of each billing cycle, predict churn risk for the next billing period."
- Classify each column as available before scoring, target/post-outcome, identifier, or excluded.
- Move learned transformations such as quantile binning into train-only preprocessing.
- Prefer keeping raw continuous variables unless bins have a business reason.

## Business Usefulness Review

### What Churn Means

The project uses a `Churn` target but does not define churn in business terms.

Missing:

- exact churn definition
- churn window
- prediction window
- scoring population
- whether churn means contract cancellation, non-renewal, inactivity, or another event

### Stakeholders

No explicit stakeholders are identified.

Likely stakeholders could include:

- retention marketing team
- customer success team
- commercial leadership
- finance / revenue operations
- product or service operations

These should be stated, not assumed.

### Connection to Retention Actions

The notebook includes short recommendations:

1. prioritise new customers
2. incentivise month-to-month users to switch contracts
3. offer discounts or bundles to high-charge fiber customers
4. promote AutoPay and bundles
5. improve OnlineSecurity and TechSupport adoption

These are useful as a starting point, but they need stronger evidence boundaries. They should be framed as hypotheses or targeting ideas, not causal claims.

### False Positives / False Negatives

No business interpretation of false positives or false negatives was found.

Recommended framing:

- False positive: customer is targeted despite not being likely to churn, causing unnecessary incentive cost or customer fatigue.
- False negative: likely churner is missed, causing preventable revenue loss.

### Threshold / Cost / ROI Thinking

No threshold, cost, retention budget, or ROI analysis was found.

This is a major portfolio opportunity because churn projects become more credible when model scores are connected to intervention economics.

### Responsible Recommendations

Recommendations should avoid unsupported causal language. For example:

- Safer: "Customers with month-to-month contracts are associated with higher predicted churn risk."
- Riskier: "Month-to-month contracts cause churn."

The current recommendations are broadly reasonable but should be tied to measured feature importance, validation metrics, and business constraints once metrics are saved.

## Reproducibility Review

### Can the Project Be Rerun?

Not reliably yet.

Issues:

- No dependency file exists.
- No README explains setup or execution.
- The notebook path `../data/telco_churn.csv` is brittle. The saved notebook currently contains a `FileNotFoundError`, likely because the notebook was run from a different working directory.
- No scripts or CLI entry points exist.
- No saved metrics or artifacts exist to compare reruns.

### Requirements Pinned?

No requirements were found. Package versions are unknown.

Libraries used in the notebook include:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- shap

### Notebook-Only?

Yes. The workflow currently exists only in a notebook.

### Portable Paths?

Paths are not robust. `pd.read_csv("../data/telco_churn.csv")` depends on the active working directory.

### Random Seeds

Some seeds are present:

- `train_test_split(random_state=42)`
- `RandomForestClassifier(random_state=42)`
- `HistGradientBoostingClassifier(random_state=42)`

### Artifact Provenance

No artifact provenance exists because no saved models, metrics, figures, or predictions were found.

### Tests

No tests were found.

## Portfolio Readiness Review

### README Quality

No README exists.

### Project Story

The story is not yet documented. A recruiter cannot tell within 60 seconds:

- what problem is solved
- what dataset is used
- what the business value is
- what model won
- what metrics were achieved
- how to rerun the project
- what decisions could be made from the output

### Folder Structure

The current structure is minimal and easy to inspect, but not portfolio-grade.

### Metrics Presentation

No saved metric values were found. This is a critical gap.

### Limitations

No limitations section exists.

### Business Framing

There are brief recommendations, but no formal business context, stakeholder framing, threshold strategy, or ROI discussion.

### Technical Depth

The notebook shows useful technical breadth:

- EDA
- feature engineering
- stratified split
- pipelines
- model comparison
- SHAP

But it needs to be hardened into a reproducible pipeline with documented validation and leakage controls.

### Visual Polish

Plots are generated in the notebook but not saved as portfolio-ready figures.

### Recruiter Readability Within 60 Seconds

Currently low. Without a README, summary chart, headline metrics, and business impact framing, a recruiter or hiring manager must open the notebook and infer the story manually.

## Critical Issues

1. No Git repository exists in this folder.
2. No README or documentation exists.
3. No dependency/environment file exists.
4. No saved model metric values were found.
5. The notebook contains a saved `FileNotFoundError` for the data path.
6. The project relies entirely on one notebook.
7. No `.gitignore` exists.
8. Raw customer-level data is present and should not be published without licence/provenance review.
9. Learned feature engineering such as `pd.qcut` occurs before the split.
10. No leakage review or prediction-time field availability review exists.
11. No threshold, calibration, cost, or ROI analysis exists.
12. No tests or reproducible scripts exist.

## Important Improvements

- Add a public-safe README with problem framing, dataset source, setup, results, and limitations.
- Add `.gitignore` before any public GitHub work.
- Add dependency files with pinned or reasonably constrained versions.
- Move reusable logic from notebook into `src/churn_model/`.
- Create a reproducible training/evaluation script.
- Save metrics to `reports/metrics/`.
- Save selected figures to `reports/figures/`.
- Add a data card and model card.
- Define prediction window and field availability.
- Move train-aware transformations into pipelines.
- Add PR-AUC, recall, precision, lift/gains, calibration, and threshold analysis.
- Convert business recommendations into evidence-linked, responsible statements.
- Add tests for data loading, preprocessing, split behavior, and feature generation.

## Recommended Target Structure

```text
business-churn-prediction/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── configs/
│   └── train_config.yaml
├── data/
│   ├── README.md
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── sample/
├── docs/
│   ├── data_card.md
│   ├── model_card.md
│   ├── leakage_review.md
│   ├── business_context.md
│   └── reproducibility.md
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_review.ipynb
├── src/
│   └── churn_model/
│       ├── __init__.py
│       ├── data.py
│       ├── features.py
│       ├── split.py
│       ├── train.py
│       ├── evaluate.py
│       ├── explain.py
│       └── inference.py
├── scripts/
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── make_sample_data.py
├── models/
├── reports/
│   ├── figures/
│   ├── metrics/
│   └── business_summary.md
└── tests/
    ├── test_data.py
    ├── test_features.py
    └── test_split.py
```

## Phase-by-Phase Improvement Plan

### Phase 1: Repository Hygiene and Public Safety

- Initialise Git only when ready.
- Add `.gitignore`.
- Decide whether the raw CSV can be committed publicly.
- Add `data/README.md` with source, licence, and public-use notes.
- Remove or avoid publishing row-level customer identifiers unless justified.
- Add a clear project licence if appropriate.

### Phase 2: Environment Setup

- Add `requirements.txt` or `pyproject.toml`.
- Pin or constrain key dependencies.
- Add setup instructions for Windows and general Python environments.
- Verify a clean install can run the project.

### Phase 3: Source Package Skeleton

- Create `src/churn_model/`.
- Move loading, cleaning, splitting, feature generation, training, evaluation, and inference into modules.
- Keep notebooks as exploration and reporting, not the only source of truth.

### Phase 4: Leakage and Validation Hardening

- Define the prediction date and prediction window.
- Create `docs/leakage_review.md`.
- Classify each column by scoring-time availability.
- Move learned transformations into train-only pipelines.
- Add validation or cross-validation.
- Consider whether a temporal split is more appropriate.

### Phase 5: Model / Evaluation Pipeline

- Build a repeatable training script.
- Save model metrics to `reports/metrics/`.
- Save figures to `reports/figures/`.
- Compare baseline and candidate models.
- Add PR-AUC, recall, precision, F1, lift/gains, calibration, and threshold analysis.
- Add test coverage for core preprocessing and split logic.

### Phase 6: Business / Recruiter Documentation

- Write a strong README with:
  - problem statement
  - stakeholder framing
  - dataset description
  - methodology
  - headline metrics
  - business interpretation
  - limitations
  - how to run
- Add `docs/business_context.md`.
- Add `docs/model_card.md`.
- Add a short `reports/business_summary.md` suitable for non-technical readers.

### Phase 7: Optional Demo / Dashboard

- Add a small Streamlit dashboard or static demo only after the core project is reproducible.
- Use sample or synthetic data for demo inputs.
- Show score distribution, threshold slider, confusion matrix, and recommended retention segment.
- Avoid exposing real customer-level records.

## Immediate Next Step

The immediate next step should be repository hygiene and public-safety setup:

1. Add `.gitignore`.
2. Add `README.md`.
3. Add `data/README.md`.
4. Decide whether `data/telco_churn.csv` can be public.
5. Add `requirements.txt`.
6. Rerun the existing notebook only after the path issue is fixed, then save verified metric outputs.

Do not publish this project to GitHub until the data provenance/licence and `.gitignore` strategy are clear.

## Suggested Prompt for Creating `SKILL.md`

Use this prompt when creating a reusable Codex skill for future phases of this portfolio project:

```text
Create a Codex SKILL.md for upgrading a churn prediction portfolio project into a public-safe, reproducible, recruiter-friendly Machine Learning / Data Science project.

The skill should guide Codex to:
- preserve user work and avoid destructive Git/file operations
- check public-safety and data provenance before committing data
- prefer reproducible Python modules over notebook-only workflows
- create README, data card, model card, leakage review, and business context docs
- build train/evaluate/inference modules under src/churn_model/
- save existing and newly generated metrics only when they are actually computed
- avoid inventing metrics, ROI claims, or business conclusions
- document prediction timing, feature availability, leakage risks, and limitations
- add tests for data loading, feature engineering, split logic, and evaluation
- maintain a UK job-ready portfolio tone for Machine Learning Engineer, Data Scientist, and Business Data Analyst roles

The skill should include a phase-based workflow:
1. repository hygiene and public safety
2. environment setup
3. source package skeleton
4. leakage and validation hardening
5. model/evaluation pipeline
6. business/recruiter documentation
7. optional demo/dashboard

The skill should require Codex to inspect the current repo before editing, summarize findings, make scoped changes, run relevant checks, and report exactly what changed.
```

