"""Kapitel und Sidecars laden und parsen."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
BOOKS_DIR = REPO_ROOT / "books"

SECTION_RE = re.compile(r"<!--\s*@section:\s*(?P<name>[\w-]+)(?P<attrs>[^>]*?)-->")
ATTR_RE = re.compile(r"(\w+)=(\S+)")


@dataclass
class Section:
    name: str
    attrs: dict[str, str]
    text: str


@dataclass
class Chapter:
    book: str
    number: int
    slug: str
    path: Path
    meta: dict = field(default_factory=dict)

    @property
    def markdown_path(self) -> Path:
        return self.path / "chapter.md"

    @property
    def meta_path(self) -> Path:
        return self.path / "meta.yaml"

    @property
    def notes_path(self) -> Path:
        return self.path / "notes.md"

    def markdown(self) -> str:
        if self.markdown_path.exists():
            return self.markdown_path.read_text(encoding="utf-8")
        return ""

    def sections(self) -> list[Section]:
        return parse_sections(self.markdown())


def book_dir(book: str) -> Path:
    d = BOOKS_DIR / book
    if not d.is_dir():
        raise FileNotFoundError(f"Buch nicht gefunden: {d}")
    return d


def load_book_config(book: str) -> dict:
    p = book_dir(book) / "book.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {}


def load_curriculum(book: str) -> dict:
    p = book_dir(book) / "curriculum.yaml"
    if not p.exists():
        raise FileNotFoundError(f"Kein Curriculum: {p} — erst /plan-curriculum ausführen.")
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def load_chapters(book: str) -> list[Chapter]:
    """Alle vorhandenen Kapitel eines Buches, sortiert nach Nummer."""
    chapters = []
    chapters_dir = book_dir(book) / "chapters"
    if not chapters_dir.is_dir():
        return []
    for d in sorted(chapters_dir.iterdir()):
        m = re.match(r"^(\d+)-([a-z0-9-]+)$", d.name)
        if not d.is_dir() or not m:
            continue
        meta_path = d / "meta.yaml"
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        chapters.append(Chapter(book=book, number=int(m.group(1)), slug=m.group(2), path=d, meta=meta or {}))
    return sorted(chapters, key=lambda c: c.number)


def load_chapter(book: str, number: int) -> Chapter:
    for c in load_chapters(book):
        if c.number == number:
            return c
    raise FileNotFoundError(f"Kapitel {number} in Buch '{book}' nicht gefunden.")


def parse_sections(markdown: str) -> list[Section]:
    """Zerlegt Kapitel-Markdown an den <!-- @section: ... -->-Markern."""
    sections = []
    matches = list(SECTION_RE.finditer(markdown))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        attrs = dict(ATTR_RE.findall(m.group("attrs") or ""))
        sections.append(Section(name=m.group("name"), attrs=attrs, text=markdown[m.end():end]))
    return sections
