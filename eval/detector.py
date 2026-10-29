#!/usr/bin/env python3
"""Conta as heurísticas do catálogo nos textos do eval.

Não é um detector de autoria. Não chama serviço externo.

    python eval/detector.py
    python eval/detector.py --write
    python eval/detector.py --check
"""

from __future__ import annotations

import hashlib
import statistics
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ptbr_humanizer.catalogo import (  # noqa: E402
    load_patterns,
    numbers_missing,
    score,
    total,
    word_count,
)

GENEROS_VITRINE = {
    "e-mail de trabalho",
    "post de LinkedIn",
    "README",
    "resposta de suporte",
    "artigo de opinião",
    "legenda de Instagram",
    "mensagem de WhatsApp",
    "texto acadêmico curto",
    "descrição de produto",
    "release de imprensa",
}


def _fmt(valor: float) -> str:
    return f"{valor:.2f}".replace(".", ",")


def carregar_ia() -> list[dict]:
    pares = []
    for meta_path in sorted((ROOT / "eval" / "textos" / "ia").glob("*/meta.yaml")):
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
        antes = (meta_path.parent / "antes.md").read_text(encoding="utf-8")
        depois = (meta_path.parent / "depois.md").read_text(encoding="utf-8")
        pares.append({"meta": meta, "antes": antes, "depois": depois})
    return pares


def carregar_humanos() -> list[tuple[str, str]]:
    pasta = ROOT / "eval" / "textos" / "humano"
    return [
        (path.name, path.read_text(encoding="utf-8"))
        for path in sorted(pasta.glob("h*.md"))
    ]


def checar_fatos(antes: str, depois: str, preservar: list[str]) -> list[str]:
    erros = []
    faltam_num = numbers_missing(antes, depois)
    if faltam_num:
        erros.append("números ausentes: " + ", ".join(faltam_num))
    for item in preservar:
        if item not in antes:
            erros.append(f"preservar não está no antes: {item}")
        elif item not in depois:
            erros.append(f"preservar sumiu no depois: {item}")
    palavras_a = word_count(antes)
    palavras_d = word_count(depois)
    if palavras_a == 0 or palavras_d < 15:
        erros.append("texto curto demais")
    else:
        razao = palavras_d / palavras_a
        if not 0.2 <= razao <= 1.8:
            erros.append(f"tamanho fora da faixa ({razao:.2f})")
    return erros


def medir(patterns: list[dict] | None = None) -> dict:
    patterns = patterns if patterns is not None else load_patterns()
    pares = carregar_ia()
    humanos = carregar_humanos()
    por_padrao = {
        p["id"]: {
            "nome": p["nome"],
            "grupo": p["grupo"],
            "textos_antes": 0,
            "occ_antes": 0,
            "occ_depois": 0,
            "textos_humano": 0,
            "occ_humano": 0,
        }
        for p in patterns
    }
    antes_totais = []
    depois_totais = []
    fatos = []
    for par in pares:
        sa = score(par["antes"], patterns)
        sd = score(par["depois"], patterns)
        antes_totais.append(total(sa))
        depois_totais.append(total(sd))
        for pid, n in sa.items():
            por_padrao[pid]["occ_antes"] += n
            if n:
                por_padrao[pid]["textos_antes"] += 1
        for pid, n in sd.items():
            por_padrao[pid]["occ_depois"] += n
        erros = checar_fatos(par["antes"], par["depois"], par["meta"]["preservar"])
        novos = [pid for pid, n in sd.items() if n and not sa.get(pid)]
        if novos:
            erros.append("padrão novo na reescrita: " + ", ".join(novos))
        if total(sa) < 2:
            erros.append("antes com menos de 2 marcas")
        if erros:
            fatos.append((par["meta"]["id"], erros))
    humano_totais = []
    humano_hits = []
    for nome, texto in humanos:
        sh = score(texto, patterns)
        humano_totais.append(total(sh))
        acertos = {pid: n for pid, n in sh.items() if n}
        if acertos:
            humano_hits.append((nome, acertos))
        for pid, n in sh.items():
            por_padrao[pid]["occ_humano"] += n
            if n:
                por_padrao[pid]["textos_humano"] += 1
    return {
        "n_padroes": len(patterns),
        "n_ia": len(pares),
        "n_humano": len(humanos),
        "antes": antes_totais,
        "depois": depois_totais,
        "humano": humano_totais,
        "por_padrao": por_padrao,
        "fatos": fatos,
        "humano_hits": humano_hits,
        "generos_vitrine": sorted(
            {p["meta"]["genero"] for p in pares if p["meta"].get("vitrine")}
        ),
        "n_vitrine": sum(1 for p in pares if p["meta"].get("vitrine")),
    }


def _media(valores: list[int]) -> float:
    return sum(valores) / len(valores) if valores else 0.0


def render_results(rel: dict) -> str:
    media_a = _media(rel["antes"])
    media_d = _media(rel["depois"])
    media_h = _media(rel["humano"])
    med_a = statistics.median(rel["antes"]) if rel["antes"] else 0
    med_d = statistics.median(rel["depois"]) if rel["depois"] else 0
    med_h = statistics.median(rel["humano"]) if rel["humano"] else 0
    queda = (media_a - media_d) / media_a * 100 if media_a else 0
    linhas = [
        "# Resultados automáticos",
        "",
        "Data dos textos: 2026-10-29. Ferramenta: `eval/detector.py`.",
        "",
        "O que esta página mede: quantas vezes as heurísticas declaradas em `patterns/` disparam. "
        "O que ela não mede: probabilidade de um texto ser de IA, nota de detector comercial "
        "(GPTZero, Originality ou outro) ou opinião de leitor. Nenhum desses serviços foi consultado.",
        "",
        "A reescrita foi feita pelo mesmo modelo que escreveu o «antes» (Grok 4.7, 2026-10-29), "
        "com a instrução de tirar estes padrões. A queda é o efeito dessa instrução nas heurísticas "
        "que o script sabe contar. Não é evidência de que uma pessoa classificaria o texto como humano.",
        "",
        "## Resumo",
        "",
        "| conjunto | textos | média de marcas por texto | mediana |",
        "| --- | ---: | ---: | ---: |",
        f"| IA, antes da skill | {rel['n_ia']} | {_fmt(media_a)} | {_fmt(float(med_a))} |",
        f"| IA, depois da skill | {rel['n_ia']} | {_fmt(media_d)} | {_fmt(float(med_d))} |",
        f"| controle humano (domínio público) | {rel['n_humano']} | {_fmt(media_h)} | {_fmt(float(med_h))} |",
        "",
        f"Queda no conjunto de IA: de {_fmt(media_a)} para {_fmt(media_d)} "
        f"({_fmt(queda)}% em relação à média inicial).",
        "",
        "## Fatos, números e tamanho",
        "",
    ]
    if rel["fatos"]:
        linhas.append("Falhas:")
        linhas.append("")
        for ident, erros in rel["fatos"]:
            linhas.append(f"- `{ident}`: {'; '.join(erros)}")
    else:
        linhas.append(
            f"Os {rel['n_ia']} pares passaram na checagem: cada número do antes aparece no depois, "
            "cada item de `preservar` também, e o tamanho ficou entre 20% e 180% do original."
        )
    linhas += [
        "",
        "## Por padrão",
        "",
        "| padrão | textos com a marca (antes) | ocorrências antes | ocorrências depois | textos do controle | ocorrências no controle |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for pid, info in rel["por_padrao"].items():
        linhas.append(
            f"| `{pid}` | {info['textos_antes']} | {info['occ_antes']} | {info['occ_depois']} | "
            f"{info['textos_humano']} | {info['occ_humano']} |"
        )
    linhas += [
        "",
        "## Controle humano",
        "",
        "Os 30 textos são parágrafos integrais de obras em domínio público, publicadas antes de 1930 "
        "(Machado de Assis, Aluísio Azevedo, Lima Barreto, Raul Pompeia). Não são e-mail, legenda nem "
        "WhatsApp de 2026. Servem para ver se a heurística dispara em prosa humana antiga. "
        "Fonte e licença: `eval/textos/humano/FONTES.md`.",
        "",
    ]
    if rel["humano_hits"]:
        linhas.append("Onde a heurística disparou no controle:")
        linhas.append("")
        for nome, acertos in rel["humano_hits"]:
            detalhe = ", ".join(f"`{k}` × {v}" for k, v in acertos.items())
            linhas.append(f"- `{nome}`: {detalhe}")
        linhas.append("")
        linhas.append(
            "Um disparo no controle não transforma o padrão em erro de catálogo. "
            "Mostra o limite da regex. «No tocante a», por exemplo, é fórmula de prosa formal, "
            "não exclusividade de modelo."
        )
    else:
        linhas.append("Nenhuma heurística disparou no controle desta medição.")
    linhas += [
        "",
        "## Avaliação cega",
        "",
        "Não foi feita. O protocolo e a planilha estão em `eval/cego.md` e `eval/planilha-cega.csv`. "
        "Nenhum número de leitor entra neste arquivo até a rodada existir, com N e data.",
        "",
    ]
    return "\n".join(linhas)


def render_stats(rel: dict) -> str:
    media_a = _media(rel["antes"])
    media_d = _media(rel["depois"])
    media_h = _media(rel["humano"])
    return (
        f"**{rel['n_padroes']} padrões.** "
        f"Nos {rel['n_ia']} textos gerados para este repositório, a média de marcas por texto "
        f"caiu de **{_fmt(media_a)}** para **{_fmt(media_d)}** "
        f"([eval/RESULTS.md](eval/RESULTS.md)). "
        f"No controle de {rel['n_humano']} trechos em domínio público, a média é **{_fmt(media_h)}**."
    )


def _substituir(texto: str, nome: str, bloco: str) -> str:
    inicio = f"<!-- {nome}:start -->"
    fim = f"<!-- {nome}:end -->"
    if inicio not in texto or fim not in texto:
        raise SystemExit(f"marcador {nome} ausente")
    pre, resto = texto.split(inicio, 1)
    _, pos = resto.split(fim, 1)
    return pre + inicio + "\n" + bloco.strip() + "\n" + fim + pos


def checar_manifesto() -> list[str]:
    pasta = ROOT / "eval" / "textos" / "humano"
    manifesto = pasta / "MANIFEST.sha256"
    if not manifesto.exists():
        return ["MANIFEST.sha256 ausente"]
    erros = []
    linhas = [ln for ln in manifesto.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if len(linhas) != 30:
        erros.append(f"manifesto com {len(linhas)} linhas")
    for linha in linhas:
        digest, nome = linha.split()
        path = pasta / nome
        if not path.exists():
            erros.append(f"manifesto aponta para arquivo ausente: {nome}")
            continue
        atual = hashlib.sha256(path.read_bytes()).hexdigest()
        if atual != digest:
            erros.append(f"hash divergente: {nome}")
    return erros


def problemas(rel: dict) -> list[str]:
    erros = []
    if rel["n_ia"] != 30:
        erros.append(f"há {rel['n_ia']} textos de IA; o esperado é 30")
    if rel["n_humano"] != 30:
        erros.append(f"há {rel['n_humano']} textos humanos; o esperado é 30")
    if rel["n_vitrine"] != 10:
        erros.append(f"vitrine com {rel['n_vitrine']} textos")
    faltam = GENEROS_VITRINE.difference(rel["generos_vitrine"])
    if faltam:
        erros.append("gêneros ausentes na vitrine: " + ", ".join(sorted(faltam)))
    if rel["fatos"]:
        for ident, msgs in rel["fatos"]:
            erros.append(f"{ident}: {'; '.join(msgs)}")
    if _media(rel["depois"]) >= _media(rel["antes"]):
        erros.append("a média depois não caiu")
    if _media(rel["humano"]) >= _media(rel["antes"]):
        erros.append("o controle humano não ficou abaixo do texto de IA bruto")
    for pid, info in rel["por_padrao"].items():
        if info["textos_humano"] > 6:
            erros.append(
                f"{pid} disparou em {info['textos_humano']} textos humanos; a heurística está larga"
            )
    erros.extend(checar_manifesto())
    return erros


def escrever(rel: dict) -> None:
    (ROOT / "eval" / "RESULTS.md").write_text(render_results(rel), encoding="utf-8")
    readme = ROOT / "README.md"
    texto = readme.read_text(encoding="utf-8")
    readme.write_text(_substituir(texto, "eval-stats", render_stats(rel)), encoding="utf-8")


def checar(rel: dict) -> int:
    erros = problemas(rel)
    results = ROOT / "eval" / "RESULTS.md"
    if not results.exists():
        erros.append("eval/RESULTS.md ausente")
    elif results.read_text(encoding="utf-8") != render_results(rel):
        erros.append("eval/RESULTS.md desatualizado")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if _substituir(readme, "eval-stats", render_stats(rel)) != readme:
        erros.append("bloco de números do README desatualizado")
    if erros:
        print("\n".join(erros))
        return 1
    print(
        f"eval ok: {_fmt(_media(rel['antes']))} → {_fmt(_media(rel['depois']))} "
        f"(controle {_fmt(_media(rel['humano']))})"
    )
    return 0


def main() -> int:
    rel = medir()
    if "--write" in sys.argv:
        escrever(rel)
        print(render_stats(rel))
        return 0
    if "--check" in sys.argv:
        return checar(rel)
    print(render_results(rel))
    return 0 if not problemas(rel) else 1


if __name__ == "__main__":
    raise SystemExit(main())
