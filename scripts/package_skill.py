#!/usr/bin/env python3
"""Empacota skills/humanizer-pt-br num zip instalável."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGEM = ROOT / "skills" / "humanizer-pt-br"
DESTINO = ROOT / "dist" / "humanizer-pt-br-1.0.0.zip"


def main() -> None:
    if not (ORIGEM / "SKILL.md").exists():
        raise SystemExit("rode scripts/build.py antes de empacotar")
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(DESTINO, "w", compression=zipfile.ZIP_DEFLATED) as pacote:
        for path in sorted(ORIGEM.rglob("*")):
            if path.is_file():
                pacote.write(path, Path("humanizer-pt-br") / path.relative_to(ORIGEM))
    with zipfile.ZipFile(DESTINO) as pacote:
        nomes = set(pacote.namelist())
    for obrigatorio in (
        "humanizer-pt-br/SKILL.md",
        "humanizer-pt-br/references/catalogo.md",
    ):
        if obrigatorio not in nomes:
            raise SystemExit(f"zip sem {obrigatorio}")
    print(DESTINO)


if __name__ == "__main__":
    main()
