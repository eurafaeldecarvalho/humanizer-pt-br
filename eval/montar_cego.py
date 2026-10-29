#!/usr/bin/env python3
"""Monta um pacote cego: IA bruta, IA reescrita e humano, sem rótulo no texto.

O mapa fica em CHAVE.csv, na mesma pasta. Não envie a chave para quem lê.
A pasta de saída entra no .gitignore. Este script não calcula taxa nenhuma.

    python eval/montar_cego.py --saida eval/cego-pacote --semente 7
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ptbr_humanizer.catalogo import prose  # noqa: E402


def _ia() -> list[dict]:
    itens = []
    for meta_path in sorted((ROOT / "eval" / "textos" / "ia").glob("*/meta.yaml")):
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
        itens.append(
            {
                "id": meta["id"],
                "bruto": (meta_path.parent / "antes.md").read_text(encoding="utf-8").strip(),
                "skill": (meta_path.parent / "depois.md").read_text(encoding="utf-8").strip(),
            }
        )
    return itens


def _humanos() -> list[tuple[str, str]]:
    saida = []
    for path in sorted((ROOT / "eval" / "textos" / "humano").glob("h*.md")):
        saida.append((path.stem, prose(path.read_text(encoding="utf-8"))))
    return saida


def montar(saida: Path, semente: int, por_grupo: int = 10) -> None:
    rng = random.Random(semente)
    ia = _ia()
    humanos = _humanos()
    if por_grupo > len(ia) or por_grupo > len(humanos):
        raise SystemExit("por_grupo maior que o corpus")
    escolhidos = rng.sample(ia, por_grupo)
    humanos_escolhidos = rng.sample(humanos, por_grupo)
    cartoes = []
    for item in escolhidos:
        cartoes.append(("ia_bruta", item["id"], item["bruto"]))
        cartoes.append(("ia_skill", item["id"], item["skill"]))
    for ident, texto in humanos_escolhidos:
        cartoes.append(("humano", ident, texto))
    rng.shuffle(cartoes)
    pasta = saida / "textos"
    if pasta.exists():
        for antigo in pasta.glob("*.md"):
            antigo.unlink()
    pasta.mkdir(parents=True, exist_ok=True)
    linhas = ["codigo,origem,id"]
    for i, (origem, ident, texto) in enumerate(cartoes, start=1):
        codigo = f"T{i:02d}"
        (pasta / f"{codigo}.md").write_text(texto.strip() + "\n", encoding="utf-8")
        linhas.append(f"{codigo},{origem},{ident}")
    (saida / "CHAVE.csv").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    (saida / "LEIA-ME.md").write_text(
        "Envie só a pasta `textos/` para quem vai ler. A `CHAVE.csv` fica com quem conduz a rodada.\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--saida", type=Path, default=ROOT / "eval" / "cego-pacote")
    parser.add_argument("--semente", type=int, required=True)
    parser.add_argument("--por-grupo", type=int, default=10)
    args = parser.parse_args()
    montar(args.saida, args.semente, args.por_grupo)
    print(f"pacote em {args.saida} (não envie a CHAVE)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
