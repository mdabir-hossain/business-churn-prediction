# Data README

## Current Local Dataset

The project currently contains a local CSV file at `data/telco_churn.csv`.

This appears to be a customer-level telecom churn dataset, but the dataset source, licence, and redistribution permissions still need to be confirmed. Until that is verified, treat the raw CSV as local-only data that should not be published to a public GitHub repository.

## Public-Safety Guidance

- Do not publish raw customer-level data until provenance and licence are confirmed.
- Treat `customerID` carefully, even if it appears synthetic or comes from a public dataset.
- Do not commit row-level prediction dumps that identify or re-identify customers.
- Do not add private customer data, credentials, or local-only files to the repository.
- Prefer `data/sample/` for small public-safe samples or synthetic examples.

## How Future Users Should Provide Data

For local development, place the approved dataset at:

```text
data/telco_churn.csv
```

Future documentation should include:

- the original dataset source
- licence or usage terms
- download instructions if the dataset can be redistributed or obtained publicly
- schema notes
- privacy and publication constraints

If the raw dataset cannot be redistributed, keep the full data local and provide only a safe sample or synthetic substitute under `data/sample/`.

## Current Publication Status

Publication status: to be confirmed.

Do not assume `data/telco_churn.csv` is safe to publish until the project owner has verified the dataset provenance and licence.

