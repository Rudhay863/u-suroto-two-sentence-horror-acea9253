#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes the entry story to /output/entry.txt (creating /output if needed).
The story is exactly two sentences, at most 400 characters.
Deterministic: the same story is written on every run.
"""

import os
import re
import sys

STORY = (
    "Every night since the funeral, my daughter leaves a glass of milk "
    "by the back door for her grandmother. "
    "This morning the glass was empty, the door was locked from the "
    "outside, and her small footprints in the frost led away from the "
    "house, toward the cemetery."
)

OUTPUT_PATH = "/output/entry.txt"


def check_story(text: str) -> None:
    """Self-check: exactly 2 sentences, 1-400 chars, non-whitespace."""
    stripped = text.strip()
    assert stripped, "story must not be empty"
    assert 1 <= len(stripped) <= 400, f"story is {len(stripped)} chars, must be 1-400"
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", stripped) if s]
    assert len(sentences) == 2, f"story has {len(sentences)} sentences, must be exactly 2"


def main() -> int:
    check_story(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")
    print(f"Wrote {len(STORY)}-character, 2-sentence story to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
