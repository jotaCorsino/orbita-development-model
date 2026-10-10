# 11 — Inicialização de um novo projeto

## Objetivo

Este documento define como um projeto novo entra em operação no Método ÓRBITA.

A inicialização só é considerada concluída quando os quatro ambientes do projeto apontam inequivocamente para o mesmo software:

```text
Contexto do agente de planejamento
        ↕
Contexto do agente de implementação
        ↕
Pasta local
        ↕
Repositório GitHub
```

O repositório GitHub continua sendo a referência persistente.

## Independência de ferramenta

A sequência abaixo descreve papéis. Neste repositório, ChatGPT e Codex aparecem como configuração de referência para planejamento e implementação. Outras combinações de IA podem ser usadas sem alterar o fluxo.

## Sequência padrão

### 1. O responsável humano cria o contexto de planejamento

O responsável humano:

1. define um nome para o projeto;
2. cria um contexto próprio no agente de planejamento escolhido com esse nome;
3. inicia uma nova conversa dentro desse Projeto;
4. apresenta a ideia inicial do software;
5. fornece o repositório do Método ÓRBITA;
6. fornece o repositório remoto criado para o novo software.

Neste momento não existe autorização implícita para implementar funcionalidades.

### 2. O agente de planejamento aprende o método

O agente de planejamento deve:

1. ler o onboarding do ÓRBITA;
2. compreender papéis, governança, fluxo, evidências e homologação;
3. inspecionar o repositório remoto do novo projeto;
4. confirmar que entendeu como deverá trabalhar;
5. compreender a ideia, problema, usuários, restrições e objetivo inicial do software.

### 3. O agente de planejamento funda o projeto no repositório remoto

Antes de enviar qualquer tarefa de implementação, o agente de planejamento prepara a fundação documental do novo projeto no próprio repositório remoto, quando possuir acesso autorizado para isso.

A fundação deve ser proporcional ao projeto, mas normalmente inclui:

- README inicial no padrão ÓRBITA;
- objetivo e contexto do software;
- escopo inicial;
- arquitetura ou visão técnica inicial, quando necessária;
- roadmap ou planejamento por etapas;
- regras locais do projeto;
- estados de acompanhamento;
- critérios de homologação;
- riscos e restrições conhecidos;
- estrutura documental necessária para que outra sessão ou agente consiga retomar o projeto.

O planejamento não deve inventar implementação prematura. O objetivo desta etapa é transformar a ideia conversada em uma base persistente e organizada.

Se o agente não possuir permissão para escrever no repositório, deve preparar os arquivos para que sejam registrados antes do avanço.

### 4. O agente de planejamento confirma a fundação

Ao terminar, o agente apresenta ao responsável humano:

- o que foi criado;
- a estrutura documental;
- o planejamento inicial;
- decisões e premissas adotadas;
- pendências que exigem decisão humana.

Somente depois dessa fundação o projeto está pronto para receber a primeira tarefa do agente de implementação.

### 5. O responsável humano prepara o contexto local de implementação

O responsável humano:

1. cria uma pasta local com o mesmo nome do projeto;
2. abre essa pasta no ambiente do agente de implementação escolhido;
3. inicia a conversa/sessão do projeto nesse agente;
4. entrega ao agente de implementação a primeira tarefa gerada pelo agente de planejamento.

A pasta pode estar vazia. Ela não precisa ter Git inicializado previamente.

### 6. Primeira tarefa do agente de implementação — bootstrap local

A primeira tarefa de implementação de um projeto novo é uma tarefa de **bootstrap**, não uma funcionalidade.

Objetivo:

> transformar a pasta local já criada em uma working copy segura do repositório remoto que contém a fundação documental do projeto.

O agente de implementação deve, conforme o estado encontrado:

1. confirmar que está na pasta correta;
2. verificar se Git já está inicializado;
3. inicializar o repositório local somente se necessário;
4. configurar ou validar o remoto `origin`;
5. buscar o estado do repositório remoto;
6. sincronizar a branch principal sem apagar conteúdo local único silenciosamente;
7. confirmar que README e documentação inicial estão presentes localmente;
8. verificar branch atual, remoto e estado da árvore;
9. relatar as evidências da sincronização;
10. parar.

Essa tarefa não deve implementar funcionalidades do produto.

Se a pasta já possuir conteúdo, histórico Git ou remoto diferente, o agente de implementação deve inspecionar e reportar a situação antes de qualquer ação destrutiva.

Um template específico está em [../templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md](../templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md).


### Restrições do ambiente de implementação

Uma falha observada pelo agente ao criar, ler ou atualizar `.git` não deve ser interpretada automaticamente como falha de permissão da pasta real do projeto.

Ambientes de implementação podem aplicar isolamento, mounts temporários ou políticas de sandbox que alteram a forma como o filesystem é apresentado ao agente. Por isso, quando o bootstrap encontrar `.git` inacessível, somente leitura ou comportamento incompatível com a pasta esperada, o agente deve primeiro identificar **em qual camada está a restrição**:

```text
pasta real do projeto
        ↓
ambiente / sandbox do agente
        ↓
visão observada durante a execução
```

Antes de abandonar, renomear ou substituir a pasta canônica:

1. inspecionar o estado da pasta e de `.git` sem executar ações destrutivas;
2. distinguir permissões reais do filesystem de restrições impostas pelo ambiente isolado;
3. quando disponível, verificar permissões e características de montagem do caminho afetado;
4. preservar a pasta original sempre que ela continuar sendo a working copy pretendida;
5. se houver mecanismo formal de execução fora do sandbox, utilizá-lo somente mediante autorização humana;
6. reinspecionar a pasta real antes de inicializar ou clonar qualquer repositório;
7. considerar uma nova working copy somente depois de demonstrar que a pasta original não pode cumprir seu papel com segurança.

A existência de um bloqueio no sandbox **não autoriza** por si só `sudo`, alterações recursivas de permissão, remoção de `.git`, desmontagens, `reset --hard` ou criação automática de outro workspace.

Se a origem da restrição não puder ser determinada com segurança, o agente deve interromper o bootstrap e reportar o bloqueio.


## Estado ao final do bootstrap

Ao concluir a inicialização:

```text
Responsável humano
      │
      ├── Agente de planejamento ── contexto
      │
      ├── Agente de implementação ─ implementação
      │
      ├── Pasta local ───── working copy
      │
      └── GitHub ────────── estado persistente
```

Todos reconhecem o mesmo nome, o mesmo repositório e o mesmo estado inicial.

A partir daí começa o ciclo normal:

```text
Planejar → Executar → Evidenciar → Homologar
```

## Regra essencial

A fundação documental vem **antes** da primeira implementação.

A sincronização local vem **antes** da primeira funcionalidade.

Isso garante que planejamento, implementação e histórico já nasçam vinculados ao mesmo projeto.
