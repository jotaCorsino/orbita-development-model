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

## Retomada após interrupção

Quando uma tarefa for interrompida inesperadamente, pausada por longo período ou transferida para outro agente com alterações materiais possivelmente ainda locais, a retomada deve começar pela **preservação do estado existente**, não pela reconstrução.

Antes de sincronizar, limpar ou refazer trabalho, o agente deve, de forma proporcional:

1. confirmar pasta, branch e `HEAD` local;
2. comparar o estado local com o remoto;
3. identificar commits locais ainda não publicados;
4. inventariar alterações rastreadas, arquivos não rastreados e artefatos ignorados relevantes;
5. verificar, quando aplicável, Git LFS e arquivos-fonte editáveis;
6. preservar ou criar backup dos artefatos materiais antes de qualquer operação potencialmente destrutiva;
7. registrar o último passo comprovadamente concluído e o ponto em que a execução foi interrompida.

A ausência de alterações no PR ou no remoto **não prova ausência de trabalho local**.

Durante a retomada, comandos como `reset --hard`, `clean -fdx`, force push ou descarte de mudanças não devem ser usados como reação automática. Se houver dúvida sobre a integridade ou o valor do estado local, preserve primeiro e decida depois.

Somente após distinguir claramente **estado local**, **estado remoto** e **trabalho ainda não persistido** a tarefa deve retornar ao estágio adequado do fluxo.

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

## Checkpoints de resiliência

Em tarefas longas ou com artefatos difíceis de reconstruir, o agente deve considerar **checkpoints de resiliência** após marcos verificáveis.

Eles são recomendados quando houver, por exemplo:

- geração ou edição de arquivos pesados ou trabalhosos;
- várias etapas dependentes entre si;
- operações longas sujeitas a interrupção de sessão ou limite de uso;
- troca provável de agente ou ambiente;
- custo relevante para reconstruir o último estado válido.

Um checkpoint deve preservar material suficiente para que o trabalho possa ser retomado sem depender da memória da sessão. Conforme o projeto e a autorização existente, ele pode consistir em:

- salvar corretamente os arquivos-fonte editáveis;
- manter backup seguro de artefatos materiais;
- registrar o último marco comprovado;
- criar commit local rastreável;
- publicar commit/branch quando o fluxo já autorizar essa persistência remota;
- registrar limitações, arquivos ainda não validados e próxima ação segura.

O checkpoint deve acontecer **por marco útil**, não por intervalo rígido de tempo nem após cada microalteração.

Um checkpoint parcial **não equivale a conclusão, aprovação ou homologação**. Ele apenas reduz o custo e o risco de uma eventual retomada.

Projetos curtos, baratos de reproduzir ou sem estado material relevante não precisam introduzir checkpoints adicionais apenas para cumprir o método.

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
