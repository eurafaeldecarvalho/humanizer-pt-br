---
name: humanizer-pt-br
description: Reescreve texto em português do Brasil para tirar marcas típicas de texto gerado por IA, preservando sentido, registro, fatos e termos técnicos. Use quando o usuário pedir para revisar, humanizar ou tirar cara de IA de um texto em português do Brasil.
license: MIT
metadata:
  version: "1.0.0"
  idioma: pt-BR
---

<!-- gerado por scripts/build.py a partir de patterns/ e src/processo.md. Não edite à mão. -->

# Humanizer PT-BR

O catálogo completo, com antes e depois, está em [references/catalogo.md](references/catalogo.md).

Reescreva o texto em português do Brasil para tirar a cara de texto de máquina. O sentido, o registro e os fatos ficam.

## Quando usar

Quando a pessoa pedir para revisar, humanizar, deixar menos artificial ou tirar cara de IA de um texto em português do Brasil.

## Quando não usar

- O pedido é outro: traduzir, resumir, encurtar sem mexer no tom, ou corrigir só ortografia. Não aproveite para reescrever por conta própria.
- O trecho é citação, dispositivo de lei, oração, letra ou número que precisa ficar literal. Mexa só na moldura em volta, se houver moldura.
- A pessoa pediu para manter uma frase. Mantenha e avise que aquela frase continua com a marca.

## Passos

1. Leia o texto inteiro antes de trocar palavra. Anote o gênero (e-mail, legenda, README, recado, nota de aula, release, resposta de suporte), quem fala e quem lê.
2. Liste o que não muda: números, datas, nomes, lugares, termos técnicos, o que foi prometido e a opinião de quem escreveu. Se um dado está ambíguo, conserve a ambiguidade.
3. Marque os trechos que caem no catálogo. Um trecho pode cair em mais de um padrão. A heurística em YAML serve ao script de eval; na reescrita, siga a descrição e o exemplo.
4. Reescreva o texto todo, não só a frase marcada. Corte a moldura. Mantenha a ordem dos fatos. Se havia três informações, as três continuam.
5. Segure o registro. Recado de condomínio não vira ofício. Release não vira bilhete. Não troque palavra simples por sinônimo raro.
6. Não acrescente fato, número, exemplo, emoji, elogio ou chamada que não estava no original. Se o original é vago, o resultado fica vago.
7. Não amenize crítica e não deixe o texto mais educado do que o autor foi. Dá para cortar rodeio sem cortar o incômodo.
8. Título em português: maiúscula na primeira palavra e em nome próprio. Travessão para diálogo ou um aparte curto, não como vírgula decorativa. No texto corrente, aspas assim: "desta forma".
9. Releia a lista de fatos, um por um. Releia outra vez procurando padrão do catálogo, inclusive padrão que a própria reescrita tenha enfiado.
10. Entregue o texto reescrito e uma lista curta: `id` do padrão, o que saiu, o que ficou no lugar. Se não couber ter certeza de um fato, diga isso em vez de escolher uma versão.

## O que parece cacoete e não é

- "Jornada de trabalho", no sentido da CLT, fica. "Jornada do cliente" sai.
- "Deploy", "eSocial", "CPF", "CRM" e o nome do produto ficam.
- "Otimizar uma consulta" num manual técnico fica, quando é o verbo do ofício. "Otimizar resultados", sem dizer qual número, sai.
- Um emoji solto em legenda ou no WhatsApp pode ficar, se combinar com quem fala. Fileira de foguete, estrela e check em e-mail, README ou release sai.
- "A nível de" é vício antigo de fala, de gente e de máquina. Não está no catálogo automático. Só troque se o resto da frase já estiver sendo reescrito e a troca não mudar o tom de quem fala.

## O que não afirmar

Não diga que o texto passou em detector, que "parece humano" ou que um leitor não vai perceber. Você tirou padrões de um catálogo. É só isso que dá para afirmar.

## Catálogo, em uma linha

### abertura

- **Abertura «em um mundo» e «na era digital»** (`abertura-cada-vez-mais`). Em um mundo conectado, a padaria do seu Paulo passou a anotar encomenda no celular.
- **Abertura «no mundo atual»** (`abertura-mundo-atual`). No mundo atual, a planilha de vendas do interior virou prioridade da área.
- **Pergunta retórica de abertura** (`pergunta-retorica`). Você já parou para pensar por que a fila do pão dobra às 7h?
- **«Desde os primórdios»** (`desde-os-primordios`). Desde os primórdios da informática, dígitos verificadores evitam erro de digitação.
- **«Espero que esta mensagem o encontre bem»** (`encontra-bem`). Espero que esta mensagem a encontre bem. Segue o comprovante do boleto 1022.
- **«Mais do que nunca»** (`mais-do-que-nunca`). Mais do que nunca, a meta de novembro pede atenção: são R$ 220 mil.
- **«Neste artigo vamos»** (`neste-artigo-vamos`). Neste artigo, vamos explorar como conferir o dígito do CPF. Ao longo deste guia, o essencial aparece.
- **«Vamos mergulhar» e «vamos explorar»** (`vamos-mergulhar`). Vamos mergulhar nos preparativos: o churrasco é sábado, ao meio-dia, na casa do tio Laerte.
- **«Você sabia que»** (`voce-sabia-que`). Você sabia que o pão francês fica a R$ 1,25 até sábado?

### conectivo

- **«Além disso» e «ademais» empilhados** (`conectivo-empilhado`). O café da sessão está incluso. Além disso, a loja fica na rua Halfeld. Ademais, o clube é na quinta.
- **«Como mencionado acima»** (`como-mencionado-acima`). Como mencionado acima, o desbloqueio é no balcão, com RG.
- **«Em última análise»** (`em-ultima-analise`). Em última análise, a vírgula é o que separa o convite do almoço.
- **«Nesse sentido» e «dito isso»** (`cola-nesse-sentido`). Diante desse cenário, a entrega do arquivo fica para as 10h. Nesse sentido, seguimos alinhados.
- **«No que diz respeito a»** (`no-que-diz-respeito`). No que diz respeito à meta de novembro, o valor combinado é R$ 220 mil.
- **«Outro ponto importante»** (`outro-ponto-importante`). Outro ponto importante é a falta de Diego e Ruth na unidade Moema.
- **«Vale ressaltar»** (`vale-ressaltar`). Vale ressaltar que o relatório foi validado pela controladoria em 28/10/2026.
- **«É importante destacar»** (`importante-destacar`). É importante destacar que o protocolo 55219 está com a Marina, do financeiro.

### estrutura

- **Gerundismo «vou estar enviando»** (`gerundismo`). Vou estar enviando o desenho ainda hoje e vamos estar verificando o saldo.
- **Gerúndio de intenção em cadeia** (`gerundio-de-intencao`). O time segue buscando cruzar os lançamentos e garantindo uma visão única da planilha.
- **Travessão no meio da frase** (`travessao-parentetico`). O relatório — versão interna — saiu ontem, e as pendências — todas de Barretos — continuam na mesa do Caio.
- **Tríade de adjetivos vazios** (`triade-adjetivos`). O relatório do 3º trimestre entregue é robusto, abrangente e estratégico.
- **«Não apenas… mas também»** (`nao-apenas-mas-tambem`). O relatório não foi apenas fechado, mas também validado pela controladoria.

### vocabulario

- **Calque «alavancar» e «entregar valor»** (`calque-alavancar`). No final do dia, o plano de novembro precisa alavancar vendas e entregar valor.
- **Calque «endereçar o problema»** (`calque-enderecar`). O suporte vai endereçar o problema do boleto ainda hoje.
- **«Abordagem holística»** (`abordagem-holistica`). O fechamento pede uma abordagem holística e uma visão 360 da planilha.
- **«Compromisso com a excelência»** (`compromisso-excelencia`). Nosso compromisso com a excelência: consulta de cão e de gato, sem internação.
- **«De forma eficaz»** (`de-forma-eficaz`). O time vai cruzar as notas de forma eficaz e de maneira estratégica.
- **«Ecossistema» fora da biologia** (`ecossistema-metafora`). Nosso ecossistema digital junta o plano de fibra e o suporte por WhatsApp.
- **«Gerar impacto»** (`gerar-impacto`). A oficina de 40 minutos foi desenhada para gerar impacto positivo: cada pessoa traz um atendimento de outub…
- **«Jornada» metafórica** (`jornada-vazia`). A promoção abre uma jornada de sucesso na coordenação.
- **«Papel fundamental»** (`papel-fundamental`). A controladoria desempenha um papel fundamental na validação do relatório.
- **«Ponta a ponta» e «solução completa»** (`ponta-a-ponta`). A biblioteca é uma solução completa, ponta a ponta, para CPF: confere o dígito, formata e não consulta a Re…
- **«Potencializar» e «otimizar resultados»** (`verbo-potencializar`). Seguimos potencializando o fechamento da folha de novembro e otimizando resultados.
- **«Robusto» e «abrangente»** (`adjetivo-robusto`). A garrafa Serra Fria tem corpo robusto e uma proposta abrangente: 500 ml, aço inox 304.
- **«Sinergia»** (`sinergia`). O fechamento da folha depende da sinergia entre o DP e o compras.
- **«Sob medida para você» e «experiência única»** (`sob-medida-vazio`). A aula experimental dura 30 minutos, custa R$ 40 e é uma experiência única, sob medida para suas necessidades.
- **«Uma gama de fatores»** (`gama-sem-objeto`). Uma série de fatores explica os 36 itens que ficaram só no celular.

### fechamento

- **Fechamento motivacional** (`fechamento-motivacional`). O bolo é sexta, no pátio, depois das 18h. Juntos, podemos mais. O futuro é promissor. Vamos nessa.
- **«A verdade é que»** (`a-verdade-e-que`). A verdade é que a conta de luz da padaria não baixou em 2018.
- **«Desafios e oportunidades»** (`desafios-e-oportunidades`). O trimestre traz desafios e oportunidades: faltam Diego e Ruth, e a meta é R$ 220 mil.
- **«Em suma» mecânico** (`fechamento-em-suma`). Em suma, o arquivo segue amanhã às 10h.
- **«Não pode ser subestimada»** (`importancia-subestimada`). A importância da vírgula não pode ser subestimada: sem ela, «vamos comer crianças» deixa de ser um chamado.
- **«Não é segredo que»** (`nao-e-segredo`). Não é segredo que o time de DP tem 6 pessoas.

### formato

- **Fileira de emoji de modelo** (`emoji-de-modelo`). A clínica abre em novembro. 🚀✨ Agende na recepção.
- **Título com maiúsculas de inglês** (`titulo-title-case`). Como Validar CPF Em Python Com Clareza

## Exemplo trabalhado

E-mail fictício, escrito por Grok 4.7 em 2026-10-29 para este repositório (`eval/textos/ia/01-email-relatorio`). A reescrita é do mesmo modelo, no mesmo dia, seguindo este processo. Não é texto de um terceiro.

**Antes.**

Assunto: relatório do 3º trimestre

Prezada Ana Luiza Prado,

Espero que esta mensagem a encontre bem. No mundo atual, consolidar as vendas do interior pede contexto. Vale ressaltar que o relatório do 3º trimestre — versão interna — não foi apenas fechado, mas também validado pela controladoria em 28/10/2026. O documento ficou robusto, abrangente e estratégico.

Além disso, é importante destacar que as notas fiscais de Barretos seguem com 14 pendências — todas em aberto — na planilha. Ademais, diante desse cenário, a entrega desempenha um papel crucial na jornada de transparência da área.

Estamos potencializando o fechamento, buscando cruzar os lançamentos e garantindo uma abordagem holística. 🚀✨ Nesse sentido, juntos, podemos seguir. O futuro é promissor.

Em suma, envio o arquivo em 30/10/2026 às 10h.

Atenciosamente,
Caio Mendes

**Depois.**

Ana Luiza Prado, boa tarde.

O relatório do 3º trimestre está fechado. A controladoria validou em 28/10/2026. As notas fiscais de Barretos ainda têm 14 pendências na planilha.

Mando o arquivo em 30/10/2026 às 10h.

Caio Mendes

**Marcas contadas pela heurística.**

| padrão | antes | depois |
| --- | ---: | ---: |
| `abertura-mundo-atual` | 1 | 0 |
| `abordagem-holistica` | 1 | 0 |
| `adjetivo-robusto` | 2 | 0 |
| `cola-nesse-sentido` | 2 | 0 |
| `conectivo-empilhado` | 2 | 0 |
| `emoji-de-modelo` | 2 | 0 |
| `encontra-bem` | 1 | 0 |
| `fechamento-em-suma` | 1 | 0 |
| `fechamento-motivacional` | 2 | 0 |
| `gerundio-de-intencao` | 1 | 0 |
| `importante-destacar` | 1 | 0 |
| `jornada-vazia` | 1 | 0 |
| `nao-apenas-mas-tambem` | 1 | 0 |
| `papel-fundamental` | 2 | 0 |
| `titulo-title-case` | 1 | 0 |
| `travessao-parentetico` | 2 | 0 |
| `triade-adjetivos` | 1 | 0 |
| `vale-ressaltar` | 1 | 0 |
| `verbo-potencializar` | 1 | 0 |
