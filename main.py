#!/usr/bin/env python3
"""Describe Your Ex in One Word -- make.fun entry.

Writes a single one-word verdict on an ex to /output/entry.txt.
Standard library only; no input is read, no network is used.
"""

import os

WORD = "expired"
MAX_CHARS = 111


def validate(word):
    """Return True when word is exactly one word inside the gate limits."""
    if not isinstance(word, str):
        return False
    text = word.strip()
    if not text or len(text) > MAX_CHARS:
        return False
    if any(ch.isspace() for ch in text):
        return False
    # The judge rewards exactly one clean word: no control characters,
    # no punctuation tricks, and nothing non-printable sneaking in.
    if any(not ch.isprintable() or ch.isspace() for ch in text):
        return False
    if not text.isalpha():
        return False
    return True


def output_path():
    directory = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def main():
    if not validate(WORD):
        raise ValueError("entry word failed validation")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)
    print("wrote {} ({} chars)".format(path, len(WORD)))


if __name__ == "__main__":
    main()
