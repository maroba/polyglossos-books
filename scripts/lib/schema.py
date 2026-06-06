"""jsonschema-Validierung der YAML-Dateien."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import yaml

from .chapters import REPO_ROOT

SCHEMAS_DIR = REPO_ROOT / "schemas"


def load_schema(name: str) -> dict:
    return json.loads((SCHEMAS_DIR / f"{name}.schema.json").read_text(encoding="utf-8"))


def validate_yaml(path: Path, schema_name: str) -> list[str]:
    """Validiert eine YAML-Datei; gibt Liste von Fehlermeldungen zurück (leer = ok)."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"{path}: YAML-Syntaxfehler: {e}"]
    validator = jsonschema.Draft202012Validator(load_schema(schema_name))
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"{path}: {loc}: {err.message}")
    return errors
