# Avaliação cega

Ainda não foi feita. Não há N, data nem taxa. O README só pode citar esses números depois de uma rodada real.

## O que se quer medir

Uma pessoa que lê português do Brasil vê três tipos de texto, sem rótulo:

- texto de IA bruto, escrito para este repositório
- o mesmo texto depois da skill
- parágrafo humano em domínio público

Ela marca cada um como «parece IA», «parece humano» ou «não sei». A comparação que importa é a taxa de «parece IA» no bruto e na reescrita. O humano entra para ver se o leitor está marcando tudo como IA.

## Como montar

Quem conduz a rodada não deve ser leitor se já viu os originais. Oito leitores é um piso razoável; o dono escolhe N.

```bash
python eval/montar_cego.py --semente 7 --saida eval/cego-pacote
```

Isso embaralha 10 textos brutos, 10 reescritos e 10 humanos em `eval/cego-pacote/textos/`. A `CHAVE.csv` fica com quem conduz. O leitor recebe só a pasta `textos/` e uma cópia de [planilha-cega.csv](planilha-cega.csv).

Não diga ao leitor qual skill está em teste nem mostre o catálogo antes da leitura.

## Como registrar

Na planilha: `leitor_id`, data, código do texto (`T01`…), julgamento (`ia`, `humano` ou `nao_sei`) e um comentário opcional. Quem conduz junta a chave depois e calcula:

- entre os brutos, quantos foram marcados `ia`
- entre os reescritos, quantos foram marcados `ia`
- entre os humanos, quantos foram marcados `ia`

Publique N, a data, o critério de quem leu (por exemplo «lê e escreve em português do Brasil no dia a dia») e as três taxas. Não arredonde uma rodada piloto para parecer estudo fechado.
