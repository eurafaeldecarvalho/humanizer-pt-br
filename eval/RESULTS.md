# Resultados automáticos

Data dos textos: 2026-10-29. Ferramenta: `eval/detector.py`.

O que esta página mede: quantas vezes as heurísticas declaradas em `patterns/` disparam. O que ela não mede: probabilidade de um texto ser de IA, nota de detector comercial (GPTZero, Originality ou outro) ou opinião de leitor. Nenhum desses serviços foi consultado.

A reescrita foi feita pelo mesmo modelo que escreveu o «antes» (Grok 4.7, 2026-10-29), com a instrução de tirar estes padrões. A queda é o efeito dessa instrução nas heurísticas que o script sabe contar. Não é evidência de que uma pessoa classificaria o texto como humano.

## Resumo

| conjunto | textos | média de marcas por texto | mediana |
| --- | ---: | ---: | ---: |
| IA, antes da skill | 30 | 5,93 | 5,00 |
| IA, depois da skill | 30 | 0,00 | 0,00 |
| controle humano (domínio público) | 30 | 0,03 | 0,00 |

Queda no conjunto de IA: de 5,93 para 0,00 (100,00% em relação à média inicial).

## Fatos, números e tamanho

Os 30 pares passaram na checagem: cada número do antes aparece no depois, cada item de `preservar` também, e o tamanho ficou entre 20% e 180% do original.

## Por padrão

| padrão | textos com a marca (antes) | ocorrências antes | ocorrências depois | textos do controle | ocorrências no controle |
| --- | ---: | ---: | ---: | ---: | ---: |
| `a-verdade-e-que` | 2 | 2 | 0 | 0 | 0 |
| `abertura-cada-vez-mais` | 4 | 4 | 0 | 0 | 0 |
| `abertura-mundo-atual` | 2 | 2 | 0 | 0 | 0 |
| `abordagem-holistica` | 2 | 2 | 0 | 0 | 0 |
| `adjetivo-robusto` | 2 | 3 | 0 | 0 | 0 |
| `calque-alavancar` | 3 | 3 | 0 | 0 | 0 |
| `calque-enderecar` | 3 | 3 | 0 | 0 | 0 |
| `cola-nesse-sentido` | 2 | 3 | 0 | 0 | 0 |
| `como-mencionado-acima` | 2 | 2 | 0 | 0 | 0 |
| `compromisso-excelencia` | 3 | 3 | 0 | 0 | 0 |
| `conectivo-empilhado` | 2 | 4 | 0 | 0 | 0 |
| `de-forma-eficaz` | 3 | 3 | 0 | 0 | 0 |
| `desafios-e-oportunidades` | 2 | 2 | 0 | 0 | 0 |
| `desde-os-primordios` | 3 | 3 | 0 | 0 | 0 |
| `ecossistema-metafora` | 2 | 3 | 0 | 0 | 0 |
| `em-ultima-analise` | 4 | 4 | 0 | 0 | 0 |
| `emoji-de-modelo` | 12 | 26 | 0 | 0 | 0 |
| `encontra-bem` | 2 | 2 | 0 | 0 | 0 |
| `fechamento-em-suma` | 5 | 5 | 0 | 0 | 0 |
| `fechamento-motivacional` | 7 | 8 | 0 | 0 | 0 |
| `gama-sem-objeto` | 5 | 5 | 0 | 0 | 0 |
| `gerar-impacto` | 2 | 3 | 0 | 0 | 0 |
| `gerundio-de-intencao` | 3 | 3 | 0 | 0 | 0 |
| `gerundismo` | 3 | 3 | 0 | 0 | 0 |
| `importancia-subestimada` | 3 | 3 | 0 | 0 | 0 |
| `importante-destacar` | 4 | 4 | 0 | 0 | 0 |
| `jornada-vazia` | 2 | 2 | 0 | 0 | 0 |
| `mais-do-que-nunca` | 2 | 2 | 0 | 0 | 0 |
| `nao-apenas-mas-tambem` | 3 | 3 | 0 | 0 | 0 |
| `nao-e-segredo` | 3 | 3 | 0 | 0 | 0 |
| `neste-artigo-vamos` | 3 | 4 | 0 | 0 | 0 |
| `no-que-diz-respeito` | 2 | 2 | 0 | 1 | 1 |
| `outro-ponto-importante` | 3 | 3 | 0 | 0 | 0 |
| `papel-fundamental` | 2 | 4 | 0 | 0 | 0 |
| `pergunta-retorica` | 3 | 3 | 0 | 0 | 0 |
| `ponta-a-ponta` | 4 | 5 | 0 | 0 | 0 |
| `sinergia` | 2 | 2 | 0 | 0 | 0 |
| `sob-medida-vazio` | 4 | 5 | 0 | 0 | 0 |
| `titulo-title-case` | 11 | 12 | 0 | 0 | 0 |
| `travessao-parentetico` | 2 | 4 | 0 | 0 | 0 |
| `triade-adjetivos` | 2 | 2 | 0 | 0 | 0 |
| `vale-ressaltar` | 4 | 4 | 0 | 0 | 0 |
| `vamos-mergulhar` | 5 | 5 | 0 | 0 | 0 |
| `verbo-potencializar` | 2 | 2 | 0 | 0 | 0 |
| `voce-sabia-que` | 3 | 3 | 0 | 0 | 0 |

## Controle humano

Os 30 textos são parágrafos integrais de obras em domínio público, publicadas antes de 1930 (Machado de Assis, Aluísio Azevedo, Lima Barreto, Raul Pompeia). Não são e-mail, legenda nem WhatsApp de 2026. Servem para ver se a heurística dispara em prosa humana antiga. Fonte e licença: `eval/textos/humano/FONTES.md`.

Onde a heurística disparou no controle:

- `h24-lima-policarpo.md`: `no-que-diz-respeito` × 1

Um disparo no controle não transforma o padrão em erro de catálogo. Mostra o limite da regex. «No tocante a», por exemplo, é fórmula de prosa formal, não exclusividade de modelo.

## Avaliação cega

Não foi feita. O protocolo e a planilha estão em `eval/cego.md` e `eval/planilha-cega.csv`. Nenhum número de leitor entra neste arquivo até a rodada existir, com N e data.
