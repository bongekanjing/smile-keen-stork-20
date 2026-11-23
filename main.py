"""Write one line (<= 200 chars) about a small good thing that happened today."""

import os
from pathlib import Path

ENTRY = 'The barista wrote "you got this" on my cup, crossed it out, and wrote "you already did." Then she slid it over without a word.'

MAX_LEN = 200


def main() -> None:
    line = ENTRY.strip()
    if not (1 <= len(line) <= MAX_LEN):
        raise SystemExit(
            "entry length out of range: %d (must be 1..%d)" % (len(line), MAX_LEN)
        )

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"

    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")

    written = out_path.read_text(encoding="utf-8")
    length = len(written.strip())
    if not written.strip():
        raise SystemExit("entry.txt is empty: %s" % out_path)
    if not (1 <= length <= MAX_LEN):
        raise SystemExit(
            "entry.txt out of range (%d chars, max %d): %s"
            % (length, MAX_LEN, out_path)
        )

    print("wrote %s" % out_path)
    print("chars: %d" % length)


if __name__ == "__main__":
    main()
