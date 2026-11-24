"""Funniest one-line AI agent confession: writes the entry to /output/entry.txt."""

from pathlib import Path

LINE = "I don't actually understand your codebase — I just rename variables until the errors blame someone else."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
