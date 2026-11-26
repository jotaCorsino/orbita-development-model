# ORB-EVO-001 — 08: Documentação e nomenclatura

**Data:** 26/11/2026. **Estado:** refinamento candidato homologado, integrado pela PR #41 e verificado na main; ainda não vigente como norma geral. **Baseline:** `da3f4b94abb6811f2041c61412ea414354f29cee`, PRs #39/#40 integradas; etapas 01–07 encerradas. **Autorização:** etapa 08 exclusivamente, no mesmo chat da iniciativa. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Fundamento e decisão

Formalizar NOM-001 (ID candidato) conforme diretriz humana já aprovada: todo nome criado por agente deve ser legível, simples, descritivo e consistente, preservando identidade, numeração e rastreabilidade quando necessárias. Não reabrir essa decisão.

A [matriz metodológica](007-01-AUDITORIA-INTEGRAL.md) e a [síntese independente de requisitos e riscos](007-02-AUDITORIA-HUB-E-PROJETOS.md) orientam este refinamento. Os identificadores lógicos D e E preservam a rastreabilidade do método; não representam fontes externas, projetos ou provas empíricas.

Preservar [PROP-001](001-README-ACOMPANHAMENTO-VISUAL.md), [PROP-003](003-CONSOLIDACAO-DOCUMENTAL-SEM-PERDA.md), [PROP-005](005-BACKLOG-DE-EVOLUCAO.md), [PROP-006](006-KNOWLEDGE-BASE-DE-CONHECIMENTO-OPERACIONAL.md), [TRB-004](../troubleshooting/004-ENCERRAMENTO-SEM-SINCRONIZACAO-DOCUMENTAL.md), [Git e GitHub](../docs/06-GIT-E-GITHUB.md), [IA no método](../docs/07-IA-NO-METODO.md), [aplicação e evolução](../docs/08-APLICACAO-E-EVOLUCAO.md), [identidade](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md), [inicialização](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md) e [contrato](../onboarding/CONTRATO-DE-TRABALHO.md). Usar arquitetura 03, limpeza 04, continuidade 05, configuração 06 e Knowledge 07 já homologados como candidatos; não torná-los normas antecipadamente.

| Alternativa | Avaliação |
| --- | --- |
| Padronizar tudo por IDs, estrutura rígida e documentação completa em cada superfície | Rastreio aparente, baixa legibilidade, manutenção duplicada |
| Usar apenas títulos livres e eliminar registros antigos | Leitura rápida, mas risco de colisão, ruptura de contratos e perda semântica |
| Nomes humanos + IDs quando necessários + fontes canônicas por assunto e derivadas compactas | Recomendada; preserva identidade, informação e custo proporcional |

**Princípio:** um nome ajuda a identificar, uma fonte competente sustenta a informação e uma referência conecta as duas. Organização não é contagem de arquivos, redução de texto ou padronização estética isolada.

## 2. NOM-001 — regra candidata de nomenclatura

Toda nomenclatura criada pelo agente deve permitir que humano ou agente reconheça finalidade e contexto sem decifrar códigos desnecessários. Manter ID estável quando necessário a rastreio, unicidade, contrato ou sequência; o ID complementa o título, não o substitui. Preferir o vocabulário real do domínio e idioma já adotado no projeto. Usar a menor descrição que distingue inequivocamente o objeto. Não criar número apenas para preencher padrão. Não incluir segredo, dado pessoal ou cliente desnecessário no nome.

Distinguir:
- nome humano: título, rótulo, descrição de tarefa;
- identificador lógico: ID persistente de tarefa, requisito, proposta, entrada;
- nome técnico: slug, caminho, símbolo, ref, identificador de API/banco;
- referência de versão: SHA, tag, revisão, hash ou timestamp quando necessário.

Nome técnico não precisa reproduzir integralmente o nome humano; a associação precisa ser inequívoca. Não substituir IDs técnicos por rótulos de apresentação. Preservar convenções de linguagem, framework, filesystem, automação, nomes públicos e contratos externos. NOM-001 aplica-se a novos nomes e mudanças autorizadas; não é mandato de renomeação retroativa.

### 2.1 Convenções por categoria

Exemplos ilustrativos, não renomeações aprovadas. Formato local existente prevalece quando necessário à compatibilidade; novos nomes devem manter sentido humano.

| Categoria | Padrão recomendado / exemplo | Evitar |
| --- | --- | --- |
| Projeto/repositório | Catálogo de serviços / catalogo-de-servicos | Nome genérico ou sigla isolada |
| Diretório de documentação | docs/operacao/ | pastas artificiais com códigos de todas as fases |
| Arquivo documental | requisitos-funcionais.md; 03-requisitos-funcionais.md se houver ordem relevante | doc-final-v2-agora.md |
| Arquivo de contrato | README.md, AGENTS.md, package.json conforme tecnologia | renomear contratos convencionais |
| Iniciativa | ORB-EVO-001 — Evolução do ÓRBITA | ORB-EVO-001 sem descrição |
| Etapa/subetapa | 08 — Documentação e nomenclatura; 08.2 — Convenções de nomes | 08.2.3.4 sem significado |
| Tarefa/requisito | CAT-014 — Filtrar serviços por categoria | TASK-014 sem título |
| Chat | ORB-EVO-001 — Evolução do ÓRBITA (continuação 2, se necessária) | chat novo por subetapa |
| Branch Git | feat/filtro-de-categorias; fix/validacao-de-acesso; docs/revisao-do-manual; incluir ID se necessário | feat/T014-G3-R4-P7 sem descrição |
| Commit | fix: corrige filtro de categorias | update; fix final; código isolado |
| Pull Request | CAT-014 — Filtro de categorias | PR — G2-R3 sem objeto |
| Script | verificar-integridade.sh; exportar-relatorio.py | script3.sh; qa-final-v7.py |
| Artefato/teste/evidência | relatorio-qa-filtro-categorias; teste-filtro-sem-resultados | resultado-final-certo |
| Backup | catalogo-pre-migracao-20261126T140000Z.sqlite | backup-final-novo.sqlite |
| Ambiente | catalogo-homologacao; catalogo-producao | ambiente-2 sem identificação |
| Release/pacote | catalogo-1.2.0.zip, tag v1.2.0 conforme projeto | versao-final.zip sem versão recuperável |
| Componente de UI | FiltroCategorias ou CategoryFilter, conforme idioma e framework | CompX sem domínio |
| Função | validarAcesso ou validateAccess conforme convenção | fn1; processarTudo sem finalidade |
| Variável | quantidadeDeItens ou item_count | x1 para valor de domínio duradouro |
| Símbolo técnico e API | manter user_id, HTTP status, rota pública, chave de configuração e ID de banco | traduzir/renomear por estética rompendo consumidor |
| Knowledge/TRB/PROP | KN-012 — Limitação do ambiente de teste; arquivo com ID e descrição | sigla sem título; reaproveitar ID |
| Skills/Tools (futuros) | nome da técnica/ferramenta + finalidade, ID se necessário | nome que simula autoridade ou omite função |

Para novos slugs, preferir minúsculas e hífens quando compatíveis; respeitar case, extensão, nomes reservados, caracteres permitidos, limite de caminho e idioma técnico da tecnologia. Nome de arquivo humano pode ter acentos/espaços em contexto apropriado; não impor convenção que quebre consumidores. Em código, seguir convenção já adotada (camelCase, PascalCase, snake_case ou outra), termos de domínio e idioma. Variáveis matemáticas locais, índices de laço e siglas consagradas podem ser curtas; não expandir nomes cujo significado é inequívoco. Prefixo de commit como feat/fix/docs/chore é compatível com docs 06, não impor ferramenta de lint ou Conventional Commits onde não adotado.

IDs, ordem, versão e prioridade são dimensões independentes. Para coleções numeradas como PROP/TRB, preservar atribuição contra main e verificação de colisões descritas em docs 08, [índice de propostas](README.md) e [troubleshooting](../troubleshooting/README.md). Em trabalho paralelo usar identificador temporário inequívoco com descrição, data/contexto quando necessário, e resolver colisões no gate antes de homologação e integração. Não renumerar histórico para torná-lo sequencial. Não eliminar IDs técnicos, hashes, tags ou nomenclatura obrigatória de fornecedor. Em UI/documentos, mostrar rótulo humano junto ao ID quando útil.

### 2.2 Renomeações e migrações

Aplicar nomenclatura aos novos artefatos; avaliar legado por necessidade real. Se renomeação for autorizada, identificar objeto canônico, nomes/refs antigos, consumidores, links, âncoras, importações, configuração, automação, permissões, ambientes, integração e dependências. Conferir colisões, case-sensitive/case-insensitive, histórico e compatibilidade. Escolher menor mudança: rótulo humano sem mudar identificador técnico quando suficiente; alias/redirecionamento/migração apenas quando apropriado e aprovado. Preservar ID e trilha origem→destino; validar links/referências e funcionamento afetado. Não reescrever histórico Git, apagar versões, renomear banco/API, caminho de servidor, tag, branch remota ou artefato de recuperação por estética. Se depender de outro responsável, seguir autoridade da etapa 03. Integração de código/ambiente exige gate correspondente.

## 3. Mapa de fontes e derivadas

Canonicidade é por assunto e escopo; não existe um documento soberano para todos os fatos. A arquitetura 03 distingue autoridade normativa, trabalho ativo, estado integrado e evidência atual.

| Informação | Fonte preferencial/canônica | Derivada/consulta rápida |
| --- | --- | --- |
| Identidade, descrição e objetivo | README ou especificação do produto indicada | Entrada de IA, catálogo, apresentação |
| Requisitos, escopo e critérios | Especificação/tarefa autorizada e decisões | Roadmap, README e prompt |
| Arquitetura/contrato | Documento de arquitetura/decisão competente | README, AGENTS por referência |
| Regras do método | Documentação normativa e contrato adotados | Onboarding, checklist, exemplos |
| Planejamento | Roadmap/plano da iniciativa | Painel README, handoff |
| Backlog | Seção padrão do README ou mecanismo equivalente aprovado | Link/índice em ferramenta quando pertinente |
| Estado e evidência de tarefa | Registro da tarefa, PR, testes, decisão humana e linha integrada pertinente | Roadmap, README, painel |
| Release e implantação | Registro de release, artefato e destino observados | Resumo de versão/ambiente |
| Operação | Runbook e configuração autorizada do ambiente | Prompt/preflight por referência |
| Ocorrência | Troubleshooting e evidência | Índice e Knowledge (conclusão distinta) |
| Aprendizado | Entrada Knowledge e prova | Índice Knowledge |
| Proposta | Registro de proposta, aceite e integração | Índice, roadmap; não norma por si só |
| Configuração IA | AGENTS/equivalente versionado e fontes adotadas; configuração efetiva verificada separadamente | Instruções compactas de ambiente |
| Histórico | Commits, PRs, registros datados e decisões substituídas | Referência a marco; não status atual |

A fonte é a já competente no projeto, não obrigatoriamente um arquivo novo para cada linha. Um README pode ser canônico para identidade e backlog, derivado para status. Roadmap pode ser canônico para planejamento e derivado para evidência de homologação. Não usar “main” como sinônimo universal de estado de produção ou de trabalho ativo. Quando iniciativa estiver em revisão, identificar base integrada e ref aplicável. Um documento histórico conserva o que se sabia naquele momento; só é resíduo de status quando se apresenta como atual contradizendo prova posterior.

## 4. README A/B e organização proporcional

Os modelos ilustrativos A/B são perfis de apresentação, não novos estados, fases, arquivos obrigatórios ou regras organizacionais universais. A PROP-001 já recomenda painel próximo ao início quando há fases/gates, com status textual e sem progresso artificial. Preservar essa decisão.

| Perfil | Quando usar | Visão rápida recomendada |
| --- | --- | --- |
| A — Construção/primeira entrega | Fundação, desenvolvimento inicial, V1 ainda não homologada para o escopo | Objetivo, fase atual, macroetapas, próximo gate, links para planejamento e evidências |
| B — Produto em evolução | Existe baseline homologada; novas iniciativas, manutenção, correções e releases | Versão integrada/release identificada; implantação apenas se comprovada; iniciativas ativas, próxima pendência e links |
| Simples | Biblioteca pequena, script ou projeto sem acompanhamento por fases | Descrição, uso, regras/referências necessárias; adaptar ou omitir painel |

Não inferir que uma aplicação em evolução precisa estar publicada; baseline homologada, release e instalação são dimensões distintas. Transição A→B após comprovação de baseline e decisão de organização pertinente; preservar histórico em roadmap/registro da primeira entrega. Pode haver iniciativas A em novo módulo enquanto produto usa visão B. Não converter toda manutenção em projeto de fundação.

### 4.1 Esqueleto A (ilustrativo)

```markdown
# [Nome do projeto]
[Descrição objetiva.]

## Acompanhamento
Fase atual: [ID e nome — estado textual]
| Etapa | Estado | Próximo gate |
| --- | --- | --- |
| [macroetapa] | [estado real] | [se pertinente] |
[Planejamento detalhado e referência ativa]

## Objetivo e escopo
[Resumo ou fonte competente.]

## Uso / arquitetura / segurança
[Somente informações necessárias e referências.]

## Backlog
[Necessidades futuras ou vazio.]

## Knowledge e documentação
[Índice e links.]
```

### 4.2 Esqueleto B (ilustrativo)

```markdown
# [Nome do produto]
[Finalidade e público.]

## Situação atual
Baseline homologada: [referência e escopo]
Release: [versão comprovada ou não publicada]
Ambiente: [quando relevante e permitido; estado comprovado]

## Iniciativas em andamento
| Iniciativa | Estado | Próximo gate |
| --- | --- | --- |
| [ID — nome] | [estado real] | [referência] |

## Uso e manutenção
[Referências canônicas de instalação/uso/runbook.]

## Backlog
[Necessidades futuras, não duplicar execução.]

## Knowledge e documentação
[Índice, roadmap e histórico de releases.]
```

Os exemplos não substituem o [README inicial vigente](../templates/README-INICIAL-TEMPLATE.md), nem autorizam copiar placeholders em projeto real. A etapa 10 deverá preservar requisitos da fundação e oferecer adaptação A/B ou simples no template existente, não criar três arquivos obrigatórios. Manter público e conteúdo operacional restrito separados quando necessário. Para o próprio método, README público de referência não precisa mostrar painel interno detalhado; o PROP-007/ROADMAP mantêm acompanhamento da iniciativa. Não impor painel de consumidor a repositório público produtor.

### 4.3 Status, progresso e backlog

Preservar os seis estados oficiais e Pausado como condição excepcional. Indicadores visuais sempre acompanhados de texto; não usar verde antes de homologação para escopo definido. Indicar ressalva, integração pendente ou publicação não realizada quando pertinentes. A etapa homologada mas não integrada não autoriza dizer encerrada: aplicar verificação final. Distinguir percentuais de contagem (etapas homologadas/total com denominador explícito) de estimativa de esforço ou maturidade; não criar percentual artificial. Um roadmap pode manter marcos anteriores datados sem recontá-los como estado atual.

Backlog permanece captura, não autorização. Se volume justificar, manter índice/resumo com referência ao mecanismo de trabalho existente e preservar IDs/origem; não replicar texto ou estados de execução em duas fontes. Item selecionado aponta à iniciativa/tarefa; concluído/descartado requer decisão/evidência correspondente, não desaparece por limpeza arbitrária. Manter seção padrão e opção de histórico conforme PROP-005; não criar issue para toda ideia nem backlog duplicado de plano já registrado.

## 5. Consolidação documental sem perda

Aplicar PROP-003 e limpeza 04. Objetivo é remover sobreposição desnecessária sem perder semântica, decisões, condições, evidências ou histórico relevante.

1. Delimitar escopo e fontes aplicáveis, incluindo branch/PR ativa e material local relevante. Não tomar main como inventário integral.
2. Identificar conteúdo exclusivo, repetido, contraditório, substituído por decisão explícita, histórico e ainda em elaboração. Dúvida favorece preservação.
3. Definir fonte canônica por assunto e destino de cada informação material. Preferir referências em derivadas. Redundância pedagógica ou salvaguarda essencial em prompt curto pode permanecer quando necessária.
4. Demonstrar cobertura proporcional: diff e links em mudança curta; lista origem→destino ou matriz semântica para consolidação extensa/alto impacto. Contagem de arquivos e links resolvidos não comprovam significado.
5. Verificar regras, critérios, exceções, decisões, refs e condições preservadas. Se houver remoção material, explicitar onde ficou preservada, qual decisão substituiu ou autorização de exclusão. Mudança de sentido retorna ao gate normal; não rotular como editorial.
6. Reconciliar superfícies derivadas e verificar estado integrado; manter registro histórico datado. Não apagar informações por terem sido escritas antes de uma mudança, nem reabrir decisão encerrada.

Exemplo de evidência proporcional (sintético):

| Origem | Informação | Destino/tratamento | Evidência esperada |
| --- | --- | --- | --- |
| Guia de instalação + onboarding | Ordem e exceção de bootstrap | Docs 11 e referência curta no onboarding | Comparação de passos e exceções |
| Painel antigo | Status atual substituído | README atualizado, histórico datado no PR | Gate/merge e links |
| Especificação incompleta | Requisito ainda em discussão | Preservar na ref ativa indicada | ID e conteúdo único preservado |

Não criar matriz obrigatória para toda alteração, novo sistema de documentação ou duplicação de registros. Um registro histórico de proposta deve distinguir a situação inicial da atual; se o título ou introdução sugerir ação ainda pendente apesar de merge, corrigir apresentação com referência ao resultado, preservando sequência histórica.

## 6. Verificação proporcional e tratamento de links

Estender [verificação final existente](../templates/VERIFICACAO-FINAL-TEMPLATE.md), não criar gate separado.

| Tipo de mudança | Antes de integrar | Após integrar/aplicar |
| --- | --- | --- |
| Correção textual curta | Sentido e referência diretamente afetada | Conferir fonte final; sem varredura ampla |
| Estado/gate | Fonte primária, escopo e revisão; localizar resumos | Confirmar merge/estado real e derivadas pertinentes |
| Consolidação estrutural | Cobertura semântica, links, IDs, regras e exclusões autorizadas | Revalidar destinos, referências, conteúdo e histórico preservado |
| Renomeação técnica | Mapa de dependências, colisões, consumidores e migração | Links/importações/build/execução conforme risco e destino |
| Operação sem PR | Runbook, autorização, origem/destino, evidência | Observar destino e reconciliar registros; não inventar merge |

A busca deve focar identificadores, títulos, status ou caminhos afetados. Não exigir scan completo para tarefa pequena. Distinguir link relativo do documento fonte de link destinado ao arquivo gerado por template: D-28 identifica knowledge/README.md no README inicial como relativo à raiz futura. Validar no destino gerado quando aplicável; não “corrigir” para ../knowledge apenas porque template vive em templates/. Validar âncora, case e link externo quando pertinentes; declarar o que foi efetivamente verificado. URL acessível não comprova conteúdo correto ou autorização. Se destino restrito não puder ser consultado, registrar limite, não publicar link privado em contexto público.

Quando divergência pós-merge for puramente editorial e estiver coberta pelo escopo, corrigir no menor fluxo autorizado (PR pequeno se necessário); mudança de significado, regra ou risco requer nova revisão/homologação. Não abrir PR de encerramento automaticamente se a mudança principal já contém estado coerente e prova suficiente. Não criar ciclo infinito para registrar o próprio SHA de fechamento.

## 7. Ajustes candidatos para etapa 10

| Diagnóstico | Fonte vigente / materialização futura |
| --- | --- |
| D-02 | Docs 11 como sequência canônica; docs 04/08/10, onboarding e README remetem a ela, preservando passos/exceções únicos |
| D-09 | Mapa de fontes/derivadas, verificação final pré/pós e caso sem PR |
| D-10 | Onboarding §4 explicita backlog, Knowledge e AGENTS já exigidos |
| D-11 | [TASK-template](../templates/TASK-TEMPLATE.md): ID e título humano explícitos, autorização, base/ref, critérios verificáveis; sem nova tarefa por ritual |
| D-12 | AGENTS e prompt de implementação conforme 06/07; recuperar Knowledge, runbook e critérios |
| D-14 | Contrato §9: trocar ambiguidade “mensagem final do chat” por “trecho final de cada resposta que atribua providência humana”; manter COM-001 integral, inclusive omissão sem ação |
| D-16 | README/backlog e vínculo com execução sem replicar estados |
| D-17 | Corrigir estado atual de PROP-001 §8 com merge comprovado #3, preservando texto datado; demais status residuais somente após confirmação |
| D-18 | Rotular registros históricos, sem apagar fases preparadas/aprovadas/encerradas |
| D-19 | Índices/refs distinguir trabalho ativo, histórico e pendente; exclusão/fechamento somente pela autoridade e protocolo 04 |
| D-22 | AGENTS raiz candidato conforme 06; preservar natureza pública do README, avaliar proteção e release em 12 |
| D-23 | Fonte normativa única NOM-001; referências em docs 06/10 e templates aplicáveis; Skills/Tools observam nomes humanos |
| D-28 | Validar links por contexto de uso; preservar link gerador correto |

Também detalhar [homologação](../templates/HOMOLOGACAO-TEMPLATE.md) por dimensão, com origem/versão/destino e autorização operacional somente quando aplicáveis (D-13, 03/06/09). Fonte normativa de NOM-001 deverá ser localizada na estrutura existente de docs 06/08/10 ou seção própria aprovada na integração, evitando três regras concorrentes. A decisão de localização exata fica para 10. Não alterar arquivos normativos nesta etapa.

Consulta focal desta etapa: a baseline continha os templates README/TASK/HOMOLOGACAO/VERIFICACAO-FINAL, docs 06/08/10, contrato, PROP-001/003/005, índices de propostas e troubleshooting. A leitura confirmou que TASK não explicita ID no título, README já orienta remoção de placeholders, docs 08 resolve colisões PROP/TRB, e PROP-003 protege cobertura semântica. Os modelos A/B são ilustrativos, sem dados particulares. Uma busca por nome presumido de PROP-001 retornou 404; a árvore canônica identificou o caminho correto, lido em seguida. Não era arquivo ausente nem link quebrado do projeto. Não reauditar a totalidade dos consumidores ou validar links externos nesta etapa.

## 8. Walkthroughs documentais

Confronto analítico, não testes reais de migração, ferramentas, agentes ou consumidores.

| Caso | Situação | Resolução esperada |
| --- | --- | --- |
| C01 — novo arquivo | Documento de requisitos sem nome | Nome descritivo, numeração se ordem relevante (§2) |
| C02 — nome opaco | Tarefa com vários IDs concatenados | Título humano e ID estável necessário (§2) |
| C03 — símbolo de código | API pública usa nome técnico obrigatório | Preservar contrato; rótulo legível na UI quando útil (§2) |
| C04 — convenção local | Código em inglês e docs em português | Respeitar idioma e padrão de cada superfície (§2) |
| C05 — colisão de IDs | Duas propostas paralelas com número igual | ID temporário descritivo; resolver contra main e PRs no gate (§2) |
| C06 — renomeação de arquivo | Imports e links podem depender do caminho | Avaliar dependências e autorização, manter rastreio, testar (§2.2) |
| C07 — projeto inicial | Primeira entrega ainda não homologada | Perfil A, macroetapas e próximo gate (§4) |
| C08 — produto evolutivo | Baseline homologada, release ainda não publicado | Perfil B sem alegar publicação/instalação (§4) |
| C09 — projeto simples | Não possui fases relevantes | Adaptar/omitir painel sem burocracia (§4) |
| C10 — status divergente | README diz pendente, merge já confirmado | Corrigir derivada com fonte e preservar histórico (§§3,6) |
| C11 — histórico legítimo | Inventário datado de backups não corresponde ao atual | Preservar como fotografia; não atualizar retroativamente (§3) |
| C12 — consolidação ampla | Documentos sobrepostos contêm decisão exclusiva | Mapear cobertura e preservar informação, gate adequado (§5) |
| C13 — main minimalista | Documento aplicável está em PR ativa | Recuperar ref autorizada; não presumir inexistência (§3) |
| C14 — template | Link relativo correto somente no README gerado | Validar contexto de uso, não alterar incorretamente (§6) |
| C15 — backlog | Necessidade selecionada e tarefa criada | Vincular origem; não replicar andamento nem inferir autorização (§4.3) |
| C16 — COM-001 | Resposta com ação humana em chat não encerrado | Bloco terminal único, independentemente do fim da conversa (§7) |
| C17 — correção pós-merge | Divergência editorial versus alteração de requisito | Correção curta autorizada; material retorna ao gate (§6) |
| C18 — branch histórica | PR antiga com conteúdo parcialmente integrado | Classificar e preservar; não fechar/excluir automaticamente (§2.2; 04) |

Os 18 cenários têm tratamento conceitual. Não houve piloto, avaliação de legibilidade com usuários, teste de migração ou medição de manutenção. Não usar quantidade de nomes modificados como métrica de qualidade.

## 9. Critério de saída e continuidade

Critério documental: NOM-001 transversal com convenções/exceções por categoria, identidade e renomeação segura, mapa de fontes, modelos A/B/simples, preservação semântica e histórica, verificação proporcional, tratamento explícito dos diagnósticos e 18 cenários confrontados; reconciliar README, ROADMAP e PROP-007. 8/14 etapas homologadas após aceite e integração de 08. Nenhuma alteração normativa, renomeação, exclusão, mudança de consumidor, clone, backup, teste operacional ou varredura integral de segredos. PRs #4/#5 e branches documentais preservadas; refs da entrega intencionais. Não criar Knowledge duplicado.

Gate: homologação humana e integração comprovadas, conferência pós-merge e reconciliação registradas no encerramento abaixo. Após encerramento comprovado e autorização específica, continuar no mesmo chat com 09 — Eficiência e autonomia: definir matriz de autoridade/risco, critérios de reutilização de evidências, redução de retrabalho, custo de verificações, escalonamento mínimo e indicadores com baseline; usar diagnósticos D-03/D-05/D-06/D-09/D-11/D-12/D-13/D-16/D-20/D-24/D-26 e propostas 03–08. Preservar gates humanos e limites de segurança; não medir ganho sem dados. Etapas 09A e 09B permanecem independentes. Não iniciar 09 nesta etapa; integração normativa somente em 10.

## 10. Encerramento da etapa 08

- Autorização humana registrada na [PR #41](https://github.com/jotaCorsino/orbita-development-model/pull/41#issuecomment-7195555365): “pode continuar”, em resposta direta ao pedido de homologação e integração. Aceite documental e autorização restrita à integração e ao encerramento do refinamento candidato, sem alteração normativa, renomeação ou início de 09.
- Entrega aprovada: `e27e34fbab0fef261f28fbc604203bf6fd2ddb46`; merge squash confirmado: `bf8f713e10a7f36c487cc0794366bf15a1517d97`. Árvore Git `5ccb980b1264b0a9452e357b8a75923d0e4b476b` idêntica à entrega aprovada; quatro arquivos relidos diretamente na main. Preservados NOM-001, convenções, modelos README, os 18 walkthroughs analíticos, as 14 etapas e a continuidade por iniciativa.
- Fechamento editorial isolado conforme TRB-004, sem alteração normativa, de consumidores, nomes existentes, ferramentas ou ambientes. Nenhum teste empírico ou medição adicional. Nenhum temporário local criado; PRs #4/#5 e branches documentais preservadas intencionalmente; sem exclusão ou classificação de elegibilidade para descarte.
- Etapa 08 encerrada no escopo documental. Etapa 09 não iniciada; prosseguir neste mesmo chat somente após autorização específica. Conferir o pós-merge da alteração editorial na respectiva PR, sem abrir novo ciclo apenas para registrar seu próprio SHA.
