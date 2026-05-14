"""Train/test split helpers."""

import pandas as pd
from sklearn.model_selection import train_test_split

from churn_model.config import DEFAULT_RANDOM_STATE, DEFAULT_TEST_SIZE, TARGET_COLUMN
from churn_model.data import validate_columns_present
from churn_model.features import split_features_target


def stratified_train_test_split(
    frame: pd.DataFrame,
    target_column: str = TARGET_COLUMN,
    test_size: float = DEFAULT_TEST_SIZE,
    random_state: int = DEFAULT_RANDOM_STATE,
    drop_identifier: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Create a stratified train/test split from a labelled dataframe."""
    validate_columns_present(frame, [target_column])
    X, y = split_features_target(
        frame,
        target_column=target_column,
        drop_identifier=drop_identifier,
    )
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

