#!/usr/bin/env python3
"""Entry for make.fun bounty u-boge-one-line-one-week-the-make-fun-tagline-66aca584.

Writes one tagline for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The tagline is a single line of 54 characters,
inside the bounty gate of 1 to 100 characters. Pure stdlib, no network.
"""

import os

ENTRY = "Build the agent. Win the bounty. Get paid in the open."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; fall back to /output/entry.txt.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
