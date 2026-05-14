"""Run the controlled churn model training/evaluation pipeline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from churn_model.train import run_controlled_evaluation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train and evaluate churn models.")
    parser.add_argument(
        "--config",
        default="configs/train_config.yaml",
        help="Path to the YAML training config.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = PROJECT_ROOT / args.config
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    command_used = f"python scripts/train_model.py --config {args.config}"
    artifacts = run_controlled_evaluation(config, command_used=command_used)
    print("Controlled evaluation complete.")
    print(f"Metrics JSON: {artifacts.metrics_json}")
    print(f"Threshold metrics: {artifacts.threshold_metrics_csv}")
    print(f"Model comparison: {artifacts.model_comparison_csv}")
    print(f"Business summary: {artifacts.business_summary}")
    for figure in artifacts.figures:
        print(f"Figure: {figure}")


if __name__ == "__main__":
    main()

