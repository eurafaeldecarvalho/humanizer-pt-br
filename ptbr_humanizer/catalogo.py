"""Carrega `patterns/*.yaml` e conta as heurísticas do catálogo.

A contagem não é um detector de autoria. Ela só aplica as regras declaradas
em cada arquivo de padrão.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

SMALL_WORDS = {
    "a",
    "o",
    "as",
    "os",
    "um",
    "uma",
    "de",
    "da",
    "do",
    "das",
    "dos",
    "e",
    "em",
    "na",
    "no",
    "nos",
    "nas",
    "para",
    "com",
    "por",
    "ao",
    "à",
    "às",
    "aos",
    "ou",
    "num",
    "numa",
    "que",
    "se",
}

NUM_RE = re.compile(
    r"\d{1,2}/\d{1,2}/\d{2,4}"
    r"|\d{4}-\d{2}-\d{2}"
    r"|\d{1,2}h\d{2}"
    r"|\d{1,2}h"
    r"|\d+º"
    r"|\d+(?:\.\d{3})+,\d+"
    r"|\d+,\d+"
    r"|\d+\.\d+(?:\.\d+)*"
    r"|\d+%"
    r"|\d+"
)

GRUPOS = (
    "abertura",
    "conectivo",
    "estrutura",
    "vocabulario",
    "fechamento",
    "formato",
)


def repo_root() -> Path:
    return ROOT


def patterns_dir() -> Path:
    return ROOT / "patterns"


def load_patterns() -> list[dict]:
    files = sorted(patterns_dir().glob("*.yaml"))
    if not files:
        raise FileNotFoundError(f"nenhum padrão em {patterns_dir()}")
    patterns = []
    for path in files:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"{path.name} não é um mapa YAML")
        data["_arquivo"] = path.name
        _compile(data, path.name)
        patterns.append(data)
    return patterns


def _compile(data: dict, nome: str) -> None:
    heur = data.get("heuristica") or {}
    tipo = heur.get("tipo")
    if tipo in ("regex", "regex_minimo"):
        compiled = []
        for i, fonte in enumerate(heur.get("padroes") or []):
            try:
                compiled.append(re.compile(fonte))
            except re.error as exc:
                raise ValueError(f"{nome}: regex {i} inválida: {exc}") from exc
        heur["_compiled"] = compiled
    elif tipo not in ("travessao", "title_case"):
        raise ValueError(f"{nome}: tipo de heurística desconhecido: {tipo}")


def prose(text: str) -> str:
    """Tira frontmatter e blocos cercados, que não são prosa a reescrever."""
    if text.startswith("---\n"):
        fim = text.find("\n---", 4)
        if fim != -1:
            text = text[fim + 4 :]
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return text.strip()


def count_pattern(text: str, pattern: dict) -> int:
    heur = pattern["heuristica"]
    tipo = heur["tipo"]
    if tipo in ("regex", "regex_minimo"):
        minimo = int(heur.get("minimo", 1 if tipo == "regex" else 2))
        total = 0
        for compiled in heur["_compiled"]:
            total += len(compiled.findall(text))
        return total if total >= minimo else 0
    if tipo == "travessao":
        n = _count_travessao(text)
        return n if n >= int(heur.get("minimo", 3)) else 0
    if tipo == "title_case":
        n = _count_title_case(text)
        return n if n >= int(heur.get("minimo", 1)) else 0
    raise ValueError(tipo)


def score(text: str, patterns: list[dict] | None = None) -> dict[str, int]:
    patterns = patterns if patterns is not None else load_patterns()
    limpo = prose(text)
    return {p["id"]: count_pattern(limpo, p) for p in patterns}


def total(contagens: dict[str, int]) -> int:
    return sum(contagens.values())


def _count_travessao(text: str) -> int:
    """Pares de travessão com aparte curto no meio.

    Não conta o travessão de diálogo («— Bonita canoa!») nem um aparte único.
    O interior do par não pode trazer ! ou ?, que marcam fala.
    """
    return len(re.findall(r"—\s[^—!?\n]{2,80}?\s—", text))


def _count_title_case(text: str) -> int:
    """Linha curta com miolo em maiúsculas, no hábito de título em inglês."""
    n = 0
    for line in text.splitlines():
        s = line.strip().lstrip("#").strip()
        if not s or s.endswith((".", "!", "?", "…", ";")):
            continue
        if len(s) > 90 or len(s) < 12:
            continue
        letters = [ch for ch in s if ch.isalpha()]
        if letters and all(ch.isupper() for ch in letters):
            continue
        words = re.findall(r"[A-Za-zÀ-ÿ0-9]+", s)
        if len(words) < 4:
            continue
        resto = []
        for w in words[1:]:
            if w.lower() in SMALL_WORDS:
                continue
            if any(ch.isdigit() for ch in w):
                continue
            resto.append(w)
        if len(resto) < 3:
            continue
        caps = sum(1 for w in resto if w[0].isupper())
        if caps >= 3 and caps / len(resto) >= 0.75:
            n += 1
    return n


def extract_numbers(text: str) -> list[str]:
    vistos: list[str] = []
    for match in NUM_RE.finditer(prose(text)):
        token = match.group(0)
        if token not in vistos:
            vistos.append(token)
    return vistos


def _number_present(token: str, texto: str) -> bool:
    return re.search(rf"(?<!\d){re.escape(token)}(?!\d)", texto) is not None


def numbers_missing(antes: str, depois: str) -> list[str]:
    destino = prose(depois)
    return [n for n in extract_numbers(antes) if not _number_present(n, destino)]


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", prose(text)))
