# Como foi feito

Grok 4.7, rodando como agente no Cursor, escreveu o catálogo, os exemplos, a reescrita, o detector, o README e os testes em 2026-10-29. Também rodou a contagem e a checagem de n-gramas.

O dono do repositório, nativo de português do Brasil, ainda não revisou padrão por padrão. Enquanto isso não acontece, a curadoria humana está pendente. Não trate a v1 como lista fechada por um revisor humano.

Os textos «antes» foram gerados nesse dia, para este repositório, com o prompt gravado em cada `meta.yaml`. Não são posts, e-mails ou releases de terceiros. Empresas, clínicas, planos e prefeituras que aparecem ali são cenário.

Os textos «depois» são do mesmo modelo, no mesmo dia, aplicando `src/processo.md` e o catálogo. Não houve um segundo modelo reescrevendo às cegas, nem pós-edição para forçar a heurística a zerar à custa do sentido. Onde a reescrita zerou a contagem, é porque as frases que a regex procura saíram. Isso não significa que um leitor, ou um detector comercial, daria o texto como humano. Nenhum detector externo foi consultado, e o repositório não afirma resultado de nenhum.

Cada padrão da v1 tem exemplo de um único modelo. A regra de «dois modelos», em `CONTRIBUTING.md`, vale para padrão novo daqui em diante.

A avaliação cega descrita em `eval/cego.md` não foi aplicada. Não há N nem data de leitor.

O repositório permanece privado até o dono decidir o contrário.
