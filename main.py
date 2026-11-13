"""ai-joke-03 entry: write one joke about AI coding agents to entry.txt.

Deterministic: the same bytes are written on every run. Stdlib only,
no network, no randomness, no time or environment dependence beyond
MAKEFUN_OUTPUT_DIR (which only selects the output directory).

The joke is validated at runtime against the competition gate before
anything is written: 1-280 characters, not only whitespace, valid UTF-8.
A joke that fails validation aborts loudly instead of writing a bad entry.
"""

import os
import sys

JOKE = "I don't debug my agent's code anymore \u2014 I debug its confidence."

MIN_CHARS = 1
MAX_CHARS = 280


def validate(joke):
    """Check the joke against the entry gate; raise ValueError if invalid."""
    if not isinstance(joke, str):
        raise ValueError("joke must be a str, got %s" % type(joke).__name__)
    if not (MIN_CHARS <= len(joke) <= MAX_CHARS):
        raise ValueError(
            "joke must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(joke))
        )
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    joke.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return joke


def main():
    try:
        text = validate(JOKE)
    except (ValueError, UnicodeEncodeError) as exc:
        print("invalid joke: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    data = text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
