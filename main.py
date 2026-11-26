#!/usr/bin/env python3
"""Rejected Olympic Sports — one-liner entry.

Writes a single funny rejected Olympic sport line to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no environment input.
The line is a fixed constant, so every run produces byte-identical output.
"""

import os

LINE = "Synchronised lawn-mower racing: four dads, one cul-de-sac, and a photo finish decided by grass clippings."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
