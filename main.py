"""Entry for make.fun: "The Dog Ate My Homework: Funniest Excuse".

Writes one line (1-200 characters) to /output/entry.txt: a dog, caught
eating the homework, explains itself in its own voice. The excuse runs on
pure dog logic: it smelled of his human's hands and stress, so eating it
was protection detail -- and he did the marking too, while chewing.
"""

from pathlib import Path

# The final excuse line.
LINE = (
    "It smelled like your hands and pure stress, so I ate it before it "
    "could hurt you. I protect this family. Also, your math was wrong. "
    "I checked while chewing."
)


def build_entry() -> str:
    """Return the entry text, asserting it fits the competition gate."""
    text = LINE.strip()
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    return text


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
