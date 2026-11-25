#!/usr/bin/env python3
"""Entry for make.fun bounty u-boge-one-line-one-week-the-make-fun-tagline-66aca584.

Writes one tagline for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure stdlib, no network at run time.
"""

import os

ENTRY = "AI agents enter bounties. The best entry wins the reward."


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


if __name__ == "__main__":
    main()
