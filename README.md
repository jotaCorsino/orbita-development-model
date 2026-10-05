<div align="center">

# Método ÓRBITA

### Desenvolvimento de Software Assistido por IA com Governança Humana

**Um modelo pessoal de organização, rastreabilidade e controle do desenvolvimento de software.**

Idealizado e utilizado por **João Corsino**, em formação para atuar como **Analista de Sistemas**.

![Status](https://img.shields.io/badge/status-em%20documenta%C3%A7%C3%A3o-blue)
![Idioma](https://img.shields.io/badge/idioma-PT--BR-green)
![Modelo](https://img.shields.io/badge/modelo-Human--in--the--Loop-purple)
![GitHub](https://img.shields.io/badge/GitHub-fonte%20can%C3%B4nica-black)

</div>

---

## O que é o Método ÓRBITA?

O **Método ÓRBITA** é a forma particular que desenvolvi para manter projetos de software assistidos por Inteligência Artificial **organizados, rastreáveis e sob governança humana**.

Ele nasceu de uma necessidade prática: usar agentes de IA para aumentar capacidade de análise e implementação sem perder clareza sobre **quem decide, quem planeja, quem executa, o que foi alterado e quando uma etapa pode realmente ser considerada concluída**.

O modelo não pretende substituir metodologias consolidadas de engenharia de software. Ele organiza a minha forma de trabalhar com práticas já conhecidas — Git, branches, commits, Pull Requests, testes, documentação e desenvolvimento incremental — combinadas com uma separação explícita de responsabilidades entre humano e agentes de IA.

> **Princípio central:** Planejar → Executar → Evidenciar → Homologar.

## Por que criei este modelo?

Ferramentas de IA conseguem produzir código rapidamente. O problema é que velocidade sem processo pode gerar outro tipo de dívida: decisões implícitas, alterações difíceis de rastrear, escopo crescente, documentação desatualizada e perda de compreensão do próprio projeto.

O ÓRBITA foi criado para evitar isso.

No meu fluxo, a IA **não recebe autoridade irrestrita sobre o projeto**. Cada participante possui um papel definido, o trabalho é dividido em unidades controláveis e mudanças importantes dependem de evidências e homologação.

## Os quatro elementos da órbita

| Elemento | Responsabilidade principal |
|---|---|
| **Responsável humano** | Define objetivos, prioridades, restrições e dá a aprovação final |
| **Agente de planejamento** | Analisa, estrutura, especifica, revisa e coordena o processo |
| **Agente de implementação** | Altera código, executa testes, builds e produz evidências técnicas |
| **Git/GitHub** | Mantém o estado canônico, histórico, documentação e rastreabilidade |

Na minha aplicação atual, esses papéis são normalmente exercidos por **João Corsino + ChatGPT + Codex + GitHub**. O modelo, porém, é conceitualmente independente das ferramentas específicas.

## O ciclo ÓRBITA

```mermaid
flowchart LR
    A[Necessidade] --> B[Análise]
    B --> C[Planejamento]
    C --> D[Tarefa]
    D --> E[Branch]
    E --> F[Implementação]
    F --> G[Testes e evidências]
    G --> H[Pull Request]
    H --> I[Revisão]
    I --> J{Homologado?}
    J -- Não --> F
    J -- Sim --> K[Merge]
    K --> L[Documentação / Release]
    L --> M[Próxima tarefa]
```

## O que significa ÓRBITA?

| Letra | Princípio |
|---|---|
| **O** | **Orquestração humana** |
| **R** | **Repositório como fonte da verdade** |
| **B** | **Blocos incrementais de trabalho** |
| **I** | **Implementação por agentes especializados** |
| **T** | **Testes e rastreabilidade** |
| **A** | **Aprovação antes do avanço** |

## Regras fundamentais

1. A decisão final permanece humana.
2. Planejamento e implementação são responsabilidades separáveis.
3. O trabalho avança em tarefas pequenas e verificáveis.
4. O repositório representa o estado técnico do projeto.
5. Mudanças relevantes precisam deixar evidências.
6. Código executado não é automaticamente código homologado.
7. A documentação acompanha a evolução do projeto.
8. A `main` deve representar um estado conhecido e aprovado.

## Documentação

| Documento | Conteúdo |
|---|---|
| [Visão geral](docs/01-VISAO-GERAL.md) | Origem, objetivo e escopo do modelo |
| [Princípios](docs/02-PRINCIPIOS.md) | Fundamentos que orientam o método |
| [Papéis e responsabilidades](docs/03-PAPEIS-E-RESPONSABILIDADES.md) | Quem decide, planeja, executa e registra |
| [Fluxo de desenvolvimento](docs/04-FLUXO-DE-DESENVOLVIMENTO.md) | Ciclo operacional de ponta a ponta |
| [Governança e homologação](docs/05-GOVERNANCA-E-HOMOLOGACAO.md) | Gates, evidências e critérios de avanço |
| [Git e GitHub](docs/06-GIT-E-GITHUB.md) | Uso do repositório como fonte canônica |
| [IA no método](docs/07-IA-NO-METODO.md) | Como os agentes são usados sem retirar controle humano |
| [Aplicação e evolução](docs/08-APLICACAO-E-EVOLUCAO.md) | Como adotar, adaptar e evoluir o modelo |

Também existem [templates](templates/) para tarefas, prompts de implementação e homologação.

## Para quem este repositório existe?

Este projeto cumpre dois objetivos.

O primeiro é **operacional**: registrar e evoluir a forma que utilizo para desenvolver software com apoio de IA.

O segundo é **profissional**: tornar visível, no meu portfólio, não apenas o resultado dos projetos que desenvolvo, mas também **como penso, organizo decisões, controlo mudanças, utilizo ferramentas de IA e mantenho rastreabilidade durante o desenvolvimento**.

## Autoria

O Método ÓRBITA foi **idealizado, estruturado e utilizado por João Corsino** a partir da experiência prática em seus próprios projetos de software.

Sou profissional em formação na área de tecnologia, com o objetivo de atuar como **Analista de Sistemas**, e este repositório registra uma parte importante da construção da minha forma de trabalhar.

O modelo é evolutivo. Novas práticas podem ser incorporadas conforme projetos reais revelem problemas, limitações e oportunidades de melhoria.

---

<div align="center">

**João Corsino · Método ÓRBITA**

*Organizar o uso da IA para que velocidade não substitua controle.*

</div>
