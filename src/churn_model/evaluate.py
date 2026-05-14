"""Evaluation helpers for controlled model evaluation."""

from typing import Any

import numpy as np
import pandas as pd
from sklearn.metrics import (
    average_precision_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    precision_recall_fscore_support,
    recall_score,
    roc_auc_score,
)


def predictions_at_threshold(probabilities: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """Convert predicted probabilities into binary labels at a threshold."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    return (np.asarray(probabilities) >= threshold).astype(int)


def binary_classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_score: np.ndarray | None = None,
    positive_label: int = 1,
) -> dict[str, Any]:
    """Calculate standard binary classification metrics from provided arrays.

    This helper does not load data, train models, or generate project metrics by
    itself. Use it only with explicit validation outputs in a controlled phase.
    """
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=[positive_label],
        average="binary",
        pos_label=positive_label,
        zero_division=0,
    )
    metrics: dict[str, Any] = {
        "precision_churn_class": float(precision),
        "recall_churn_class": float(recall),
        "f1_churn_class": float(f1),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "classification_report": classification_report(
            y_true,
            y_pred,
            output_dict=True,
            zero_division=0,
        ),
    }
    if y_score is not None:
        metrics["roc_auc"] = float(roc_auc_score(y_true, y_score))
        metrics["pr_auc"] = float(average_precision_score(y_true, y_score))
    return metrics


def threshold_metrics(
    y_true: np.ndarray,
    y_score: np.ndarray,
    thresholds: list[float],
    positive_label: int = 1,
) -> pd.DataFrame:
    """Return threshold-specific churn-class metrics."""
    rows = []
    for threshold in thresholds:
        y_pred = predictions_at_threshold(y_score, threshold)
        matrix = confusion_matrix(y_true, y_pred, labels=[0, positive_label])
        rows.append(
            {
                "threshold": threshold,
                "precision_churn_class": precision_score(
                    y_true, y_pred, pos_label=positive_label, zero_division=0
                ),
                "recall_churn_class": recall_score(
                    y_true, y_pred, pos_label=positive_label, zero_division=0
                ),
                "f1_churn_class": f1_score(
                    y_true, y_pred, pos_label=positive_label, zero_division=0
                ),
                "true_negatives": int(matrix[0, 0]),
                "false_positives": int(matrix[0, 1]),
                "false_negatives": int(matrix[1, 0]),
                "true_positives": int(matrix[1, 1]),
            }
        )
    return pd.DataFrame(rows)


def top_fraction_capture(
    y_true: np.ndarray,
    y_score: np.ndarray,
    fraction: float = 0.1,
    positive_label: int = 1,
) -> float:
    """Calculate positive-class capture in the highest-risk fraction."""
    if not 0 < fraction <= 1:
        raise ValueError("fraction must be greater than 0 and less than or equal to 1")
    y_true_array = np.asarray(y_true)
    y_score_array = np.asarray(y_score)
    total_positives = np.sum(y_true_array == positive_label)
    if total_positives == 0:
        return 0.0
    top_n = max(1, int(np.ceil(len(y_true_array) * fraction)))
    top_indices = np.argsort(y_score_array)[::-1][:top_n]
    captured = np.sum(y_true_array[top_indices] == positive_label)
    return float(captured / total_positives)


def evaluate_probability_predictions(
    y_true: np.ndarray,
    y_score: np.ndarray,
    thresholds: list[float],
    default_threshold: float = 0.5,
    top_fraction: float = 0.1,
    positive_label: int = 1,
) -> tuple[dict[str, Any], pd.DataFrame]:
    """Evaluate probability outputs without loading data or training models."""
    y_pred = predictions_at_threshold(y_score, default_threshold)
    metrics = binary_classification_metrics(
        y_true,
        y_pred,
        y_score=y_score,
        positive_label=positive_label,
    )
    metrics["default_threshold"] = default_threshold
    metrics["top_fraction"] = top_fraction
    metrics["top_fraction_capture"] = top_fraction_capture(
        y_true,
        y_score,
        fraction=top_fraction,
        positive_label=positive_label,
    )
    return metrics, threshold_metrics(
        y_true,
        y_score,
        thresholds=thresholds,
        positive_label=positive_label,
    )
