"""Project-level constants for the churn modelling workflow."""

from pathlib import Path

PROJECT_NAME = "business-churn-prediction"

TARGET_COLUMN = "Churn"
IDENTIFIER_COLUMN = "customerID"
EXCLUDED_IDENTIFIER_COLUMNS = [IDENTIFIER_COLUMN]
SAFE_FEATURE_EXCLUSIONS = [TARGET_COLUMN, IDENTIFIER_COLUMN]

DATA_DIR = Path("data")
SAMPLE_DATA_DIR = DATA_DIR / "sample"
DEFAULT_DATA_FILENAME = "telco_churn.csv"
DEFAULT_DATA_PATH = DATA_DIR / DEFAULT_DATA_FILENAME

SERVICE_COLUMNS = [
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
]

RAW_REQUIRED_COLUMNS = [
    IDENTIFIER_COLUMN,
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges",
    TARGET_COLUMN,
]

DEFAULT_RANDOM_STATE = 42
DEFAULT_TEST_SIZE = 0.2

PROPOSED_PREDICTION_MOMENT = "End of billing cycle before the future churn outcome"
PROPOSED_PREDICTION_WINDOW = "Next billing period or near-term retention window"
