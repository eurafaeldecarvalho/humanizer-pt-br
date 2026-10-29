#!/usr/bin/env python3
"""Baixa trechos em domínio público no Wikisource e grava o controle do eval.

Regra de corte, estável: em cada obra, percorre os capítulos na ordem listada,
fica com parágrafos de 70 a 150 palavras que terminam em pontuação, e guarda
os cinco primeiros. Não reescreve a ortografia da edição.

Uso: python scripts/fetch_humanos.py
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "eval" / "textos" / "humano"
API = "https://pt.wikisource.org/w/api.php"
UA = "humanizer-pt-br-eval/1.0 (trechos em dominio publico para controle de heuristicas)"

OBRAS = [
    {
        "id": "machado-memorias",
        "autor": "Machado de Assis",
        "obra": "Memórias Póstumas de Brás Cubas",
        "ano_publicacao": 1881,
        "morte_autor": 1908,
        "prefixo": "Memórias Póstumas de Brás Cubas/",
        "capitulos": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"],
    },
    {
        "id": "machado-dom",
        "autor": "Machado de Assis",
        "obra": "Dom Casmurro",
        "ano_publicacao": 1899,
        "morte_autor": 1908,
        "prefixo": "Dom Casmurro/",
        "capitulos": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"],
    },
    {
        "id": "machado-quincas",
        "autor": "Machado de Assis",
        "obra": "Quincas Borba",
        "ano_publicacao": 1891,
        "morte_autor": 1908,
        "prefixo": "Quincas Borba/",
        "capitulos": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"],
    },
    {
        "id": "aluisio-cortico",
        "autor": "Aluísio Azevedo",
        "obra": "O Cortiço",
        "ano_publicacao": 1890,
        "morte_autor": 1913,
        "prefixo": "O Cortiço/",
        "capitulos": ["I", "II", "III", "IV"],
    },
    {
        "id": "lima-policarpo",
        "autor": "Lima Barreto",
        "obra": "Triste Fim de Policarpo Quaresma",
        "ano_publicacao": 1915,
        "morte_autor": 1922,
        "prefixo": "Triste Fim de Policarpo Quaresma/I/",
        "capitulos": ["I", "II", "III", "IV", "V"],
    },
    {
        "id": "pompeia-ateneu",
        "autor": "Raul Pompeia",
        "obra": "O Ateneu",
        "ano_publicacao": 1888,
        "morte_autor": 1895,
        "prefixo": "O Ateneu/",
        "capitulos": ["I", "II", "III"],
    },
]


def _get(params: dict) -> dict:
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def paragrafos(titulo: str) -> tuple[list[str], str]:
    data = _get(
        {
            "action": "parse",
            "page": titulo,
            "prop": "text",
            "format": "json",
            "redirects": 1,
        }
    )
    if "error" in data:
        raise RuntimeError(f"{titulo}: {data['error'].get('code')}")
    bruto = data["parse"]["text"]["*"]
    edicao = ""
    m = re.search(r"Edição de referência:([^<]+)", bruto)
    if m:
        edicao = re.sub(r"\s+", " ", html.unescape(m.group(1))).strip(" .")
    saida = []
    for pedaco in re.findall(r"<p>(.*?)</p>", bruto, flags=re.S):
        texto = re.sub(r"<[^>]+>", "", pedaco)
        texto = html.unescape(texto)
        texto = texto.replace("\xa0", " ")
        texto = re.sub(r"\[\d+\]", "", texto)
        texto = re.sub(r"\s+", " ", texto).strip()
        if not texto:
            continue
        if any(s in texto for s in ("Edição de referência", "Wikisource", "http", "Categoria:")):
            continue
        palavras = texto.split()
        if not 70 <= len(palavras) <= 150:
            continue
        if texto[-1] not in ".!?;»":
            continue
        saida.append(texto)
    return saida, edicao


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for antigo in OUT.glob("*.md"):
        if antigo.name != "LEIA-ME.md":
            antigo.unlink()
    linhas = ["# Fontes do controle humano", "", "Trechos integrais de parágrafo, sem corte no meio da frase.", ""]
    manifesto = []
    n = 0
    for obra in OBRAS:
        pegos = 0
        edicoes = []
        for cap in obra["capitulos"]:
            if pegos >= 5:
                break
            titulo = obra["prefixo"] + cap
            try:
                paras, edicao = paragrafos(titulo)
            except Exception as exc:  # noqa: BLE001 — registra e segue
                linhas.append(f"- Falha em {titulo}: {exc}")
                time.sleep(0.3)
                continue
            if edicao:
                edicoes.append(edicao)
            for texto in paras:
                if pegos >= 5:
                    break
                n += 1
                pegos += 1
                slug = f"h{n:02d}-{obra['id']}"
                fonte = "https://pt.wikisource.org/wiki/" + urllib.parse.quote(titulo.replace(" ", "_"))
                meta = (
                    "---\n"
                    f"id: {slug}\n"
                    f"autor: {obra['autor']}\n"
                    f"obra: {obra['obra']}\n"
                    f"ano_publicacao: {obra['ano_publicacao']}\n"
                    f"morte_autor: {obra['morte_autor']}\n"
                    f"capitulo: {titulo}\n"
                    f"edicao: {edicao or 'não identificada na página'}\n"
                    "licenca: dominio-publico\n"
                    f"fonte: {fonte}\n"
                    "nota: Parágrafo integral da transcrição. Ortografia da edição, sem modernizar.\n"
                    "---\n\n"
                )
                corpo = meta + texto + "\n"
                path = OUT / f"{slug}.md"
                path.write_text(corpo, encoding="utf-8")
                digest = hashlib.sha256(corpo.encode("utf-8")).hexdigest()
                manifesto.append(f"{digest}  {path.name}")
                linhas.append(
                    f"- `{path.name}` — {obra['autor']}, *{obra['obra']}* ({obra['ano_publicacao']}), `{titulo}`."
                )
            time.sleep(0.25)
        if pegos < 5:
            raise SystemExit(f"{obra['obra']} só rendeu {pegos} parágrafos")
    if n != 30:
        raise SystemExit(f"esperava 30 trechos, veio {n}")
    (OUT / "MANIFEST.sha256").write_text("\n".join(manifesto) + "\n", encoding="utf-8")
    linhas += [
        "",
        "Licença: obras em domínio público no Brasil (prazo de 70 anos após a morte do autor já vencido) e nos Estados Unidos (publicação anterior a 1930). A transcrição foi lida no Wikisource; o trecho guardado é só o parágrafo literário, sem nota editorial.",
        "",
        "Estes textos não são amostra do português de e-mail ou de rede em 2026. Servem para ver se a heurística dispara em prosa humana anterior à escrita de máquina.",
        "",
    ]
    (OUT / "FONTES.md").write_text("\n".join(linhas), encoding="utf-8")
    print(f"{n} trechos em {OUT}")


if __name__ == "__main__":
    main()
