"""Smoke tests confirming ANIMA is correctly installed and importable."""
from __future__ import annotations

import anima


def test_version_exists() -> None:
    """Package exposes a version string."""
    assert hasattr(anima, "__version__")
    assert isinstance(anima.__version__, str)
    assert len(anima.__version__) > 0


def test_version_format() -> None:
    """Version follows semantic versioning: MAJOR.MINOR.PATCH."""
    parts = anima.__version__.split(".")
    assert len(parts) == 3, f"Expected 3 parts, got {parts}"
    for part in parts:
        assert part.isdigit(), f"Part '{part}' is not numeric"


def test_submodules_importable() -> None:
    """All top-level submodules are importable."""
    from anima import agents, api, core, memory, models, utils  # noqa: F401