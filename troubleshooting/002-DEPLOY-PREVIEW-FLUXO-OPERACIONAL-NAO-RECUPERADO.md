# Problema observado 002 — Deploy de preview sem recuperação do fluxo operacional existente

- **Categoria:** continuidade de contexto / handoff entre agentes / operação de preview / dependência entre repositórios.
- **Registro:** 22/10/2026.
- **Projeto da ocorrência:** [Novo Site Technolife](https://github.com/jotaCorsino/novo-site-technolife-1610).
- **Natureza:** **uma ocorrência identificada**, ainda não demonstrada como problema recorrente do método.
- **Impacto confirmado:** orientação operacional prematura, retrabalho de diagnóstico e perda de confiança do responsável. **Não houve deploy nem alteração dos arquivos públicos pelas instruções rejeitadas.**
- **Estado técnico da ocorrência:** a tentativa inicial foi interrompida sem deploy; em continuação supervisionada, o procedimento manual documentado foi recuperado e o preview atualizado para a revisão `e898876`, com backup, autenticação HTTP `401` e exportação JSON multipágina verificadas. Homologação funcional completa permanece separada.
- **Estado metodológico:** **refinamento metodológico homologado e incorporado à `main` pelo PR #7**.

## 1. Contexto e sintoma

Após a homologação das páginas desktop e mobile do Novo Site Technolife, o responsável solicitou **atualizar o preview já hospedado**, antes de continuar a adaptação para tablets. O preview existente tinha um **Modo Revisão** integrado (CSS, JS, autenticação e referências nos três HTMLs). O próprio sistema de revisão possuía um projeto/repositório operacional separado, `technolife-presenca-modelo-review`, e documentação de fluxo de publicação.

O agente de planejamento, porém, tratou inicialmente a tarefa como se precisasse desenhar um deploy novo. Sugeriu uma sequência de clone, backup e `rsync` **sem inspecionar primeiro a organização do servidor e sem recuperar o procedimento do projeto de revisão**. Após os diagnósticos fornecidos pelo responsável, identificou que o preview continha referências específicas ao Modo Revisão; mesmo assim, propôs **reinjetá-las nos HTMLs via `awk`** num staging improvisado, em vez de consultar o processo canônico de integração. O responsável rejeitou essa proposta e transferiu a operação ao agente adequado.

**Falha central:** recomendar execução antes de recuperar o fluxo operacional existente e as dependências entre projetos. Não foi demonstrado defeito no Git nem ausência de procedimento documentado.

## 2. Linha do tempo e fatos observados

1. **21/10/2026:** `main` do Novo Site Technolife continha as páginas mobile homologadas e o planejamento de tablets, com HEAD `e898876f6068f9a53b2ce0e391716516c81b508f` ([commit](https://github.com/jotaCorsino/novo-site-technolife-1610/commit/e898876f6068f9a53b2ce0e391716516c81b508f)).
2. O responsável pediu **comandos exatos para executar no terminal do servidor**. A primeira resposta incluiu comandos de atualização antes de inspecionar o ambiente. O responsável solicitou explicitamente diagnóstico prévio.
3. A inspeção somente leitura identificou o preview publicado em pasta separada da working copy Git, arquivos próprios `.htaccess` e `_review/`, e um clone Git existente do site no servidor. O clone estava na branch antiga `feat/SITE-003R-ti-desktop`, commit `a3dd59f`, com working tree limpa.
4. `git ls-remote` confirmou HEAD remoto `e898876`. Em seguida, **`git fetch origin main` foi executado com sucesso**: `origin/main` e `FETCH_HEAD` passaram a referenciar o mesmo commit, sem alterar a branch de trabalho ou a pasta pública.
5. O diagnóstico revelou os três HTMLs publicados com scripts e stylesheet do Modo Revisão e atributo `data-revision="a3dd59f"`; os arquivos públicos diferiam do `dist/` da branch antiga. Os recursos mobile novos existiam na `main`, mas não no diretório público.
6. Apesar dessa evidência de integração específica, foi proposta a geração de staging com injeção genérica das referências de revisão nos HTMLs e um `rsync --dry-run`, **sem recuperar o runbook original**. O responsável considerou a solução inadequada e solicitou um repasse ao agente especializado.
7. **Resultado da abordagem rejeitada:** executados apenas inspeções e um `git fetch`; o staging improvisado, a sincronização e a reinjeção propostas **não foram executados**.
8. **Continuação em 21/10/2026:** a documentação operacional do modelo de presença online foi localizada e lida. Ela distinguia um sincronizador automático **experimental/não homologado no cPanel** do procedimento manual efetivamente validado. O agente inicialmente inferiu, de modo prematuro, que o sincronizador automático já poderia ser usado; corrigiu a orientação após examinar o `README` do script.
9. Foi confirmada a referência homologada `e898876` em `origin/main`, mantendo o checkout ativo em `a3dd59f`. Usou-se `git archive` para extrair a pasta publicável para staging fora do webroot, seguida de simulação `rsync --dry-run`, backup integral validado e publicação manual sem `--delete`.
10. **Verificação após publicação:** tags CSS/JS do módulo de revisão instaladas nos três HTMLs com `data-revision="e898876"`, recursos mobile presentes e resposta anônima `HTTP 401` preservada. Um JSON exportado a partir de uma página reuniu três comentários artificiais de teste, um de cada página.
11. **Limites da evidência:** exportação JSON não prova por si só posicionamento visual dos pins, persistência pós-recarregamento ou funcionamento real de formulários. A auditoria de eventuais arquivos antigos no destino, a decisão de limpar o staging e o rollback entre commits distintos continuaram pendentes. Nenhuma publicação em produção foi executada.

**Fonte das evidências:** saídas do terminal e decisões informadas pelo responsável durante a conversa de operação. Nenhuma credencial, caminho absoluto de conta de hospedagem ou conteúdo privado de configuração é reproduzido aqui.

## 3. Diagnóstico e distinção entre fato e hipótese

### Confirmado

- Havia **dois contextos de trabalho relevantes**: o repositório do novo site e o projeto/módulo de presença e revisão.
- O preview **não era apenas uma cópia literal de `dist/`**: os HTMLs publicados incluíam recursos de revisão e um identificador de revisão.
- O repositório do site no servidor já existia e pôde receber a `main` atualizada por `git fetch`; criar outro clone não era necessário para diagnosticar o problema.
- O agente de planejamento **não consultou o procedimento do Modo Revisão antes de sugerir como publicar**. Na retomada, também foi necessário distinguir explicitamente automação experimental de método manual já validado.
- O responsável rejeitou a integração manual improvisada e solicitou continuidade com o agente do módulo.

### Confirmado na continuação

- A integração do Modo Revisão e o deploy **já estavam documentados** no repositório do modelo de presença online. O script automático existia, mas permanecia experimental; o fluxo manual era a referência operacional.
- O deploy manual de `e898876` foi executado com backup e verificações de segurança. A validação de um aspecto do modo de revisão (exportação consolidada JSON) foi realizada.
- `git archive` permitiu publicar o commit homologado sem fazer o checkout ativo coincidir com a revisão efetivamente instalada; por isso, `HEAD` isoladamente **não comprova a revisão do preview**.

### Ainda não verificado

- Se há falha sistemática de referências entre projetos, ou se neste caso bastou ao agente deixar de procurar a documentação operacional.
- Se o problema ocorreu em mais projetos: este relato ainda representa **uma ocorrência**.
- Auditoria de resíduos, rollback real entre commits distintos e homologação funcional completa do site.

**Interpretação:** a dificuldade é principalmente de **aplicação e recuperação de contexto**. O ÓRBITA já determina análise, rastreabilidade, proteção da `main` e homologação, mas a prática revelou uma lacuna na **checagem de procedimentos operacionais externos ao repositório principal** antes de emitir comandos para um ambiente ativo.

## 4. Riscos evitados e impacto

- Sobrescrever HTMLs do preview com `dist/` sem considerar o Modo Revisão poderia suprimir sua integração.
- Reinjetar scripts manualmente, mesmo preservando os arquivos em `_review/`, não garante compatibilidade com o procedimento de publicação, metadados de versão ou futuras revisões.
- Propor um novo clone, atualização direta do checkout ou alterações públicas sem entender o fluxo anterior geraria divergência operacional e retrabalho.
- A validação humana impediu uma alteração não fundamentada: **não há dano operacional confirmado**. A publicação posterior seguiu procedimento distinto e validado, com escopo limitado ao preview.

## 5. Conduta correta para retomar o caso

1. Identificar quem mantém o Modo Revisão e recuperar sua documentação operacional existente; não inventar novo procedimento.
2. Confirmar origem, `main`/commit aprovado, pasta de staging, destino público, artefatos gerados/transformados, preservações e condições de rollback.
3. Obter primeiro um **plano ou dry-run somente leitura**, quando o procedimento canônico o oferecer; pedir autorização específica antes da aplicação.
4. Usar os comandos aprovados pelo **runbook do módulo** e verificar autenticação, revisão visual, páginas, mobile e ausência de regressões após a sincronização.
5. Registrar no projeto do site o commit implantado e o resultado; atualizar as referências cruzadas ao módulo quando necessário.

**Não interpretar este troubleshooting como autorização para executar comandos de deploy.** A continuação bem-sucedida não transforma o sincronizador experimental em mecanismo homologado nem dispensa a revisão de cada runbook.

## 6. Lição aprendida

**Antes de propor comandos para alterar um ambiente existente, o agente deve identificar o fluxo de operação já estabelecido e as dependências que podem estar fora do repositório do projeto principal.**

A ausência desse contexto não autoriza recriar o processo. A decisão adequada é **parar, inspecionar e encaminhar ao responsável pelo fluxo**. Isso preserva a orquestração humana e evita uma falsa sensação de segurança baseada apenas na versão aprovada do código.

## 7. Resultado da avaliação metodológica

Ver [Proposta 002 — Preflight operacional e dependências entre projetos](../proposals/002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md).

A análise concluiu que a ocorrência combina **falha de aplicação do agente** com uma **lacuna operacional pequena e real** no método.

O ÓRBITA já exigia inspeção do estado atual, identificação de riscos e dependências, rastreabilidade e homologação. O agente falhou ao não aplicar adequadamente essas regras. Porém, o método não tornava suficientemente explícito que, em ambientes operacionais existentes, o agente deve recuperar também o **fluxo de operação vigente**, inclusive quando esse conhecimento estiver em outro projeto, módulo ou runbook.

O refinamento preparado na branch `docs/TRB-002-preflight-operacional` propõe:

- preflight operacional **condicional**, integrado à análise e sem criar nova etapa universal;
- distinção entre homologação do artefato e autorização para operar o ambiente;
- possibilidade de ambas estarem no mesmo gate quando a tarefa e o runbook já autorizarem explicitamente a implantação;
- registro da revisão ou artefato efetivamente implantado, sem inferi-lo apenas pelo `HEAD` da working copy;
- reconhecimento de dependências entre projetos sem romper a regra de um repositório canônico por software;
- parada em diagnóstico quando runbook, dependência ou autoridade relevante não puderem ser recuperados com segurança.

Foram conscientemente **descartados neste refinamento**:

- novo estado no fluxo;
- nova etapa obrigatória para todo projeto;
- checklist operacional universal;
- novo template de tarefa;
- exigência de duas aprovações humanas separadas em todo deploy.

Documentos normativos preparados:

- [docs/04-FLUXO-DE-DESENVOLVIMENTO.md](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md);
- [docs/05-GOVERNANCA-E-HOMOLOGACAO.md](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md);
- [docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md);
- [onboarding/CONTRATO-DE-TRABALHO.md](../onboarding/CONTRATO-DE-TRABALHO.md).

**Estado atual:** refinamento **APROVADO e INCORPORADO** à `main` pelo PR #7. TRB-002 encerrado.

## 8. Referências

- [Método ÓRBITA — fluxo e gates](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md).
- [Método ÓRBITA — governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
- [TRB-001 — diagnóstico do ambiente antes de modificar a working copy](001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md).
- [Projeto Novo Site Technolife](https://github.com/jotaCorsino/novo-site-technolife-1610).
- [PR #22 — T.I. mobile homologada](https://github.com/jotaCorsino/novo-site-technolife-1610/pull/22).
- [PR #23 — planejamento tablets homologado](https://github.com/jotaCorsino/novo-site-technolife-1610/pull/23).

**Para futuras ocorrências:** acrescentar data, ambiente, evidência, causa confirmada e resultado, distinguindo falha de execução de deficiência metodológica demonstrada.
