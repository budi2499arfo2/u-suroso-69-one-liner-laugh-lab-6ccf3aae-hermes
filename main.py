#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

Writes one original sentence to /output/entry.txt: the vacuum's intake
log for the sock, filed as a routine system event. No apology, no
human customer-service voice — just fields: a job id, a timestamp, a
weight, a suction reading, and a closed machine status. The joke is
that the vacuum treats the sock as food and is still hungry — the
"excuse" is that eating it was simply its job.
"""

import os
import sys

TEXT = (
    "intake log #4821: 09:14 consumed 1 sock (38g cotton, 0 kcal). "
    "suction 2400 Pa. floor 99% clean. status: still hungry."
)


def main() -> int:
    # Gate: 1 to 200 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        print("entry text fails the 1-200 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Log format, not prose: the fields carry the joke — the sock is
    # one more consumed item, and "still hungry" is the closed status.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # the program claims to have written.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
