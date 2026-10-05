# 05 — Governança e homologação

## Governança humana

Governança, no ÓRBITA, significa que capacidade técnica do agente não equivale a autoridade decisória.

O responsável humano controla:

- início de mudanças relevantes;
- alteração de escopo;
- aceitação de trade-offs;
- homologação funcional;
- merge ou liberação de etapas sensíveis.

## Gates

Um **gate** é uma condição que precisa ser satisfeita antes do próximo estágio.

Exemplos:

- requisitos compreendidos antes de implementar;
- testes aprovados antes do PR;
- revisão antes do merge;
- validação funcional antes da release.

## Evidência antes de confiança

O agente implementador deve demonstrar o que fez.

Dependendo da tarefa, evidências podem incluir:

- arquivos alterados;
- resumo do diff;
- testes executados;
- quantidade de testes aprovados/falhos;
- resultado do build;
- logs relevantes;
- commit SHA;
- branch;
- Pull Request;
- limitações ou pontos não validados.

## Homologação

**Homologar não significa apenas confirmar que o código compila.**

A homologação responde se a mudança atende ao objetivo esperado pelo responsável pelo projeto.

Possíveis resultados:

- **Aprovado** — pode avançar;
- **Aprovado com ressalvas** — avança com pendências registradas;
- **Correção necessária** — retorna à implementação;
- **Replanejamento necessário** — a solução ou requisito precisa ser revisto.

O template está em [../templates/HOMOLOGACAO-TEMPLATE.md](../templates/HOMOLOGACAO-TEMPLATE.md).
