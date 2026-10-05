# 06 — Git e GitHub

## Fonte canônica

No ÓRBITA, conversas com agentes ajudam a raciocinar e coordenar, mas **o repositório é a referência persistente do projeto**.

Uma decisão que precisa sobreviver ao contexto da conversa deve, quando relevante, ser transferida para documentação, issue, código, commit ou Pull Request.

## Repositório remoto e pasta local

O repositório GitHub e a pasta local representam o mesmo projeto, mas não são a mesma coisa.

- **GitHub**: referência persistente e compartilhável;
- **pasta local**: working copy usada para editar, executar e testar.

Na organização padrão do ÓRBITA, a pasta local usa o mesmo nome do projeto/repositório sempre que possível e deve estar vinculada ao remoto correto.

Antes de uma implementação, o agente deve confirmar que está trabalhando na pasta e no remoto correspondentes ao projeto. O estado local pode conter trabalho ainda não publicado e não deve ser confundido automaticamente com o estado oficial.

Quando a implementação depender da base mais recente, a working copy deve ser sincronizada antes de criar a branch da tarefa.

Ver também [Identidade e ambiente do projeto](10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md).

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

## Segurança do repositório

Git/GitHub também fazem parte da superfície de segurança do projeto.

Boas práticas esperadas, conforme a criticidade:

- manter `.gitignore` adequado à tecnologia;
- revisar arquivos staged e diff antes do commit;
- não versionar senhas, tokens, chaves, bancos, dumps ou artefatos sensíveis;
- trabalhar com branches e Pull Requests para mudanças relevantes;
- evitar force push, reset destrutivo e reescrita de histórico sem autorização;
- proteger a branch principal quando apropriado;
- restringir permissões ao necessário;
- revisar dependências, workflows e automações de CI;
- habilitar análise de segredos/dependências quando disponível e adequada ao projeto;
- revisar exposição antes de tornar um repositório público.

Se um segredo real for encontrado no histórico, removê-lo do arquivo atual não é suficiente. O incidente deve ser reportado e a credencial deve ser revogada/rotacionada quando aplicável.

Ver [Segurança e integridade](12-SEGURANCA-E-INTEGRIDADE.md).
