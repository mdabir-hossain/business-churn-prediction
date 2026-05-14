import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from churn_model.evaluate import (
    evaluate_probability_predictions,
    predictions_at_threshold,
    threshold_metrics,
    top_fraction_capture,
)


def test_predictions_at_threshold() -> None:
    probabilities = np.array([0.1, 0.5, 0.9])

    assert predictions_at_threshold(probabilities, threshold=0.5).tolist() == [0, 1, 1]


def test_threshold_metrics_use_synthetic_arrays() -> None:
    y_true = np.array([0, 0, 1, 1])
    y_score = np.array([0.1, 0.4, 0.6, 0.9])

    rows = threshold_metrics(y_true, y_score, thresholds=[0.5])

    assert rows.shape[0] == 1
    assert rows.loc[0, "true_positives"] == 2
    assert rows.loc[0, "false_positives"] == 0


def test_evaluate_probability_predictions_returns_metrics_and_thresholds() -> None:
    y_true = np.array([0, 0, 1, 1])
    y_score = np.array([0.1, 0.4, 0.6, 0.9])

    metrics, thresholds = evaluate_probability_predictions(
        y_true,
        y_score,
        thresholds=[0.5],
        top_fraction=0.5,
    )

    assert "roc_auc" in metrics
    assert "pr_auc" in metrics
    assert thresholds.loc[0, "recall_churn_class"] == 1.0
    assert top_fraction_capture(y_true, y_score, fraction=0.5) == 1.0

