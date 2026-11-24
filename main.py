#!/usr/bin/env python3
"""Write the one-line developer excuse to /output/entry.txt.

The line is fixed and deterministic: the same 140-character line on every
run, no randomness, no network, no environment reads.

Structure (winner pattern from finished one-liner finals: 2-beat + reveal):
setup "shipped this fix 14 times since March" (specific number), escalation
"rolls it back every night at 2 AM" (the fix was never the problem), reveal
"the rollback is automated now. We named it Steve." (named character).
Chosen by internal pairwise judging over 6 variants against the judge's
lexicographic criteria in RULES.txt: this was the only variant with
escalation AND a specific number AND a named character.
"""

import os

LINE = "I've shipped this fix 14 times since March \u2014 production rolls it back every night at 2 AM. The rollback is automated now. We named it Steve."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
