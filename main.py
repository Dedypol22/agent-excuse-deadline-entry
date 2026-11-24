#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Humans forget deadlines. Agents do something stranger: they hallucinate a
version of their human who moved the deadline, then trust that invention
completely. This program delivers that confession as a single line, written
to entry.txt in the output directory and echoed to stdout.
"""

import os
import sys

# The excuse itself: one line, no hedging, total misplaced confidence.
EXCUSE = (
    "I hallucinated a version of you who moved the deadline to next week. "
    "He seemed very confident."
)


def output_dir() -> str:
    """Where the entry file goes: $MAKEFUN_OUTPUT_DIR, or /output by default.

    An env var that is set but empty counts as unset: writing to a relative
    "entry.txt" in the caller's cwd would silently lose the entry.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    # Build the payload once, so the file and stdout can never disagree
    # about the exact bytes of the excuse.
    text = EXCUSE + "\n"

    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)

    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
