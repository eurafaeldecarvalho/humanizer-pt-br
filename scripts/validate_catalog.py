#!/usr/bin/env python3
"""Confere o formato do catálogo e se cada exemplo antes/depois se comporta."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ptbr_humanizer.catalogo import GRUPOS, load_patterns, score  # noqa: E402

CAMPOS = (
    "id",
    "grupo",
    "nome",
    "por_que",
    "como_corrigir",
    "exemplo_antes",
    "exemplo_depois",
    "origem",
    "heuristica",
)


def main() -> int:
    erros: list[str] = []
    patterns = load_patterns()
    if len(patterns) < 40:
        erros.append(f"catálogo com {len(patterns)} padrões; o mínimo da v1 é 40")
    ids = [p["id"] for p in patterns]
    if len(ids) != len(set(ids)):
        erros.append("há id repetido")
    for p in patterns:
        nome = p.get("_arquivo", "?")
        for campo in CAMPOS:
            if not p.get(campo):
                erros.append(f"{nome}: falta {campo}")
        if p.get("id") and nome != f"{p['id']}.yaml":
            erros.append(f"{nome}: id {p['id']} não bate com o arquivo")
        if p.get("grupo") not in GRUPOS:
            erros.append(f"{nome}: grupo inválido {p.get('grupo')}")
        for texto, rotulo, minimo in (
            (p.get("por_que", ""), "por_que", 80),
            (p.get("como_corrigir", ""), "como_corrigir", 40),
            (p.get("exemplo_antes", ""), "exemplo_antes", 20),
            (p.get("exemplo_depois", ""), "exemplo_depois", 10),
        ):
            if len(texto) < minimo:
                erros.append(f"{nome}: {rotulo} curto demais ({len(texto)})")
        origem = p.get("origem") or {}
        for campo in ("modelo", "data", "prompt", "reescrita"):
            if not origem.get(campo):
                erros.append(f"{nome}: origem.{campo} vazio")
        if origem.get("data") and not str(origem["data"]).startswith("20"):
            erros.append(f"{nome}: data de origem estranha")
        if "terceiros" not in (origem.get("prompt") or ""):
            erros.append(f"{nome}: o prompt da origem não registra a regra de não copiar")
        heur = p.get("heuristica") or {}
        if heur.get("tipo") in ("regex", "regex_minimo") and not heur.get("padroes"):
            erros.append(f"{nome}: heurística sem padrões")
        contagens = score(p.get("exemplo_antes", ""), patterns)
        if contagens.get(p.get("id"), 0) < 1:
            erros.append(f"{nome}: o exemplo antes não dispara o próprio padrão")
        resto = {k: v for k, v in score(p.get("exemplo_depois", ""), patterns).items() if v}
        if resto:
            erros.append(f"{nome}: o exemplo depois ainda dispara {resto}")
    if erros:
        print("\n".join(erros))
        return 1
    print(f"catálogo ok: {len(patterns)} padrões")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
