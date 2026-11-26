#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, as recorded by a cat, to /output/entry.txt.
Deterministic, stdlib-only: no input, no network, no randomness.
"""

import os

GREETING = "You've reached Miso. I'm pushing your glass off the table. Leave a message after the meow — or open the tuna. Meow."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(GREETING)


if __name__ == "__main__":
    main()
