#!/usr/bin/env python3
"""Compara n-gramas de 8 palavras com os SKILL.md públicos de inspiração.

Não grava o texto deles. Só conta e, se houver, lista o n-grama compartilhado.

    python scripts/check_overlap.py --write
    python scripts/check_overlap.py --check
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ptbr_humanizer.ngrams import ngrams, trechos  # noqa: E402

REPOS = (
    "blader/humanizer",
    "op7418/Humanizer-zh",
    "mackswendhell/humanizer-pt-br",
)
RELATORIO = ROOT / "docs" / "originalidade.md"
LINHA = "Trechos em comum (8 palavras, com pelo menos 4 de conteúdo):"


def _token() -> str | None:
    for chave in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(chave):
            return os.environ[chave]
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True).strip() or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _get(url: str, token: str | None) -> bytes:
    headers = {"User-Agent": "humanizer-pt-br-overlap", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _json(url: str, token: str | None) -> dict:
    return json.loads(_get(url, token).decode("utf-8"))


def _nosso_texto() -> tuple[str, list[str]]:
    partes = []
    nomes = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        relativo = path.relative_to(ROOT).as_posix()
        if relativo.startswith("eval/textos/humano/"):
            continue
        if relativo in {"LICENSE", "docs/originalidade.md"}:
            continue
        if "/cego-pacote/" in f"/{relativo}/":
            continue
        partes.append(path.read_text(encoding="utf-8"))
        nomes.append(relativo)
    return "\n".join(partes), nomes


def _remoto(token: str | None) -> list[dict]:
    achados = []
    for repo in REPOS:
        meta = _json(f"https://api.github.com/repos/{repo}", token)
        branch = meta["default_branch"]
        arvore = _json(
            f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1",
            token,
        )
        if arvore.get("truncated"):
            raise SystemExit(f"{repo}: árvore truncada, a checagem não viu todos os arquivos")
        caminhos = [
            item["path"]
            for item in arvore.get("tree", [])
            if item.get("type") == "blob" and item["path"].lower().endswith("skill.md")
        ]
        if not caminhos:
            raise SystemExit(f"{repo}: nenhum SKILL.md na branch {branch}")
        for caminho in caminhos:
            url = f"https://raw.githubusercontent.com/{repo}/{branch}/{caminho}"
            bruto = _get(url, token)
            achados.append(
                {
                    "repo": repo,
                    "branch": branch,
                    "caminho": caminho,
                    "sha256": hashlib.sha256(bruto).hexdigest(),
                    "bytes": len(bruto),
                    "texto": bruto.decode("utf-8", errors="replace"),
                }
            )
    return achados


def comparar() -> dict:
    token = _token()
    nosso, arquivos = _nosso_texto()
    remotos = _remoto(token)
    nossos_trechos = trechos(nosso)
    nossos_brutos = set(ngrams(nosso))
    comum = set()
    bruto = set()
    for item in remotos:
        comum |= nossos_trechos & trechos(item["texto"])
        bruto |= nossos_brutos & set(ngrams(item["texto"]))
    return {
        "arquivos_nossos": arquivos,
        "remotos": [
            {k: v for k, v in item.items() if k != "texto"}
            for item in remotos
        ],
        "trechos": sorted(" ".join(g) for g in comum),
        "brutos": sorted(" ".join(g) for g in bruto),
    }


def render(rel: dict) -> str:
    linhas = [
        "# Originalidade",
        "",
        "Medição de 2026-10-29. O CI volta a contar a cada execução e falha se aparecer trecho em comum.",
        "",
        "O catálogo, os exemplos e o texto da skill foram escritos para este repositório. "
        "A checagem abaixo compara esse material com os `SKILL.md` públicos dos projetos citados no README. "
        "O texto deles não é copiado para cá. Entram só o caminho, o tamanho e o sha256.",
        "",
        "Método: janelas de 8 palavras, em minúsculas, sem pontuação. "
        "Conta como trecho a janela com pelo menos 4 palavras fora de uma lista de conectivos "
        "(português e inglês), em `ptbr_humanizer/ngrams.py`. "
        "Janela só de função gramatical não entra, para não marcar esqueleto de frase.",
        "",
        "Arquivos nossos: tudo em Markdown e YAML, exceto `eval/textos/humano/` (domínio público), "
        "`LICENSE` e este relatório.",
        "",
        "## Referências consultadas",
        "",
    ]
    for item in rel["remotos"]:
        linhas.append(
            f"- `{item['repo']}` (`{item['branch']}`) `{item['caminho']}` — "
            f"{item['bytes']} bytes, sha256 `{item['sha256']}`"
        )
    linhas += [
        "",
        f"Arquivos nossos na comparação: {len(rel['arquivos_nossos'])}.",
        "",
        f"{LINHA} {len(rel['trechos'])}",
        "",
        f"Janelas brutas de 8 palavras, sem o filtro de conteúdo: {len(rel['brutos'])}.",
        "",
    ]
    if rel["trechos"]:
        linhas.append("Trechos que batem:")
        linhas.append("")
        for trecho in rel["trechos"]:
            linhas.append(f"- {trecho}")
        linhas.append("")
    else:
        linhas.append("Nenhum trecho em comum com o critério acima.")
        linhas.append("")
    if rel["brutos"] and not rel["trechos"]:
        amostra = rel["brutos"][:8]
        linhas.append(
            "Amostra das janelas brutas que sobraram (não passam no filtro de conteúdo; "
            "não são frase copiada):"
        )
        linhas.append("")
        for trecho in amostra:
            linhas.append(f"- {trecho}")
        linhas.append("")
    return "\n".join(linhas)


def main() -> int:
    rel = comparar()
    texto = render(rel)
    if "--write" in sys.argv:
        RELATORIO.parent.mkdir(parents=True, exist_ok=True)
        RELATORIO.write_text(texto, encoding="utf-8")
        print(f"{LINHA} {len(rel['trechos'])}")
    if rel["trechos"]:
        print(texto)
        return 1
    if "--check" in sys.argv:
        if not RELATORIO.exists():
            print("docs/originalidade.md ausente")
            return 1
        atual = RELATORIO.read_text(encoding="utf-8")
        if f"{LINHA} 0" not in atual:
            print("o relatório não registra zero trechos")
            return 1
    print(f"{LINHA} {len(rel['trechos'])} (brutas {len(rel['brutos'])})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
