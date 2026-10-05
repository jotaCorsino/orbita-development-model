<div align="center">

# Método ÓRBITA

### Desenvolvimento de Software Assistido por IA com Governança Humana

**Um modelo pessoal de organização, rastreabilidade e controle do desenvolvimento de software.**

Idealizado e utilizado por **João Corsino**, em formação para atuar como **Analista de Sistemas**.

![Versão](https://img.shields.io/badge/vers%C3%A3o-v0.1%20candidate-blue)
![Status](https://img.shields.io/badge/status-aguardando%20homologa%C3%A7%C3%A3o-orange)
![Idioma](https://img.shields.io/badge/idioma-PT--BR-green)
![Modelo](https://img.shields.io/badge/modelo-Human--in--the--Loop-purple)

</div>

---

## Em linguagem simples: como eu trabalho

O ÓRBITA nasceu porque eu percebi que **usar IA para desenvolver software funciona muito melhor quando cada coisa tem o seu lugar**.

Quando começo um projeto, eu não quero que ele exista apenas dentro de uma conversa, nem que a implementação avance mais rápido do que a minha capacidade de entender o que está acontecendo. Quero conseguir abrir o projeto dias ou semanas depois e saber com clareza **o que estamos construindo, por que tomamos determinada decisão, o que já foi feito, o que ainda falta e qual é o próximo passo**.

Por isso organizo cada software como um projeto próprio em todos os ambientes que uso. O mesmo projeto possui um espaço para planejamento com IA, um espaço para implementação com IA, uma pasta local de trabalho no computador e um repositório correspondente no GitHub. Sempre que possível, todos usam **o mesmo nome**.

Na prática:

- **o agente de planejamento** me ajuda a compreender o problema, planejar, revisar e administrar o projeto;
- **o agente de implementação** trabalha na implementação e nas validações técnicas;
- **a pasta local** é onde a cópia de trabalho do software existe no computador;
- **o GitHub** mantém o registro persistente do código, da documentação e da evolução do projeto;
- **eu continuo responsável pelas decisões, prioridades e homologação**.

Esses espaços não competem entre si. Eles se complementam.

### Ferramentas que eu uso

Na minha configuração pessoal, prefiro usar **ChatGPT como agente de planejamento** e **Codex como agente de implementação**. Essa é apenas a combinação que escolhi para o meu fluxo atual, não uma exigência do ÓRBITA.

Quem adotar o método pode usar **Claude, Gemini ou qualquer outra IA/agente** capaz de cumprir esses papéis. Também é possível trocar as ferramentas ao longo do tempo sem alterar o método, desde que as responsabilidades, a rastreabilidade e os gates permaneçam claros.

A eficiência do modelo não vem de entregar tudo para a IA. Ela vem de **reduzir ambiguidade**: cada agente sabe qual é o seu papel, cada projeto possui um lugar definido, as mudanças são pequenas o suficiente para serem acompanhadas e o conhecimento importante volta para o repositório em vez de desaparecer dentro de uma conversa.

É isso que o ÓRBITA procura preservar: **usar a velocidade da IA sem perder organização, entendimento e controle humano.**

## O que é o Método ÓRBITA?

O **Método ÓRBITA** é a forma particular que desenvolvi para manter projetos de software assistidos por Inteligência Artificial **organizados, rastreáveis e sob governança humana**.

Ele nasceu de uma necessidade prática: usar agentes de IA para aumentar capacidade de análise e implementação sem perder clareza sobre **quem decide, quem planeja, quem executa, o que foi alterado e quando uma etapa pode realmente ser considerada concluída**.

O modelo não pretende substituir metodologias consolidadas de engenharia de software. Ele organiza a minha forma de trabalhar com práticas já conhecidas — Git, branches, commits, Pull Requests, testes, documentação e desenvolvimento incremental — combinadas com uma separação explícita de responsabilidades entre humano e agentes de IA.

> **Princípio central:** Planejar → Executar → Evidenciar → Homologar.

## Por que criei este modelo?

Ferramentas de IA conseguem produzir código rapidamente. O problema é que velocidade sem processo pode gerar outro tipo de dívida: decisões implícitas, alterações difíceis de rastrear, escopo crescente, documentação desatualizada e perda de compreensão do próprio projeto.

O ÓRBITA foi criado para evitar isso.

No meu fluxo, a IA **não recebe autoridade irrestrita sobre o projeto**. Cada participante possui um papel definido, o trabalho é dividido em unidades controláveis e mudanças importantes dependem de evidências e homologação.

## Um projeto, quatro espaços, uma identidade

Na aplicação prática atual do ÓRBITA, cada software recebe uma identidade coerente nos ambientes usados para desenvolvê-lo:

| Espaço | Organização esperada | Função principal |
|---|---|---|
| **Contexto do agente de planejamento** | projeto/conversa/workspace próprio com o nome do software | planejamento, análise, decisões, coordenação e revisão |
| **Contexto do agente de implementação** | projeto/workspace próprio com o mesmo nome | implementação, testes e produção de evidências |
| **Pasta local** | pasta com o mesmo nome do projeto | working copy do Git, arquivos locais e execução técnica |
| **Repositório GitHub** | repositório correspondente ao mesmo projeto | fonte persistente da verdade, histórico e documentação |

A regra prática é:

> **um projeto → um nome reconhecível → um contexto próprio em cada ferramenta → um repositório canônico.**

Essa padronização reduz trocas de contexto, nomes divergentes, uso acidental do repositório errado e perda de continuidade entre planejamento e implementação.

O GitHub continua sendo a fonte persistente da verdade. Os ambientes dos agentes de planejamento e implementação são contextos de trabalho; a pasta local é a working copy sincronizada com o repositório remoto.

A especificação completa está em [Identidade e ambiente do projeto](docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md).

## Como um novo projeto nasce no ÓRBITA

A organização começa **antes da primeira linha de código**.

O responsável humano cria um contexto dedicado no agente de planejamento, inicia a conversa, apresenta a ideia e informa dois repositórios: o do Método ÓRBITA e o repositório remoto reservado ao novo software.

A partir daí, o fluxo inicial é:

```text
Contexto do agente de planejamento
        ↓
ideia + Método ÓRBITA + repositório do projeto
        ↓
agente de planejamento entende o método e estrutura o software
        ↓
README + planejamento + documentação inicial no GitHub
        ↓
agente de planejamento confirma a fundação
        ↓
primeira tarefa: bootstrap do agente de implementação
        ↓
pasta local criada pelo responsável humano
        ↓
agente de implementação inicializa/valida Git e sincroniza com o remoto
        ↓
planejamento + implementação + pasta local + GitHub
estão vinculados ao mesmo projeto
        ↓
começa a primeira tarefa funcional
```

Esse detalhe é importante: **o agente de planejamento funda e documenta o projeto antes da implementação; o agente de implementação primeiro conecta a working copy local ao projeto já documentado; só depois começa o desenvolvimento funcional.**

A especificação está em [Inicialização de um novo projeto](docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Os quatro elementos da órbita

| Elemento | Responsabilidade principal |
|---|---|
| **Responsável humano** | Define objetivos, prioridades, restrições e dá a aprovação final |
| **Agente de planejamento** | Analisa, estrutura, especifica, revisa e coordena o processo |
| **Agente de implementação** | Altera código, executa testes, builds e produz evidências técnicas |
| **Git/GitHub** | Mantém o estado canônico, histórico, documentação e rastreabilidade |

Na configuração pessoal do autor, esses papéis correspondem a **responsável humano + ChatGPT + Codex + GitHub**. Essa combinação é apenas um exemplo de implementação; o método é independente das ferramentas específicas.

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

## O que o ÓRBITA evita deliberadamente?

O método foi desenhado para reduzir alguns padrões que considero perigosos no desenvolvimento assistido por IA:

- entregar um problema amplo a um agente e aceitar uma grande alteração sem decomposição;
- permitir que o mesmo agente defina, implemente e aprove sozinho a solução;
- tratar uma conversa como única fonte de documentação;
- avançar para novas funcionalidades sem homologar a etapa anterior;
- confundir “o código rodou” com “a necessidade foi atendida”;
- permitir expansão silenciosa de escopo;
- perder a relação entre requisito, implementação, evidência e decisão.

A discussão completa está em [Anti-padrões](docs/09-ANTI-PADROES.md).

## Iniciar um novo projeto com o ÓRBITA

Para aplicar o método em um novo software sem precisar reexplicar todo o processo a cada conversa, existe uma área permanente de **onboarding para agentes de IA**:

**[Começar pelo onboarding](onboarding/README.md)**

Ela define a ordem de leitura, o contrato de trabalho esperado, o checklist de início de projeto e um prompt reutilizável para apresentar o Método ÓRBITA em um novo chat.

O objetivo é permitir que um novo agente compreenda **como trabalhar** antes de receber a descrição do software e o repositório específico que será desenvolvido.

## Evidência prática

O ÓRBITA não nasceu apenas como conceito. Seus princípios vêm sendo aplicados em projetos reais.

O primeiro estudo de caso documentado é o projeto **[Tickets Recorrentes HESK](examples/01-TICKETS-RECORRENTES-HESK.md)**, no qual o desenvolvimento foi dividido em etapas como prova de conceito, persistência, scheduler, segurança contra duplicidade, processamento em lote e interface administrativa. Cada etapa avançou por implementação, validação, evidências e homologação antes da próxima.

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
| [Anti-padrões](docs/09-ANTI-PADROES.md) | Comportamentos que o método procura evitar |
| [Onboarding para novos projetos](onboarding/README.md) | Entrada permanente para novos agentes e novos projetos |
| [Identidade e ambiente do projeto](docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md) | Organização do mesmo projeto entre ChatGPT, Codex, pasta local e GitHub |
| [Inicialização de um novo projeto](docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md) | Fundação documental remota e primeiro bootstrap local do agente de implementação |
| [Roadmap](ROADMAP.md) | Maturidade e próximas evoluções do próprio método |

Também existem [templates](templates/) para tarefas, bootstrap local, prompts de implementação e homologação e uma área de [exemplos](examples/) com aplicações reais.

## Estado atual do método

Esta documentação representa a **candidata à versão v0.1**.

A fundação está em **AGUARDANDO_HOMOLOGACAO**. O objetivo desta fase é estabilizar definição, princípios, papéis, fluxo, governança e exemplos antes de ampliar o método com novos templates e estudos de caso.

Consulte o [roadmap](ROADMAP.md) para acompanhar a evolução.

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
