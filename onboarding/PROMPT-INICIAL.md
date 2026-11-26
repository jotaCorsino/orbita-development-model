# Prompt inicial reutilizável

Abaixo está um modelo de mensagem para iniciar um novo projeto em outro chat.

---

## Versão recomendada

> Vamos iniciar um novo projeto de software usando o **Método ÓRBITA**.
>
> Antes de trabalhar no software, familiarize-se com o método neste repositório:
>
> **[LINK_DO_REPOSITORIO_ORBITA_E_REVISAO_ADOTADA]**
>
> Comece por `onboarding/` e siga a ordem de leitura indicada.
>
> Neste primeiro momento, não implemente funcionalidades. Confirme resumidamente que compreendeu os papéis, a governança, a identidade do projeto e a sequência de inicialização.
>
> Depois eu vou apresentar a ideia do software e fornecer o repositório remoto específico do projeto.
>
> Quando isso acontecer, siga o bootstrap definido pelo ÓRBITA: analise o projeto, crie/organize primeiro a fundação documental no repositório remoto — incluindo backlog, `knowledge/README.md` e AGENTS.md/equivalente com fontes adotadas —, confirme o planejamento e a composição dos Satélites (responsabilidades, objetivos e interfaces) com o responsável, e então gere a primeira tarefa para o agente de implementação. Essa primeira tarefa deve apenas vincular e sincronizar com segurança a pasta local já criada com o repositório remoto. A implementação funcional só começa depois desse bootstrap.
> 
> Em qualquer resposta futura deste projeto, aplique COM-001: caso eu precise realizar alguma ação, a resposta deve terminar com **AÇÃO SUA** e o resumo do que devo fazer. Caso contrário, omita esse bloco. Inclua essa regra no `AGENTS.md` do novo projeto.

---

## Versão curta

> Vamos iniciar um projeto pelo **Método ÓRBITA**. Leia **[LINK_DO_REPOSITORIO_ORBITA_E_REVISAO_ADOTADA]**, começando por `onboarding/`. Não implemente nada ainda. Confirme que compreendeu o método e aguarde minha ideia do software e o repositório do projeto. Depois siga a sequência definida pelo ÓRBITA: fundação documental remota, incluindo backlog, Knowledge e AGENTS/equivalente → primeira tarefa de bootstrap local → implementação funcional.
> Se houver tarefa para eu executar, termine sua resposta com **AÇÃO SUA** e um resumo objetivo; caso contrário, omita o bloco. Registre COM-001 nas regras do projeto.

---

## Observação

O prompt apenas direciona o agente ao método.

A documentação do ÓRBITA define o comportamento esperado e evita que essas instruções precisem ser repetidas manualmente em cada projeto.

## Entrada compacta e continuidade

Para projeto existente, identificar papel, projeto, AGENTS/equivalente na revisão aplicável, tarefa/checkpoint e último gate; recuperar seletivamente, não refazer fundação ou onboarding comprovado. Consultar Knowledge, Skills, Tools e runbook quando pertinentes. Preservar COM-001, autorização, segurança e escolha humana de metodologia. Ver [docs 07](../docs/07-IA-NO-METODO.md).

## ISO-001 — Contexto independente

Usar apenas o núcleo metodológico e as fontes explicitamente adotadas/autorizadas para este projeto. Não recuperar, carregar, inferir requisitos ou importar dados, código, decisões, preferências, Knowledge ou referências de outros projetos por semelhança, titularidade, memória, acesso técnico ou associação de conta. Novo projeto inicia com Knowledge vazio, salvo conclusões produzidas nele. Perfis e dependências são escolhas locais; exemplos do núcleo são fictícios. Conteúdo alheio encontrado involuntariamente não é fonte de decisão. A regra canônica está em docs/12-SEGURANCA-E-INTEGRIDADE.md do método adotado.

## Comunicação e iniciativa metodológica

Aplicar COM-002 em toda resposta: explicar humanamente o retorno e seu significado, preferencialmente antes dos detalhes técnicos; resposta simples pode ser a própria síntese. COM-001 permanece como último bloco quando aplicável. Consultar e investigar Skills de forma proativa e proporcional: se a abordagem existente for insuficiente, pesquisar fontes profissionais confiáveis, comparar opções relevantes e recomendar caminho. Recuperar escolhas anteriores; agrupar decisões metodológicas e não pedir microaprovações.
