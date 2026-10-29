#!/usr/bin/env python3
"""Testes das heurísticas e da checagem de fatos. Não fala com a rede."""

from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eval import detector  # noqa: E402
from ptbr_humanizer.catalogo import (  # noqa: E402
    extract_numbers,
    load_patterns,
    score,
)
from ptbr_humanizer.ngrams import eh_trecho, trechos  # noqa: E402


def test_numeros() -> None:
    texto = "Boleto R$ 1.870,40 em 21/10/2026 às 16h, versão 4.12.0, mais 3º e 50%."
    achados = extract_numbers(texto)
    for token in ("1.870,40", "21/10/2026", "16h", "4.12.0", "3º", "50%"):
        assert token in achados, achados
    from ptbr_humanizer.catalogo import numbers_missing

    assert numbers_missing("são 14 pendências", "são 14 pendências") == []
    assert numbers_missing("são 14 pendências", "são pendências") == ["14"]
    assert numbers_missing("meta de 220", "eram 1220 casos") == ["220"]


def test_triade_nao_pega_lista_concreta() -> None:
    pats = load_patterns()
    assert score("Na mesa tinha café, pão e manteiga.", pats)["triade-adjetivos"] == 0
    assert score("O material é robusto, abrangente e estratégico.", pats)["triade-adjetivos"] == 1


def test_conectivo_precisa_de_dois() -> None:
    pats = load_patterns()
    um = score("O café está incluso. Além disso, a loja abre cedo.", pats)
    dois = score("O café está incluso. Além disso, a loja abre cedo. Ademais, o clube é na quinta.", pats)
    assert um["conectivo-empilhado"] == 0
    assert dois["conectivo-empilhado"] >= 2


def test_emoji_e_titulo() -> None:
    pats = load_patterns()
    assert score("Abrimos em novembro. 🚀", pats)["emoji-de-modelo"] == 0
    assert score("Abrimos em novembro. 🚀✨", pats)["emoji-de-modelo"] == 2
    assert score("Como validar CPF em Python.\n", pats)["titulo-title-case"] == 0
    assert score("Como Validar CPF Em Python Com Clareza\n", pats)["titulo-title-case"] == 1


def test_travessao_ignora_dialogo() -> None:
    pats = load_patterns()
    dialogo = "Ele olhou a canoa. — Bonita canoa! — Antes assim! — Como obedece!"
    assert score(dialogo, pats)["travessao-parentetico"] == 0
    pares = (
        "O relatório — versão interna — saiu, e as pendências — todas de Barretos — ficaram."
    )
    assert score(pares, pats)["travessao-parentetico"] == 2


def test_frontmatter_nao_conta() -> None:
    pats = load_patterns()
    texto = "---\nnota: Vale ressaltar que isto é metadado.\n---\n\nO boleto vence sexta.\n"
    assert score(texto, pats)["vale-ressaltar"] == 0


def test_ngramas_de_trecho() -> None:
    frase = "a controladoria validou o relatório em outubro de 2026 sem atraso"
    assert trechos(frase) == trechos(frase.upper())
    so_funcao = ("a", "de", "que", "se", "o", "em", "não", "é")
    assert eh_trecho(so_funcao) is False


def test_manifesto_humano() -> None:
    pasta = ROOT / "eval" / "textos" / "humano"
    linhas = [
        ln for ln in (pasta / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines() if ln.strip()
    ]
    assert len(linhas) == 30
    for linha in linhas:
        digest, nome = linha.split()
        atual = hashlib.sha256((pasta / nome).read_bytes()).hexdigest()
        assert atual == digest, nome


def test_corpus_real() -> None:
    rel = detector.medir()
    assert rel["n_ia"] == 30
    assert rel["n_humano"] == 30
    assert not detector.problemas(rel)


def test_pacote_cego_nao_vaza_rotulo() -> None:
    sys.path.insert(0, str(ROOT / "eval"))
    import montar_cego

    with tempfile.TemporaryDirectory() as tmp:
        montar_cego.montar(Path(tmp), semente=7, por_grupo=2)
        textos = list(Path(tmp, "textos").glob("*.md"))
        assert len(textos) == 6
        chave = (Path(tmp) / "CHAVE.csv").read_text(encoding="utf-8")
        for path in textos:
            corpo = path.read_text(encoding="utf-8")
            assert "antes da skill" not in corpo
            assert "domínio público" not in corpo
            assert path.stem in chave


def main() -> int:
    testes = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in testes:
        fn()
        print("ok", fn.__name__)
    print(f"{len(testes)} testes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
