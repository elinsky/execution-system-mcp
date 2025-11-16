"""Utility functions for execution system MCP."""

import subprocess
from pathlib import Path


def git_move(source: Path, dest: Path) -> None:
    """
    Move a file using git mv to preserve history.

    Args:
        source: Source file path
        dest: Destination file path

    Raises:
        RuntimeError: If git mv command fails
    """
    try:
        result = subprocess.run(
            ["git", "mv", str(source), str(dest)],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"git mv failed: {e.stderr}") from e
