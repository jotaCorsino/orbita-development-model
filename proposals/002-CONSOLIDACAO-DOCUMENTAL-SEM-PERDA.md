# Proposta 002 — Consolidação documental segura e rastreabilidade do cânone

- **Categoria:** melhoria do Método ÓRBITA / preservação do conhecimento / handoff entre agentes.
- **Registrada em:** 22/10/2026.
- **Origem:** [the-mmo-idea](https://github.com/jotaCorsino/the-mmo-idea), especialmente [PR documental #1](https://github.com/jotaCorsino/the-mmo-idea/pull/1).
- **Estado:** proposta em avaliação; **não é regra homologada**.
- **Distinção:** o erro de consolidação foi uma **falha de execução do agente de planejamento**, apesar de o contrato existente já proibir remoções sem autorização. O que se propõe é adicionar salvaguardas operacionais verificáveis.

## 1. Ocorrência e impacto

Durante a organização do desenvolvimento conceitual do MMO, o agente interpretou “remover ideias substituídas e versões sobrepostas” como autorização para reduzir uma documentação extensa a um resumo: o conjunto ativo foi reduzido de cerca de **33 arquivos para 6**.

O projeto ainda estava em **concepção**, portanto lore, eras, reinos, sistemas de combate, economia e experimentos não descartados explicitamente continuavam vigentes, mesmo quando incompletos. A simplificação retirou material detalhado e gerou a impressão de perda do progresso.

O conteúdo pôde ser recuperado por commits antigos e reorganizado no PR #1, sem merge na `main`. O custo foi retrabalho, perda de confiança e risco de orientar a implementação por documentos incompletos.

**Não confundir:** ausência do conteúdo na `main` (PR ainda Draft) é distinta da exclusão de conteúdo na branch de trabalho. Ambos ocorreram na comunicação do projeto, mas pedem controles diferentes.

## 2. Causa observada e lacuna prática

- “Canônico” foi confundido com “resumido” ou “concluído”. Em projetos criativos, **cânone vigente também pode estar em desenvolvimento**.
- Não houve uma **matriz de cobertura antes/depois** que comprovasse a preservação de cada decisão ou descrição única.
- Contagem de arquivos e links válidos foi usada como sinal de boa organização, mas esses testes não comprovam integridade semântica.
- A estrutura de PRs Draft encadeados e a `main` minimalista não foram suficientemente explicitadas durante o bootstrap do Codex, gerando alarme compreensível sobre o desaparecimento do trabalho.
- O agente deveria ter interrompido a limpeza quando não conseguisse demonstrar que uma ideia fora **expressamente substituída**.

## 3. Protocolo proposto — consolidação sem perda

Antes de remover ou condensar documentação não trivial:

1. **Fixar fonte e snapshot:** registrar branch, commit SHA, inventário de arquivos e objetivo da consolidação; preservar versão recuperável por Git.
2. **Classificar sem inventar estados:** `VIGENTE` (inclusive ideias em elaboração), `SUBSTITUÍDO COM EVIDÊNCIA`, `DUPLICADO SEM CONTEÚDO ÚNICO`, `DÚVIDA`. Itens em dúvida são preservados até resolução, sem impor nova homologação para cada frase.
3. **Matriz de cobertura:** para cada seção de origem, indicar destino exato (arquivo/âncora ou decisão substituta), ou justificar remoção com referência à decisão que a tornou obsoleta.
4. **Critério semântico:** conferir fatos, restrições, nomes próprios, mecânicas, relações, detalhes de lore e decisões únicas; a contagem de arquivos não substitui esse teste.
5. **Revisão do diff:** exclusões e reescritas volumosas devem acionar revisão reforçada; nunca vender “33 → 6” como melhoria por si só.
6. **Gate documental:** apresentar ao responsável resumo do que foi mantido, unido e proposto para remoção antes de incorporar à branch principal; não fazer merge silencioso.

**Regra sugerida:** **não há remoção por falta de acabamento ou homologação final; só por substituição comprovada ou duplicação sem informação exclusiva.**

## 4. Estado canônico em múltiplos PRs

Para projetos em que a fundação documental vive em um PR Draft e a implementação deriva de outros PRs Draft:

- deixar explícitos **`main` (integrada)**, **documentação vigente em revisão** e **branches de implementação dependentes**;
- mostrar relação `PR → branch base → commit → gate`;
- em relatórios de bootstrap, nunca afirmar que o projeto está vazio apenas porque `main` ainda não contém os PRs;
- antes de orientar o Codex, identificar o conjunto de documentação que efetivamente rege a tarefa e como acessá-lo sem merge prematuro;
- evitar que uma mesma decisão apareça com estados contraditórios em READMEs, roadmaps e PRs.

Um índice temático pode melhorar a navegação, mas **não substitui o conteúdo íntegro**.

## 5. Artefato operacional sugerido

Adicionar ao kit do ÓRBITA um checklist/template curto de **auditoria de consolidação**:

| Origem (arquivo / seção) | Conteúdo único | Estado | Destino / substituto | Evidência | Conferido? |
| --- | --- | --- | --- | --- | --- |
| ex.: lore, era 2 | Sim | Vigente | docs/lore.md#era-2 | conteúdo preservado | Sim/Não |
| ex.: proposta de classe A | Não | Substituída | decisão CMB-xxx | link para decisão | Sim/Não |

O template deve ser **proporcional**: exigido especialmente em migrações de documentação extensa, renomeações massivas e fusões destrutivas, não em pequenas correções gramaticais.

## 6. Critérios de aceite para eventual incorporação

- Testar em ao menos uma consolidação documental real sem perda de conteúdo vigente.
- Demonstrar rastreabilidade de seções da origem aos destinos e recuperação por Git.
- Tornar visível o estado de PRs dependentes sem exigir merge antecipado.
- Não criar duplicação permanente nem tornar toda revisão de texto burocrática.
- Submeter template e alterações normativas ao responsável humano em PR próprio; **nenhuma incorporação automática**.

## 7. Referências

- [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md): autorização, preservação, evidências e regra de parada.
- [Governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
- [Fluxo de desenvolvimento](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md).
- [the-mmo-idea — PR #1](https://github.com/jotaCorsino/the-mmo-idea/pull/1): documentação conceitual e recuperação do acervo.
