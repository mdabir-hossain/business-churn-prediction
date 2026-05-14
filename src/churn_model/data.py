"""Data loading and schema validation helpers.

These functions deliberately avoid downloading data or printing customer-level
records. Keep raw customer data local until provenance and licence are verified.
"""

from pathlib import Path
from typing import Iterable

import pandas as pd

from churn_model.config import DEFAULT_DATA_PATH, RAW_REQUIRED_COLUMNS
from churn_model.paths import resolve_project_path


def load_telco_churn_csv(path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the local telco churn CSV from an explicit or project-relative path."""
    csv_path = resolve_project_path(path)
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {csv_path}. Place the approved local CSV there "
            "or pass an explicit path."
        )
    return pd.read_csv(csv_path)


def load_clean_telco_churn_csv(
    path: str | Path = DEFAULT_DATA_PATH,
    drop_missing_total_charges: bool = True,
) -> pd.DataFrame:
    """Load, validate, and lightly clean the local telco churn dataset."""
    from churn_model.features import clean_total_charges

    frame = load_telco_churn_csv(path)
    validate_required_columns(frame)
    return clean_total_charges(frame, drop_missing=drop_missing_total_charges)


def missing_columns(
    frame: pd.DataFrame, required_columns: Iterable[str] = RAW_REQUIRED_COLUMNS
) -> list[str]:
    """Return required columns missing from a dataframe."""
    columns = set(frame.columns)
    return [column for column in required_columns if column not in columns]


def validate_required_columns(
    frame: pd.DataFrame, required_columns: Iterable[str] = RAW_REQUIRED_COLUMNS
) -> None:
    """Raise a clear error if required columns are missing."""
    missing = missing_columns(frame, required_columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_columns_present(frame: pd.DataFrame, columns: Iterable[str]) -> None:
    """Validate an arbitrary list of expected columns."""
    missing = missing_columns(frame, columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
