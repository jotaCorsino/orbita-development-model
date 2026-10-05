# 04 — Fluxo de desenvolvimento

## Preparação de um novo projeto

Antes do primeiro ciclo normal de desenvolvimento, um projeto novo passa por uma etapa própria de inicialização.

A ordem padrão é:

1. o responsável humano define um **nome canônico**;
2. cria um **Projeto próprio no ChatGPT** com esse nome;
3. inicia uma conversa de planejamento e apresenta a ideia do software;
4. fornece o repositório do **Método ÓRBITA** e o **repositório remoto do novo projeto**;
5. o agente de planejamento lê o método, compreende a ideia e inspeciona o repositório do projeto;
6. o agente de planejamento cria no repositório remoto a **fundação documental inicial**: README, visão, planejamento, roadmap, regras, critérios e demais documentos proporcionais ao projeto;
7. o agente confirma ao responsável humano o que foi criado;
8. o responsável humano cria uma **pasta local** com o mesmo nome e abre essa pasta em um **Projeto/workspace no Codex**;
9. o agente de planejamento gera a **primeira tarefa do Codex**, dedicada exclusivamente ao bootstrap local;
10. o Codex inicializa Git se necessário, conecta a pasta ao repositório remoto, sincroniza a branch principal com segurança, valida documentação/remoto/HEAD e para;
11. somente depois dessa cadeia estar vinculada começa a primeira tarefa funcional.

A primeira tarefa do Codex em projeto novo, portanto, **não é implementar funcionalidade**. É estabelecer com segurança a working copy local do repositório já documentado.

A especificação completa está em [11 — Inicialização de um novo projeto](11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Ciclo padrão

1. **Necessidade** — surge um problema, melhoria ou funcionalidade.
2. **Análise** — o contexto é compreendido antes da alteração.
3. **Planejamento** — a mudança é decomposta e seus critérios são definidos.
4. **Tarefa** — uma unidade de trabalho recebe objetivo, escopo e aceite.
5. **Branch** — quando aplicável, a mudança é isolada da versão homologada.
6. **Implementação** — o agente executor trabalha no escopo autorizado.
7. **Validação técnica** — testes, build e verificações são executados.
8. **Evidências** — resultados e alterações são apresentados.
9. **Pull Request** — a mudança torna-se revisável e comparável.
10. **Revisão** — coerência técnica e aderência ao objetivo são avaliadas.
11. **Homologação humana** — o responsável aceita ou solicita correções.
12. **Merge** — o estado aprovado passa a integrar a linha principal.
13. **Documentação/Release** — registros são atualizados quando necessário.
14. **Próxima tarefa** — somente então o ciclo recomeça.

## Estados sugeridos

```text
PLANEJADA
   ↓
AUTORIZADA
   ↓
EM_IMPLEMENTACAO
   ↓
EM_VALIDACAO
   ↓
AGUARDANDO_HOMOLOGACAO
   ↓
CONCLUIDA
```

Quando uma validação falha, a tarefa retorna ao estágio adequado.

## Tarefas

Uma boa tarefa deve responder, no mínimo:

- O que deve mudar?
- Por que isso é necessário?
- O que está dentro do escopo?
- O que não deve ser alterado?
- Como saberemos que terminou?
- Quais evidências devem ser retornadas?

O template oficial está em [../templates/TASK-TEMPLATE.md](../templates/TASK-TEMPLATE.md).
