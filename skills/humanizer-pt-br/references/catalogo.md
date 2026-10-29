<!-- gerado por scripts/build.py a partir de patterns/ e src/processo.md. Não edite à mão. -->

# Catálogo

Cada exemplo foi escrito para este repositório por Grok 4.7 em 2026-10-29. A heurística automática é mais estreita que o texto: na reescrita, siga a descrição.

## abertura

### Abertura «em um mundo» e «na era digital»

`abertura-cada-vez-mais`

«Em um mundo…» e «na era digital» anunciam novidade sem dizer o que mudou. O leitor de 2026 já está nesse mundo; a frase não informa. «Cada vez mais», sozinho, também é fala de gente, então a heurística não conta essa expressão isolada.

**Como corrigir.** Diga a mudança concreta, com o objeto e, se existir, a data. Se não houver mudança no texto, comece pelo pedido.

**Antes.** Em um mundo conectado, a padaria do seu Paulo passou a anotar encomenda no celular.

**Depois.** A padaria do seu Paulo agora anota encomenda no celular.

*Limite da contagem automática:* Não conta «cada vez mais» solto: é frase comum em texto humano.

### Abertura «no mundo atual»

`abertura-mundo-atual`

O texto começa com um panorama que serve para qualquer assunto: «no mundo atual», «no cenário atual», «no mundo de hoje». Não diz cidade, data nem quem fez o quê. O fato, que era a razão do texto, fica para o segundo período.

**Como corrigir.** Apague a moldura e abra com o fato. Se o contexto importa e já está no texto, troque o chavão pelo nome do lugar e pela data. Não invente cenário para justificar a abertura.

**Antes.** No mundo atual, a planilha de vendas do interior virou prioridade da área.

**Depois.** A planilha de vendas do interior é a prioridade da área nesta semana.

### Pergunta retórica de abertura

`pergunta-retorica`

«Você já parou para pensar…?» abre artigo, legenda e e-mail sem esperar resposta. A pergunta não traz dado; ela segura o fato por uma linha. Em conversa de verdade a pergunta costuma ser específica («o forno de 1998 aguentou o sábado?»).

**Como corrigir.** Tire a pergunta e entre no fato. Se a pergunta for de fato uma pergunta (a pessoa precisa responder), deixe e deixe claro o que se espera de volta.

**Antes.** Você já parou para pensar por que a fila do pão dobra às 7h?

**Depois.** A fila do pão dobra às 7h, quando chega o turno da fábrica.

### «Desde os primórdios»

`desde-os-primordios`

Puxa a história da humanidade para introduzir um assunto pequeno: um festival, um dígito verificador, um app. O salto não explica o fato de hoje. Também entra «desde a aurora» e «ao longo da história da humanidade».

**Como corrigir.** Comece na data e no lugar do fato. Se a história antiga está no original e é específica (um forno de 1998, uma lei de um ano), cite esse marco, não «os primórdios».

**Antes.** Desde os primórdios da informática, dígitos verificadores evitam erro de digitação.

**Depois.** O dígito verificador pega erro de digitação no CPF.

### «Espero que esta mensagem o encontre bem»

`encontra-bem`

É decalque de «I hope this message finds you well». Em e-mail brasileiro, a abertura costuma ser «bom dia», o nome da pessoa e o assunto. A fórmula aparece mesmo quando quem escreve e quem lê se falam toda semana.

**Como corrigir.** Use o cumprimento do registro real: «Ana, bom dia» no trabalho, «oi» no recado. Se o original não pergunta como a pessoa está, não pergunte.

**Antes.** Espero que esta mensagem a encontre bem. Segue o comprovante do boleto 1022.

**Depois.** Ana, bom dia. Segue o comprovante do boleto 1022.

### «Mais do que nunca»

`mais-do-que-nunca`

Aumenta a urgência sem medida. «Mais do que nunca, precisamos alinhar» não diz mais do que quando, nem o que acontece se ninguém alinhar. Gente também usa a expressão; aqui ela entra quando serve de abertura vazia, e a heurística conta a expressão sempre que aparece, com essa limitação.

**Como corrigir.** Troque pela consequência prática ou apague. Se o prazo é sexta, escreva sexta.

**Antes.** Mais do que nunca, a meta de novembro pede atenção: são R$ 220 mil.

**Depois.** A meta de novembro é R$ 220 mil.

*Limite da contagem automática:* A expressão também aparece em texto humano. A heurística não distingue abertura vazia de ênfase real.

### «Neste artigo vamos»

`neste-artigo-vamos`

O texto anuncia o que vai fazer em vez de fazer. «Neste artigo, vamos explorar» e «ao longo deste guia» são moldura de blog. Um README ou uma nota de aula podem dizer o que o leitor encontra, em uma linha, sem prometer uma viagem.

**Como corrigir.** Substitua o anúncio pelo conteúdo. «Neste artigo vamos ver como validar CPF» vira a primeira instrução, ou uma frase: «A função confere o dígito; não consulta a Receita».

**Antes.** Neste artigo, vamos explorar como conferir o dígito do CPF. Ao longo deste guia, o essencial aparece.

**Depois.** A função confere o dígito do CPF. Ela não consulta a Receita Federal.

### «Vamos mergulhar» e «vamos explorar»

`vamos-mergulhar`

Convite de vídeo transferido para texto: «vamos mergulhar», «mergulhe de cabeça», «vamos explorar». Não diz em quê, nem até onde. Em nota curta, o verbo que importa é o da tarefa (conferir, cortar, enviar).

**Como corrigir.** Troque pelo verbo da tarefa. Se o original é uma aula e a pessoa realmente conduz o passo, use o imperativo direto: «abra o arquivo», «sepah a sacola».

**Antes.** Vamos mergulhar nos preparativos: o churrasco é sábado, ao meio-dia, na casa do tio Laerte.

**Depois.** O churrasco é sábado, ao meio-dia, na casa do tio Laerte.

### «Você sabia que»

`voce-sabia-que`

Abre legenda e texto de produto com uma curiosidade que em geral não é curiosa: é o próprio recado, disfarçado de quiz. Quem lê a legenda da padaria já quer o preço e o horário.

**Como corrigir.** Diga o recado. Se houver uma curiosidade real e específica no original, deixe o fato sem o prefácio.

**Antes.** Você sabia que o pão francês fica a R$ 1,25 até sábado?

**Depois.** O pão francês fica a R$ 1,25 até sábado.

## conectivo

### «Além disso» e «ademais» empilhados

`conectivo-empilhado`

Um «além disso» é fala normal. Dois ou mais, somados a «ademais» e «outrossim» no mesmo texto curto, são o modelo costurando parágrafos que não têm ligação própria. «Outrossim» em e-mail de 2026 quase nunca é escolha de quem escreve no trabalho.

**Como corrigir.** Una os fatos na ordem em que acontecem, sem cola. Se os fatos não se ligam, faça duas frases curtas ou dois parágrafos, sem conectivo de redação.

**Antes.** O café da sessão está incluso. Além disso, a loja fica na rua Halfeld. Ademais, o clube é na quinta.

**Depois.** O café da sessão está incluso. A loja fica na rua Halfeld. O clube é na quinta.

*Limite da contagem automática:* Um conectivo só não conta. A heurística dispara a partir de duas ocorrências.

### «Como mencionado acima»

`como-mencionado-acima`

O modelo finge que já explicou. «Como mencionado anteriormente» aponta para um parágrafo que não disse aquilo, ou que disse de passagem. Em texto curto, o leitor não precisa ser mandado de volta.

**Como corrigir.** Repita o fato em meia linha, se ele ainda faz falta. Se não faz, apague a remissão.

**Antes.** Como mencionado acima, o desbloqueio é no balcão, com RG.

**Depois.** O desbloqueio é no balcão, com RG.

### «Em última análise»

`em-ultima-analise`

«Em primeira análise» e «em última análise» emprestam tom de parecer a um relato que não analisou nada. «Em última instância» tem uso jurídico real; a heurística não separa esse uso do enfeite, e isso está declarado aqui.

**Como corrigir.** Diga a conclusão como frase sua. «Em última análise, a linha 221 está curta» vira «a 221 está curta nesse horário».

**Antes.** Em última análise, a vírgula é o que separa o convite do almoço.

**Depois.** A vírgula separa o convite do almoço.

*Limite da contagem automática:* Não distingue o uso jurídico de «em última instância».

### «Nesse sentido» e «dito isso»

`cola-nesse-sentido`

«Nesse sentido», «dito isso», «diante desse cenário» e «posto isso» ligam duas frases que não chegaram a formar um argumento. O cenário quase nunca foi descrito. Não confundir com «sendo assim» depois de uma conta que acaba de ser feita: esse ficou de fora da heurística de propósito.

**Como corrigir.** Mostre a ligação, se houver («como a ponte está alagada, o prazo de 18 minutos não fecha»). Se não houver, comece a frase seguinte direto.

**Antes.** Diante desse cenário, a entrega do arquivo fica para as 10h. Nesse sentido, seguimos alinhados.

**Depois.** O arquivo sai às 10h.

*Limite da contagem automática:* «Sendo assim» e «diante disso», mais comuns em prosa humana, não entram.

### «No que diz respeito a»

`no-que-diz-respeito`

«No que diz respeito a», «no tocante a» e «no que tange a» atrasam o tema em quatro ou cinco palavras. É fórmula de ofício que o modelo cola em legenda, e-mail e nota de campo. O tema vem logo depois e quase sempre cabe como sujeito.

**Como corrigir.** Faça o tema de sujeito. «No que diz respeito à meta de novembro» vira «a meta de novembro é…».

**Antes.** No que diz respeito à meta de novembro, o valor combinado é R$ 220 mil.

**Depois.** A meta de novembro é R$ 220 mil.

### «Outro ponto importante»

`outro-ponto-importante`

Numera ideias sem número e sem hierarquia: «outro ponto importante», «outro aspecto relevante». O leitor não ficou sabendo qual era o primeiro ponto. A frase seguinte é que tem o conteúdo, e ela se sustenta sozinha.

**Como corrigir.** Escreva o conteúdo. Se a ordem importa, numere de verdade ou use «primeiro» e «depois» com os fatos.

**Antes.** Outro ponto importante é a falta de Diego e Ruth na unidade Moema.

**Depois.** Diego e Ruth não estão na unidade Moema.

### «Vale ressaltar»

`vale-ressaltar`

«Vale ressaltar», «vale destacar», «vale lembrar», «vale pontuar» anunciam que a próxima frase é importante, em vez de escrever a frase importante. Empilhado no começo do parágrafo, vira muleta. Um «vale lembrar» solto num recado de síndico às vezes é fala natural; a heurística não faz essa distinção e conta a muleta sempre.

**Como corrigir.** Apague o anúncio e deixe a informação. Se ela for realmente um aviso, o imperativo basta: «enche a caixa na quarta».

**Antes.** Vale ressaltar que o relatório foi validado pela controladoria em 28/10/2026.

**Depois.** A controladoria validou o relatório em 28/10/2026.

*Limite da contagem automática:* Conta também o «vale lembrar» de recado cotidiano, que nem sempre é cacoete.

### «É importante destacar»

`importante-destacar`

Parente de «vale ressaltar», com verbo de ênfase: «é importante destacar», «é fundamental ressaltar», «cabe salientar», «é imprescindível destacar». A ênfase ocupa o lugar do dado. Em ofício antigo a fórmula existe; em e-mail curto ela quase sempre é enchimento.

**Como corrigir.** Fique com o dado. Se houver risco real, diga o risco («sem a baixa, o boleto continua em aberto»), não a palavra «importante».

**Antes.** É importante destacar que o protocolo 55219 está com a Marina, do financeiro.

**Depois.** O protocolo 55219 está com a Marina, do financeiro.

## estrutura

### Gerundismo «vou estar enviando»

`gerundismo`

«Vou estar enviando», «vamos estar verificando»: o futuro composto com gerúndio no lugar de «envio» ou «vejo». É vício de fala no telefone e também um tique de modelo em e-mail de suporte, onde a ação cabe no presente ou no futuro simples.

**Como corrigir.** Use o verbo simples no tempo verdadeiro. «Vou estar enviando o desenho» vira «o desenho vai anexo» ou «envio o desenho hoje», conforme o fato.

**Antes.** Vou estar enviando o desenho ainda hoje e vamos estar verificando o saldo.

**Depois.** O desenho vai ainda hoje. O saldo eu confiro em seguida.

*Limite da contagem automática:* Não marca «está enviando» nem «estar + gerúndio» sem o verbo de futuro na frente.

### Gerúndio de intenção em cadeia

`gerundio-de-intencao`

«Buscando», «visando», «garantindo», «promovendo», «fomentando» enfileirados na mesma frase. Cada um promete uma ação e não diz quem faz o quê até quando. Um gerúndio só («fico aguardando o arquivo») é fala comum e não entra.

**Como corrigir.** Troque por oração com sujeito e verbo no tempo certo. «Buscando cruzar os lançamentos e garantindo visão» vira «a Marina cruza os lançamentos hoje», se isso estiver no texto. Se ninguém foi nomeado, não invente o responsável: diga só o que está feito e o que falta.

**Antes.** O time segue buscando cruzar os lançamentos e garantindo uma visão única da planilha.

**Depois.** O time está cruzando os lançamentos da planilha.

*Limite da contagem automática:* Exige dois gerúndios dessa lista na mesma frase. Um gerúndio isolado não conta.

### Travessão no meio da frase

`travessao-parentetico`

O travessão de diálogo, no começo da réplica, é pontuação de prosa. O cacoete é outro: dois apartes no meio da frase, no lugar de vírgula ou de parêntese, muitas vezes com um elogio dentro («o relatório — documento robusto — saiu»). A heurística conta pares (abre e fecha) e só dispara a partir do segundo par, para não marcar um aparte único nem a fala «— Bonita canoa!».

**Como corrigir.** Se o aparte é um fato, vire frase. Se é elogio, corte. Um travessão só, quando a pessoa falaria assim, pode ficar.

**Antes.** O relatório — versão interna — saiu ontem, e as pendências — todas de Barretos — continuam na mesa do Caio.

**Depois.** O relatório interno saiu ontem. As pendências de Barretos continuam na mesa do Caio.

*Limite da contagem automática:* Conta pares de travessão com aparte no meio, sem ! ou ? dentro do par. Dispara a partir de dois pares. Um aparte só não conta. Fala de diálogo não conta.

### Tríade de adjetivos vazios

`triade-adjetivos`

Três adjetivos em fila, tirados de um estoque pequeno: robusto, abrangente, estratégico, inovador, escalável, integrado. A tríade não diferencia um relatório de uma garrafa. Três substantivos concretos («fica, conserto, doação») não entram na heurística.

**Como corrigir.** Troque a tríade pelo traço que distingue a coisa, ou corte. «Relatório robusto, abrangente e estratégico» vira «relatório do 3º trimestre», se é isso que ele é.

**Antes.** O relatório do 3º trimestre entregue é robusto, abrangente e estratégico.

**Depois.** O relatório entregue é o do 3º trimestre.

*Limite da contagem automática:* Só reconhece uma lista fechada de adjetivos. «Café, pão e manteiga» não conta.

### «Não apenas… mas também»

`nao-apenas-mas-tambem`

A estrutura «não apenas X, mas também Y» (e «não só X, como também Y») infla duas informações que caberiam numa coordenação simples. O modelo usa a forma mesmo quando X e Y não contrastam: fechar e validar, desconto e convite, armário e capítulo.

**Como corrigir.** Se os dois fatos importam, escreva os dois em sequência. Se o segundo é enfeite, fique só com o primeiro. Não mantenha o contraste se não houver contraste.

**Antes.** O relatório não foi apenas fechado, mas também validado pela controladoria.

**Depois.** O relatório está fechado e a controladoria validou.

## vocabulario

### Calque «alavancar» e «entregar valor»

`calque-alavancar`

«Alavancar resultados», «entregar valor» e «no final do dia» são decalques de leverage, deliver value e at the end of the day. Em português de trabalho a gente diz aumentar a venda, cumprir o prazo, no fim do expediente. «Alavancar» um objeto físico (uma tampa, com uma alavanca) não é o caso destes exemplos.

**Como corrigir.** Escreva o verbo do fato: vender, cortar, atrasar, cobrar. «No final do dia» vira «no fim do expediente» só se for horário; se for «afinal», escreva «afinal».

**Antes.** No final do dia, o plano de novembro precisa alavancar vendas e entregar valor.

**Depois.** O plano de novembro existe para vender mais.

### Calque «endereçar o problema»

`calque-enderecar`

«Endereçar um problema» traduz to address. Em português, a gente trata, resolve, responde ou olha o problema. O verbo «endereçar» continua válido para pôr endereço em envelope. A heurística só marca «endereçar» seguido de problema, questão, desafio, ponto ou tema.

**Como corrigir.** Use o verbo que diz o que vai ser feito. «Vamos endereçar essa questão» vira «a Marina responde hoje» ou «isso ainda está em aberto», conforme o fato.

**Antes.** O suporte vai endereçar o problema do boleto ainda hoje.

**Depois.** O suporte baixa o boleto ainda hoje.

*Limite da contagem automática:* Não marca «endereçar uma carta».

### «Abordagem holística»

`abordagem-holistica`

«Holístico», «visão holística» e «visão 360» prometem que nada ficou de fora. Em geral é o contrário: o texto não listou as partes. A palavra chegou ao português corporativo por slide traduzido e o modelo a usa fora de qualquer método.

**Como corrigir.** Liste as partes, ou diga o limite («só dígito e máscara, sem consulta à Receita»). Não troque «holística» por «integrada».

**Antes.** O fechamento pede uma abordagem holística e uma visão 360 da planilha.

**Depois.** O fechamento usa a planilha inteira.

### «Compromisso com a excelência»

`compromisso-excelencia`

«Compromisso com a excelência», «excelência operacional» e «busca incessante pela excelência» fecham parágrafo sem critério. Excelência não diz se a folha fecha na sexta ou se o pão sai às 6h. É assinatura de release e de página de vaga.

**Como corrigir.** Troque pelo critério que dá para cobrar. Se o original não tem critério, a frase sai.

**Antes.** Nosso compromisso com a excelência: consulta de cão e de gato, sem internação.

**Depois.** A clínica faz consulta de cão e de gato e não faz internação.

### «De forma eficaz»

`de-forma-eficaz`

«De forma eficaz», «de maneira significativa», «de forma assertiva», «de forma estratégica». O advérbio não diz como. Esconde a falta do método. «De forma» seguida de adjetivo de slide é moldura; «de forma alguma» não entra na lista.

**Como corrigir.** Descreva o método em uma frase, se ele estiver no texto. Se não estiver, apague o advérbio e deixe o verbo.

**Antes.** O time vai cruzar as notas de forma eficaz e de maneira estratégica.

**Depois.** O time vai cruzar as notas.

### «Ecossistema» fora da biologia

`ecossistema-metafora`

«Ecossistema digital», «ecossistema de inovação», «todo o ecossistema» incham um conjunto de coisas que têm nome: o app e o suporte, a feira e o pix, o plano e a instalação. Ecossistema marinho ou de floresta não entra na lista.

**Como corrigir.** Nomeie as partes. Se são duas, escreva as duas.

**Antes.** Nosso ecossistema digital junta o plano de fibra e o suporte por WhatsApp.

**Depois.** O plano é a fibra. O suporte é por WhatsApp.

*Limite da contagem automática:* Não marca «ecossistema» de biologia ou geografia.

### «Gerar impacto»

`gerar-impacto`

«Gerar impacto», «impactar positivamente», «impacto significativo» medem nada. Não dizem em quem, em quanto, em qual prazo. Relato de campo e texto de ONG usam «impacto» de modo concreto às vezes; a heurística não lê o complemento e conta a expressão da lista.

**Como corrigir.** Troque pela consequência que já está escrita (o prazo de 18 minutos, a fila, o cheiro do balde). Se a consequência não está no texto, corte.

**Antes.** A oficina de 40 minutos foi desenhada para gerar impacto positivo: cada pessoa traz um atendimento de outubro que deu errado.

**Depois.** Na oficina de 40 minutos, cada pessoa traz um atendimento de outubro que deu errado.

*Limite da contagem automática:* Não julga se o complemento torna «impacto» concreto.

### «Jornada» metafórica

`jornada-vazia`

«Jornada do cliente», «jornada de compra», «jornada de sucesso», «nesta jornada». A palavra saiu do dia de trabalho e virou caminho heroico para qualquer processo. «Jornada de trabalho» no sentido da CLT não está na lista.

**Como corrigir.** Diga o processo pelo nome: a compra, o primeiro mês na função, o fechamento da folha. Se for a jornada da CLT, deixe.

**Antes.** A promoção abre uma jornada de sucesso na coordenação.

**Depois.** A promoção é para a coordenação do DP. O time tem 6 pessoas.

*Limite da contagem automática:* Não marca «jornada de trabalho».

### «Papel fundamental»

`papel-fundamental`

«Desempenha um papel fundamental», «papel crucial», «papel essencial». A frase diz que algo importa e não diz o que a coisa faz. Quase sempre dá para substituir pelo verbo real: a controladoria valida, a vírgula separa, o boleto cobra.

**Como corrigir.** Troque «desempenha um papel» pelo verbo. Se não houver verbo no original, a frase pode cair fora.

**Antes.** A controladoria desempenha um papel fundamental na validação do relatório.

**Depois.** A controladoria valida o relatório.

### «Ponta a ponta» e «solução completa»

`ponta-a-ponta`

«Solução completa», «plataforma completa» e «ponta a ponta» dizem que o produto faz tudo. Quase nunca faz. O leitor precisa da lista curta: o que entra, o que não entra (não consulta a Receita, não cifra, não tem TV).

**Como corrigir.** Liste o que o produto faz e, se o original diz, o que ele não faz. Corte «completa» se a lista já existe.

**Antes.** A biblioteca é uma solução completa, ponta a ponta, para CPF: confere o dígito, formata e não consulta a Receita.

**Depois.** A biblioteca confere o dígito do CPF e formata o número. Não consulta a Receita.

### «Potencializar» e «otimizar resultados»

`verbo-potencializar`

«Potencializar» e «otimizar» sem objeto técnico viram verbo de slide. Não dizem se o número sobe, desce ou deixa de ser refeito. Num manual, «otimizar a consulta» pode ser o termo do ofício: a heurística não lê esse contexto e conta o verbo mesmo assim.

**Como corrigir.** Diga a mudança. «Potencializar o fechamento» vira «fechar a folha sem hora extra no fim de semana», se isso estiver escrito. Se não estiver, corte o verbo.

**Antes.** Seguimos potencializando o fechamento da folha de novembro e otimizando resultados.

**Depois.** Estamos fechando a folha de novembro.

*Limite da contagem automática:* Não separa «otimizar uma consulta SQL» de «otimizar resultados».

### «Robusto» e «abrangente»

`adjetivo-robusto`

«Robusto», «abrangente» e «disruptivo» elogiam sem dizer o que a coisa aguenta, cobre ou muda. Colados em relatório, plataforma e processo, não diferenciam nada. «Robusto» para um parafuso que não espanou seria concreto; o modelo quase nunca está falando de parafuso.

**Como corrigir.** Troque pelo limite real, se estiver no texto (aguenta 8 horas, cobre 14 notas, não faz internação). Se não houver limite, corte o adjetivo.

**Antes.** A garrafa Serra Fria tem corpo robusto e uma proposta abrangente: 500 ml, aço inox 304.

**Depois.** A garrafa Serra Fria leva 500 ml e é de aço inox 304.

### «Sinergia»

`sinergia`

«Sinergia» ocupa o lugar de «as duas pessoas vão se falar» ou «o dado sai de um sistema e entra no outro». Sozinha, não diz quem combina o quê. É palavra de slide que o modelo deixa cair em vaga, e-mail e legenda.

**Como corrigir.** Escreva a combinação real. Se o original não diz como as partes se encontram, não invente o rito: diga só quem falta ou o que falta.

**Antes.** O fechamento da folha depende da sinergia entre o DP e o compras.

**Depois.** O fechamento da folha depende do DP e do compras.

### «Sob medida para você» e «experiência única»

`sob-medida-vazio`

«Sob medida» é termo certo de marceneiro e de alfaiate. O cacoete é «sob medida para você», «sob medida para suas necessidades», «totalmente personalizado» e «experiência única» em legenda de padaria, aula e app. A heurística não marca «móveis sob medida» nem «roupa sob medida».

**Como corrigir.** Diga a medida real (3,2 m, 30 minutos, R$ 40) ou o que a pessoa pode escolher (duas cores). Corte o resto.

**Antes.** A aula experimental dura 30 minutos, custa R$ 40 e é uma experiência única, sob medida para suas necessidades.

**Depois.** A aula experimental dura 30 minutos e custa R$ 40.

*Limite da contagem automática:* Não marca «sob medida» de móvel, roupa ou peça.

### «Uma gama de fatores»

`gama-sem-objeto`

«Uma série de fatores», «uma gama de benefícios», «um leque de soluções», «uma infinidade de possibilidades». O substantivo que segue é genérico, então a expressão não lista nada. «Uma série de três e-mails» seria concreta; a heurística só marca a combinação com a lista de palavras vazias.

**Como corrigir.** Enumere, ou diga que a causa não está no texto. Não troque «gama» por «leque».

**Antes.** Uma série de fatores explica os 36 itens que ficaram só no celular.

**Depois.** Os 36 itens ficaram só no celular.

## fechamento

### Fechamento motivacional

`fechamento-motivacional`

«Juntos, podemos», «o futuro é promissor», «agora é a hora», «o melhor ainda está por vir», «vamos nessa». Fecha release, legenda e e-mail com aplauso. Não diz o que a pessoa faz amanhã. Não é a mesma coisa que um «obrigado» ou um «até sábado».

**Como corrigir.** Feche no próximo passo, se houver (confirmar até quarta, encher a caixa, mandar o currículo). Se o original é só comemoração, um «até sexta, no pátio» basta.

**Antes.** O bolo é sexta, no pátio, depois das 18h. Juntos, podemos mais. O futuro é promissor. Vamos nessa.

**Depois.** O bolo é sexta, no pátio, depois das 18h.

### «A verdade é que»

`a-verdade-e-que`

«A verdade é que», «a realidade é que» e «a resposta é simples» anunciam franqueza. Às vezes a frase seguinte é franca; muitas vezes é outro chavão. Gente usa «a verdade é que» o tempo todo. A heurística conta a expressão e não decide se o que vem depois é concreto. Por isso, sozinha, ela não separa máquina de pessoa.

**Como corrigir.** Fique com a frase de depois, se ela tiver fato ou opinião. A opinião fica: não amenize para parecer neutro.

**Antes.** A verdade é que a conta de luz da padaria não baixou em 2018.

**Depois.** A conta de luz da padaria não baixou em 2018.

*Limite da contagem automática:* Expressão muito usada por gente. Presença dela não indica autoria.

### «Desafios e oportunidades»

`desafios-e-oportunidades`

O par vem junto, quase sempre nessa ordem, e não lista nem o desafio nem a oportunidade. Serve de fim de parágrafo quando o modelo não tem o fato. Um texto que diz «o desafio é a chuva das 16h» não usa o par e não deve ser reescrito para evitá-lo.

**Como corrigir.** Separe: qual é o problema, qual é a chance, se os dois estiverem no texto. Se só a expressão estiver, corte.

**Antes.** O trimestre traz desafios e oportunidades: faltam Diego e Ruth, e a meta é R$ 220 mil.

**Depois.** No trimestre faltam Diego e Ruth, e a meta é R$ 220 mil.

### «Em suma» mecânico

`fechamento-em-suma`

«Em suma», «em conclusão», «em síntese» anunciam o fim como numa redação de vestibular. Em e-mail e recado, o último período já é o pedido («mando o arquivo às 10h»). O rótulo não acrescenta.

**Como corrigir.** Deixe o pedido ou o fato final sem rótulo. Se o texto for de fato um resumo escolar com tese, a última frase carrega a tese, ainda sem «em suma».

**Antes.** Em suma, o arquivo segue amanhã às 10h.

**Depois.** O arquivo segue amanhã às 10h.

### «Não pode ser subestimada»

`importancia-subestimada`

«A importância de X não pode ser subestimada» e «não deve ser ignorada» gastam uma frase inteira para dizer que X importa, sem dizer o que acontece se alguém ignorar. É fechamento de parágrafo escolar e de release.

**Como corrigir.** Diga a consequência. «A importância da vírgula não pode ser subestimada» vira a frase em que a vírgula muda quem é chamado para o almoço.

**Antes.** A importância da vírgula não pode ser subestimada: sem ela, «vamos comer crianças» deixa de ser um chamado.

**Depois.** Sem a vírgula, «vamos comer crianças» deixa de ser um chamado.

### «Não é segredo que»

`nao-e-segredo`

«Não é segredo que» e «não é novidade que» apresentam um fato comum como se fosse revelação. O fato em si pode ser útil; o prefácio não. Também aparece em coluna de jornal. A heurística não distingue.

**Como corrigir.** Diga o fato. Se ele for óbvio a ponto de não precisar estar no texto, corte o período inteiro, não só o prefácio.

**Antes.** Não é segredo que o time de DP tem 6 pessoas.

**Depois.** O time de DP tem 6 pessoas.

*Limite da contagem automática:* Também aparece em texto humano. Não prova autoria.

## formato

### Fileira de emoji de modelo

`emoji-de-modelo`

Foguete, estrela, lâmpada, check, alvo e gráfico no meio de e-mail, release ou README. Um emoji em legenda ou no Zap pode ser de gente; a fileira decorativa, repetida como se fosse bullet, é moldura de modelo. A heurística conta um conjunto fechado e só dispara com dois ou mais. Sorriso e risada ficam de fora.

**Como corrigir.** Em texto formal, tire. Em legenda, se sobrar um e combinar com quem fala, pode ficar um. Não substitua emoji por adjetivo animado.

**Antes.** A clínica abre em novembro. 🚀✨ Agende na recepção.

**Depois.** A clínica abre em novembro. O agendamento é na recepção.

*Limite da contagem automática:* Não conta emoji fora dessa lista. Um emoji só, mesmo da lista, não conta.

### Título com maiúsculas de inglês

`titulo-title-case`

Em inglês, o título capitaliza quase cada palavra. Em português, o título é frase: maiúscula na primeira palavra e nos nomes próprios. «Como Validar CPF Em Python Com Clareza» é o hábito do modelo, não o do manual brasileiro.

**Como corrigir.** Deixe maiúscula só na primeira palavra e em nome, sigla e marca. «Como Validar CPF Em Python» vira «Como validar CPF em Python».

**Antes.** Como Validar CPF Em Python Com Clareza

**Depois.** Como validar CPF em Python

*Limite da contagem automática:* Olha só linhas curtas sem ponto final. Não trata sigla no meio de uma frase.
