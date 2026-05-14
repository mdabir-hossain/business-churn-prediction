import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from churn_model.config import IDENTIFIER_COLUMN, TARGET_COLUMN
from churn_model.features import engineer_safe_features, split_features_target
from churn_model.train import build_model_pipelines


def test_pipeline_construction_excludes_identifier_and_target() -> None:
    frame = pd.DataFrame(
        {
            IDENTIFIER_COLUMN: ["A", "B", "C", "D"],
            "gender": ["Female", "Male", "Female", "Male"],
            "SeniorCitizen": [0, 1, 0, 1],
            "Partner": ["Yes", "No", "No", "Yes"],
            "Dependents": ["No", "No", "Yes", "No"],
            "tenure": [1, 2, 3, 4],
            "PhoneService": ["Yes", "Yes", "No", "Yes"],
            "MultipleLines": ["No", "Yes", "No phone service", "No"],
            "InternetService": ["DSL", "Fiber optic", "DSL", "No"],
            "OnlineSecurity": ["No", "Yes", "No", "No internet service"],
            "OnlineBackup": ["Yes", "No", "No", "No internet service"],
            "DeviceProtection": ["No", "Yes", "No", "No internet service"],
            "TechSupport": ["No", "No", "Yes", "No internet service"],
            "StreamingTV": ["No", "Yes", "No", "No internet service"],
            "StreamingMovies": ["No", "No", "Yes", "No internet service"],
            "Contract": ["Month-to-month", "One year", "Two year", "Month-to-month"],
            "PaperlessBilling": ["Yes", "No", "Yes", "No"],
            "PaymentMethod": [
                "Electronic check",
                "Bank transfer (automatic)",
                "Mailed check",
                "Credit card (automatic)",
            ],
            "MonthlyCharges": [30.0, 70.0, 50.0, 20.0],
            "TotalCharges": [30.0, 140.0, 150.0, 80.0],
            TARGET_COLUMN: [0, 1, 0, 1],
        }
    )
    engineered = engineer_safe_features(frame)
    X, _ = split_features_target(engineered)

    pipelines = build_model_pipelines(
        X,
        model_config={
            "logistic_regression": {"enabled": True},
            "random_forest": {"enabled": False},
            "hist_gradient_boosting": {"enabled": False},
        },
        random_seed=42,
    )

    assert list(pipelines) == ["logistic_regression"]
    assert IDENTIFIER_COLUMN not in X.columns
    assert TARGET_COLUMN not in X.columns

