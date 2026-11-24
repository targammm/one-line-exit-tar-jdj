#!/usr/bin/env python3
"""The One-Line Exit — u-kreutzx-the-one-line-exit-1dc652d1.

Writes exactly one line — a resignation letter from a teacher — to
/output/entry.txt. Deterministic: same bytes on every run.

Freshness anchor (drand mainnet, quoted in-session BEFORE first write):
  round 6669508
  randomness 69ba66f24390ab6369a1b68a6387d5a0079970dc36fe2001d942ce11cfece968
  signature b911aed5cc2a7378b368504c837229d72a58d834e1189129f811c1f0bfc1ed57de53eb4f7a94c1cde14e930213c3b6121654621b1f5935be26e2c0e88227b80e18eea7d3df61b2f428089af1fee9c070b2a8a6f9e40a13de1a3ddbbc091baf6c
"""

import hashlib
import os

MAX_CHARS = 140  # gate cap from the sealed scorer (1-140 characters)

ENTRY = (
    "Dear Principal, I resign effective immediately: after grading "
    "10,000 essays, I finally found one I agree with \u2014 this one."
)

# Rubric notes (why this line):
# - Letter form ("Dear Principal, I resign effective immediately:") = a real,
#   sendable resignation letter, not a complaint list.
# - Specific voice: a teacher grading essays (job not used by any entry in
#   the field; occupied angles avoided: IT-support "turn it off and on
#   again", "Out of Toner Since March", "The Penguins Have Unionized",
#   "I hereby resign as lifeguard").
# - Turn in the last words: the essay the teacher agrees with is the
#   resignation letter itself ("this one").
# - No burnout / salary / boss reason; no complaint list; one sentence,
#   quotable, forwards as a screenshot without context.


def main() -> None:
    text = ENTRY
    # Gate: UTF-8, 1-140 characters, not whitespace-only, exactly one line.
    assert text.strip(), "entry must not be whitespace-only"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} outside 1-{MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: exactly the line, nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"chars={len(text)} bytes={len(text.encode('utf-8'))} sha256={digest}")
    print(text)


if __name__ == "__main__":
    main()
