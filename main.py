"""Six Words, One Story -- make.fun entry.

Writes one complete six-word story to /output/entry.txt.
A lifetime of waiting ends in one unexpected apology.
Pure standard library; deterministic; no network, no clock, no files read.
"""

import os

# One lifetime, one meeting, one apology.
STORY = "I finally met God. He apologized."
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """The sealed gate: UTF-8 text, 1-60 chars, exactly six words.

    Every word must earn its place: six words, one whole story.
    """
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"expected exactly 6 words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"entry must be 1-60 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
