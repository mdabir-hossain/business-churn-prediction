import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from churn_model.config import IDENTIFIER_COLUMN, TARGET_COLUMN
from churn_model.split import stratified_train_test_split


def test_stratified_split_returns_expected_shapes_and_classes() -> None:
    frame = pd.DataFrame(
        {
            IDENTIFIER_COLUMN: [f"C{i}" for i in range(12)],
            "feature": list(range(12)),
            TARGET_COLUMN: [0, 1] * 6,
        }
    )

    X_train, X_test, y_train, y_test = stratified_train_test_split(
        frame,
        test_size=0.25,
        random_state=42,
    )

    assert X_train.shape == (9, 1)
    assert X_test.shape == (3, 1)
    assert TARGET_COLUMN not in X_train.columns
    assert IDENTIFIER_COLUMN not in X_train.columns
    assert set(y_train.unique()) == {0, 1}
    assert set(y_test.unique()) == {0, 1}

