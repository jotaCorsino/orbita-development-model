# Proposta 002 — Preflight operacional e dependências entre projetos

- **Tipo:** refinamento futuro / continuidade de contexto / governança de operação.
- **Registrada em:** 22/10/2026.
- **Origem:** [TRB-002 — Deploy do preview sem recuperação do fluxo existente](../troubleshooting/002-DEPLOY-PREVIEW-FLUXO-OPERACIONAL-NAO-RECUPERADO.md), observado no Novo Site Technolife.
- **Estado:** **PROPOSTA — NÃO HOMOLOGADA**. Este documento não altera o contrato, o ciclo, templates ou gates oficiais do Método ÓRBITA.
- **Prioridade sugerida:** avaliar como refinamento pequeno e **condicional**, não como nova burocracia transversal.

## 1. Problema que motiva a proposta

A `main` do projeto pode estar atualizada e homologada, mas isso **não demonstra que o agente conhece como publicar o resultado** num ambiente já configurado.

Na ocorrência do Novo Site Technolife, o agente de planejamento consultou corretamente o repositório principal, mas inicialmente ignorou a dependência operacional com o **Modo Revisão** mantido em outro contexto. Sugeriu comandos de deploy sem consultar o runbook original; mesmo depois de identificar scripts injetados nos HTMLs publicados, propôs recriar o mecanismo manualmente. O responsável bloqueou a abordagem.

Essa observação **não comprova que o método ÓRBITA esteja conceitualmente errado**. O método já exige análise, delimitação de escopo, evidência e homologação. O que pode ser aperfeiçoado é um **gatilho explícito para recuperação de runbooks e dependências** antes de tocar um ambiente ativo.

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

## 6. Onde avaliar eventual incorporação

**Somente após aprovação humana** e confirmação de utilidade em aplicação real, avaliar alterações pequenas e coerentes em:

- [docs/04-FLUXO-DE-DESENVOLVIMENTO.md](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md): ressalva condicional na análise/etapa documentação-release;
- [docs/05-GOVERNANCA-E-HOMOLOGACAO.md](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md): autorização separada para operação em ambiente ativo e preservação das integrações preexistentes;
- [docs/08-APLICACAO-E-EVOLUCAO.md](../docs/08-APLICACAO-E-EVOLUCAO.md): tratamento proporcional a risco, sem checklist universal;
- templates operacionais **apenas se** houver lacuna demonstrada, evitando conteúdo duplicado em todas as tarefas.

O [TRB-001](../troubleshooting/001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md) já estabelece diagnóstico do ambiente antes de reorganizar working copy durante bootstrap. Essa proposta é uma **extensão para operação/deploy**, não uma substituição daquele aprendizado.

## 7. Critérios de avaliação e aceite

1. A distinção entre **erro de execução do agente** e **lacuna metodológica real** fica documentada.
2. A proposta impede recomendação de comandos destrutivos ou divergentes antes de recuperar o procedimento canônico.
3. Em dois projetos com operações diferentes, o preflight identifica dependências sem atrasar tarefas comuns ou criar relatórios desnecessários.
4. Os documentos normativos eventualmente alterados não criam conflitos com a regra de repositório canônico, responsabilidades humanas ou `main` homologada.
5. Uma **homologação humana específica** aprova ou rejeita o texto normativo proposto; até então esta proposta permanece informativa.

## 8. Decisão pendente

**Não aprovada nem incorporada.** Solicitar avaliação humana sobre:

- incluir explicitamente o preflight em tarefas operacionais;
- manter a proposta apenas como lição de uso, caso os princípios atuais já sejam suficientes;
- testar em outro projeto antes de promover para norma.

A inclusão deste registro em `proposals/` **não concede permissão de deploy ou modificação dos procedimentos existentes**.
