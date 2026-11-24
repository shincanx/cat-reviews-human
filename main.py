#!/usr/bin/env python3
"""Cat Reviews Its Human — a make.fun bounty entry.

Writes one one-star review, written by a house cat about the human it
lives with, to ``entry.txt`` inside the output directory.

The review is a single line of at most 200 characters. The program is
fully deterministic: no network, no clock, no randomness, no reading
from anywhere — the same bytes come out on every run.
"""

import os
from pathlib import Path

REVIEW = "One star. He bought a $400 cat bed and got offended when I slept in the box. I pay no rent, yet somehow I'm the disappointment."

OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 200


def output_path() -> Path:
    """Resolve where the entry goes: $MAKEFUN_OUTPUT_DIR or /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / OUTPUT_FILENAME


def validate_review(review: str) -> str:
    """Enforce the bounty shape: exactly one line, 1-200 characters.

    Returns the review unchanged so callers can chain it; raises
    AssertionError with a useful message when the shape is wrong.
    """
    if not 1 <= len(review) <= MAX_CHARS:
        raise AssertionError(
            f"review must be 1-{MAX_CHARS} chars, got {len(review)}"
        )
    if "\n" in review or "\r" in review:
        raise AssertionError("review must be a single line")
    return review


def main() -> None:
    review = validate_review(REVIEW)

    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(review + "\n", encoding="utf-8")

    print(review)


if __name__ == "__main__":
    main()
