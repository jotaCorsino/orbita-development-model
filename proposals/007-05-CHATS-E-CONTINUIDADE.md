# ORB-EVO-001 — 05: Chats e continuidade

**Data:** 26/11/2026. **Estado:** protocolo candidato homologado, integrado pela PR #35 e verificado na main; ainda não vigente como norma geral. **Baseline:** `255e5b7acc5461b1ba1d348b03ccf5868c14f05b`. PRs #33/#34 integradas; etapas 01–04 encerradas. **Autorização:** etapa 05 exclusivamente, no mesmo chat. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Fundamento e decisão preservada

A decisão humana registrada após o encerramento de 02 é o ponto de partida: uma iniciativa permanece no mesmo chat enquanto houver contexto suficiente. Etapas internas não justificam, por si só, novos chats. Gates independem da divisão das conversas. A formulação original do PROP-007 é histórica e não será restabelecida.

A [auditoria integral](007-01-AUDITORIA-INTEGRAL.md) registra D-03 (bootstrap contextual), D-07 (handoff) e D-23 (nomenclatura); D-04/D-09/D-26 delimitam estado, reconciliação e eficiência. A [auditoria HUB](007-02-AUDITORIA-HUB-E-PROJETOS.md) apresenta E-04/E-07/E-08/E-10/E-13/E-20/E-21: perda de procedimento aprovado, trabalho ativo fora da main, necessidade de preservar evidências e retomar somente o teste pendente, referências e estados desatualizados, cadeias de PRs e IDs difíceis de acompanhar. Essas ocorrências não comprovam que toda falha foi causada por troca de chat, nem medem economia de tempo.

Preservar [fluxo](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md), [retomada e checkpoints](../docs/06-GIT-E-GITHUB.md), [IA no método](../docs/07-IA-NO-METODO.md), [identidade](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md), [contrato de trabalho, especialmente §§3,4,9,11 e COM-001](../onboarding/CONTRATO-DE-TRABALHO.md), [TRB-003](../troubleshooting/003-INTERRUPCAO-CODEX-TRABALHO-LOCAL.md), [arquitetura candidata](007-03-ARQUITETURA-METODOLOGICA.md) e [limpeza operacional candidata](007-04-LIMPEZA-OPERACIONAL.md). A retomada material já possui protocolo homologado: inspecionar → preservar → distinguir local/remoto → retomar. Não duplicar nem substituir.

## 2. Granularidade e identidade

| Unidade | Finalidade | Regra proposta |
| --- | --- | --- |
| Projeto | Identidade canônica do produto/método em todos os ambientes | Um contexto de planejamento e um de execução inequivocamente associados, quando aplicáveis; não exige ferramenta específica |
| Iniciativa | Objetivo de evolução delimitado, com planejamento, entregas e gates | Unidade preferencial da conversa de coordenação |
| Chat | Sessão conversacional para conduzir a iniciativa | Um chat de coordenação por iniciativa por padrão; pode haver continuidade quando necessário |
| Etapa/subetapa/tarefa | Unidade de execução, dependência, autorização e evidência | Mantida dentro da iniciativa; possui gate conforme risco, não chat próprio obrigatório |
| Sessão de implementação | Execução técnica por agente/ferramenta | Pode ter sessões próprias, respeitando tarefa autorizada e identidade; não cria iniciativa nova nem autoridade paralela |

**Regra candidata:** a unidade de organização do chat de planejamento é a iniciativa, não o número de etapas, commits, PRs ou homologações. Uma iniciativa pode conter tarefas sucessivas e subtarefas sem criar novos chats. Iniciativas pequenas podem ser tratadas como uma tarefa coerente, sem inventar níveis de gestão. O mesmo projeto pode ter iniciativas independentes simultâneas, cada uma com escopo, refs e decisões próprios.

A separação de papéis entre planejamento e implementação permanece. Transferir uma tarefa a outro agente é comunicação de execução, não obrigação de abrir outro chat de planejamento. A continuidade não pressupõe que ferramentas diferentes compartilhem contexto, memória ou permissões.

| Alternativa | Avaliação |
| --- | --- |
| Um chat para todo o projeto indefinidamente | Evita fragmentação, mas mistura objetivos independentes e decisões de diferentes épocas |
| Um chat por etapa ou tarefa | Facilita separação artificial, mas multiplica transferências e reconstrução de contexto |
| Um chat por iniciativa, continuidade condicional | Mantém coerência e rastreabilidade sem abolir gates; recomendada conforme decisão humana |

## 3. Quando continuar e quando abrir outro chat

| Situação | Comportamento candidato |
| --- | --- |
| Nova etapa, subtarefa, revisão, correção ou homologação da mesma iniciativa | Continuar no chat existente |
| Nova decisão dentro do escopo atual | Registrar decisão na fonte persistente se relevante; continuar |
| Conversa longa, mas contexto ainda recuperável com segurança | Continuar; comprimento por si só não é motivo para troca |
| Nova iniciativa independente, com objetivo e escopo próprios | Novo chat de coordenação associado ao mesmo projeto |
| Mudança de projeto ou fronteira de acesso/privacidade | Contexto separado; transmitir somente referências/dados autorizados |
| Saturação, truncamento, indisponibilidade da conversa, repetidas perdas de decisões materiais | Recuperar checkpoint e abrir continuação somente se necessário |
| Troca de implementador ou ambiente | Handoff da tarefa ao executor; manter chat de coordenação se possível |
| Interrupção sem perda do chat e com trabalho local possivelmente existente | Retomar no mesmo chat pelo protocolo vigente de preservação |

Critérios objetivos de necessidade: impossibilidade de recuperar autorização/último gate/refs ou decisões essenciais com segurança; perda de acesso à conversa; limite da ferramenta; inconsistências contextuais repetidas que persistem após recuperação focal; mudança de iniciativa/projeto ou requisito de isolamento. Não inferir saturação a partir de número de mensagens, duração, quantidade de etapas ou estimativa inventada de tokens. Não migrar por conveniência quando a recuperação focal resolve. Se contexto/autoridade indispensável não puder ser recuperado, suspender apenas a ação dependente e solicitar a menor decisão/evidência faltante.

Não abrir, renomear, arquivar ou apagar chats existentes em massa; o protocolo não concede acesso a essas operações. Chat encerrado não implica tarefa homologada; chat novo não reabre tarefa concluída. Um handoff pode ser útil sem troca de chat quando houver executor distinto, pausa longa ou necessidade de preservar estado.

## 4. Nomenclatura humanizada

Aplicar NOM-001 candidato apenas à organização de chats nesta etapa; demais categorias serão detalhadas em 08. Nome legível primeiro, ID estável quando existente, indicação de continuação somente se realmente necessária. O nome do projeto já está no contexto dedicado quando isso for inequívoco; não repetir toda a hierarquia.

| Caso | Exemplo sugerido |
| --- | --- |
| Iniciativa identificada | ORB-EVO-001 — Evolução do ÓRBITA |
| Iniciativa sem ID obrigatório | Revisão do catálogo de produtos |
| Continuação necessária | ORB-EVO-001 — Evolução do ÓRBITA (continuação 2) |
| Iniciativa paralela | Revisão de segurança — acessos e permissões |
| Tarefa referida no chat, não novo chat | 05 — Chats e continuidade |
| Execução delegada, se precisar de nome | ORB-EVO-001 — 05 — Revisão de continuidade |

Evitar “Chat 1”, códigos sem descrição, concatenação de IDs de todas as subtarefas e nomes com estados voláteis (“aguardando”, “final”, “versão atual”) quando o registro persistente já os controla. Não exigir ID inexistente, prefixo numérico global ou renomeação retroativa. Manter nomes técnicos obrigatórios e relação inequívoca com o projeto. Não incluir segredo, dado de cliente ou informação sensível desnecessária em título de conversa.

## 5. Contexto recuperável e checkpoint

O repositório/registro técnico é referência persistente, não a conversa ou a memória do agente. Seguindo a etapa 03, distinguir main integrada, trabalho em PR/branch ativa, alterações locais não publicadas, artefato, ambiente, evidência e autorização. Um chat pode conter decisões humanas recentes ainda não persistidas: registrar essas decisões no fluxo competente, sem presumir que um resumo anterior seja mais autorizado. Uma aprovação verbal precisa identificar o objeto de aceite, seu escopo e revisão quando relevante; preservar registro e não pedir a mesma decisão novamente.

Checkpoint é marco verificável de continuidade, não entrega aprovada, publicação ou novo estado. Reutilizar tarefa/PR/decisão/registro já existente; nenhum arquivo de checkpoint obrigatório. Registrar mudança material de objetivo/escopo, decisão que afeta etapas futuras, último gate cumprido, referência de trabalho ativo, bloqueio relevante ou ponto de recuperação de tarefa longa/cara. Não registrar cada mensagem, microalteração ou toda a conversa. Não exigir commit/push se o fluxo não autorizar; material local deve ser protegido pelo procedimento vigente.

Na continuidade normal, a entrega/aceite já registrados podem ser checkpoint suficiente. Na interrupção, indicar último estado normativo comprovado e condição Pausado quando aplicável; não inventar novo estado. Se ação de efeito externo ficou com resultado desconhecido, verificar situação real antes de repetir, pois a tentativa pode ter concluído parcialmente ou integralmente. Não declarar encerramento, restauração ou ausência de alterações locais sem evidência.

### 5.1 Handoff mínimo condicional

Reutilizar referência persistente e transmitir só informações indispensáveis. Para tarefa curta, um parágrafo com fonte, estado e ação pode bastar. Para transferência material, usar os campos abaixo conforme aplicáveis; não criar formulário/gate separado.

| Campo | Conteúdo |
| --- | --- |
| Identidade | Projeto canônico, iniciativa/tarefa, objetivo atual e executor/dono quando pertinente |
| Autoridade | Escopo já autorizado, decisão/referência, exclusões do escopo e gate humano pendente |
| Estado comprovado | Último marco, dimensões de implementação/teste/homologação/integração/operação, limites |
| Referências | Fonte canônica, revisão adotada, branch/PR/HEAD, artefato/ambiente quando relevante |
| Trabalho não persistido | Working copy, arquivos materiais, commits locais, evidência preservada ou estado desconhecido |
| Pendência real | Bloqueio, erro, verificação não realizada e o que não deve ser repetido |
| Próxima ação | Menor ação segura já autorizada; dependência/critério que impede avanço |
| Restrições | Runbook vigente, decisões que precisam ser preservadas, risco, acesso, privacidade |

Não enviar transcrições integrais, tokens, credenciais, conteúdo privado para contexto sem autorização, prompts duplicados, dumps ou logs desnecessários. Handoff deve referenciar a fonte restrita quando necessário e permitido; acesso ausente deve permanecer explícito. Em transferência regular, indicar destino e se o próximo agente precisa inspecionar material local; não afirmar que a transferência ocorreu até haver evidência. COM-001 somente quando existe providência humana real.

## 6. Recuperação seletiva antes de agir

| Modo | Leitura proporcional |
| --- | --- |
| Continuação no mesmo chat | Recuperar decisão/gate imediatamente anterior, refs afetadas, estado relevante e índice Knowledge; abrir só entradas aplicáveis |
| Nova iniciativa em projeto conhecido | Confirmar identidade, regras/versões aplicáveis, objetivo e dependências; usar documentação atual e decisões relevantes |
| Novo chat de continuação | Ler checkpoint e fontes apontadas; confirmar identidade, autorização, último marco, refs e menor tarefa pendente |
| Retomada após interrupção ou troca de executor | Inspecionar e preservar estado material conforme docs 06/TRB-003 antes de sincronizar, limpar ou reconstruir; recuperar limites e evidências |
| Projeto novo/adoção inicial | Seguir onboarding vigente; não reduzir requisitos de fundação a uma retomada curta |

Fluxo candidato:
1. Identificar iniciativa, tarefa e tipo de continuidade.
2. Recuperar checkpoint ou último gate comprovado e decisões aplicáveis. Se não houver checkpoint dedicado, reconstruir somente o trecho necessário a partir de registros existentes.
3. Confirmar projeto, autoridade, revisão, estado atual e dependências relevantes; para operações, recuperar runbook e destino. Não assumir que main representa trabalho ativo.
4. Consultar índice Knowledge quando exigido pelo contrato; reutilizar conclusão aplicável e evidência cujo pressuposto continua válido. Revalidar fato volátil, teste afetado, versão/ambiente alterado, autorização incerta ou fonte contraditória. Não refazer auditoria, testes ou fundação por reflexo.
5. Se houver possível estado local não persistido, aplicar protocolo vigente de preservação antes de escrita. Se indisponível e essencial, manter ação bloqueada.
6. Retomar a menor ação realmente pendente e autorizada, mantendo gates. Caso o último gate seja homologação pendente, apresentar o objeto a aprovar; caso seja pós-merge, verificar estado integrado em vez de reimplementar.

A recuperação seletiva não dispensa preflight, validação proporcional, segurança ou verificações exigidas pelo método. Não usar memória conversacional como prova de estado externo. A etapa 06 definirá configuração compacta, fontes/versões e leitura inicial por perfil; a etapa 09 definirá critérios de reuso, autonomia e métricas. Não criar instruções de IA ou templates normativos agora.

## 7. Exemplo de handoff sintético e aplicação observada

Exemplo ilustrativo, sem execução: “Projeto Catálogo — iniciativa Revisão de navegação, tarefa Ajuste de menu. Implementação no PR ativo, revisão X; teste visual aprovado, teste de teclado ainda pendente. Homologação final não concedida. Preservar comportamento e identidade já aprovados. Confirmar HEAD e executar somente teste de teclado no ambiente de QA; se falhar, corrigir no escopo autorizado. Nenhum deploy autorizado.” O exemplo não pressupõe que execução ou teste ocorreram.

Aplicação observada na ORB-EVO-001: após a etapa 02, o responsável rejeitou a fragmentação de um chat por etapa e autorizou continuidade por iniciativa. Etapas 03 e 04 foram conduzidas sem exigir abertura de novo chat; respectivas propostas, aprovações, merges e verificações foram registradas no repositório. Para iniciar 05, a baseline `255e5b7acc5461b1ba1d348b03ccf5868c14f05b` e PRs #33/#34 foram confirmadas; plano, fontes pertinentes e índice Knowledge foram consultados seletivamente. Não houve reauditoria integral. Isso demonstra o fluxo adotado nesta iniciativa, não prova redução quantitativa de custo, desempenho superior geral ou completude de memória do agente. Nenhum inventário dos chats do usuário, inspeção local ou transferência de dados entre ferramentas foi realizado.

## 8. Walkthroughs documentais

Os casos são confrontos analíticos do desenho; não constituem testes executados em serviços de IA nem observação de outras conversas.

| Caso | Situação | Resolução esperada |
| --- | --- | --- |
| C01 — nova etapa | Mesma iniciativa, próximo gate autorizado | Continuar no mesmo chat (§§2–3) |
| C02 — iniciativa nova | Objetivo independente no mesmo projeto | Novo chat associado ao projeto (§3) |
| C03 — conversa longa | Contexto suficiente e fontes recuperáveis | Continuar sem limite numérico fictício (§3) |
| C04 — contexto perdido | Última aprovação não recuperável na conversa, mas registrada no PR | Consultar registro, confirmar objeto e retomar; nova sessão se necessária (§§3,5–6) |
| C05 — interrupção | Trabalho material possivelmente só local | Preservar antes de sincronizar; Pausado sem falso encerramento (§§5–6; TRB-003) |
| C06 — PR ativa | Main não contém decisão em revisão que rege tarefa | Recuperar ref explicitamente aplicável, distinguir status (§§5–6; E-08) |
| C07 — autorização vigente | Gate anterior já aprovado e comprovado | Não solicitar novamente; não ampliar para gate futuro (§§5–6) |
| C08 — QA parcial | Teste principal passou, negativo não executado | Reutilizar prova válida e retomar teste pendente; não repetir mutação (§6; E-10) |
| C09 — operação incerta | Sessão terminou durante escrita externa | Verificar destino e resultado antes de repetir (§5) |
| C10 — transferência | Novo implementador, mesmo objetivo | Handoff focal da tarefa sem novo chat de coordenação obrigatório (§§2,5.1) |
| C11 — privacidade | Fonte restrita não acessível ao executor | Referência permitida, limite explícito, sem copiar segredo (§§3,5.1) |
| C12 — nome ilegível | Título com cadeia de IDs de subetapas | Nome descritivo com ID da iniciativa e continuação se necessária (§4) |
| C13 — tarefa simples | Ajuste pequeno sem estado material difícil de recuperar | Registro existente suficiente; sem checkpoint adicional (§5) |
| C14 — evidência volátil | Versão de ambiente mudou desde teste anterior | Revalidar apenas efeitos relevantes, manter gates (§6) |

Os 14 casos possuem tratamento conceitual, preservando o protocolo vigente de interrupção. Nenhum piloto, medição de tokens/tempo, verificação de plataformas ou validação de recuperação empírica executado.

## 9. Integração futura e critérios de saída

| Diagnóstico | Tratamento candidato | Materialização |
| --- | --- | --- |
| D-03 | Modos de recuperação seletiva e confirmação de refs/autoridade | 06, 09, 10–11 |
| D-07 | Handoff condicional, checkpoint e retomada pelo protocolo existente | 06, 10–11 |
| D-23 | Título humano, ID de iniciativa e continuação quando necessária | 08, 10–11 |
| D-04/D-09/D-26 | Dimensões de estado, reutilização de registro, não repetir sem motivo | 08, 09, 10–11 |

A etapa 10 deverá reconciliar contrato §9, docs 07, referências de onboarding e plano de evolução, mantendo fonte canônica e evitando duplicação do protocolo de docs 06/TRB-003. Não tornar obrigatório um template independente de handoff, novo estado, chat por etapa, contador de mensagens ou sistema externo. Na etapa 11, avaliar casos reais autorizados: tempo/custo de recuperação, intervenções humanas, repetição indevida, decisões recuperadas e preservação de material; definir baseline antes de concluir ganho. Não medir nesta etapa.

Critério de saída documental: granularidade, nomenclatura, gatilhos de troca/continuidade, checkpoints proporcionais, handoff mínimo, recuperação seletiva, autorização, privacidade, preservação e 14 cenários confrontados; reconciliação de README, ROADMAP e PROP-007; 5/14 etapas homologadas após aceite e integração de 05. Nenhuma alteração normativa, configuração de ferramenta, criação/renomeação/exclusão de chats, alteração de consumidor, clone, backup ou operação externa executada. Sem auditoria integral de segredos. As branches/PRs documentais são rastros intencionais; preservar PRs #4/#5 e demais refs sem nova autorização. Não criar Knowledge duplicado para proposta ainda candidata.

## 10. Continuidade condicional — etapa 06

Gate: homologação humana e integração comprovadas, conferência pós-merge e reconciliação registradas no encerramento abaixo. Somente após encerramento comprovado e autorização aplicável, iniciar 06 — Configuração de projetos IA neste mesmo chat. Usar arquitetura 03, protocolo 05 e diagnósticos D-03/D-10/D-12/D-21/D-22; definir instruções versionadas e compactas, composição de fontes, leitura seletiva e bootstrap contextual para adoção, continuidade e retomada. Não implementar configuração de consumidores nem tornar candidatos vigentes antes da etapa 10. Não iniciar 06 neste trabalho.

## 11. Encerramento da etapa 05

- Homologação humana registrada na [PR #35](https://github.com/jotaCorsino/orbita-development-model/pull/35#issuecomment-7193558014): “aprovado, pode continuar”. Autorização restrita à integração e encerramento documental do protocolo candidato, sem alteração normativa ou início de 06.
- Entrega aprovada: `e190195bf8e9ef39bba77ae8ef9a0b9ec2686067`; merge squash confirmado: `dcafdf86f66f145713ed5443eafe7b8124d181dc`. Árvore Git `ae511e044b9a82a03a0a70cce9263988ab578ee8` idêntica à entrega aprovada; quatro arquivos relidos diretamente na main. Preservados os 14 walkthroughs analíticos, as 14 etapas e a continuidade por iniciativa. Formulação inicial de um chat por etapa mantida como registro histórico, não como regra candidata concorrente.
- Fechamento editorial isolado conforme TRB-004, sem alteração normativa, de consumidores, chats ou configuração de ferramentas. Nenhum piloto ou medição de eficiência adicional. Nenhum temporário local criado; PRs #4/#5 e branches documentais preservadas intencionalmente; sem exclusão ou classificação de elegibilidade para descarte.
- Etapa 05 encerrada no escopo documental. Etapa 06 não iniciada; prosseguir neste mesmo chat somente após autorização específica. Conferir o pós-merge da alteração editorial na respectiva PR, sem abrir novo ciclo apenas para registrar seu próprio SHA.
