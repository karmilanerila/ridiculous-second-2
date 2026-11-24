"""Ridiculous at First Glance, Real by the Second — backup angle.

Writes one single-sentence pitch for a bizarre startup that sounds
absurd until you realise it would actually sell: professional
mourners rented out for video calls.
"""
import os

SENTENCE = "We rent out professional mourners for video calls, because nobody wants to cry alone on Zoom anymore."

MAX_CHARS = 200


def is_single_sentence(text):
    """True when text is one sentence: no newline and exactly one
    terminal full stop, with no other sentence-ending punctuation."""
    if "\n" in text or "\r" in text:
        return False
    stripped = text.strip()
    if not stripped.endswith("."):
        return False
    return stripped.count(".") == 1 and "!" not in stripped and "?" not in stripped


def write_entry(path):
    """Write the pitch as exactly one sentence of UTF-8 text."""
    if len(SENTENCE) > MAX_CHARS or not is_single_sentence(SENTENCE):
        raise ValueError("entry must be a single sentence of at most 200 characters")
    data = SENTENCE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
