# Proposta 002 — Preflight operacional e dependências entre projetos

- **Tipo:** refinamento futuro / continuidade de contexto / governança de operação.
- **Registrada em:** 22/10/2026.
- **Origem:** [TRB-002 — Deploy do preview sem recuperação do fluxo existente](../troubleshooting/002-DEPLOY-PREVIEW-FLUXO-OPERACIONAL-NAO-RECUPERADO.md), observado no Novo Site Technolife.
- **Estado:** refinamento metodológico preparado na branch `docs/TRB-002-preflight-operacional` e **aguardando homologação humana**. Nenhuma alteração normativa foi incorporada à `main` até o momento.
- **Prioridade sugerida:** avaliar como refinamento pequeno e **condicional**, não como nova burocracia transversal.

## 1. Problema que motiva a proposta

A `main` do projeto pode estar atualizada e homologada, mas isso **não demonstra que o agente conhece como publicar o resultado** num ambiente já configurado.

Na ocorrência do Novo Site Technolife, o agente de planejamento consultou corretamente o repositório principal, mas inicialmente ignorou a dependência operacional com o **Modo Revisão** mantido em outro contexto. Sugeriu comandos de deploy sem consultar o runbook original; mesmo depois de identificar scripts injetados nos HTMLs publicados, propôs recriar o mecanismo manualmente. O responsável bloqueou a abordagem.

Essa observação **não comprova que o método ÓRBITA esteja conceitualmente errado**. O método já exige análise, delimitação de escopo, evidência e homologação. O que pode ser aperfeiçoado é um **gatilho explícito para recuperação de runbooks e dependências** antes de tocar um ambiente ativo.

### Desfecho que esclareceu a necessidade

Na continuação da operação, a equipe encontrou dois caminhos documentados: um sincronizador **experimental e não homologado no servidor** e o fluxo manual já testado. A identificação de arquivo/script sem ler seu status causou uma segunda orientação prematura, corrigida antes da execução. O fluxo manual publicou o commit `e898876` com backup, verificação HTTP `401` e exportação de comentários multipágina.

A versão instalada foi extraída por `git archive` sem mover o `HEAD` do checkout ativo. Portanto, além de recuperar o runbook, o preflight deve distinguir **referência de origem**, **commit realmente publicado** e **estado do checkout**. O encerramento deve separar **publicação técnica**, **verificações funcionais parciais** e **homologação completa**, incluindo pendências de resíduos e rollback.

## 2. Regra mínima candidata

> **Em tarefas que modificam um ambiente operacional preexistente**, antes de fornecer comandos de execução, o agente identifica qual procedimento canônico mantém esse ambiente, quais projetos/módulos externos participam do processo, o estado real observado e quem autoriza a operação. Na falta dessas informações, realiza somente diagnóstico não destrutivo e encaminha ao responsável adequado. Não substitui silenciosamente um fluxo já implantado por outro criado na conversa.

### Ativação proporcional

Aplicar a verificação quando houver **deploy, migração, atualização de preview, sincronização de servidores, alteração de ambiente, CMS, autenticação, integração ou infraestrutura compartilhada**.

**Não** aplicar como checklist adicional obrigatório para toda mudança de CSS, texto ou tarefa local isolada. O objetivo é evitar risco em um handoff operacional, não aumentar a formalidade de cada PR.

## 3. Preflight objetivo (cinco perguntas)

1. **Origem e estado aprovado:** qual repositório/branch/commit tem o artefato correto? Essa versão foi homologada para o escopo desejado?
2. **Destino real:** o que já existe no ambiente, em quais pastas e sob quais proteções? Quais arquivos são **gerados ou transformados** no deploy e não devem ser tratados como cópia literal?
3. **Dependências e ownership:** existe ferramenta, módulo, repositório auxiliar ou agente responsável pelo deploy/revisão/integração? Onde está o **runbook operacional atual**?
4. **Procedimento existente:** quais passos do runbook podem ser realizados sem escrita (`status`, `diff`, `dry-run`) e quais exigem autorização, backup, rollback ou janela operacional?
5. **Gate de saída:** quais verificações pós-operação demonstram que o ambiente e suas integrações continuam funcionando, e como registrar o commit efetivamente publicado?

**Saída sugerida:** resposta curta com **fluxo identificado**, **dependências**, **evidências verificadas**, **itens não confirmados** e **comando autorizado ou bloqueio**. Não criar documentos extensos ou tarefas extras quando o fluxo já for claro.

## 4. Handoff entre repositórios, sem violar a identidade do projeto

O princípio de um **repositório canônico por software** continua válido. Isso não impede que um site consuma **módulos e processos auxiliares operados por outros projetos**.

Nesses casos, uma referência breve, proporcional ao risco, deve apontar:

- módulo/projeto de que depende;
- responsabilidade pelo ciclo de integração/preview;
- localização do procedimento oficial (link, não cópia divergente);
- restrições operacionais relevantes;
- evidência/versão implantada, quando aplicável.

A proposta **não** exige mesclar repositórios, expor caminhos internos, copiar credenciais ou duplicar a documentação do módulo no site consumidor.

## 5. Exemplos de resultado esperado

### Fluxo já conhecido

> O preview depende do Modo Revisão, com runbook próprio. O repositório oficial está atualizado, mas o HTML publicado inclui recursos adicionais. Vou consultar o procedimento existente e apresentar primeiro o plano/dry-run previsto por ele. Não farei `rsync` direto nem reinjetarei scripts por conta própria.

### Fluxo indisponível ao agente

> Confirmei origem e estado do servidor, mas não tenho acesso ao procedimento do módulo responsável pelo deploy. Não vou inventar comandos de publicação. Encaminho ao agente responsável com o diagnóstico obtido, sem modificar a área pública.

### Fluxo sem dependências especiais

> Origem, destino e runbook validados; a operação segue o procedimento documentado e autorizado, com validações de pós-execução e rollback definidos.

## 6. Incorporação metodológica preparada

A avaliação foi realizada e resultou em um refinamento menor do que a proposta inicial, preservando a proporcionalidade do método.

Foram preparados ajustes em:

- [docs/04-FLUXO-DE-DESENVOLVIMENTO.md](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md): preflight condicional incorporado à fase de análise para tarefas operacionais, sem nova etapa universal;
- [docs/05-GOVERNANCA-E-HOMOLOGACAO.md](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md): separação entre homologação do artefato e autorização operacional, permitindo que ambas sejam cobertas pelo mesmo gate quando explicitamente autorizado;
- [docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md): dependências entre projetos, módulos e runbooks sem romper a identidade canônica de cada software;
- [onboarding/CONTRATO-DE-TRABALHO.md](../onboarding/CONTRATO-DE-TRABALHO.md): obrigação de recuperar o fluxo operacional vigente antes de fornecer comandos de escrita em ambientes existentes.

Após revisão cruzada, **não** foram considerados necessários neste momento:

- alteração de [docs/08-APLICACAO-E-EVOLUCAO.md](../docs/08-APLICACAO-E-EVOLUCAO.md) especificamente para este caso;
- novo template operacional;
- novo estado;
- checklist obrigatório para tarefas comuns;
- duas aprovações humanas formais para qualquer implantação.

O [TRB-001](../troubleshooting/001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md) continua tratando restrições de ambiente durante bootstrap. Esta proposta trata uma situação diferente: **continuidade e governança antes de operar um ambiente já existente**.

## 7. Critérios de avaliação e aceite

Para homologar este **refinamento mínimo**:

1. a distinção entre **erro de execução do agente** e **lacuna metodológica real** fica documentada;
2. o texto impede recomendação de comandos divergentes antes de recuperar o procedimento canônico;
3. os documentos normativos alterados não criam conflitos com a regra de repositório canônico, responsabilidades humanas ou `main` homologada;
4. o preflight permanece condicional, sem criar etapa, estado, template ou checklist universal;
5. uma **homologação humana específica** aprova ou rejeita o texto normativo proposto.

### Validação posterior

Como a origem ainda é **uma ocorrência documentada**, a utilidade do refinamento deve continuar sendo observada em outros projetos operacionais.

Um sinal de maturação será confirmar, em pelo menos outro contexto de operação, que o preflight identifica dependências relevantes sem atrasar tarefas comuns ou gerar documentação desnecessária. Essa validação futura pode justificar novo ajuste, simplificação ou até reversão parcial da regra.

Ela **não é apresentada como evidência já cumprida** neste PR.

## 8. Decisão pendente

O refinamento foi **preparado e revisado**, mas ainda depende de homologação humana antes de qualquer merge na `main`.

A proposta final é incorporar o preflight como regra **condicional e proporcional**, sem transformar operações comuns em um processo adicional.

A evidência atual vem de uma ocorrência documentada. Por isso, a mudança foi deliberadamente mantida pequena, baseada em princípios já existentes e sem criar estrutura operacional extensa que ainda não foi validada em outros projetos.

A inclusão deste registro em `proposals/` **não concede permissão de deploy ou modificação dos procedimentos existentes**.
