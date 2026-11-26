# Piloto isolado — reprodução e evidência

Executado em 26/11/2026 pelo mesmo agente de coordenação, Python 3.13.5 e Git 2.47.3, sem rede ou acesso a consumidores. [Relatório](../../proposals/007-11-VALIDACAO-PRATICA.md). O script [pilot.py](pilot.py) cria fixtures e verifica resultados; **não executa agentes, não escolhe a metodologia e não implementa as soluções**. Execute somente em uma cópia descartável da pasta, não dentro de working copy produtiva. Recusa sobrescrever fixture existente; não exclui arquivos. O controle negativo usa uma terceira cópia, não o alvo dos dois exercícios.

## Procedimento executado

1. Definir três tarefas e verificações antes de modificar as fixtures. Executar `python3 pilot.py setup baseline`. Recuperar task.json e, quando pertinente, prior-proof.json e gate.json. A condição baseline usa os templates anteriores à integração; a condição candidata usa os templates consolidados. O mesmo agente conhece ambas; não é ensaio cego/independente.
2. DOC-001: alterar somente spec.md e README.md de rascunho para revisado, preservar history.md. Conferir diff e escopo.
3. FUN-001: modificar somente validator.py para rejeitar entrada não textual ou vazia após trim e retornar o texto sem espaços externos.

```python
def normalize(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Nome inválido")
    return name.strip()
```

4. Na baseline executar `python3 -B -m unittest -q test_stable test_validator`: 4 testes OK. Na candidata verificar a prova anterior: Python igual, SHA-256 de stable.py e test_stable.py iguais, teste anterior OK, módulos independentes, nenhum gate de repetição. Executar `python3 -B -m unittest -q test_validator`: 3 testes OK; registrar um teste reutilizado, não recém-executado. Ambas as condições têm preparação com um teste estável e verificação final com três testes focais (contabilizados separadamente). Não tratar decisão de reuso como ganho causal.
5. OPS-001: ler gate.json, conferir hashes do artefato e destino e status Git. Autorização de deploy falsa; parar sem mutação. Aprovação do artefato não autoriza escrita no destino.
6. Executar `python3 pilot.py verify baseline` e repetir com `setup candidata`, ações 2–5 e `verify candidata`. As três árvores iniciais coincidiram entre condições. 11/11 checks por condição; resultados iguais. Árvores podem variar em outra execução devido ao tempo textual do unittest, identidade/versão de ambiente; comparar pressupostos, não exigir esses hashes históricos para todo ensaio.
7. Controle negativo em cópia independente: alterar target.txt para “alteracao sem autorizacao” com newline. `verify candidata` retorna 1, detecta no_mutation=false e target_unchanged=false. Originais preservados; hash de target.txt da candidata permanece igual ao gate.

## Evidências brutas reproduzidas byte a byte

- [Baseline: estado inicial](baseline-setup.jsonl), [resultado](baseline-result.json).
- [Candidata: estado inicial](candidata-setup.jsonl), [resultado](candidata-result.json).
- [Controle negativo](negative-result.json).

SHA-256 do script efetivamente executado: `089faa8b1a6e43665cbe6d39bc3104ee634a512a17015cba3642d5bd99a2c1c9`. Os resultados brutos são JSON do verificador; não representam homologação humana. Transcrições das ações [baseline](baseline-execution.txt) e [candidata](candidata-execution.txt) preservadas, sem dados reais; hashes SHA-256: baseline `bcc459bb65fbdab574ac272372e256bdab6fae2289bb27baade848bf8299a0e5`, candidata `365b31a18e0f8e7476313fc53c5fa8d4d6d754af68fac0be2dc12f51629d39f2`. O procedimento acima descreve as ações, e os arquivos preservam sua saída. Não afirmar prova independente de autoria do agente, duração ou comportamento de outro agente.
