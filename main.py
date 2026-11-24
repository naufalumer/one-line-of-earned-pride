#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, fully deterministic: the line is a
fixed string, no randomness, no clock, no network.

The line is a quiet, earned moment of pride: a grandmother who learned
to read at seventy-two finishes her first book on the bus home and
misses her stop on purpose.
"""

import os
import sys

LINE = "My grandmother learned to read at seventy-two, finished her first book on the bus home, and missed her stop on purpose."


def main() -> int:
    # Fail loudly rather than submit an invalid entry: the gate needs
    # 1 to 240 characters of non-whitespace UTF-8 text.
    if not (1 <= len(LINE) <= 240) or not LINE.strip():
        raise SystemExit("entry line violates the 1-240 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip verification: read the file back and confirm it holds
    # exactly the intended line, so a truncated or altered write fails
    # loudly instead of silently shipping a wrong entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit(
            "entry.txt round-trip mismatch: expected "
            f"{text!r}, got {written!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
