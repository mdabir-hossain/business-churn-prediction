"""Controlled training and evaluation pipeline for churn models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from churn_model.config import (
    DEFAULT_RANDOM_STATE,
    DEFAULT_TEST_SIZE,
    IDENTIFIER_COLUMN,
    TARGET_COLUMN,
)
from churn_model.data import load_clean_telco_churn_csv
from churn_model.evaluate import evaluate_probability_predictions
from churn_model.features import engineer_safe_features, split_features_target
from churn_model.paths import resolve_project_path
from churn_model.split import stratified_train_test_split


@dataclass(frozen=True)
class EvaluationArtifacts:
    """Paths to public-safe aggregate evaluation artifacts."""

    metrics_json: Path
    threshold_metrics_csv: Path
    model_comparison_csv: Path
    business_summary: Path
    figures: list[Path]


def prepare_churn_dataframe(
    dataset_path: str | Path,
    target_column: str = TARGET_COLUMN,
    drop_missing_total_charges: bool = True,
) -> pd.DataFrame:
    """Load, clean, and add deterministic leakage-safe features."""
    frame = load_clean_telco_churn_csv(
        dataset_path,
        drop_missing_total_charges=drop_missing_total_charges,
    )
    frame = engineer_safe_features(frame)
    output = frame.copy()
    output[target_column] = (output[target_column] == "Yes").astype(int)
    return output


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Build preprocessing fitted only inside downstream model pipelines."""
    categorical_features = X.select_dtypes(include=["object", "category", "string"]).columns.tolist()
    numeric_features = X.select_dtypes(include=["int64", "int32", "float64", "float32", "bool"]).columns.tolist()
    return ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
            ("num", "passthrough", numeric_features),
        ],
        remainder="drop",
        sparse_threshold=0.0,
    )


def build_model_pipelines(
    X: pd.DataFrame,
    model_config: dict[str, Any],
    random_seed: int = DEFAULT_RANDOM_STATE,
) -> dict[str, Pipeline]:
    """Build candidate model pipelines with preprocessing inside each pipeline."""
    pipelines: dict[str, Pipeline] = {}

    if model_config.get("logistic_regression", {}).get("enabled", True):
        cfg = model_config.get("logistic_regression", {})
        pipelines["logistic_regression"] = Pipeline(
            steps=[
                ("preprocess", build_preprocessor(X)),
                (
                    "model",
                    LogisticRegression(
                        max_iter=cfg.get("max_iter", 1000),
                        class_weight=cfg.get("class_weight", "balanced"),
                        solver=cfg.get("solver", "liblinear"),
                        random_state=random_seed,
                    ),
                ),
            ]
        )

    if model_config.get("random_forest", {}).get("enabled", True):
        cfg = model_config.get("random_forest", {})
        pipelines["random_forest"] = Pipeline(
            steps=[
                ("preprocess", build_preprocessor(X)),
                (
                    "model",
                    RandomForestClassifier(
                        n_estimators=cfg.get("n_estimators", 400),
                        class_weight=cfg.get("class_weight", "balanced"),
                        n_jobs=cfg.get("n_jobs", -1),
                        random_state=random_seed,
                    ),
                ),
            ]
        )

    if model_config.get("hist_gradient_boosting", {}).get("enabled", True):
        cfg = model_config.get("hist_gradient_boosting", {})
        pipelines["hist_gradient_boosting"] = Pipeline(
            steps=[
                ("preprocess", build_preprocessor(X)),
                (
                    "model",
                    HistGradientBoostingClassifier(
                        max_iter=cfg.get("max_iter", 300),
                        learning_rate=cfg.get("learning_rate", 0.05),
                        max_depth=cfg.get("max_depth", 6),
                        random_state=random_seed,
                    ),
                ),
            ]
        )

    if not pipelines:
        raise ValueError("No model candidates are enabled in the config.")
    return pipelines


def run_controlled_evaluation(config: dict[str, Any], command_used: str) -> EvaluationArtifacts:
    """Run controlled model evaluation and save aggregate public-safe artifacts."""
    dataset_cfg = config.get("dataset", {})
    split_cfg = config.get("split", {})
    output_cfg = config.get("outputs", {})
    eval_cfg = config.get("evaluation", {})

    dataset_path = dataset_cfg.get("path", "data/telco_churn.csv")
    target_column = dataset_cfg.get("target_column", TARGET_COLUMN)
    identifier_columns = dataset_cfg.get("identifier_columns", [IDENTIFIER_COLUMN])
    test_size = split_cfg.get("test_size", DEFAULT_TEST_SIZE)
    random_seed = split_cfg.get("random_seed", DEFAULT_RANDOM_STATE)
    thresholds = eval_cfg.get("candidate_thresholds", [0.5])
    positive_label = eval_cfg.get("positive_label", 1)
    top_fraction = eval_cfg.get("top_decile_fraction", 0.1)

    frame = prepare_churn_dataframe(
        dataset_path=dataset_path,
        target_column=target_column,
        drop_missing_total_charges=dataset_cfg.get("drop_missing_total_charges", True),
    )

    X_train, X_test, y_train, y_test = stratified_train_test_split(
        frame,
        target_column=target_column,
        test_size=test_size,
        random_state=random_seed,
        drop_identifier=True,
    )

    for identifier_column in identifier_columns:
        if identifier_column in X_train.columns or identifier_column in X_test.columns:
            raise ValueError(f"Identifier column {identifier_column!r} leaked into features.")
    if target_column in X_train.columns or target_column in X_test.columns:
        raise ValueError(f"Target column {target_column!r} leaked into features.")

    pipelines = build_model_pipelines(
        X_train,
        model_config=config.get("models", {}),
        random_seed=random_seed,
    )

    all_metrics: dict[str, Any] = {}
    threshold_frames = []
    comparison_rows = []

    for model_name, pipeline in pipelines.items():
        pipeline.fit(X_train, y_train)
        if not hasattr(pipeline, "predict_proba"):
            raise ValueError(f"Model pipeline {model_name!r} does not expose predict_proba.")
        y_score = pipeline.predict_proba(X_test)[:, 1]
        metrics, threshold_frame = evaluate_probability_predictions(
            y_test.to_numpy(),
            y_score,
            thresholds=thresholds,
            default_threshold=0.5,
            top_fraction=top_fraction,
            positive_label=positive_label,
        )
        all_metrics[model_name] = metrics
        threshold_frame.insert(0, "model", model_name)
        threshold_frames.append(threshold_frame)
        comparison_rows.append(
            {
                "model": model_name,
                "roc_auc": metrics.get("roc_auc"),
                "pr_auc": metrics.get("pr_auc"),
                "precision_churn_class": metrics.get("precision_churn_class"),
                "recall_churn_class": metrics.get("recall_churn_class"),
                "f1_churn_class": metrics.get("f1_churn_class"),
                "top_decile_capture": metrics.get("top_fraction_capture"),
            }
        )

    model_comparison = pd.DataFrame(comparison_rows).sort_values("roc_auc", ascending=False)
    threshold_metrics_all = pd.concat(threshold_frames, ignore_index=True)

    metrics_json_path = resolve_project_path(output_cfg.get("metrics_json", "reports/metrics/model_metrics.json"))
    threshold_csv_path = resolve_project_path(output_cfg.get("threshold_metrics_csv", "reports/metrics/threshold_metrics.csv"))
    comparison_csv_path = resolve_project_path(output_cfg.get("model_comparison_csv", "reports/metrics/model_comparison.csv"))
    business_summary_path = resolve_project_path(output_cfg.get("business_summary", "reports/business_summary.md"))
    figures_dir = resolve_project_path(output_cfg.get("figures_dir", "reports/figures"))

    metrics_json_path.parent.mkdir(parents=True, exist_ok=True)
    threshold_csv_path.parent.mkdir(parents=True, exist_ok=True)
    comparison_csv_path.parent.mkdir(parents=True, exist_ok=True)
    business_summary_path.parent.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    threshold_metrics_all.to_csv(threshold_csv_path, index=False)
    model_comparison.to_csv(comparison_csv_path, index=False)

    figure_paths = save_safe_figures(model_comparison, figures_dir)

    provenance = {
        "run_datetime_utc": datetime.now(timezone.utc).isoformat(),
        "dataset_path": dataset_path,
        "row_count_after_cleaning": int(len(frame)),
        "target_distribution_after_cleaning": {
            str(key): int(value) for key, value in frame[target_column].value_counts().sort_index().items()
        },
        "split_method": "stratified_train_test_split",
        "test_size": test_size,
        "random_seed": random_seed,
        "model_names": list(pipelines.keys()),
        "selected_threshold_policy": eval_cfg.get("threshold_policy", "not_selected"),
        "candidate_thresholds": thresholds,
        "command_used": command_used,
        "public_safety": "aggregate metrics only; no row-level predictions saved",
    }

    payload = {
        "provenance": provenance,
        "metrics": all_metrics,
    }
    metrics_json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    write_business_summary(
        business_summary_path,
        model_comparison,
        threshold_metrics_all,
        metrics_json_path,
        threshold_csv_path,
        comparison_csv_path,
    )

    return EvaluationArtifacts(
        metrics_json=metrics_json_path,
        threshold_metrics_csv=threshold_csv_path,
        model_comparison_csv=comparison_csv_path,
        business_summary=business_summary_path,
        figures=figure_paths,
    )


def save_safe_figures(model_comparison: pd.DataFrame, figures_dir: Path) -> list[Path]:
    """Save aggregate, public-safe model comparison figures."""
    paths: list[Path] = []
    for metric in ["roc_auc", "pr_auc", "recall_churn_class"]:
        if metric not in model_comparison.columns:
            continue
        fig, ax = plt.subplots(figsize=(8, 4.5))
        model_comparison.plot(kind="bar", x="model", y=metric, legend=False, ax=ax)
        ax.set_title(metric.replace("_", " ").title())
        ax.set_xlabel("Model")
        ax.set_ylabel(metric.replace("_", " ").title())
        ax.set_ylim(0, 1)
        fig.tight_layout()
        path = figures_dir / f"{metric}_comparison.png"
        fig.savefig(path, dpi=150)
        plt.close(fig)
        paths.append(path)
    return paths


def write_business_summary(
    path: Path,
    model_comparison: pd.DataFrame,
    threshold_metrics: pd.DataFrame,
    metrics_json_path: Path,
    threshold_csv_path: Path,
    comparison_csv_path: Path,
) -> None:
    """Write a business-friendly aggregate summary without ROI claims."""
    best_model = model_comparison.iloc[0]["model"] if not model_comparison.empty else "to be confirmed"
    content = f"""# Business Summary

This summary is generated from aggregate Phase 5 evaluation artifacts. It does not contain row-level customer predictions and does not claim causal business impact.

## Evaluation Outputs

- Metrics JSON: `{metrics_json_path.as_posix()}`
- Threshold metrics CSV: `{threshold_csv_path.as_posix()}`
- Model comparison CSV: `{comparison_csv_path.as_posix()}`

## Model Review

The highest-ranked model by ROC-AUC in the controlled run is `{best_model}`. Model selection should not rely on a single metric: churn decisions also need recall, precision, PR-AUC, calibration, retention capacity, and threshold trade-off review.

## False Positives And False Negatives

- False positives are customers flagged as likely churners who would not churn. These can create unnecessary contact cost, discount leakage, or customer fatigue.
- False negatives are likely churners missed by the model. These can represent missed retention opportunities.

## Threshold Trade-Offs

Lower thresholds usually identify more potential churners but increase false positives. Higher thresholds usually focus on fewer, higher-risk customers but may miss more churners. Any selected threshold should reflect retention team capacity, intervention cost, and acceptable customer-contact volume.

## Responsible Interpretation

The model identifies predictive associations, not causal drivers. Recommendations should be framed as prioritisation ideas for further business review, not proof that changing a feature will reduce churn.
"""
    path.write_text(content, encoding="utf-8")
