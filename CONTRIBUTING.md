# Contribuir

Um padrão entra no catálogo quando dá para apontar o cacoete, mostrar um exemplo com origem limpa e corrigir sem mudar o sentido. O CI confere o formato. A regra dos dois modelos fica para quem revisa o PR: o script não tem como adivinhar de qual modelo veio a frase.

## O que um padrão novo precisa ter

1. O cacoete aparece em textos de pelo menos dois modelos, com o nome do modelo e a data. Pode ser texto gerado para o PR. Não vale colar post de terceiro sem licença, nem exemplo tirado de [blader/humanizer](https://github.com/blader/humanizer), [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) ou [mackswendhell/humanizer-pt-br](https://github.com/mackswendhell/humanizer-pt-br).
2. O «antes» e o «depois» preservam fato, número, nome e opinião. O depois não pode só apagar a frase e inventar outra.
3. Dá para dizer por que soa a texto de máquina em português do Brasil, com a limitação da heurística quando ela também pega prosa humana.
4. A correção não troca um chavão por outro («holístico» não vira «robusto»).

## Arquivo

Crie `patterns/<id>.yaml`. O `id` é o nome do arquivo, em minúsculas e hífen. Campos:

- `grupo`: `abertura`, `conectivo`, `estrutura`, `vocabulario`, `fechamento` ou `formato`
- `nome`, `por_que`, `como_corrigir`
- `exemplo_antes`, `exemplo_depois`
- `origem.modelo`, `origem.data`, `origem.prompt`, `origem.reescrita`
- `heuristica.tipo`: `regex`, `regex_minimo`, `travessao` ou `title_case`
- em `regex` e `regex_minimo`, a lista `padroes`; em `regex_minimo`, também `minimo`

O exemplo antes tem de disparar o próprio padrão. O exemplo depois não pode disparar padrão nenhum do catálogo.

## Antes do PR

```bash
python scripts/validate_catalog.py
python scripts/build.py
python eval/detector.py --write
python eval/test_detector.py
python scripts/build.py --check
python eval/detector.py --check
```

`build.py` regenera `skills/`, `prompt/` e `examples/`. Não edite esses arquivos à mão. Se a heurística disparar em mais de seis trechos do controle humano, ela está larga: estreite ou explique o limite no YAML, com o número real no `eval/RESULTS.md`.

Não prometa que o texto passa em detector. A contagem daqui não é isso.
