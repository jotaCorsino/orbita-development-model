# 03 — Papéis e responsabilidades

O ÓRBITA trabalha com papéis, não com dependência obrigatória de ferramentas específicas.

## 1. Responsável humano

Responsabilidades:

- definir necessidade e objetivo;
- estabelecer prioridades e restrições;
- aprovar decisões relevantes;
- avaliar resultado funcional;
- homologar ou rejeitar entregas;
- decidir quando o projeto avança.

O humano é o **proprietário da decisão**, não apenas o autor do prompt.

## 2. Agente de planejamento

Responsabilidades:

- transformar necessidades em problemas claros;
- estruturar requisitos;
- criar e manter a fundação documental inicial do projeto no repositório remoto, quando autorizado;
- criar README, visão, planejamento, roadmap e regras proporcionais ao projeto;
- decompor trabalho em tarefas;
- identificar riscos e dependências;
- produzir instruções de implementação;
- gerar a primeira tarefa de bootstrap para vincular a pasta local ao repositório remoto antes da primeira funcionalidade;
- interpretar evidências retornadas;
- revisar coerência entre planejamento e execução;
- manter visão global do projeto.

O agente de planejamento não substitui a homologação humana.

## 3. Agente de implementação

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

## Frentes profissionais integradas

O ÓRBITA organiza o trabalho como uma estrutura profissional de desenvolvimento a serviço do responsável humano. Frentes são responsabilidades por resultados e aspectos do produto, não departamentos obrigatórios, novos níveis de autoridade, instâncias de IA ou repositórios. Um mesmo agente pode assumir sucessivamente competências distintas; agentes separados são opcionais quando disponíveis, autorizados e úteis. Preservar a separação entre planejar, executar, revisar e homologar, mesmo que um agente desempenhe mais de um papel. Atribuição de papel não comprova qualificação, independência de avaliação, acesso ou execução de trabalho por outra pessoa.

| Frente ilustrativa | Responsabilidade predominante | Entregável ou interface com outras frentes |
| --- | --- | --- |
| Produto e análise de necessidades | Problema, valor, prioridades, requisitos e critérios | Objetivos, requisitos, hipóteses e decisões |
| UX, UI e design | Jornadas, informação, interação, acessibilidade e linguagem visual | Fluxos, protótipos, componentes e critérios de experiência |
| Arquitetura e engenharia | Viabilidade, qualidade, contratos, dependências e implementação | Decisões arquiteturais, interfaces e incrementos testáveis |
| Qualidade e segurança | Revisão de critérios, riscos e evidências; prevenção de regressões | Achados, testes, limites e recomendações de correção |
| Operações e entrega | Ambiente, preparação, aplicação e recuperação autorizadas | Artefato, runbook, prova de versão e estado observado |
| Coordenação e documentação | Visão global, dependências, decisões e consistência | Plano, tarefas, checkpoints e estado integrado |

Estas são frentes possíveis, adaptáveis ao domínio e à escala. Não criar frente, equipe, chat, pasta, reunião ou documento somente para cumprir organograma. Identificar a competência necessária para a etapa atual; combinar funções em tarefas pequenas, separar quando a independência exigida, o risco, a especialização ou as dependências justificarem. Quando competência, ferramenta ou revisão independente indispensável não estiver disponível, declarar a lacuna e obter o recurso autorizado ou bloquear apenas a ação dependente.

Todas as frentes do mesmo projeto compartilham o contexto canônico autorizado e versionado: objetivo, requisitos, decisões, contratos, roadmap, backlog, Knowledge local, tarefas e evidências pertinentes, com fonte competente por assunto. Compartilhar referência, não replicar contexto em silos. Acesso continua limitado por função, finalidade, dados e ambiente; ISO-001 impede herança de outro projeto. Coordenação resolve dependências e conflitos entre frentes conforme autoridade por assunto. O responsável humano permanece proprietário das decisões e dos gates; delegação técnica não transfere homologação.

## Papéis e ambientes não são a mesma coisa

O ÓRBITA separa **quem faz o quê** de **onde o trabalho acontece**.

| Ambiente atual | Papel predominante | Observação |
|---|---|---|
| Contexto do agente de planejamento | planejamento e coordenação | pode ser ChatGPT, Claude, Gemini ou outra ferramenta equivalente; não substitui a documentação persistente |
| Contexto do agente de implementação | implementação e validação técnica | pode ser Codex ou outro agente capaz de trabalhar sobre o repositório e o escopo autorizado |
| Pasta local | execução material do projeto | contém a working copy Git sincronizada com o remoto |
| GitHub | registro persistente | é a fonte canônica de código, documentação e histórico |

O mesmo nome de projeto deve ser usado entre esses ambientes sempre que possível.

Essa separação evita dois erros comuns: imaginar que o chat é o próprio projeto ou imaginar que a pasta local, isoladamente, representa o estado oficial do projeto.

## Configuração de referência

Neste repositório, **ChatGPT** é usado como exemplo de agente de planejamento e **Codex** como exemplo de agente de implementação. Essa combinação serve apenas como referência prática; outras ferramentas podem substituir qualquer um dos agentes desde que cumpram as responsabilidades definidas pelo ÓRBITA.

## Composição modular e autoridade por assunto

| Fonte competente | Autoridade e limite |
| --- | --- |
| Núcleo ÓRBITA adotado | Princípios, papéis, gates, segurança, evidência e evolução; não escolhe requisitos ou stack do consumidor |
| HUB organizacional (opcional) | Políticas comuns e coordenação entre projetos explicitamente abrangidos; não adquire autoridade sobre todo repositório por associação |
| Método especializado (opcional, um ou mais) | Fluxo técnico, critérios, templates e procedimentos do domínio declarado; não redefine objetivo nem dispensa restrições superiores aplicáveis |
| Projeto | Requisitos, arquitetura, prioridades, tarefas, decisões e ambiente próprio, conforme responsáveis competentes |
| Dono de ambiente/dados | Acesso, destino, dados, custo, autorização operacional e recuperação |
| Mantenedor/curador de Knowledge, Skills ou Tools | Conteúdo e validade no escopo próprio; não amplia autoridade, transfere propriedade ou homologa consumidor |

Não há hierarquia organizacional obrigatória: um projeto pode consumir núcleo diretamente, combinar métodos por assunto ou pertencer a HUB(s) com escopo explícito. Não inferir adoção transitiva. O responsável registra fontes/revisões, domínio e limites; referências públicas ou conteúdo de PR não são autorização. Restrições legais, de plataforma, segurança e contratos aplicáveis não são dispensáveis. Acumular restrições compatíveis; distinguir regra, decisão delegada, preferência e fato volátil. Conflito: recuperar fonte competente e decisão vigente, aplicar interpretação segura quando delegada; se persistir divergência material, bloquear somente ação dependente e elevar ao responsável competente, sem escolher por recência ou conveniência. Nenhum agente homologa a própria entrega.

A escolha humana de abordagem metodológica entre alternativas viáveis é regida por [Skills](08-APLICACAO-E-EVOLUCAO.md); a seleção e consumo de ferramenta por [dependências e Tools](10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md).

A composição respeita ISO-001: um projeto não herda contexto, preferências ou dados de outro; somente fontes escolhidas para o escopo pelo responsável. O núcleo não é catálogo de projetos ou organização.
