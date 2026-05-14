import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from churn_model.config import IDENTIFIER_COLUMN, TARGET_COLUMN
from churn_model.features import (
    add_autopay_flag,
    add_observed_revenue_to_date,
    add_service_count,
    clean_total_charges,
    split_features_target,
)


def test_total_charges_cleaning_converts_invalid_values_to_missing() -> None:
    frame = pd.DataFrame({"TotalCharges": ["10.5", " ", "bad"]})

    cleaned = clean_total_charges(frame)

    assert cleaned["TotalCharges"].iloc[0] == 10.5
    assert cleaned["TotalCharges"].isna().sum() == 2


def test_feature_helpers_use_synthetic_data_only() -> None:
    frame = pd.DataFrame(
        {
            "PhoneService": ["Yes", "No"],
            "MultipleLines": ["No", "Yes"],
            "InternetService": ["Fiber optic", "DSL"],
            "OnlineSecurity": ["Yes", "No"],
            "OnlineBackup": ["No", "No"],
            "DeviceProtection": ["Yes", "No"],
            "TechSupport": ["No", "Yes"],
            "StreamingTV": ["Yes", "No"],
            "StreamingMovies": ["No", "Yes"],
            "PaymentMethod": ["Bank transfer (automatic)", "Mailed check"],
            "MonthlyCharges": [80.0, 40.0],
            "tenure": [10, 5],
        }
    )

    with_counts = add_service_count(frame)
    with_autopay = add_autopay_flag(with_counts)
    with_revenue = add_observed_revenue_to_date(with_autopay)

    assert with_revenue["ServiceCount"].tolist() == [4, 3]
    assert with_revenue["IsAutoPay"].tolist() == [1, 0]
    assert with_revenue["ObservedRevenueToDate"].tolist() == [800.0, 200.0]


def test_split_features_target_excludes_target_and_identifier() -> None:
    frame = pd.DataFrame(
        {
            IDENTIFIER_COLUMN: ["A", "B"],
            "feature": [1, 2],
            TARGET_COLUMN: ["No", "Yes"],
        }
    )

    X, y = split_features_target(frame)

    assert TARGET_COLUMN not in X.columns
    assert IDENTIFIER_COLUMN not in X.columns
    assert y.tolist() == ["No", "Yes"]
