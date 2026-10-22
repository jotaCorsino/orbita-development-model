# Problema observado 002 — Deploy de preview sem recuperação do fluxo operacional existente

- **Categoria:** continuidade de contexto / handoff entre agentes / operação de preview / dependência entre repositórios.
- **Registro:** 22/10/2026.
- **Projeto da ocorrência:** [Novo Site Technolife](https://github.com/jotaCorsino/novo-site-technolife-1610).
- **Natureza:** **uma ocorrência identificada**, ainda não demonstrada como problema recorrente do método.
- **Impacto confirmado:** orientação operacional prematura, retrabalho de diagnóstico e perda de confiança do responsável. **Não houve deploy nem alteração dos arquivos públicos por essas instruções.**
- **Estado técnico da ocorrência:** diagnóstico parcial realizado e repasse ao agente responsável pelo Modo Revisão; procedimento efetivo de publicação **não executado nem validado** nesta ocorrência.
- **Estado metodológico:** análise e [proposta de melhoria](../proposals/002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md) **pendentes de avaliação e homologação humana**. Este relato, por si só, não muda o ÓRBITA.

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
7. **Resultado conhecido:** foram executadas inspeções e um `git fetch`; não foram executados o staging proposto, a sincronização, o merge, o deploy, a remoção de arquivos ou a publicação em produção.

**Fonte das evidências:** saídas do terminal e decisões informadas pelo responsável durante a conversa de operação. Nenhuma credencial, caminho absoluto de conta de hospedagem ou conteúdo privado de configuração é reproduzido aqui.

## 3. Diagnóstico e distinção entre fato e hipótese

### Confirmado

- Havia **dois contextos de trabalho relevantes**: o repositório do novo site e o projeto/módulo de presença e revisão.
- O preview **não era apenas uma cópia literal de `dist/`**: os HTMLs publicados incluíam recursos de revisão e um identificador de revisão.
- O repositório do site no servidor já existia e pôde receber a `main` atualizada por `git fetch`; criar outro clone não era necessário para diagnosticar o problema.
- O agente de planejamento **não consultou o procedimento do Modo Revisão antes de sugerir como publicar**.
- O responsável rejeitou a integração manual improvisada e solicitou continuidade com o agente do módulo.

### Ainda não verificado nesta ocorrência

- O mecanismo exato e a versão vigente do deploy/ciclo de revisão: exigem leitura e conferência pelo agente que mantém o módulo operacional.
- Se a documentação do projeto principal já contém todos os links de dependência necessários, ou se falta um índice de runbooks.
- Se a falha é recorrente em outros projetos ÓRBITA: este é **um caso**.

**Interpretação:** a dificuldade é principalmente de **aplicação e recuperação de contexto**. O ÓRBITA já determina análise, rastreabilidade, proteção da `main` e homologação, mas a prática revelou uma lacuna na **checagem de procedimentos operacionais externos ao repositório principal** antes de emitir comandos para um ambiente ativo.

## 4. Riscos evitados e impacto

- Sobrescrever HTMLs do preview com `dist/` sem considerar o Modo Revisão poderia suprimir sua integração.
- Reinjetar scripts manualmente, mesmo preservando os arquivos em `_review/`, não garante compatibilidade com o procedimento de publicação, metadados de versão ou futuras revisões.
- Propor um novo clone, atualização direta do checkout ou alterações públicas sem entender o fluxo anterior geraria divergência operacional e retrabalho.
- A validação humana impediu uma alteração não fundamentada: **não há dano operacional confirmado**.

## 5. Conduta correta para retomar o caso

1. Identificar quem mantém o Modo Revisão e recuperar sua documentação operacional existente; não inventar novo procedimento.
2. Confirmar origem, `main`/commit aprovado, pasta de staging, destino público, artefatos gerados/transformados, preservações e condições de rollback.
3. Obter primeiro um **plano ou dry-run somente leitura**, quando o procedimento canônico o oferecer; pedir autorização específica antes da aplicação.
4. Usar os comandos aprovados pelo **runbook do módulo** e verificar autenticação, revisão visual, páginas, mobile e ausência de regressões após a sincronização.
5. Registrar no projeto do site o commit implantado e o resultado; atualizar as referências cruzadas ao módulo quando necessário.

**Não interpretar este troubleshooting como autorização para executar comandos de deploy.**

## 6. Lição aprendida

**Antes de propor comandos para alterar um ambiente existente, o agente deve identificar o fluxo de operação já estabelecido e as dependências que podem estar fora do repositório do projeto principal.**

A ausência desse contexto não autoriza recriar o processo. A decisão adequada é **parar, inspecionar e encaminhar ao responsável pelo fluxo**. Isso preserva a orquestração humana e evita uma falsa sensação de segurança baseada apenas na versão aprovada do código.

## 7. Proposta de avaliação metodológica

Ver [Proposta 002 — Preflight operacional e dependências entre projetos](../proposals/002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md).

A proposta recomenda uma verificação proporcional de continuidade/dependências em operações sobre ambientes existentes, **sem criar automaticamente uma nova etapa obrigatória para cada tarefa de código**.

## 8. Referências

- [Método ÓRBITA — fluxo e gates](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md).
- [Método ÓRBITA — governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
- [TRB-001 — diagnóstico do ambiente antes de modificar a working copy](001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md).
- [Projeto Novo Site Technolife](https://github.com/jotaCorsino/novo-site-technolife-1610).
- [PR #22 — T.I. mobile homologada](https://github.com/jotaCorsino/novo-site-technolife-1610/pull/22).
- [PR #23 — planejamento tablets homologado](https://github.com/jotaCorsino/novo-site-technolife-1610/pull/23).

**Para futuras ocorrências:** acrescentar data, ambiente, evidência, causa confirmada e resultado, distinguindo falha de execução de deficiência metodológica demonstrada.
