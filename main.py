#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes a single-line weather forecast (<=120 chars) for the invented
city of Hailstone Hollow to /output/entry.txt.
"""

import os

LINE = "Hailstone Hollow, 12\u00b0C: hail at noon; each stone introduced by name, largest first, before it lands."


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
