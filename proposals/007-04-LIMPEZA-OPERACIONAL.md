# ORB-EVO-001 — 04: Limpeza operacional

**Data:** 26/11/2026. **Estado:** protocolo candidato homologado, integrado pela PR #33 e verificado na main; ainda não vigente como norma. **Baseline:** `7850d7115f8baef1e752d6861572cdafc7d843ee`, PRs #31/#32 integradas; etapas 01–03 encerradas. **Autorização:** etapa 04 exclusivamente, neste mesmo chat da iniciativa. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Fundamento e decisão

D-08 e D-19 da [auditoria integral](007-01-AUDITORIA-INTEGRAL.md), corroborados pela [auditoria HUB](007-02-AUDITORIA-HUB-E-PROJETOS.md), são a origem deste protocolo. E-03/E-12 demonstram inventário e exclusões nominais autorizadas; E-13 mostra a necessidade de preservar trabalho e distinguir pós-check estrutural de QA autenticado; E-14 evidencia que backup declarado/legível não é recuperação demonstrada. E-05/E-08 reforçam que Git não recupera necessariamente dados, artefatos históricos ou trabalho ativo. Não reabrir essas auditorias. O número de backups em um projeto e a existência de PRs antigas não são regras de retenção universal.

Preservar [Git e GitHub](../docs/06-GIT-E-GITHUB.md), [governança](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md), [segurança](../docs/12-SEGURANCA-E-INTEGRIDADE.md), [contrato](../onboarding/CONTRATO-DE-TRABALHO.md), [TRB-004](../troubleshooting/004-ENCERRAMENTO-SEM-SINCRONIZACAO-DOCUMENTAL.md) e [arquitetura homologada candidata](007-03-ARQUITETURA-METODOLOGICA.md). A proposta estende o alcance operacional da verificação final já existente, não cria estado de tarefa, aprovação paralela ou sistema de limpeza universal.

| Alternativa | Avaliação |
| --- | --- |
| Limpar por idade, extensão, nome ou status de merge | Rápido, mas não demonstra finalidade, dependência, titularidade nem recuperabilidade. Rejeitada. |
| Preservar tudo e exigir autorização humana por arquivo | Minimiza descarte imediato, acumula dados, custo, risco e trabalho desnecessário. Rejeitada como default. |
| Verificação obrigatória, inventário proporcional, descarte delimitado e autorização por impacto | Preserva ativos, permite autonomia sobre temporários comprovadamente descartáveis e mantém controle de ações sensíveis. Recomendada. |

**Princípio:** limpar continuamente o que a tarefa gera, verificar no encerramento e registrar exceções; a obrigação é verificar e tratar, não excluir a qualquer custo. A proposta não autoriza deleções reais, mudanças de consumidores, configuração de retenção, transferência de ferramentas ou execução de 05. Integração normativa somente na etapa 10.

## 2. Classificação, escopo e responsabilidade

| Classe | Exemplos | Tratamento candidato |
| --- | --- | --- |
| Permanente/canônico | Código, docs, configuração oficial, tags/releases, dados e runbooks | Preservar; alteração/exclusão somente pelo fluxo competente |
| Operacional | Serviços, agendamentos, dependências, integrações, versões instaladas, ambientes ativos | Preservar até decisão operacional explícita; considerar consumidores e dono do ambiente |
| Recuperação | Backup oficial, rollback, snapshot necessário à operação | Preservar conforme política aprovada; provar identidade, integridade, cobertura e capacidade de recuperação proporcional |
| Evidência | Logs sanitizados, resultados QA, screenshots, relatório de auditoria, hashes | Preservar prova suficiente e legível pelo prazo aplicável; não copiar segredo/log bruto para Git público |
| Trabalho ativo | Alterações locais staged/unstaged/untracked/ignored relevantes, branches, worktrees, PRs e artefatos de agentes | Preservar; retomar/encerrar pelo responsável, não presumir abandono |
| Temporário descartável | Scratch da tarefa, cache/saída reproduzível sem valor material, clone de ensaio isolado | Remover somente se dentro de autorização, finalidade encerrada, não compartilhado e preservação confirmada |
| Obsoleto candidato | Versão substituída, backup excedente, ambiente desligado, PR/branch antiga | Inventariar, verificar dependências e retenção, propor tratamento; status não autoriza exclusão |
| Indeterminado | Origem, proprietário, valor, dependência, integridade ou acesso desconhecido | Preservar/segregar com autorização; esclarecer antes de descartar |

Uma classe não substitui avaliação de risco: cache compartilhado pode ser operacional, um arquivo ignorado pode conter trabalho único e um clone descartável pode conter alterações não publicadas. Um objeto pode cumprir várias funções; proteger a mais relevante até que todas estejam resolvidas. A classificação não é novo estado normativo de tarefa.

O **projeto** detém seus recursos e o registro de limpeza; o **dono de ambiente/dados** autoriza ações operacionais; o **HUB**, quando aplicável, coordena políticas comuns e impactos cruzados sem adquirir autoridade automática sobre consumidores; o **método especializado** detalha procedimentos da categoria; o **núcleo** define princípios e limites. O agente inventaria, recomenda, executa quando autorizado e demonstra resultado; não homologa a própria entrega. Knowledge registra apenas aprendizado comprovado e reutilizável, não inventário ou logs duplicados. Tools pode apoiar verificações, sem adquirir direitos de descarte.

## 3. Proporcionalidade e autorização

| Perfil de impacto | Alcance mínimo | Autoridade e evidência |
| --- | --- | --- |
| Pequeno/local/documental | Objetos criados pela tarefa e superfícies diretamente afetadas | Reutilizar autorização existente; declaração curta de ausência de resíduos ou destinação, com evidência pertinente |
| Intermediário/integração | Artefatos, worktrees/branches e PRs da tarefa, staging/QA, dependências e referências afetadas | Inventário delimitado; dry-run/preview quando houver; preservação e prova pré/pós; autorização agrupada quando necessária |
| Alto/operacional/irreversível | Dados, produção, backups, ambientes compartilhados, credenciais, serviços, refs/histórico, exclusão em massa | Runbook canônico, análise de impacto, autorização específica de responsáveis, preservação/rollback testado conforme risco, plano de interrupção e pós-validação adequada |

Esses perfis são critérios de desenho, não etiquetas obrigatórias, nem substituem a matriz de risco da etapa 09. A operação mais sensível determina a profundidade das verificações necessárias; não torna toda a tarefa crítica. Não exigir varredura de disco, todos os repositórios ou todas as branches para mudança pequena. Inventário transversal periódico pode ser tarefa autorizada separadamente conforme necessidade, sem cron obrigatório.

**Autonomia delimitada:** quando a tarefa ou runbook vigente já prevê o ciclo de vida de um diretório temporário isolado criado pelo próprio agente, e não existem dependências, trabalho material, dados/evidências exclusivos ou acesso de terceiros, a remoção estritamente delimitada pode ocorrer sob essa autorização existente. Não pedir aprovação por cada temporário nessas condições. Se essa autorização não estiver clara, preservar e solicitar decisão. Não interpretar “organize”, “limpe”, “pode continuar”, merge ou homologação do artefato como licença para eliminar recursos preexistentes, material ou compartilhados.

**Autorização específica:** exclusão de backup, dados, ambiente, branch/tag/release remota, PR histórica, trabalho não integrado, artefato único, recurso de terceiro ou ação material/irreversível exige decisão competente, escopo explícito e identificação dos alvos (lista nominal ou conjunto fechado verificável). Lotes são aceitáveis quando homogêneos, com risco, condições e limites aprovados. Um responsável não dispensa política de outro dono; aplicar resolução de conflitos da etapa 03. A autorização deve corresponder ao alvo e ao estado observado; alteração material entre pré-check e ação invalida a execução do item afetado.

## 4. Protocolo integrado ao ciclo de trabalho

### A. Antes e durante a execução

1. Identificar tarefa, projeto/ambiente, runbook vigente, autorização e limites. Consultar Knowledge seletivamente. Não criar backup, clone, staging, script ou log adicional sem finalidade; reutilizar recursos válidos quando permitido.
2. Delimitar onde a tarefa pode gerar resíduos e o que precisa permanecer. Criar temporários em diretório/namespace exclusivo, nome legível e ownership rastreável, sem sobrepor recursos existentes; não impor estrutura nova a projetos estabelecidos. Definir destino/retorno de evidências, validade e condição de descarte quando relevante.
3. Preservar trabalho material antes de qualquer operação potencialmente destrutiva, inclusive staged/unstaged/untracked/ignored relevantes, alterações locais de outros agentes, submódulos/worktrees e estado não publicado. Não assumir que GitHub contém todo o trabalho.
4. Remover durante a execução apenas temporários comprovadamente dispensáveis, dentro da autorização vigente e com proteção contra falhas. Rotinas de saída/cleanup não devem destruir evidência de erro, dados nem trabalho recuperável. Se houver interrupção, preservar checkpoint e material necessário à retomada.

### B. Antes do encerramento/integração

5. Inventariar os objetos gerados e afetados pela tarefa, incluindo resíduos preexistentes descobertos no alcance; distinguir origem. Usar leitura segura, identificar caminhos/refs exatos, tipo, versão, proprietário, finalidade, dependências, tamanho/contagem quando útil, existência/estado, retenção e autoridade. Não recolher conteúdo sensível desnecessário.
6. Classificar cada item ou grupo homogêneo pelas classes do §2. Decidir preservar, remover sob autorização existente, propor remoção específica, ou manter pendência justificada. Confirmar a fonte canônica e evidência preservada; distinguir backup oficial de cópia incidental.
7. Preparar conjunto de alvos fechado, sem glob não resolvido, diretórios ascendentes, descoberta expansiva ou expansão baseada em idade. Validar destino e identidade real, links simbólicos/reparse points, montagem, permissões, referências e dependências conforme tecnologia. Simular/listar ação quando disponível; não executar se identidade, autoridade ou recuperabilidade material estiverem incertas. Dry-run não prova ausência de corrida.
8. Agrupar decisão humana necessária no gate já aplicável, apresentando alvo, justificativa, impacto, preservação, pós-check e risco residual. Evitar pedir aprovação já concedida. Registrar decisão/referência; não executar exclusões sem autorização. Realizar limpeza antes do merge somente se o item já for descartável naquele momento; não remover evidências ainda necessárias à homologação ou branch em trabalho.

### C. Execução delimitada e verificação

9. Reconfirmar identidade/estado imediatamente antes da escrita, incluindo escopo autorizado, refs, alterações concorrentes e dependências; se divergente, interromper o item/lote afetado. Executar somente os alvos aprovados, evitando seguir links, usar privilégios desnecessários ou comandos destrutivos genéricos. Em lote, registrar itens removidos, preservados, falhos ou não executados; não prosseguir após falha que invalide pressupostos. Operações não atômicas exigem distinguir sucesso parcial de sucesso integral. Não repetir indiscriminadamente.
10. Verificar ausência dos alvos efetivamente removidos, presença/integridade das fontes e pontos de recuperação preservados, referências e comportamento das superfícies impactadas. Pós-check deve observar o destino real: estrutura/hash não prova serviço funcional, HTTP anônimo não prova fluxo autenticado, merge não prova deploy. A profundidade segue risco; declarar limitações de acesso/teste e não simular PASS.
11. Reconciliar documentação/refs afetadas no fluxo existente de [verificação final](../templates/VERIFICACAO-FINAL-TEMPLATE.md), inclusive diretamente na linha integrada quando aplicável; remover indicação antiga somente quando comprovada. Após merge pode haver temporários/refs que só então se tornam candidatos a descarte: reavaliar autorização e dependências. Não abrir PR de encerramento por reflexo; somente quando houver inconsistência que precise ser corrigida.
12. Registrar resultado, pendência/exceção, responsável e próxima condição. Concluir somente o escopo comprovado; não dizer “ambiente limpo” sem delimitar o universo. Se limpeza necessária ao critério de saída estiver bloqueada, manter encerramento pendente; se resíduo for preservado por razão legítima e não bloquear critério, registrar e encerrar sem falso descarte. Manter evidência da falha e recuperar conforme runbook/autorização.

## 5. Tratamento por categoria

| Categoria | Preflight específico | Pós-check/condição de preservação |
| --- | --- | --- |
| Arquivos/pastas e scripts | Identidade absoluta/canônica, criação pela tarefa, conteúdo material, links/montagens, compartilhamento, referências | Apenas alvos definidos ausentes; arquivo oficial e dependências intactos |
| Git local / worktrees / clones | Status, staged/unstaged/untracked e ignored relevantes, stash, refs locais, worktrees, submódulos, locks, trabalho de outros agentes | Material único preservado em checkpoint adequado e acessível; working copy/refs necessárias íntegras |
| Git remoto / PRs | Head/base, estado PR, diff semântico, squash/rebase, commits únicos, refs dependentes, revisão/discussão e proteção; autorização de fechamento e de deleção distintas | PR corretamente classificada, refs preservadas/ausentes conforme plano e fonte integrada conferida; não reescrever histórico |
| Artefatos de build e caches | Reprodutibilidade, versão/manifesto, integridade, evidência, consumidores, custo de reconstrução | Artefato de distribuição/rollback e evidência única preservados; ausência de intermediários confirmada |
| Backups/snapshots | Política, dono, cobertura, data, localização, legibilidade, integridade, criptografia/acesso, relação com dados e rollback, recuperação demonstrada conforme risco | Ponto(s) exigido(s) permanecem acessíveis e aptos no nível demonstrado; não declarar restore sem ensaio |
| Bancos/dados, serviços e ambientes | Runbook, dono, dados únicos, dependências, agendamento, destino e estado atual, retenção/obrigações, plano de reversão | Dados/serviço/integrações preservados, verificação funcional proporcional, limitação explícita; operação de alto impacto |
| Logs, evidências e exports | Valor probatório, privacidade, prazo, fonte/versão, síntese suficiente, responsabilidade | Prova necessária legível e rastreável; eliminação de sensíveis conforme política e autorização, sem copiar para Git público |

### 5.1 Backups oficiais e retenção

Não há quantidade universal de backups. O projeto/HUB e dono de dados definem retenção conforme criticidade, obrigações, objetivos de recuperação, rollback, espaço, segurança e dependências. Uma política de manter um único backup oficial pode ser adequada para certo fluxo de rollback, mas não implica eliminar histórico exigido ou que uma única cópia proteja contra falha do destino. Não criar backup adicional apenas porque o agente não consultou a política existente.

Antes de reduzir retenção, identificar nominalmente os pontos que permanecerão, distingui-los de cópias transitórias, confirmar capacidade de acesso e recuperação no nível exigido, e verificar se a operação atual necessita de snapshot novo (backup pré-migração antigo pode não cobrir dados atuais). Se o backup oficial estiver ausente/desconhecido, interromper a deleção dependente e comunicar. Hash, tamanho e leitura são evidências de integridade parcial, não prova de restauração. Ensaio de restore quando exigido deve ser isolado/autorizado, nunca sobrescrever produção por conveniência. Remoção de backup não é autorizada pelo presente protocolo.

### 5.2 Branches e PRs

Merge normal pode demonstrar ancestralidade; squash/rebase exige confrontar conteúdo/decisões e material exclusivo, além de dependências. Uma branch integrada pode sustentar referência de auditoria, PR histórica, outra branch ou release; verificar antes de excluir. Fechar PR não remove branch nem autoriza apagá-la; fechar ou preservar requer classificação e decisão conforme escopo. Não usar “merged”, “stale” ou ausência de atividade como critério suficiente; não apagar trabalho ativo de outro agente. Uma PR antiga com conteúdo substituído pode ser encerrada após decisão nominal, preservando histórico/discussão e fonte do resultado equivalente. Não reescrever histórico para limpeza ordinária.

## 6. Registro mínimo e exceções

Reutilizar tarefa, PR, relatório ou registro operacional já existente. Não exigir novo arquivo, inventário de todos os recursos ou formulário para cada item.

Exemplo **sintético**, sem execução:

| Alvo/grupo e origem | Classe | Decisão/autoridade | Preservação | Resultado esperado |
| --- | --- | --- | --- | --- |
| Pasta temporária exclusiva criada pelo ensaio | Temporário | Descarte previsto no runbook | QA relevante em registro aprovado; sem trabalho único | Ausência da pasta e evidência intacta |
| Backup oficial de rollback | Recuperação | Preservar conforme política | Identidade, hash e teste de recuperação no nível exigido | Presença/integridade comprovadas |
| PR histórica com conteúdo possivelmente exclusivo | Indeterminado | Preservar até decisão competente | Branch, discussão e comparação | Pendente; não declarar descarte |

Em tarefa documental simples, basta registro como “nenhum temporário local criado; PR/branch da entrega preservadas intencionalmente; verificação remota delimitada”. Para operação material, incluir projeto/ambiente, snapshot prévio, identificação dos alvos, classificação e dependências, autoridade, pontos preservados, ação/resultado individual ou lote, pós-check, falhas/limitações e pendências. Evidências sensíveis ficam em fonte restrita, com resumo sanitizado.

Exceção deve indicar alvo, motivo, risco residual, responsável, condição/prazo de revisão quando útil, evidência e se bloqueia o critério de saída. Classificar resíduo preexistente fora do escopo sem autorizá-lo: registrar no fluxo adequado apenas se relevante; não abrir backlog ou tarefa duplicada. Uma exceção justificada permite preservar, não excluir. Se não houver acesso para inventariar um ambiente relevante, registrar “não verificado”; se o ambiente for essencial ao encerramento, não declarar conclusão operacional. Não confundir interrupção com limpeza concluída.

## 7. Walkthroughs documentais e exemplo observado

Os casos abaixo são confrontos analíticos do desenho, não testes reais de exclusão, restauração ou serviço.

| Caso | Situação | Resolução esperada |
| --- | --- | --- |
| C01 — tarefa curta | Apenas documento remoto modificado | Verificar refs e derivadas; declarar ausência de temporários criados, sem varrer disco (§§3–4) |
| C02 — scratch | Ensaio criou diretório exclusivo e descartável, runbook autoriza | Preservar prova, confirmar identidade, remover só alvo e verificar (§§3–4) |
| C03 — interrupção | Clone/worktree com arquivo ignorado potencialmente único | Preservar e recuperar estado; não limpar automaticamente (§§2,5) |
| C04 — link ou montagem | Caminho autorizado redireciona para recurso compartilhado | Bloquear alvo por identidade divergente, não seguir link (§4) |
| C05 — backup oficial ausente | Registro antigo afirma existência; busca não confirma | Não reduzir retenção; esclarecer dono e cobertura (§5.1; E-14) |
| C06 — backup legível | Hash correto, restore não ensaiado | Registrar integridade observada; não afirmar recuperação (§5.1; E-14) |
| C07 — branch squash | Conteúdo equivalente, PR dependente ou decisão exclusiva possível | Comparar e obter autorização nominal; preservar até resolução (§5.2; D-19) |
| C08 — lote concorrente | Head ou arquivo muda após aprovação | Suspender item/lote afetado, revalidar; não ampliar alvos (§§3–4) |
| C09 — pós-check limitado | Temporário removido; só HTTP anônimo disponível | Não declarar QA autenticado; registrar limite (§4; E-13) |
| C10 — evidência privada | Log bruto contém dados; resumo sanitizado suficiente | Reter conforme política restrita, não publicar; eliminação autorizada à parte (§§5–6) |
| C11 — dependência compartilhada | Ambiente antigo ainda referenciado por consumidor | Preservar, envolver dono e avaliar dependência (§§2–4) |
| C12 — falha parcial | Dois de três alvos removidos; terceiro falha | Registrar resultados individuais e parar se pressuposto inválido; não declarar limpeza integral (§4) |
| C13 — preservação legítima | Branch documental retida para revisão/auditoria, sem impedir gate | Classificar como intencional; encerrar escopo com razão registrada (§6) |
| C14 — escopo desconhecido | Agente sem acesso ao host relevante ao gate | Não inventar inventário; diagnóstico seguro e decisão sobre bloqueio (§6) |

**Exemplo observado nesta etapa, somente leitura:** no início da etapa 04, a API GitHub retornou 33 branches (32 não-main), duas PRs abertas em draft (#4 e #5) e seis branches documentais da iniciativa (três entregas e três encerramentos). O snapshot inicial de D-19 continha 26 branches não-main; crescimento observado de seis refs não é prova de resíduo descartável. A árvore da baseline continha 54 entradas, incluindo diretórios. As PRs #4/#5 permaneciam abertas; cabe comparação semântica/decisão específica para eventual fechamento ou exclusão. As seis refs documentais são rastros intencionais das etapas anteriores, não inventário de elegibilidade para apagar. Nenhum checkout ou ambiente físico foi inspecionado; não afirmar que não existem resíduos locais. A etapa 04 não autoriza excluir nenhuma ref, fechar PR antiga ou alterar consumidores. A branch/PR da entrega são rastros intencionais adicionais. O levantamento é fotografia, não política nem inventário permanente.

## 8. Integração futura e critérios de saída

| Diagnóstico | Tratamento candidato | Próxima materialização |
| --- | --- | --- |
| D-08 | Inventário proporcional, classes, autoridade, proteção de trabalho/backup/evidência e prova pós-limpeza | 09 (autonomia), 10 (contrato/fluxo/checklist), 11 (pilotos) |
| D-19 | Classificar refs antigas por valor/atividade/dependência, fechamento e exclusão distintos | 08 (documentação), 09 (autoridade), 10–11 (integração e validação) |
| D-06/D-13/D-27 | Escopo delimitado, gate operacional, privacidade e limites de teste | 09–11 |

A etapa 10 deverá estender o contrato, o fluxo e o checklist de verificação final onde necessário, com referência única ao protocolo e sem cópias concorrentes. A etapa 09 detalhará autoridade proporcional; 11 avaliará cenários práticos autorizados em perfis distintos e registrará baseline, tempo, intervenções, resíduos sem classificação, falhas e preservação comprovada. Não medir ganho sem dados. A etapa 12 verificará maturidade e publicação. Não criar script de remoção, automação, serviço, rotina de retenção ou novo estado obrigatório nesta etapa.

Critério de saída documental: inventário delimitado, classificação, autoridade por impacto, preservação, preflight, execução delimitada, pós-check, exceção e 14 walkthroughs consistentes; compatibilidade com TRB-004 e arquitetura candidata; registro de limites e reconciliação das superfícies derivadas. A entrega não é execução de limpeza nem piloto. Nenhuma exclusão, operação real, alteração normativa, implantação, backup, clone, teste de restore ou varredura de segredos executados. As evidências públicas permanecem sanitizadas. Não gerar Knowledge duplicado porque o protocolo ainda é candidato. 4/14 etapas homologadas após o aceite e integração da etapa 04.

## 9. Continuidade condicional — etapa 05

Gate: homologação humana e integração comprovadas, conferência pós-merge e reconciliação registradas no encerramento abaixo; não tornar o protocolo vigente antes da etapa 10. Somente após encerramento comprovado e autorização específica, continuar no mesmo chat com 05 — Chats e continuidade. Usar a decisão já aprovada pelo responsável sobre um chat por iniciativa, D-03/D-07/D-23 e evidências pertinentes das auditorias, sem reabrir arquitetura ou auditorias. Formalizar granularidade, nomenclatura, handoff condicional, checkpoint, retomada por preservação, distinção de interrupção e encerramento e recuperação seletiva; não impor novo chat por etapa. A etapa 06 detalhará bootstrap/instruções. Não iniciar 05 neste trabalho.

## 10. Encerramento da etapa 04

- Homologação humana registrada na [PR #33](https://github.com/jotaCorsino/orbita-development-model/pull/33#issuecomment-7193083857): “aprovado, pode continuar”. Autorização restrita à integração e encerramento documental do protocolo candidato, sem exclusões reais ou início de 05.
- Entrega aprovada: `ce41eaae15f4f3da8087313e6de66420509404c6`; merge squash confirmado: `82c92ce73ff7c0ef9c263706df68aeb2d42e6c91`. Árvore Git `05aec30ff238e032267d620827cc11dcffece5ed` idêntica à entrega aprovada; quatro arquivos relidos diretamente na main. Preservados os 14 walkthroughs analíticos, as 14 etapas e a decisão de continuidade no mesmo chat.
- Fechamento editorial isolado conforme TRB-004, sem alteração normativa, de consumidores, ambientes, licença ou política de retenção. Nenhum piloto, restore, exclusão, inspeção física ou verificação empírica adicional. As limitações do levantamento remoto permanecem. PRs #4/#5 e branches documentais preservadas intencionalmente; classificação de elegibilidade para eventual descarte não realizada. Nenhum temporário local foi criado nesta etapa.
- Etapa 04 encerrada no escopo documental. Etapa 05 não iniciada; prosseguir neste mesmo chat somente após autorização específica. Conferir o pós-merge da alteração editorial na respectiva PR, sem abrir novo ciclo apenas para registrar seu próprio SHA.
