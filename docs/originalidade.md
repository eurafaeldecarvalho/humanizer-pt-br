# Originalidade

Medição de 2026-10-29. O CI volta a contar a cada execução e falha se aparecer trecho em comum.

O catálogo, os exemplos e o texto da skill foram escritos para este repositório. A checagem abaixo compara esse material com os `SKILL.md` públicos dos projetos citados no README. O texto deles não é copiado para cá. Entram só o caminho, o tamanho e o sha256.

Método: janelas de 8 palavras, em minúsculas, sem pontuação. Conta como trecho a janela com pelo menos 4 palavras fora de uma lista de conectivos (português e inglês), em `ptbr_humanizer/ngrams.py`. Janela só de função gramatical não entra, para não marcar esqueleto de frase.

Arquivos nossos: tudo em Markdown e YAML, exceto `eval/textos/humano/` (domínio público), `LICENSE` e este relatório.

## Referências consultadas

- `blader/humanizer` (`main`) `SKILL.md` — 32348 bytes, sha256 `0612f1dfb1672b0ea9b97e139bf1f06cabe98d8b27424fe8ff01e1fb4cc99cad`
- `op7418/Humanizer-zh` (`main`) `SKILL.md` — 20527 bytes, sha256 `95627fd4437d886f98032ccc62d79136e6310f1fc04e354bb86431795ff206df`
- `mackswendhell/humanizer-pt-br` (`main`) `SKILL.md` — 25512 bytes, sha256 `2ddd6fcd759097991534aa7740bc75a26419e927d03e88199e3b6349dec6ffbe`

Arquivos nossos na comparação: 188.

Trechos em comum (8 palavras, com pelo menos 4 de conteúdo): 0

Janelas brutas de 8 palavras, sem o filtro de conteúdo: 0.

Nenhum trecho em comum com o critério acima.
