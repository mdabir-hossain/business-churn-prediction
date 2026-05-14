# Data Card

## Source And Provenance

Dataset file used locally:

```text
data/telco_churn.csv
```

Provenance status: to be confirmed.  
Licence status: to be confirmed.

The raw customer-level CSV should not be published publicly until source, licence, and redistribution permissions are verified.

## Schema Overview

Known columns:

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

## Target Definition

Target column: `Churn`.

The exact business definition of churn and the prediction window are not confirmed in the dataset documentation available in this project. Phase 4 proposes treating `Churn` as a future churn label for a near-term retention window, but this remains an assumption.

## Controlled Run Data Summary

From saved Phase 5B artifacts:

- Rows after cleaning: 7,032
- Non-churn after cleaning: 5,163
- Churn after cleaning: 1,869
- Cleaning step: `TotalCharges` converted to numeric and missing `TotalCharges` rows dropped

## Identifier Handling

`customerID` is treated as an identifier:

- excluded from model features
- not used for training
- not published in row-level outputs

No row-level prediction dumps are saved.

## Public-Safety Constraints

The project `.gitignore` excludes customer-level CSV files by default. These paths are treated cautiously:

- `data/raw/`
- `data/interim/`
- `data/processed/`
- customer-level CSV files
- prediction dumps
- model artifacts unless intentionally released

Use `data/sample/` only for public-safe sample or synthetic data.

## Known Limitations

- Dataset source and licence are unverified.
- No event dates are available in the current schema.
- Prediction timing is proposed, not confirmed.
- Demographic fields require responsible-use review before final modelling decisions.
- `TotalCharges` and `tenure` require scoring-time justification.

## Recommended Next Steps

- Confirm source and licence before public release.
- Add a public dataset link or data access instructions if redistribution is allowed.
- Create a public-safe sample dataset if the raw CSV cannot be shared.
- Add a final target definition and prediction-window statement.

