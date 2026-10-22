# Proposta 003 — Consolidação documental segura e rastreabilidade do cânone

- **Categoria:** melhoria do Método ÓRBITA / preservação do conhecimento / handoff entre agentes.
- **Registrada em:** 22/10/2026.
- **Origem:** [the-mmo-idea](https://github.com/jotaCorsino/the-mmo-idea), especialmente [PR documental #1](https://github.com/jotaCorsino/the-mmo-idea/pull/1).
- **Estado:** refinamento metodológico **APROVADO pelo responsável humano no PR #11**, aguardando integração à `main`.
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

## 3. Resultado da avaliação metodológica

A análise concluiu que houve uma **falha de execução do agente**, acompanhada de duas lacunas práticas que valem explicitar no método:

1. a `main` representa o estado integrado/homologado, mas não necessariamente todo o trabalho ainda relevante que vive em branches ou PRs ativos;
2. consolidações documentais extensas precisam demonstrar preservação **semântica**, não apenas redução de arquivos, links válidos ou reorganização estrutural.

O refinamento preparado incorpora estas regras:

- antes de concluir que algo “não existe”, identificar qual documentação efetivamente rege a tarefa atual;
- conteúdo em branch/PR ativo não se torna canônico apenas por existir;
- pedidos de organizar, consolidar, resumir ou deduplicar não autorizam exclusão ampla por interpretação;
- conteúdo incompleto ou ainda em elaboração continua preservado enquanto não houver substituição explícita, duplicação sem conteúdo exclusivo ou autorização humana;
- consolidações extensas devem apresentar evidência proporcional de cobertura;
- na dúvida sobre perda semântica, **preservar e sinalizar** em vez de resumir de forma irreversível.

Foram conscientemente **descartados ou simplificados**:

- criar novos estados normativos como `VIGENTE`, `SUBSTITUÍDO` ou `DÚVIDA`;
- tornar matriz de cobertura obrigatória em toda consolidação;
- criar agora um template oficial exclusivo de auditoria documental;
- exigir nova homologação para cada frase ou documento reorganizado;
- tratar redução do número de arquivos como objetivo do método.

A regra resultante é:

> **organizar não autoriza perder conteúdo; consolidar exige preservar o significado ainda vigente.**

## 4. Estado integrado e trabalho ativo em revisão

O refinamento diferencia explicitamente:

- **`main`** — estado integrado e deliberadamente aceito;
- **branch ou PR ativo** — trabalho em elaboração ou revisão, ainda não integrado;
- **documentação vigente para a tarefa** — conjunto explicitamente indicado pelo planejamento ou pelas dependências daquela tarefa.

Essa distinção evita tanto considerar um projeto “vazio” apenas porque certo conteúdo ainda não entrou na `main`, quanto tratar qualquer branch ativa como cânone definitivo.

Quando uma tarefa depender de trabalho ainda não integrado, a referência relevante deve ser identificada de forma inequívoca por branch, PR, commit ou base.

## 5. Evidência proporcional de cobertura

A matriz de cobertura foi mantida como **ferramenta possível**, não como template obrigatório do ÓRBITA.

Conforme volume e risco, a evidência pode ser:

- lista de documentos unidos e seus destinos;
- referências origem → destino;
- tabela ou matriz de cobertura;
- indicação da decisão que substituiu conteúdo removido;
- diff revisado com justificativas para exclusões relevantes.

A exigência é tornar a consolidação auditável com a **menor evidência suficiente**, sem criar documentação paralela desnecessária.

## 6. Critérios para homologar o refinamento

Para homologar este refinamento mínimo:

- `main` e trabalho ativo em revisão permanecem conceitualmente distintos;
- consolidação extensa exige evidência de preservação semântica proporcional ao risco;
- conteúdo incompleto não é removido apenas por ainda não estar finalizado;
- dúvidas de cobertura favorecem preservação, não exclusão;
- não é criado template obrigatório neste momento;
- pequenas correções e reorganizações simples não ganham burocracia adicional;
- a incorporação depende de homologação humana explícita.

### Limite da evidência

A proposta nasce de **uma ocorrência documentada** no projeto MMO.

O refinamento não afirma que toda consolidação documental exige matriz formal nem que o problema seja recorrente em todos os projetos. Ele introduz uma proteção proporcional contra um risco já demonstrado e deve continuar sendo observado em usos futuros.

## 7. Referências

- [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md): autorização, preservação, evidências e regra de parada.
- [Governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
- [Fluxo de desenvolvimento](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md).
- [the-mmo-idea — PR #1](https://github.com/jotaCorsino/the-mmo-idea/pull/1): documentação conceitual e recuperação do acervo.


## 8. Estado de incorporação

Foram preparados ajustes em:

- [IA no método](../docs/07-IA-NO-METODO.md);
- [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md).

A proposta foi **APROVADA** pelo responsável humano no PR #11 em 22/10/2026 e está liberada para integração à `main`.


## 9. Decisão de homologação

**APROVADA** pelo responsável humano no PR #11 em 22/10/2026.

A homologação confirma o refinamento proporcional:

- preservação semântica em consolidações relevantes;
- distinção entre `main` integrada e trabalho ativo em revisão;
- ausência de template obrigatório;
- matriz de cobertura apenas quando útil;
- nenhuma burocracia adicional para pequenas correções;
- preservação preferida quando houver dúvida sobre perda de conteúdo.

A aprovação não transforma toda revisão textual em consolidação formal e não autoriza exclusões documentais amplas sem evidência ou gate adequado.
