import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from churn_model.config import IDENTIFIER_COLUMN, RAW_REQUIRED_COLUMNS, TARGET_COLUMN
from churn_model.data import missing_columns, validate_required_columns


def test_required_columns_are_detected() -> None:
    frame = pd.DataFrame(columns=RAW_REQUIRED_COLUMNS)

    assert missing_columns(frame) == []
    validate_required_columns(frame)


def test_missing_required_columns_raise_clear_error() -> None:
    frame = pd.DataFrame(columns=[TARGET_COLUMN, IDENTIFIER_COLUMN])

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_required_columns(frame)

