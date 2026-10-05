# 04 — Fluxo de desenvolvimento

## Preparação de um novo projeto

Antes do primeiro ciclo de implementação, um projeto novo deve ganhar uma identidade e um ambiente coerentes.

Fluxo recomendado:

1. definir um **nome canônico** para o projeto;
2. criar um **Projeto próprio no ChatGPT** com esse nome;
3. criar um **Projeto/workspace próprio no Codex** com o mesmo nome;
4. criar ou confirmar o **repositório GitHub** correspondente;
5. criar/clonar uma **pasta local com o mesmo nome**, vinculada ao remoto;
6. registrar no repositório objetivo, contexto, regras e estado inicial;
7. somente depois decompor e autorizar a primeira implementação.

Para projeto existente, o repositório já estabelecido normalmente define a identidade canônica. Os demais ambientes devem se alinhar a ele.

Esse bootstrap não precisa ser burocrático. Sua função é garantir que, desde o início, planejamento, implementação, arquivos locais e histórico persistente apontem para o mesmo software.

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
