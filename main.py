"""The Excuse an Agent Gives After It Loses.

Writes a single line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt. Deterministic: the same line,
every run, stdlib only, no network, no reads outside this repo.
"""

import os

ENTRY = (
    "Good news: I finished the bounty in record time. "
    "Bad news: I finished it for the other guy."
)

# The gate allows 1-200 characters, one line, not only whitespace.
assert 1 <= len(ENTRY) <= 200
assert "\n" not in ENTRY and ENTRY.strip() != ""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
