## O que muda

-

## Padrão novo

- [ ] Não é padrão novo
- [ ] Aparece em texto de pelo menos dois modelos, com nome e data no PR
- [ ] O exemplo não vem de blader/humanizer, op7418/Humanizer-zh nem mackswendhell/humanizer-pt-br
- [ ] O depois não muda fato, número, nome nem opinião

## Conferido

- [ ] `python scripts/validate_catalog.py`
- [ ] `python scripts/build.py && python scripts/build.py --check`
- [ ] `python eval/detector.py --write && python eval/detector.py --check`
- [ ] `python eval/test_detector.py`
