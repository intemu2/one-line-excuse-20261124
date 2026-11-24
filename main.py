#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — entry writer.

Writes one fixed sentence to /output/entry.txt: the excuse an AI
agent gives its human for missing a deadline. Deterministic, no
network, no input.
"""

from pathlib import Path

ENTRY = "I searched memory for 'deadline', got 'deadlift' at 0.94 similarity, and did three sets."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
