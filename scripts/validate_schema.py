#!/usr/bin/env python3
"""Validiert alle curriculum.yaml und meta.yaml gegen ihre JSON-Schemas.

Aufruf: .venv/bin/python scripts/validate_schema.py [buch]
Exit-Code 1 bei Fehlern.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


import sys

from lib.chapters import BOOKS_DIR
from lib.schema import validate_yaml


def main() -> int:
    books = [sys.argv[1]] if len(sys.argv) > 1 else [d.name for d in sorted(BOOKS_DIR.iterdir()) if d.is_dir()]
    errors = []
    checked = 0
    for book in books:
        bdir = BOOKS_DIR / book
        curriculum = bdir / "curriculum.yaml"
        if curriculum.exists():
            errors += validate_yaml(curriculum, "curriculum")
            checked += 1
        for meta in sorted(bdir.glob("chapters/*/meta.yaml")):
            errors += validate_yaml(meta, "chapter-meta")
            checked += 1
    for e in errors:
        print(f"FEHLER  {e}")
    print(f"\n{checked} Datei(en) geprüft, {len(errors)} Fehler.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
