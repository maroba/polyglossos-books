#!/usr/bin/env python3
"""Baut die GitHub-Pages-Site nach _site/.

  python3 scripts/build_site.py [--out DIR]

Pro Buch mit vorhandenen Kapiteln:
  - Kapitel rendern (Vokabelboxen aus meta.yaml)
  - pandoc chunkedhtml → _site/<buch>/   (eine HTML-Seite pro Kapitel)
  - PDF/EPUB aus books/<buch>/dist/ kopieren, falls vorhanden (werden lokal
    mit `make release/<buch>` gebaut — CI baut nur HTML)
Dazu eine Landing-Page _site/index.html mit allen Büchern.

Benötigt nur pyyaml + pandoc (kein spacy, kein LaTeX) — läuft so in CI.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import argparse
import html
import shutil
import subprocess

import yaml

from lib.chapters import BOOKS_DIR, REPO_ROOT, load_book_config, load_chapters
from build_chapter import render

SITE_CSS = REPO_ROOT / "shared" / "pandoc" / "site.css"


def build_book_html(book: str, out_dir: Path) -> int:
    """Rendert die Kapitel und baut die chunkedhtml-Version. Gibt Kapitelzahl zurück."""
    chapters = [c for c in load_chapters(book) if c.markdown_path.exists()]
    if not chapters:
        return 0
    rendered_dir = BOOKS_DIR / book / "build" / "rendered"
    rendered_dir.mkdir(parents=True, exist_ok=True)
    rendered_files = []
    for ch in chapters:
        f = rendered_dir / f"{ch.number:02d}-{ch.slug}.md"
        f.write_text(render(ch), encoding="utf-8")
        rendered_files.append(f)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    subprocess.run(
        ["pandoc", "-d", "shared/pandoc/html.yaml",
         "--metadata-file", f"books/{book}/book.yaml",
         *[str(f) for f in rendered_files],
         "-o", str(out_dir)],
        cwd=REPO_ROOT, check=True,
    )
    shutil.copy(SITE_CSS, out_dir / "site.css")
    return len(chapters)


def copy_dist(book: str, out_dir: Path) -> dict[str, str]:
    """Kopiert PDF/EPUB aus dist/ in die Site; gibt {format: dateiname} zurück."""
    downloads = {}
    dist = BOOKS_DIR / book / "dist"
    for ext in ("pdf", "epub"):
        src = dist / f"{book}.{ext}"
        if src.exists():
            out_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, out_dir / src.name)
            downloads[ext] = src.name
    return downloads


def book_card(book: str, cfg: dict, n_chapters: int, downloads: dict[str, str]) -> str:
    title = html.escape(cfg.get("title", book))
    subtitle = html.escape(cfg.get("subtitle", ""))
    links = []
    if n_chapters:
        links.append(f'<a class="read" href="{book}/index.html">Online lesen</a>')
        links.append(f"<span>{n_chapters} Kapitel</span>")
    else:
        links.append("<span>in Vorbereitung</span>")
    for ext, fname in downloads.items():
        links.append(f'<a href="{book}/{fname}">{ext.upper()}</a>')
    return (
        f'<div class="card"><h2>{title}</h2>'
        f"<p>{subtitle}</p>"
        f'<p class="links">{" · ".join(links)}</p></div>'
    )


def landing_page(cards: list[str]) -> str:
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Polyglossos — Sprachlehrbücher</title>
<link rel="stylesheet" href="site.css">
</head>
<body>
<h1>Polyglossos</h1>
<p>Sprachlehrbücher für Deutschsprachige — vom ersten Wort (A0) bis zur
fortgeschrittenen Sprachverwendung (C1).</p>
{"".join(cards)}
<footer>Erstellt mit dem Polyglossos-Autorensystem.</footer>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=REPO_ROOT / "_site")
    args = ap.parse_args()

    site = args.out
    if site.exists():
        shutil.rmtree(site)
    site.mkdir(parents=True)
    shutil.copy(SITE_CSS, site / "site.css")

    cards = []
    for bdir in sorted(BOOKS_DIR.iterdir()):
        if not bdir.is_dir() or not (bdir / "book.yaml").exists():
            continue
        book = bdir.name
        cfg = load_book_config(book)
        out_dir = site / book
        n = build_book_html(book, out_dir)
        downloads = copy_dist(book, out_dir)
        cards.append(book_card(book, cfg, n, downloads))
        print(f"{book}: {n} Kapitel, Downloads: {', '.join(downloads) or 'keine'}")

    (site / "index.html").write_text(landing_page(cards), encoding="utf-8")
    (site / ".nojekyll").write_text("", encoding="utf-8")
    print(f"→ {site}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
