"""N-gramas para a checagem de sobreposição. Não baixa nada."""

from __future__ import annotations

import re

STOP = {
    "a",
    "o",
    "os",
    "as",
    "um",
    "uma",
    "uns",
    "umas",
    "de",
    "da",
    "do",
    "das",
    "dos",
    "e",
    "ou",
    "mas",
    "que",
    "se",
    "em",
    "no",
    "na",
    "nos",
    "nas",
    "por",
    "para",
    "com",
    "sem",
    "ao",
    "à",
    "aos",
    "às",
    "é",
    "são",
    "foi",
    "ser",
    "ter",
    "tem",
    "há",
    "não",
    "sim",
    "mais",
    "menos",
    "muito",
    "já",
    "também",
    "como",
    "quando",
    "onde",
    "porque",
    "entre",
    "sobre",
    "até",
    "desde",
    "pelo",
    "pela",
    "pelos",
    "pelas",
    "seu",
    "sua",
    "seus",
    "suas",
    "ele",
    "ela",
    "eles",
    "elas",
    "isso",
    "isto",
    "este",
    "esta",
    "esse",
    "essa",
    "eu",
    "você",
    "tu",
    "nós",
    "me",
    "te",
    "lhe",
    "ou",
    "nem",
    "the",
    "of",
    "and",
    "to",
    "in",
    "a",
    "is",
    "for",
    "on",
    "with",
    "as",
    "that",
    "this",
    "it",
    "be",
    "or",
    "by",
    "an",
    "at",
    "from",
}

TOKEN_RE = re.compile(r"[0-9A-Za-zÀ-ÿ]+")


def tokens(texto: str) -> list[str]:
    return [t.casefold() for t in TOKEN_RE.findall(texto)]


def ngrams(texto: str, n: int = 8) -> list[tuple[str, ...]]:
    toks = tokens(texto)
    if len(toks) < n:
        return []
    return [tuple(toks[i : i + n]) for i in range(len(toks) - n + 1)]


def eh_trecho(grama: tuple[str, ...], minimo_conteudo: int = 4) -> bool:
    conteudo = sum(1 for t in grama if t not in STOP)
    return conteudo >= minimo_conteudo


def trechos(texto: str, n: int = 8, minimo_conteudo: int = 4) -> set[tuple[str, ...]]:
    return {g for g in ngrams(texto, n) if eh_trecho(g, minimo_conteudo)}
