# 02 — Princípios

## O — Orquestração humana

A IA participa do trabalho, mas não define sozinha o rumo do projeto. Objetivos, prioridades, concessões e homologação pertencem ao responsável humano.

## R — Repositório como fonte da verdade

Informações importantes não devem depender apenas do contexto temporário de uma conversa. Código, documentação, decisões relevantes e histórico precisam convergir para o repositório.

## B — Blocos incrementais

O desenvolvimento é dividido em tarefas pequenas o suficiente para serem compreendidas, executadas, testadas e revisadas sem ocultar mudanças relevantes.

## I — Implementação por agentes especializados

Planejamento e implementação podem ser atribuídos a agentes diferentes. Essa separação reduz a tendência de um único agente definir o problema, escolher a solução e aprovar a própria execução sem revisão externa.

## T — Testes e rastreabilidade

Uma tarefa concluída deve produzir evidências compatíveis com seu risco: testes, build, diff, logs, validações funcionais, commit, PR ou documentação.

## A — Aprovação antes do avanço

Uma etapa tecnicamente concluída não é necessariamente homologada. O avanço depende do gate definido para aquela etapa.

## Princípio operacional

> **Planejar → Executar → Evidenciar → Homologar**

Esse ciclo é o núcleo operacional do método.

## Princípio de proporcionalidade

Nem todo projeto exige a mesma burocracia. O ÓRBITA deve aumentar ou reduzir formalidade conforme complexidade, impacto, número de participantes e risco da mudança.

## Princípio complementar — Identidade única do projeto

Cada software deve possuir uma identidade reconhecível e consistente nos ambientes em que é trabalhado.

Na configuração de referência, o padrão preferido é utilizar o mesmo nome para:

- contexto do agente de planejamento;
- contexto do agente de implementação;
- pasta local;
- repositório GitHub.

Quando uma limitação técnica exigir nomes diferentes, o mapeamento deve ser óbvio ou documentado.

A intenção não é estética. Essa consistência reduz erros de contexto e facilita a retomada do projeto por humanos e agentes.

## Princípio complementar — Sincronização de contexto

Contexto de conversa pode ficar desatualizado. Antes de planejar ou implementar trabalho relevante, o agente deve consultar o estado atual do repositório correspondente.

O fluxo de informação esperado é:

```text
conversa / planejamento
        ↓
decisão relevante
        ↓
repositório
        ↓
novo agente ou nova sessão
        ↓
releitura do estado atual
```

O objetivo é impedir que a continuidade do projeto dependa de memória implícita de uma sessão específica.

## Princípio transversal — Segurança proporcional ao risco

Segurança deve ser considerada desde o planejamento até a homologação, e não apenas como revisão final.

O nível de controle deve ser proporcional ao impacto, aos dados tratados, à exposição e à criticidade do projeto.

Isso inclui, quando aplicável:

- segurança do software;
- segurança da informação;
- proteção de segredos e dados sensíveis;
- autenticação e autorização;
- dependências;
- exposição pública;
- práticas seguras de Git/GitHub;
- testes e verificações de segurança.

Testes são evidência importante, mas não provam ausência de vulnerabilidades.

Ver [12 — Segurança e integridade do projeto](12-SEGURANCA-E-INTEGRIDADE.md).
