# 06 — Git e GitHub

## Fonte canônica

No ÓRBITA, conversas com agentes ajudam a raciocinar e coordenar, mas **o repositório é a referência persistente do projeto**.

Uma decisão que precisa sobreviver ao contexto da conversa deve, quando relevante, ser transferida para documentação, issue, código, commit ou Pull Request.

## `main`

A branch principal deve representar um estado conhecido e deliberadamente aceito.

Regra conceitual:

> **funcionar não é o mesmo que estar homologado.**

## Branches

Branches isolam mudanças e tornam o trabalho comparável.

Exemplos de convenção:

```text
feat/NOME-DA-TAREFA
fix/NOME-DA-CORRECAO
docs/NOME-DA-DOCUMENTACAO
chore/NOME-DA-MANUTENCAO
```

## Commits

Commits devem explicar a intenção da mudança.

Exemplos:

```text
feat: adiciona criação de recorrências
fix: corrige validação do serviço
docs: documenta processo de homologação
chore: inicializa estrutura do projeto
```

## Pull Requests

O PR funciona como ponto de convergência entre:

- alteração proposta;
- diff;
- testes;
- discussão;
- revisão;
- aprovação;
- histórico.

Em projetos pequenos, nem toda mudança precisa do mesmo nível de formalidade, mas alterações relevantes devem permanecer rastreáveis.
