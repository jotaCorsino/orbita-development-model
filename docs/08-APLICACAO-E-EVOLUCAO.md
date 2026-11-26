# 08 — Aplicação e evolução

## Como começar

Uma adoção mínima do ÓRBITA pode usar apenas:

1. um responsável humano;
2. um repositório Git;
3. um agente para planejamento;
4. um agente ou ferramenta para implementação;
5. tarefas com critérios de aceite;
6. validação antes do merge.

## Organização recomendada de um projeto

Na configuração de referência, um projeto novo é inicializado nesta ordem:

1. definir o nome canônico;
2. criar um contexto dedicado no agente de planejamento;
3. apresentar a ideia e os repositórios do ÓRBITA e do novo projeto;
4. o agente de planejamento cria a fundação documental no repositório remoto;
5. o responsável humano cria a pasta local e a abre no ambiente do agente de implementação;
6. o agente de planejamento entrega a primeira tarefa de bootstrap;
7. o agente de implementação inicializa/valida Git e sincroniza a pasta com o remoto;
8. somente depois começa a primeira implementação funcional.

Os quatro ambientes devem permanecer associados pelo mesmo nome sempre que possível.

O repositório continua sendo a referência persistente. Os demais ambientes reduzem troca de contexto e especializam o trabalho.

Essa organização é recomendada, não um requisito tecnológico universal. Se uma ferramenta mudar, o princípio permanece: **um projeto deve ter identidade clara e ambientes de trabalho inequivocamente associados ao mesmo repositório**.

Ver [Inicialização de um novo projeto](11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Níveis de formalidade

### Projeto simples

- tarefa curta;
- implementação;
- teste;
- revisão humana;
- commit.

### Projeto intermediário

- roadmap;
- tarefas identificadas;
- branches;
- testes;
- PR;
- homologação;
- documentação contínua.

### Projeto crítico

O ÓRBITA deve ser complementado por processos formais adequados: revisão especializada, segurança, CI/CD, controle de acesso, QA, compliance e outros requisitos organizacionais.

## Evolução por experiência real

O método deve mudar quando a prática demonstrar necessidade.

Uma nova regra deve responder a pelo menos uma pergunta:

- Qual problema recorrente ela evita?
- Qual decisão torna mais clara?
- Qual risco reduz?
- Qual evidência passa a exigir?
- O ganho justifica a complexidade adicionada?

## Registros de aprendizado e evolução

Ocorrências e propostas surgidas durante a aplicação do método devem ser registradas antes de se tornarem regras normativas.

As áreas `troubleshooting/` e `proposals/` preservam, respectivamente:

- problemas e ocorrências observadas em uso real;
- melhorias candidatas ainda sujeitas a análise, teste e homologação.

### Numeração em trabalho paralelo

IDs numéricos como `TRB-002` ou `PROP-003` são **canônicos somente depois de atribuídos contra o estado atual da `main`**.

Branches paralelas não devem presumir que o próximo número visto na sua base continua disponível. Enquanto um registro estiver sendo elaborado fora da linha principal, prefira um identificador temporário inequívoco, por exemplo:

```text
TRB-DRAFT-20261022-deploy-preview
PROP-DRAFT-20261022-consolidacao-documental
```

No gate de integração:

1. consultar a `main` atual;
2. identificar o último número canônico de cada coleção;
3. atribuir o próximo número livre;
4. atualizar nome do arquivo, título e referências internas;
5. verificar colisões com outros PRs/branches ainda ativos;
6. somente então homologar e integrar.

A ordem de numeração não define prioridade metodológica. Quando dois registros concorrentes precisarem ser saneados, a ordem de criação comprovável pode ser usada como critério neutro de desempate.

As convenções locais estão documentadas em [../troubleshooting/README.md](../troubleshooting/README.md) e [../proposals/README.md](../proposals/README.md).

## Backlog de evolução do projeto

Todo projeto ÓRBITA deve possuir, por padrão, uma seção **Backlog** no `README.md` para registrar necessidades futuras sem expandir silenciosamente o escopo atual.

O backlog é uma área de **captura de evolução potencial**. Ele não substitui roadmap, tarefas, issues ou critérios de aceite.

Princípio:

> **Registrar no backlog não significa autorizar implementação.**

Modelo mínimo:

```md
## Backlog

Necessidades identificadas para evolução futura do projeto.
A inclusão de um item neste backlog não autoriza sua implementação.

| ID | Tipo | Item | Prioridade | Origem | Status |
| --- | --- | --- | --- | --- | --- |
| BL-001 | Feature | [descrição curta] | Média | Homologação | Backlog |
```

Os estados recomendados são:

- **Backlog** — necessidade registrada;
- **Selecionado** — item escolhido para análise e planejamento;
- **Concluído** — necessidade atendida;
- **Descartado** — item deliberadamente não seguirá para execução.

O backlog não replica estados de execução como `Em implementação`, `Em validação` ou `Aguardando homologação`. Quando um item é selecionado, a execução passa a ser controlada pelo fluxo normal do ÓRBITA.

A distinção é:

```text
Backlog = captura
Roadmap = planejamento
Tarefa = execução autorizada
```

Antes do encerramento de uma tarefa, deve-se verificar proporcionalmente se surgiram necessidades futuras relevantes fora do escopo corrente. Quando houver, elas devem ser registradas no backlog em vez de serem incorporadas silenciosamente à entrega atual.

## Knowledge — conhecimento operacional reutilizável

Projetos ÓRBITA devem manter uma base `knowledge/` para preservar conclusões operacionais comprovadas que possam evitar redescoberta, reincidência de erros ou decisões inadequadas em sessões futuras.

Estrutura mínima:

```text
knowledge/
├── README.md
└── KN-xxx-descricao-curta.md
```

O `knowledge/README.md` funciona como índice rápido. Antes de uma tarefa relevante, o agente consulta esse índice e abre apenas as entradas potencialmente aplicáveis.

Princípio:

> **Descobrir uma vez, validar, registrar e reutilizar quando aplicável.**

Knowledge não substitui documentação canônica, troubleshooting, backlog ou inspeção do estado atual.

A distinção operacional é:

```text
README / docs = o que o projeto é e como funciona
Backlog       = o que talvez faremos
Troubleshooting = o que aconteceu e como foi investigado
Knowledge     = o que aprendemos e devemos reutilizar
```

Uma entrada Knowledge deve ser reutilizável, operacionalmente relevante, não trivial, comprovada e compactável. Hipóteses, logs brutos, transcrições, tarefas futuras, segredos e cópias de documentação canônica não pertencem à base.

Estados de validade:

- **Vigente** — conhecimento validado e aplicável ao escopo declarado;
- **Revalidar** — deve ser confirmado antes de uso porque alguma condição pode ter mudado;
- **Obsoleto** — deixou de representar a realidade atual ou foi substituído.

Conhecimento anterior orienta a investigação, mas **evidência atual confirma a decisão** quando o estado puder ter mudado.

Ao final de uma tarefa relevante, deve-se verificar proporcionalmente se surgiu alguma conclusão comprovada e reutilizável que uma sessão futura provavelmente precisaria redescobrir. Quando houver, a entrada existente deve ser atualizada ou uma nova `KN-xxx` criada.

### Validade e compartilhamento de Knowledge

Identificar tipo de evidência (inspeção estática, teste isolado, operação datada, documentação de fornecedor ou relato), origem, data da comprovação, versão/ambiente/condições e limites. Relato não equivale a observação direta; hipótese nunca Vigente; prova parcial sustenta somente conclusão parcial. Distinguir data de edição da data de verificação. Estados Vigente/Revalidar/Obsoleto mantidos; transição justificada por mudança de condição, conflito, substituição ou nova prova, sem validade arbitrária, reativação só com evidência. Revalidar não é depósito de hipóteses. Consultar índice local seletivamente; fontes externas só pertinentes/autorizadas. Conflitos não se resolvem pelo registro mais recente; consultar fonte competente e estado atual. Atualizar índice e entrada equivalente, preservar história e ID. Base vazia é válida.

Knowledge de projeto pertence ao contexto que o produziu. HUB ou método especializado podem manter bases próprias explicitamente escolhidas pelo responsável, sem herança automática. O Knowledge do núcleo só pode registrar conclusões comprovadas sobre o próprio método, usando evidência independente e sem referências, aliases ou dados oriundos de outros projetos. Não promover entradas de projeto ao núcleo, mesmo sanitizadas. Uma nova regra universal pode ser proposta sem transferir a entrada, seu conteúdo particular ou sua origem e validada em cenário independente. Não copiar entre projetos sem autorização específica do responsável e finalidade legítima; um novo projeto inicia com base vazia.

## NOM-001 — Nomenclatura humanizada

Todo nome criado por agente deve ser legível, simples, descritivo e consistente. Nome humano comunica finalidade; ID lógico preserva rastreio/unicidade; slug/símbolo técnico respeita tecnologia; hash/tag/revisão identifica versão. ID complementa título, não o substitui. Exemplos: `03-requisitos-funcionais.md`, `feat/revisao-de-interface`, `fix: corrige navegação lateral`, “UX-003 — Revisão da interface”, `verificar-integridade.sh`, `catalogo-homologacao`, `catalogo-pre-migracao-20261126T140000Z.sqlite`, `FiltroCategorias` e `validarAcesso`. Aplicar a arquivos, pastas, etapas/subetapas, tarefas, chats, branches, commits, PRs, scripts, backups, ambientes, releases, componentes, funções, variáveis, Skills, Tools e Knowledge. Não impor IDs a tudo, nem renumerar histórico; respeitar idioma, siglas consagradas, convenções de framework, caminhos, API, nomes obrigatórios, IDs de banco e variáveis locais inequívocas. Não incluir segredos ou dado pessoal desnecessário.

Renomear legado apenas quando autorizado e necessário: confirmar identidade, dependentes, links/âncoras, imports, configurações, automação, ambientes, colisões/case e contratos. Preferir rótulo humano sem mudar identificador técnico se suficiente; preservar ID e origem→destino, testar referências e funcionamento. Não reescrever histórico nem renomear recursos operacionais por estética. [Convenções por categoria e exemplos](../proposals/007-08-DOCUMENTACAO-E-NOMENCLATURA.md) §2.

## Fontes canônicas e documentação proporcional

Canonicidade por assunto: README para identidade/visão rápida e backlog; especificação/tarefa para requisitos, autorização e critérios; arquitetura/decisão para contratos; roadmap para planejamento; PR/testes/gate para evidência; release e destino observado para implantação; runbook para operação; troubleshooting para ocorrência; Knowledge para aprendizado; Skills para técnica; Tools para instrumento; AGENTS para fontes adotadas/regras locais. Resumos referenciam fonte, não replicam estado concorrente. Histórico datado não é status atual. Consolidar sem perda semântica conforme [IA no método](07-IA-NO-METODO.md); verificar cobertura origem→destino em mudanças extensas, links no contexto gerado e derivadas pertinentes antes/depois. Backlog pode usar mecanismo equivalente aprovado com índice/referência, sem duplicar execução; manter seção padrão no README. Selecionado aponta à tarefa; conclusão/descarte exige decisão/evidência.

## Skills — seleção de técnicas profissionais

Catálogo por problema/competência, não prompt de papel ou obrigação de framework. Consultar [índice Skills](../skills/README.md) seletivamente; ficha identifica finalidade, tipo, condições, contraindicações, alternativas/complementos, esforço, insumos, passos, entregáveis, evidência, gates, autoria, fonte, versão/data, direitos e revisão. Curador propõe e responsável competente admite/revisa; síntese própria, fontes primárias, direitos verificados para reprodução, evidência de eficácia distinta de descrição. Revalidar por mudança de fonte/condição; não inventar pesquisa, teste ou eficácia. Distinguir método integral, adaptação e técnica complementar. Padrão obrigatório não é opção descartável.

**Seleção:** recuperar objetivo, restrições, incerteza, acesso e critérios. Quando houver alternativas metodológicas viáveis, apresentar opções pertinentes e condicionais (inclusive abordagem direta/manter método vigente quando cabível), comparar adequação, esforço/custo, riscos, limites, entregáveis e provas; explicitar recomendação contextual e justificar. O humano escolhe antes da execução dependente, salvo escolha anterior ou delegação expressa registrada. Não fabricar alternativa se só uma for admissível; explicar exclusões. Passos internos já delegados não exigem microgate. Registrar escolha, revisão, adaptação e evidência no plano/tarefa existente; mudança material reabre apenas a decisão afetada. Não confundir escolha com autorização de contato, dados, custo, deploy ou homologação. [Contrato detalhado e piloto](../proposals/007-09A-ORBITA-SKILLS.md).

## Exemplos, conhecimento e evolução sem transferência de contexto

O núcleo descreve princípios, protocolos e exemplos independentes, fictícios e identificados como tais. Um projeto pode manter suas próprias evidências e materiais de portfólio fora do núcleo, sob responsabilidade e autorização próprias. Não importar casos, registros, aliases, decisões, dados ou referências de projetos reais para documentação, treinamento, exemplos, pilotos ou bases do ÓRBITA. A evolução pode ser motivada por experiência, mas a mudança incorporada ao núcleo deve ser formulada como regra autônoma, com validação independente por fixtures genéricas. Não apresentar cenário fictício como evidência real.

## Portfólio

Este repositório também existe para demonstrar uma competência que nem sempre aparece apenas no código final: **capacidade de organizar o processo de engenharia**.

Projetos mostram o que foi construído.

O Método ÓRBITA procura mostrar **como o trabalho é conduzido**.
