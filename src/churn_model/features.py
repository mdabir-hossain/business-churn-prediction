"""Reusable, safe feature helpers based on the current notebook logic."""

from collections.abc import Sequence

import pandas as pd

from churn_model.config import (
    IDENTIFIER_COLUMN,
    SERVICE_COLUMNS,
    TARGET_COLUMN,
)
from churn_model.data import validate_columns_present


def clean_total_charges(
    frame: pd.DataFrame,
    column: str = "TotalCharges",
    drop_missing: bool = False,
) -> pd.DataFrame:
    """Convert TotalCharges to numeric, optionally dropping rows made missing."""
    validate_columns_present(frame, [column])
    output = frame.copy()
    output[column] = pd.to_numeric(output[column], errors="coerce")
    if drop_missing:
        output = output.dropna(subset=[column])
    return output


def add_service_count(
    frame: pd.DataFrame,
    service_columns: Sequence[str] = SERVICE_COLUMNS,
    output_column: str = "ServiceCount",
) -> pd.DataFrame:
    """Count service columns equal to Yes."""
    validate_columns_present(frame, service_columns)
    output = frame.copy()
    output[output_column] = output[list(service_columns)].eq("Yes").sum(axis=1)
    return output


def add_autopay_flag(
    frame: pd.DataFrame,
    payment_column: str = "PaymentMethod",
    output_column: str = "IsAutoPay",
) -> pd.DataFrame:
    """Add a binary flag for automatic payment methods."""
    validate_columns_present(frame, [payment_column])
    output = frame.copy()
    output[output_column] = (
        output[payment_column].astype("string").str.contains("automatic", case=False, na=False)
    ).astype(int)
    return output


def add_fiber_flag(
    frame: pd.DataFrame,
    internet_column: str = "InternetService",
    output_column: str = "IsFiber",
) -> pd.DataFrame:
    """Add a binary flag for fibre optic internet service."""
    validate_columns_present(frame, [internet_column])
    output = frame.copy()
    output[output_column] = (output[internet_column] == "Fiber optic").astype(int)
    return output


def add_senior_alone_flag(
    frame: pd.DataFrame,
    output_column: str = "SeniorAlone",
) -> pd.DataFrame:
    """Add a binary flag for senior customers without partner or dependents."""
    required = ["SeniorCitizen", "Partner", "Dependents"]
    validate_columns_present(frame, required)
    output = frame.copy()
    output[output_column] = (
        (output["SeniorCitizen"] == 1)
        & (output["Partner"] == "No")
        & (output["Dependents"] == "No")
    ).astype(int)
    return output


def add_observed_revenue_to_date(
    frame: pd.DataFrame,
    monthly_charges_column: str = "MonthlyCharges",
    tenure_column: str = "tenure",
    output_column: str = "ObservedRevenueToDate",
) -> pd.DataFrame:
    """Add observed revenue-to-date; do not interpret this as future CLTV."""
    validate_columns_present(frame, [monthly_charges_column, tenure_column])
    output = frame.copy()
    output[output_column] = output[monthly_charges_column] * output[tenure_column]
    return output


def drop_identifier_column(
    frame: pd.DataFrame,
    identifier_column: str = IDENTIFIER_COLUMN,
) -> pd.DataFrame:
    """Return a copy without the customer identifier column when present."""
    return frame.drop(columns=[identifier_column], errors="ignore")


def split_features_target(
    frame: pd.DataFrame,
    target_column: str = TARGET_COLUMN,
    identifier_column: str = IDENTIFIER_COLUMN,
    drop_identifier: bool = True,
) -> tuple[pd.DataFrame, pd.Series]:
    """Split a dataframe into X/y, excluding target and optionally identifier."""
    validate_columns_present(frame, [target_column])
    y = frame[target_column].copy()
    drop_columns = [target_column]
    if drop_identifier and identifier_column in frame.columns:
        drop_columns.append(identifier_column)
    X = frame.drop(columns=drop_columns)
    if target_column in X.columns:
        raise ValueError(f"Target column {target_column!r} is still present in features.")
    return X, y


def engineer_safe_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Apply deterministic row-level feature helpers used by the notebook."""
    output = clean_total_charges(frame)
    output = add_service_count(output)
    output = add_fiber_flag(output)
    output = add_autopay_flag(output)
    output = add_senior_alone_flag(output)
    output = add_observed_revenue_to_date(output)
    return output


def experimental_add_charges_tier_qcut(
    frame: pd.DataFrame,
    charges_column: str = "MonthlyCharges",
    output_column: str = "ChargesTier",
    q: int = 4,
) -> pd.DataFrame:
    """Add qcut charges tiers.

    Experimental only: this is not leakage-safe if fitted on the full dataset
    before train/test splitting. Prefer a train-only transformer or fixed bins.
    """
    validate_columns_present(frame, [charges_column])
    output = frame.copy()
    output[output_column] = pd.qcut(output[charges_column], q=q, duplicates="drop")
    return output

