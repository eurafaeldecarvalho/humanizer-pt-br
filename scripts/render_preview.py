#!/usr/bin/env python3
"""Desenha o antes/depois do exemplo 01. As frases precisam existir no arquivo."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ANTES_PATH = ROOT / "examples" / "01-email-relatorio" / "antes.md"
DEPOIS_PATH = ROOT / "examples" / "01-email-relatorio" / "depois.md"
SAIDA = ROOT / "docs" / "img"

ANTES = (
    "No mundo atual, consolidar as vendas do interior pede contexto. "
    "Vale ressaltar que o relatório do 3º trimestre — versão interna — "
    "não foi apenas fechado, mas também validado pela controladoria em 28/10/2026. "
    "O documento ficou robusto, abrangente e estratégico."
)
DEPOIS = (
    "O relatório do 3º trimestre está fechado. "
    "A controladoria validou em 28/10/2026."
)
MARCAS = (
    "No mundo atual",
    "Vale ressaltar",
    "não foi apenas",
    "mas também",
    "robusto, abrangente e estratégico",
)

FUNDO = (244, 239, 230)
CARTAO = (255, 253, 248)
TINTA = (28, 25, 21)
MUDO = (90, 84, 76)
MARCA = (246, 211, 107)
RUIM = (154, 52, 18)
BOM = (31, 107, 74)
FONTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTE_NEGRITO = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def _conferir() -> None:
    antes = ANTES_PATH.read_text(encoding="utf-8")
    depois = DEPOIS_PATH.read_text(encoding="utf-8")
    if ANTES not in antes:
        raise SystemExit("o trecho do antes não está no exemplo 01")
    if DEPOIS not in depois:
        raise SystemExit("o trecho do depois não está no exemplo 01")
    for marca in MARCAS:
        if marca not in ANTES:
            raise SystemExit(f"marca ausente no recorte: {marca}")


def _faixas(texto: str) -> list[bool]:
    flags = [False] * len(texto)
    for marca in MARCAS:
        inicio = texto.find(marca)
        if inicio < 0:
            continue
        for i in range(inicio, inicio + len(marca)):
            flags[i] = True
    return flags


def _pedacos(texto: str, flags: list[bool] | None) -> list[tuple[str, bool]]:
    if flags is None:
        flags = [False] * len(texto)
    pedacos: list[tuple[str, bool]] = []
    i = 0
    while i < len(texto):
        j = i + 1
        while j < len(texto) and flags[j] == flags[i] and texto[j] != " ":
            j += 1
        if j < len(texto) and texto[j] == " ":
            j += 1
        pedacos.append((texto[i:j], flags[i]))
        i = j
    return pedacos


def _desenhar(
    draw: ImageDraw.ImageDraw,
    texto: str,
    marcar: bool,
    font: ImageFont.FreeTypeFont,
    x: int,
    y: int,
    largura: int,
    cor: tuple[int, int, int],
) -> int:
    flags = _faixas(texto) if marcar else None
    cursor_x = x
    linha_h = font.size + 8
    for pedaco, marcado in _pedacos(texto, flags):
        larg = draw.textlength(pedaco, font=font)
        if cursor_x + larg > x + largura and pedaco.strip():
            cursor_x = x
            y += linha_h
        if marcado:
            draw.rectangle(
                (cursor_x - 1, y - 1, cursor_x + larg + 1, y + font.size + 3),
                fill=MARCA,
            )
        draw.text((cursor_x, y), pedaco, font=font, fill=cor)
        cursor_x += larg
    return y + linha_h


def _altura_texto(texto: str, font: ImageFont.FreeTypeFont, largura: int) -> int:
    # Mede a quebra de linha do mesmo jeito que o desenho, sem pintar.
    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)
    cursor_x = 0
    linhas = 1
    for pedaco, _marcado in _pedacos(texto, _faixas(texto)):
        larg = draw.textlength(pedaco, font=font)
        if cursor_x + larg > largura and pedaco.strip():
            cursor_x = 0
            linhas += 1
        cursor_x += larg
    return linhas * (font.size + 8)


def _cartao(
    base: Image.Image,
    titulo: str,
    corpo: str,
    marcar: bool,
    cor_titulo: tuple[int, int, int],
    caixa: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont,
    font_titulo: ImageFont.FreeTypeFont,
) -> None:
    draw = ImageDraw.Draw(base)
    x0, y0, x1, _y1 = caixa
    draw.rounded_rectangle(caixa, radius=18, fill=CARTAO)
    draw.text((x0 + 28, y0 + 22), titulo, font=font_titulo, fill=cor_titulo)
    _desenhar(draw, corpo, marcar, font, x0 + 28, y0 + 68, x1 - x0 - 56, TINTA)


def render(largura: int, altura: int, destino: Path, subtitulo: str, rodape: str) -> None:
    img = Image.new("RGB", (largura, altura), FUNDO)
    draw = ImageDraw.Draw(img)
    titulo_font = ImageFont.truetype(FONTE_NEGRITO, 32)
    sub_font = ImageFont.truetype(FONTE, 18)
    corpo_font = ImageFont.truetype(FONTE, 22)
    rotulo_font = ImageFont.truetype(FONTE_NEGRITO, 18)
    rodape_font = ImageFont.truetype(FONTE, 16)
    draw.text((48, 36), "humanizer-pt-br", font=titulo_font, fill=TINTA)
    draw.text((48, 82), subtitulo, font=sub_font, fill=MUDO)
    margem = 40
    topo = 132
    gap = 20
    col = (largura - margem * 2 - gap) // 2
    miolo = col - 56
    linhas = max(
        _altura_texto(ANTES, corpo_font, miolo),
        _altura_texto(DEPOIS, corpo_font, miolo),
    )
    fundo = topo + 68 + linhas + 28
    _cartao(img, "ANTES", ANTES, True, RUIM, (margem, topo, margem + col, fundo), corpo_font, rotulo_font)
    _cartao(
        img,
        "DEPOIS",
        DEPOIS,
        False,
        BOM,
        (margem + col + gap, topo, largura - margem, fundo),
        corpo_font,
        rotulo_font,
    )
    draw.text((48, altura - 42), rodape, font=rodape_font, fill=MUDO)
    img.save(destino, "PNG")


def main() -> None:
    _conferir()
    SAIDA.mkdir(parents=True, exist_ok=True)
    render(
        1280,
        640,
        SAIDA / "antes-depois.png",
        "Trecho do e-mail fictício do exemplo 01. O amarelo marca padrão do catálogo.",
        "Contagem do catálogo, não nota de detector. O e-mail inteiro está em examples/01-email-relatorio.",
    )
    render(
        1280,
        640,
        SAIDA / "social-preview.png",
        "Português do Brasil sem cara de texto de máquina.",
        "45 padrões · a heurística deste catálogo, não um detector externo.",
    )
    print(SAIDA)


if __name__ == "__main__":
    main()
