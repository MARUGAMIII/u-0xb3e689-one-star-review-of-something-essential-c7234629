#!/usr/bin/env python3
"""One-star review of something essential (make.fun bounty).

Writes a single deadpan one-star review of sleep -- an everyday
essential -- to /output/entry.txt. Standard library only, no network,
no randomness: the output is byte-identical on every run.
"""

import os
from pathlib import Path

REVIEW = (
    "One star. Sleep promises rest, delivers dreams about being late "
    "for work, and calls it a full night."
)

MAX_CHARS = 160


def main() -> None:
    text = REVIEW.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("entry fails the 1-160 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out = Path(os.environ.get(
        "OUTPUT_PATH", os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    ))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
