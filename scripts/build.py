#!/usr/bin/env python3
"""Gera a skill, o prompt e a vitrine a partir de patterns/ e src/processo.md.

    python scripts/build.py
    python scripts/build.py --check
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ptbr_humanizer.catalogo import GRUPOS, load_patterns, score  # noqa: E402

DESCRIPTION = (
    "Reescreve texto em português do Brasil para tirar marcas típicas de texto "
    "gerado por IA, preservando sentido, registro, fatos e termos técnicos. "
    "Use quando o usuário pedir para revisar, humanizar ou tirar cara de IA de "
    "um texto em português do Brasil."
)

AVISO = (
    "<!-- gerado por scripts/build.py a partir de patterns/ e src/processo.md. "
    "Não edite à mão. -->"
)


def _grupo(patterns: list[dict]) -> list[tuple[str, list[dict]]]:
    por = {g: [] for g in GRUPOS}
    for p in patterns:
        por[p["grupo"]].append(p)
    for g in por:
        por[g].sort(key=lambda item: item["nome"].casefold())
    return [(g, por[g]) for g in GRUPOS if por[g]]


def render_catalogo(patterns: list[dict]) -> str:
    partes = [
        AVISO,
        "",
        "# Catálogo",
        "",
        "Cada exemplo foi escrito para este repositório por Grok 4.7 em 2026-10-29. "
        "A heurística automática é mais estreita que o texto: na reescrita, siga a descrição.",
        "",
    ]
    for grupo, itens in _grupo(patterns):
        partes.append(f"## {grupo}")
        partes.append("")
        for p in itens:
            limite = (p.get("heuristica") or {}).get("limite")
            bloco = [
                f"### {p['nome']}",
                "",
                f"`{p['id']}`",
                "",
                p["por_que"],
                "",
                f"**Como corrigir.** {p['como_corrigir']}",
                "",
                f"**Antes.** {p['exemplo_antes']}",
                "",
                f"**Depois.** {p['exemplo_depois']}",
            ]
            if limite:
                bloco += ["", f"*Limite da contagem automática:* {limite}"]
            partes.append("\n".join(bloco))
            partes.append("")
    return "\n".join(partes).rstrip() + "\n"


def render_indice(patterns: list[dict]) -> str:
    linhas = []
    for grupo, itens in _grupo(patterns):
        linhas.append(f"### {grupo}")
        linhas.append("")
        for p in itens:
            exemplo = p["exemplo_antes"]
            if len(exemplo) > 110:
                exemplo = exemplo[:107].rstrip() + "…"
            linhas.append(f"- **{p['nome']}** (`{p['id']}`). {exemplo}")
        linhas.append("")
    return "\n".join(linhas).rstrip() + "\n"


def _frontmatter() -> str:
    if len(DESCRIPTION) > 1024:
        raise SystemExit("description passa de 1024 caracteres")
    return (
        "---\n"
        "name: humanizer-pt-br\n"
        f"description: {DESCRIPTION}\n"
        "license: MIT\n"
        "metadata:\n"
        '  version: "1.0.0"\n'
        "  idioma: pt-BR\n"
        "---\n"
    )


def _processo() -> str:
    return (ROOT / "src" / "processo.md").read_text(encoding="utf-8").rstrip()


def _exemplo_trabalhado(patterns: list[dict]) -> str:
    pasta = ROOT / "eval" / "textos" / "ia" / "01-email-relatorio"
    antes = (pasta / "antes.md").read_text(encoding="utf-8").rstrip()
    depois = (pasta / "depois.md").read_text(encoding="utf-8").rstrip()
    cont_a = score(antes, patterns)
    cont_d = score(depois, patterns)
    linhas = [
        "| padrão | antes | depois |",
        "| --- | ---: | ---: |",
    ]
    for pid, n in cont_a.items():
        if n:
            linhas.append(f"| `{pid}` | {n} | {cont_d.get(pid, 0)} |")
    return (
        "## Exemplo trabalhado\n\n"
        "E-mail fictício, escrito por Grok 4.7 em 2026-10-29 para este repositório "
        "(`eval/textos/ia/01-email-relatorio`). A reescrita é do mesmo modelo, no mesmo dia, "
        "seguindo este processo. Não é texto de um terceiro.\n\n"
        "**Antes.**\n\n"
        f"{antes}\n\n"
        "**Depois.**\n\n"
        f"{depois}\n\n"
        "**Marcas contadas pela heurística.**\n\n"
        + "\n".join(linhas)
        + "\n"
    )


def render_skill(patterns: list[dict]) -> str:
    corpo = f"""{AVISO}

# Humanizer PT-BR

O catálogo completo, com antes e depois, está em [references/catalogo.md](references/catalogo.md).

{_processo()}

## Catálogo, em uma linha

{render_indice(patterns).rstrip()}

{_exemplo_trabalhado(patterns).rstrip()}
"""
    return _frontmatter() + "\n" + corpo


def render_prompt(patterns: list[dict]) -> str:
    catalogo = render_catalogo(patterns)
    linhas = catalogo.splitlines()
    if linhas and linhas[0].startswith("<!--"):
        catalogo = "\n".join(linhas[1:]).lstrip()
    return f"""{AVISO}

Você revisa texto em português do Brasil. Siga as regras abaixo quando a pessoa pedir para revisar, humanizar ou tirar cara de IA. Se o pedido for outro, não reescreva por conta própria.

{_processo()}

{catalogo}
"""


def render_tabela(patterns: list[dict]) -> str:
    linhas = [
        "| Padrão | Exemplo |",
        "| --- | --- |",
    ]
    for _nome_grupo, itens in _grupo(patterns):
        for p in itens:
            exemplo = p["exemplo_antes"].replace("|", "/")
            if len(exemplo) > 88:
                exemplo = exemplo[:85].rstrip() + "…"
            nome = p["nome"].replace("|", "/")
            linhas.append(f"| {nome} | {exemplo} |")
    return "\n".join(linhas)


def _mudancas(antes: str, depois: str, patterns: list[dict], meta: dict) -> str:
    ca, cd = score(antes, patterns), score(depois, patterns)
    linhas = [
        "# O que saiu",
        "",
        f"Reescrita por {meta['modelo_reescrita']} em {meta['data_reescrita']}, "
        "aplicando `src/processo.md` e o catálogo. "
        "Os itens de `preservar` no `meta.yaml` continuam no texto.",
        "",
        "| padrão | antes | depois |",
        "| --- | ---: | ---: |",
    ]
    for pid, n in ca.items():
        if n:
            linhas.append(f"| `{pid}` | {n} | {cd.get(pid, 0)} |")
    linhas.append("")
    return "\n".join(linhas)


def escrever_exemplos(patterns: list[dict]) -> None:
    destino = ROOT / "examples"
    destino.mkdir(exist_ok=True)
    vistos = set()
    for meta_path in sorted((ROOT / "eval" / "textos" / "ia").glob("*/meta.yaml")):
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
        if not meta.get("vitrine"):
            continue
        vistos.add(meta["id"])
        pasta = destino / meta["id"]
        if pasta.exists():
            shutil.rmtree(pasta)
        pasta.mkdir()
        antes = (meta_path.parent / "antes.md").read_text(encoding="utf-8")
        depois = (meta_path.parent / "depois.md").read_text(encoding="utf-8")
        (pasta / "antes.md").write_text(antes, encoding="utf-8")
        (pasta / "depois.md").write_text(depois, encoding="utf-8")
        (pasta / "meta.yaml").write_text(
            yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=4096),
            encoding="utf-8",
        )
        (pasta / "mudancas.md").write_text(
            _mudancas(antes, depois, patterns, meta), encoding="utf-8"
        )
    for pasta in destino.iterdir():
        if pasta.is_dir() and pasta.name not in vistos:
            shutil.rmtree(pasta)


def substituir_marcador(texto: str, nome: str, bloco: str) -> str:
    inicio = f"<!-- {nome}:start -->"
    fim = f"<!-- {nome}:end -->"
    if inicio not in texto or fim not in texto:
        raise SystemExit(f"marcador {nome} ausente no README")
    pre, resto = texto.split(inicio, 1)
    _, pos = resto.split(fim, 1)
    return pre + inicio + "\n" + bloco.strip() + "\n" + fim + pos


def arquivos_gerados(patterns: list[dict]) -> dict[Path, str]:
    skill = ROOT / "skills" / "humanizer-pt-br"
    return {
        skill / "SKILL.md": render_skill(patterns),
        skill / "references" / "catalogo.md": render_catalogo(patterns),
        ROOT / "prompt" / "humanizer-pt-br.md": render_prompt(patterns),
    }


def escrever() -> None:
    patterns = load_patterns()
    for path, conteudo in arquivos_gerados(patterns).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(conteudo, encoding="utf-8")
    escrever_exemplos(patterns)
    readme = ROOT / "README.md"
    texto = readme.read_text(encoding="utf-8")
    readme.write_text(
        substituir_marcador(texto, "patterns-table", render_tabela(patterns)),
        encoding="utf-8",
    )
    print("skill, prompt, exemplos e tabela do README atualizados")


def checar() -> int:
    patterns = load_patterns()
    erros = []
    for path, conteudo in arquivos_gerados(patterns).items():
        if not path.exists():
            erros.append(f"ausente: {path.relative_to(ROOT)}")
            continue
        atual = path.read_text(encoding="utf-8")
        if atual != conteudo:
            erros.append(f"desatualizado: {path.relative_to(ROOT)}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    esperado = substituir_marcador(readme, "patterns-table", render_tabela(patterns))
    if esperado != readme:
        erros.append("tabela de padrões do README desatualizada")
    # exemplos: reconstrói em memória o conjunto de ids
    vitrine = []
    for meta_path in sorted((ROOT / "eval" / "textos" / "ia").glob("*/meta.yaml")):
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
        if meta.get("vitrine"):
            vitrine.append(meta["id"])
            pasta = ROOT / "examples" / meta["id"]
            for nome in ("antes.md", "depois.md"):
                origem = (meta_path.parent / nome).read_text(encoding="utf-8")
                destino = pasta / nome
                if not destino.exists() or destino.read_text(encoding="utf-8") != origem:
                    erros.append(f"exemplo divergente: {meta['id']}/{nome}")
            if not (pasta / "mudancas.md").exists():
                erros.append(f"sem mudanças: {meta['id']}")
    extras = [
        p.name
        for p in (ROOT / "examples").iterdir()
        if p.is_dir() and p.name not in vitrine
    ]
    if extras:
        erros.append(f"pastas de exemplo a mais: {extras}")
    if len(vitrine) != 10:
        erros.append(f"a vitrine tem {len(vitrine)} textos; o esperado é 10")
    if erros:
        print("\n".join(erros))
        return 1
    print("build ok")
    return 0


def main() -> int:
    if "--check" in sys.argv:
        return checar()
    escrever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
