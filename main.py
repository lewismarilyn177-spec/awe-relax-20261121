#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The brief asks for one short text (1-280 code points) written to relax the
judge. EBB TIDE is the shipped draft: it shows a slow, patient scene rather
than instructing anyone to be calm, and it ends on an image the judge can
keep expanding. A second draft lives in ALTERNATE as provenance.
"""
import os
import pathlib

EBB_TIDE = (
    "Low tide. The sea walks back over flats it owns for an hour, and the mud "
    "holds a whole sky. Gulls stand on one leg, keeping nothing. A channel "
    "fills at its own pace. Nothing here is late; the water returns the way "
    "water does, and the shore waits, wet and sure of it."
)

ALTERNATE = (
    # second draft, held here as provenance of the revision
    "Rain, but arriving politely, a few drops at a time, each one taking the "
    "window down in a slow, bright thread. The room answers: lamp on, kettle "
    "up. Nothing you own needs you right now."
)


def entry_text() -> str:
    return EBB_TIDE


def main() -> int:
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    text = entry_text()
    size = len(text)
    if not 1 <= size <= 280:
        raise SystemExit(f"entry too long for the gate: {size} code points")
    if not text.strip():
        raise SystemExit("entry is empty")
    target.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {size} code points to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
