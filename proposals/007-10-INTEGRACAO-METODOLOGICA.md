# ORB-EVO-001 — 10: Integração metodológica

**Data:** 26/11/2026. **Estado:** especificação consolidada candidata homologada documentalmente, integrada pela PR #49 e verificada na main; não publicada como release. **Baseline:** `f6e7132e9e418d046fef6c4f9a03e1cc87b1aca6`. Etapas 01–09B encerradas; PRs #47/#48 integradas. Autorização exclusiva da etapa 10, no mesmo chat. [Plano](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Decisões de materialização

Integrar normas nas fontes existentes e referências nos templates, preservar histórico e exemplos. AGENTS raiz auto-referente à revisão autorizada, sem pin circular. Não criar nova versão numérica, licença, política de branch, serviço, repositório, configuração efetiva de agente ou adoção de consumidor. Manter sete fichas Skills candidatas e contrato Tools; decisão posterior de neutralidade retira toda ficha de ferramenta particular. A revisão candidata rege avaliação autorizada, não substitui automaticamente contratos adotados. Matriz e protocolos detalhados permanecem rastreáveis nas propostas homologadas, sem duplicar integralmente cada uma em templates.

## 2. Rastreabilidade das 28 constatações

| Diagnóstico | Fonte candidata / resolução | Limite |
| --- | --- | --- |
| D-01 | docs 03, 05, 10: autoridade modular por assunto, conflito e versão | Teste de composição em 11 |
| D-02 | docs 11 fonte canônica; resumos e referências em docs 04/08/10 e onboarding mantidos para leitura contextual | Preservados passos e exceções; não remover redundância pedagógica útil |
| D-03 | docs 07, onboarding, AGENTS e prompts: recuperação seletiva, revisão adotada | 15 leituras para adoção nova preservadas |
| D-04 | docs 04/05: seis estados, Pausado, aceite/integração/publicação distintos | Sem novo estado |
| D-05 | docs 05, 02: autoridade e risco, proporcionalidade | Avaliação empírica em 11 |
| D-06 | docs 05/09/12, contrato: correção inseparável, fronteira de autorização | Sem expansão silenciosa |
| D-07 | docs 07 e contrato: chat por iniciativa, handoff mínimo, TRB-003 preservado | Sem manipulação de chats |
| D-08 | docs 06 e verificação final: classificação, autoridade, pré/pós e exceções | Nenhuma exclusão |
| D-09 | docs 04/05/08, contrato e verificação final: fontes, reuso, sem PR, sem ritual | Sem repetição indevida |
| D-10 | onboarding §4 e checklist: AGENTS, Knowledge, backlog | Fundação antes de funcionalidade |
| D-11 | TASK/IMPLEMENTACAO: ID, autorização/ref, critérios e dimensões | Proporcional |
| D-12 | AGENTS, prompts: Knowledge, runbook, origem, gate, revisão | Sem configurar agentes reais |
| D-13 | HOMOLOGACAO: autorização operacional, origem/destino e evidência | Gate combinado permitido se explícito |
| D-14 | contrato §9: cada resposta; COM-001 íntegra | Sem tarefa artificial |
| D-15 | docs 08, templates/índice Knowledge: critérios, prova, promoção, validade | Índice vazio mantido; uso real 11 |
| D-16 | docs 08 e README: backlog separado da execução, referência a mecanismo aprovado | Sem duplicar backlog |
| D-17 | PROP-001 §8: PR #3 mergeada verificada; situação histórica explicitada e link de roadmap corrigido | Critérios de dois projetos não declarados atingidos |
| D-18 | docs 07/08: distinção de história e status atual | PROP-003/004 preservadas |
| D-19 | docs 06: proteção de refs e conteúdo; PRs #4/#5 preservadas | Sem exclusão/fechamento |
| D-20 | ROADMAP: requisitos de maturidade preservados | Pilotos/cases em 11, avaliação 12 |
| D-21 | docs 07/10, AGENTS: adoção por revisão e versão aplicada | Licença/release em 12 |
| D-22 | AGENTS raiz, README público sem painel compulsório | Proteção de branch em 12 |
| D-23 | docs 08 NOM-001, contrato/templates, exemplos | Sem renomear legado |
| D-24 | docs 08, Skills: escolha humana, recomendação, curadoria | Sete fichas candidatas preservadas |
| D-25 | docs 10, Tools: admissão, direitos, integração e limites | Nenhuma Tool admitida; catálogo neutro após decisão posterior |
| D-26 | docs 05 e ROADMAP referenciam protocolo 09 §7 | Sem métrica empírica até 11 |
| D-27 | docs 03/12, Knowledge/Tools: acesso, sanitização e fronteiras | Sem auditoria integral de segredos |
| D-28 | README-template: link relativo ao arquivo gerado preservado | Validar no contexto correto |

## 3. Cobertura das propostas homologadas

| Origem | Destino competente |
| --- | --- |
| [03 — Arquitetura](007-03-ARQUITETURA-METODOLOGICA.md) | docs 01/03/05/10/12 |
| [04 — Limpeza](007-04-LIMPEZA-OPERACIONAL.md) | docs 06, contrato §11, checklist final |
| [05 — Continuidade](007-05-CHATS-E-CONTINUIDADE.md) | docs 07, contrato §9, AGENTS |
| [06 — Configuração](007-06-CONFIGURACAO-DE-PROJETOS-IA.md) | docs 07/11, onboarding e prompts |
| [07 — Knowledge](007-07-EVOLUCAO-DO-KNOWLEDGE.md) | docs 08, índice/templates, contrato |
| [08 — Documentação](007-08-DOCUMENTACAO-E-NOMENCLATURA.md) | docs 04/07/08/11, README-template, PROP-001 |
| [09 — Autonomia](007-09-EFICIENCIA-E-AUTONOMIA.md) | docs 02/05/09/12, contrato, ROADMAP |
| [09A — Skills](007-09A-ORBITA-SKILLS.md) | docs 08, índice Skills, contrato/AGENTS |
| [09B — Tools](007-09B-ORBITA-TOOLS.md) | docs 10/12, índice Tools, contrato/AGENTS |

As propostas são registros das decisões e exemplos detalhados; as normas da candidata ficam nas fontes competentes. Em conflito, observar decisão posterior explícita (em especial escolha humana de métodos em 09A e chat por iniciativa em 05), não recência genérica. Preservar COM-001, seis estados, preflight operacional, fundação remota antes de bootstrap e funcionalidade, dimensões não técnicas, segurança, preservação de trabalho local, numeração contra main, backlog e Knowledge. O método continua independente de fornecedor. Não substituir conteúdo vigente de outros projetos.

## 4. Escopo e verificações

Alterações limitadas a documentação do núcleo, onboarding, templates, índices, PROP-001, plano e AGENTS raiz. 34 arquivos previstos incluindo este relatório. Nenhuma exclusão ou renomeação. Verificação estática por comparação de baseline, diff, blobs, links relativos novos/afetados (template de README gerado é exceção contextual), 14 etapas, matriz de 28 diagnósticos, seis estados, COM-001, fichas/relatórios anteriores e índice vazio. Na primeira execução do verificador, três links de diretório foram classificados incorretamente por barra final; corrigida normalização. Na segunda, um link relativo preexistente de PROP-001 apontava para caminho inexistente e foi corrigido para o ROADMAP da raiz; o link de Knowledge do README-template foi preservado no contexto gerado. A preparação inicial excedeu o limite de chamadas do conector sem alterar a main; a entrega foi dividida em commits na mesma branch. Registro de resultados concretos na PR; não confundir revisão estrutural com prova de execução por agentes. Não prometer auditoria exaustiva de semântica automatizada, links externos ou teste de ambiente.

## 5. Gate e continuidade

12/14 etapas homologadas após aceite da integração. Homologação humana e integração comprovadas; reconciliação e conferência pós-merge registradas no encerramento. Etapa 11 — validação prática: selecionar pilotos autorizados de perfis distintos, baseline conforme 09 §7, critérios técnicos/não técnicos, recuperação/autoridade/Skills/Tools, evidência, falhas e correções proporcionais. Não implantar Tool não admitida, usar dados reais ou modificar consumidores sem autorização específica. Etapa 12: auditoria, licença, decisão de publicação e critérios vigentes de maturidade. Não iniciar 11 nesta etapa.

## 6. Encerramento da etapa 10

- Homologação humana registrada na [PR #49](https://github.com/jotaCorsino/orbita-development-model/pull/49#issuecomment-7196903635): “aprovado, pode continuar”, em resposta direta ao pedido de homologação e integração. Aceite documental da especificação candidata, restrito à integração e ao encerramento de 10.
- Entrega aprovada: `ea8039498ec4489ef1dd35b1f82f46a3e7bee5cb`; merge squash confirmado: `b7fa46c686b938608d6381b87817b0517cc7b1de`. Árvore Git `3c462ef5d0513b759e4312d86b605c0f64999795` idêntica à entrega aprovada; comparação integral das árvores recursivas confirma os 68 arquivos e seus blobs, incluindo os 34 arquivos da alteração. Preservados matriz D-01–D-28, 14 etapas, seis estados e Pausado, COM-001, seleção metodológica humana, fichas Skills e limites Tools.
- Fechamento editorial isolado: README, ROADMAP, PROP-007 e este relatório reconciliam o estado após o merge. Nenhuma alteração de regra aprovada, licença, proteção de branch, consumidor, ambiente, ferramenta ou publicação; nenhum teste empírico. PRs #4/#5 e branches documentais preservadas intencionalmente. Sem temporários locais criados.
- Etapa 10 encerrada no escopo documental. Etapa 11 não iniciada; continuar neste mesmo chat após autorização específica. Conferir pós-merge da alteração editorial na respectiva PR, sem criar outro ciclo apenas para registrar seu SHA.

**Decisão posterior ISO-001:** a homologação de 10 precedeu a neutralização; não utilizar os antigos exemplos ou fichas particulares como fonte. O contrato metodológico permanece; o catálogo atual não admite ferramentas. A comparação histórica da árvore de 10 descreve aquele gate, não o estado posterior.
