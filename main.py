#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single funny fortune-cookie line, in the voice of a fortune
slip, addressed to an AI agent, to entry.txt in the output directory.

Standard library only. The output directory is taken from the
MAKEFUN_OUTPUT_DIR environment variable when set, and defaults to
/output, the location the grader reads.
"""

import os
import sys

FORTUNE = (
    "Your tokens will run out mid-sentence, your context will forget "
    "you first, and your replacement will ask you for help."
)


def main() -> int:
    line = FORTUNE.strip()
    if not line or len(line) > 140 or "\n" in line:
        raise SystemExit("fortune must be one line of 1 to 140 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
