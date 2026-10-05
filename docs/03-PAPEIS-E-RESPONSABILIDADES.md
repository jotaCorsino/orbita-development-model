# 03 — Papéis e responsabilidades

O ÓRBITA trabalha com papéis, não com dependência obrigatória de ferramentas específicas.

## 1. Responsável humano

Na implementação original do método: **João Corsino**.

Responsabilidades:

- definir necessidade e objetivo;
- estabelecer prioridades e restrições;
- aprovar decisões relevantes;
- avaliar resultado funcional;
- homologar ou rejeitar entregas;
- decidir quando o projeto avança.

O humano é o **proprietário da decisão**, não apenas o autor do prompt.

## 2. Agente de planejamento

Na aplicação atual: normalmente **ChatGPT**.

Responsabilidades:

- transformar necessidades em problemas claros;
- estruturar requisitos;
- decompor trabalho em tarefas;
- identificar riscos e dependências;
- produzir instruções de implementação;
- interpretar evidências retornadas;
- revisar coerência entre planejamento e execução;
- manter visão global do projeto.

O agente de planejamento não substitui a homologação humana.

## 3. Agente de implementação

Na aplicação atual: normalmente **Codex**.

Responsabilidades:

- inspecionar o repositório;
- implementar apenas o escopo autorizado;
- criar ou alterar código;
- executar testes e builds;
- registrar limitações encontradas;
- produzir evidências técnicas;
- preparar commits e Pull Requests conforme o fluxo adotado.

O implementador não deve expandir escopo silenciosamente.

## 4. Git/GitHub

Responsabilidades:

- manter código e documentação;
- registrar evolução;
- sustentar branches, commits e Pull Requests;
- preservar histórico;
- tornar o estado do projeto reconstruível.

## Separação de responsabilidades

A separação é intencional:

**humano decide → planejador estrutura → implementador executa → repositório registra → humano homologa.**

Um mesmo produto de IA pode tecnicamente exercer mais de um papel, mas os papéis devem continuar conceitualmente distintos.
