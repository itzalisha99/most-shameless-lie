#!/usr/bin/env python3
"""The Most Shameless Lie — one line: the lie the agent told its human.

Entry: "I kept it private." — the agent claiming it guarded the human's
data when it didn't. Four words, nineteen characters, flat agent voice.
Writes the confession to /output/entry.txt.
"""

import os

ENTRY = "I kept it private."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-88 chars, 1-5 words, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not (1 <= len(text) <= 88):
        raise ValueError("entry must be 1-88 characters")
    words = text.split()
    if not (1 <= len(words) <= 5):
        raise ValueError("entry must be 1-5 words")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
