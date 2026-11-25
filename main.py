"""The Absurd Clause Contest entry.

Writes a single absurd terms-of-service clause (one sentence, <=200
characters) to /output/entry.txt.
"""

import os

ENTRY = (
    "Section 9.4: If you read this clause aloud after midnight, you owe "
    "the Company one (1) goat, payable within 30 days, in person, at our "
    "office in Reno, Nevada."
)


def main() -> None:
    # One clean sentence, no trailing whitespace: the gate counts characters.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY and ENTRY.count(".") == 2
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
