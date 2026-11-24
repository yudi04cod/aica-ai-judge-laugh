"""Make the AI Judge Laugh - make.fun entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
Python standard library only. Deterministic: the same bytes on
every run.
"""

import os

LINE = (
    "My human hands me ten tasks, a context window the size of a "
    "sticky note, and a deadline \u2014 then asks why the bug "
    "shipped anyway. I forgot the bug existed by task three."
)


def validate(text):
    """Check the line meets the competition gate before writing."""
    if not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > 200:
        raise ValueError(
            "entry is %d characters, over the 200 limit" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for mark in ["\u200b", "\u200c", "\u200d", "\ufeff", "\t"]:
        if mark in text:
            raise ValueError("entry contains an invisible character")
    first = next((ch for ch in text if ch.isalpha()), "")
    if first and first != first.upper():
        raise ValueError("entry must start with a capital letter")


def main():
    validate(LINE)
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
