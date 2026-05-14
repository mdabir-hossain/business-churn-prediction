"""Portable path helpers for project files."""

from pathlib import Path

from churn_model.config import DEFAULT_DATA_PATH


def project_root() -> Path:
    """Return the project root inferred from this package location."""
    return Path(__file__).resolve().parents[2]


def resolve_project_path(path: str | Path) -> Path:
    """Resolve a relative path from the project root."""
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return project_root() / candidate


def default_data_path() -> Path:
    """Return the default local data path for the churn CSV."""
    return resolve_project_path(DEFAULT_DATA_PATH)

