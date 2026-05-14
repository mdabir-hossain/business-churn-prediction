# Leakage Review

## Status

This Phase 4 leakage review strengthens the design before any controlled model evaluation is performed. It is based on the project audit, the existing notebook, and the Phase 3 source skeleton.

No notebook cells were executed, no models were trained, and no metrics were generated for this review.

This document is a design control, not proof that leakage has been fully solved. The existing notebook still contains patterns that must be hardened before results are presented as portfolio-grade.

## Proposed Prediction Setup

The following setup is a proposed modelling assumption for portfolio development. It is not confirmed business truth and should be revisited if a real business definition, event timestamp, or dataset documentation becomes available.

| Design item | Proposed assumption | Status |
|---|---|---|
| Prediction moment | Score active customers at the end of a billing cycle using account and service information available before any future churn event. | Proposed, not confirmed |
| Prediction window | Predict whether a customer will churn in the next billing period or near-term retention window. | Proposed, not confirmed |
| Scoring population | Existing active customers with sufficient account, billing, and service information at the scoring moment. | Proposed, not confirmed |
| Target interpretation | `Churn` is treated as the future churn label for supervised learning. The exact churn definition still needs dataset documentation. | To be confirmed |
| Available information | Only customer attributes, plan/service configuration, tenure, and billing values known at the scoring moment should be used. | To be confirmed |

The project should not claim production readiness, causal impact, or validated business performance until these assumptions are confirmed and implemented in a reproducible pipeline.

## Non-Negotiable Leakage Rules

- `Churn` must never enter feature matrices.
- `customerID` should be excluded from modelling and public row-level outputs.
- Post-outcome, cancellation-derived, or scoring-time-unavailable fields must be excluded.
- Full-dataset learned transformations must be avoided before train/test splitting.
- `pd.qcut` on the full dataset before train/test split is a leakage risk.
- `TotalCharges` and `tenure` may be valid only if known at scoring time.
- `CLTV` should not be presented as true future lifetime value. Use observed revenue-to-date wording unless future value is modelled and validated separately.
- Any field used for modelling must be documented as available before the target outcome.

## Known Leakage Risks From Current Notebook

### Full-Dataset Feature Engineering Before Split

The existing notebook performs feature engineering before splitting the data. Deterministic row-level transformations can be acceptable when their inputs are available at scoring time, but learned transformations must be fitted only on training data.

Examples of generally safer row-level transformations:

- `IsFiber` from `InternetService`
- `IsAutoPay` from `PaymentMethod`
- `ServiceCount` from service subscription fields
- observed revenue-to-date from `MonthlyCharges * tenure`, if both are known at scoring time

Examples requiring extra care:

- quantile bins such as `ChargesTier`
- any transformation that learns global thresholds or distributions
- any feature derived from future behaviour or cancellation processing

### Full-Dataset `pd.qcut`

The notebook creates `ChargesTier` with `pd.qcut(df["MonthlyCharges"], q=4, ...)` before splitting. This learns bin thresholds from all rows, including test rows. That contaminates validation because information from the evaluation set influences feature construction.

Recommended action:

- avoid `ChargesTier` for now and keep `MonthlyCharges` continuous, or
- implement quantile binning as a train-only transformer fitted inside cross-validation or the training pipeline.

### Undefined Prediction Timing

Without a defined scoring moment and prediction window, it is unclear whether `tenure`, `TotalCharges`, and derived observed revenue-to-date are valid pre-outcome features or accidentally include information too close to or after churn.

Recommended action:

- define the scoring moment before model evaluation
- document which columns are available at that moment
- reject any field whose availability is uncertain and material to leakage risk

### `CLTV` Naming

The notebook creates `CLTV = MonthlyCharges * tenure`. This is not true future customer lifetime value. It is closer to observed revenue-to-date or account value to date.

Recommended action:

- use the name `ObservedRevenueToDate`
- document it as historical account value, not expected future value
- avoid making future ROI claims from this feature

## Field Availability Review

This table reviews the known raw dataset columns only. Engineered features are handled separately below.

| Field | Role | Likely scoring-time availability | Leakage risk | Recommended action | Business interpretation caution |
|---|---|---|---|---|---|
| `customerID` | Identifier / exclude | Available, but not a predictive feature | High public-safety and memorisation risk if used | Exclude from features; avoid publishing row-level outputs with this field | Identifier is not a behavioural driver |
| `gender` | Review feature | Likely available | Low direct leakage risk; fairness and responsible-use risk | Review whether to include; document rationale if used | Avoid implying gender is the reason for churn |
| `SeniorCitizen` | Review feature | Likely available | Low direct leakage risk; fairness and responsible-use risk | Review whether to include; document rationale if used | Avoid discriminatory targeting claims |
| `Partner` | Feature / review | Likely available | Low direct leakage risk | Use only if available at scoring time | Association, not causation |
| `Dependents` | Feature / review | Likely available | Low direct leakage risk | Use only if available at scoring time | Association, not causation |
| `tenure` | Feature / review | Likely available if measured at scoring moment | Medium; can leak if measured after churn or at extract date after outcome | Use only with defined scoring date; document timing | Longer tenure may proxy loyalty and account maturity |
| `PhoneService` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Service mix is a segmentation signal, not causal proof |
| `MultipleLines` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Service mix is a segmentation signal |
| `InternetService` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Avoid overclaiming service type as the reason for churn |
| `OnlineSecurity` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Product adoption may be correlated with retention |
| `OnlineBackup` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Product adoption may be correlated with retention |
| `DeviceProtection` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Product adoption may be correlated with retention |
| `TechSupport` | Feature | Likely available | Low if pre-outcome; review if support status is updated after cancellation | Use only if it reflects pre-outcome service subscription | Support subscription is not the same as support experience quality |
| `StreamingTV` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Entertainment services may proxy bundle depth |
| `StreamingMovies` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Entertainment services may proxy bundle depth |
| `Contract` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Contract type may be strongly predictive but is not causal by itself |
| `PaperlessBilling` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Billing preference should be interpreted cautiously |
| `PaymentMethod` | Feature | Likely available | Low if pre-outcome | Use if available at scoring time | Autopay association is not proof autopay prevents churn |
| `MonthlyCharges` | Feature | Likely available | Low to medium; valid if current charge before outcome | Use if known at scoring time | Higher charges may proxy plan type and customer value |
| `TotalCharges` | Feature / review | Available only if measured as of scoring moment | Medium; can leak extra post-outcome account history if measured after churn | Use only with scoring-time definition; otherwise exclude or recompute from historical cut-off | Historical value, not future value |
| `Churn` | Target | Not available at scoring time | Critical leakage if included in features | Use only as target; enforce exclusion in code/tests | Outcome label, not an input |

## Engineered Feature Review

| Feature | Source fields | Leakage risk | Recommended action |
|---|---|---|---|
| `ServiceCount` | service subscription fields | Low if source fields are available pre-outcome | Keep as deterministic row-level feature if inputs are available |
| `TenureGroup` | `tenure` | Low for fixed bins; medium if bins are learned from full data | Prefer fixed business bins or train-only transformer |
| `ChargesTier` | `MonthlyCharges` | High if built with full-dataset `pd.qcut` before split | Avoid by default; if used, fit thresholds on training folds only |
| `IsFiber` | `InternetService` | Low if source field is available | Keep as deterministic row-level feature if useful |
| `IsAutoPay` | `PaymentMethod` | Low if source field is available | Keep as deterministic row-level feature if useful |
| `SeniorAlone` | `SeniorCitizen`, `Partner`, `Dependents` | Low direct leakage risk; fairness/responsible-use review needed | Review and document rationale before final use |
| `CLTV` | `MonthlyCharges`, `tenure` | Naming and timing risk | Rename to `ObservedRevenueToDate`; do not present as true future CLTV |

## Source Package Alignment

Phase 3 added safer helper functions under `src/churn_model/`:

- `split_features_target` excludes `Churn` and `customerID` by default.
- `stratified_train_test_split` uses stratification and configurable random state.
- `add_observed_revenue_to_date` avoids future CLTV wording.
- `experimental_add_charges_tier_qcut` is marked as experimental and warns that full-dataset qcut is not leakage-safe.

These helpers support leakage-aware development, but they do not solve leakage by themselves. The future training pipeline must use them correctly inside a documented validation design.

## Safe Next Steps

1. Confirm dataset provenance and target definition.
2. Define the final prediction moment and prediction window.
3. Decide whether demographic fields should be included, excluded, or used only for fairness review.
4. Decide whether `TotalCharges`, `tenure`, and observed revenue-to-date are valid at scoring time.
5. Avoid full-dataset quantile binning.
6. Move any learned preprocessing into train-only scikit-learn pipelines.
7. Add tests proving target and identifier columns cannot enter the feature matrix.
8. Perform controlled model evaluation only after the validation strategy is implemented.

## Responsible Interpretation

This project should present model findings as predictive associations. Retention recommendations should be framed as prioritisation ideas or hypotheses, not causal claims. Business claims about savings, ROI, retention uplift, or customer impact must not be made unless supported by explicit assumptions and validated calculations.
