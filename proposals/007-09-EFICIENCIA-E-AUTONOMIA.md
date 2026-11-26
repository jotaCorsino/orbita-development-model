# ORB-EVO-001 — 09: Eficiência e autonomia

**Data:** 26/11/2026. **Estado:** refinamento candidato para homologação documental; não integrado nem vigente como norma geral. **Baseline:** `67b4b05183c5674344bdc2fd7c0a369baa7ef898`, PRs #41/#42 integradas; etapas 01–08 encerradas. **Autorização:** etapa 09 exclusivamente, no mesmo chat da iniciativa. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Fundamento e objetivo

A [auditoria integral](007-01-AUDITORIA-INTEGRAL.md) identificou D-03 (bootstrap), D-05 (proporcionalidade), D-06 (limite de escopo), D-09 (verificação), D-11/D-12 (tarefas e instruções), D-13 (gate operacional), D-16 (backlog), D-20 (maturidade), D-24 (Skills) e D-26 (ausência de medida). A [auditoria HUB](007-02-AUDITORIA-HUB-E-PROJETOS.md) documenta E-04 (desvio de runbook), E-05 (artefato/dados/destino), E-09 (ressalva de validação), E-10 (reuso de prova e teste pendente), E-12/E-13 (operação e preservação), E-15 (QA local), E-16/E-18 (dimensões de aceite e formalidade), E-19/E-20/E-21 (contexto, documentação e refs). Não há baseline quantitativa comparável; não inferir ganho a partir de exemplos ou quantidade de PRs.

Preservar [princípios](../docs/02-PRINCIPIOS.md), [papéis](../docs/03-PAPEIS-E-RESPONSABILIDADES.md), [fluxo](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md), [governança](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md), [Git e retomada](../docs/06-GIT-E-GITHUB.md), [aplicação e formalidade](../docs/08-APLICACAO-E-EVOLUCAO.md), [anti-padrões](../docs/09-ANTI-PADROES.md), [segurança](../docs/12-SEGURANCA-E-INTEGRIDADE.md) e [contrato](../onboarding/CONTRATO-DE-TRABALHO.md). Aproveitar [arquitetura 03](007-03-ARQUITETURA-METODOLOGICA.md), [limpeza 04](007-04-LIMPEZA-OPERACIONAL.md), [continuidade 05](007-05-CHATS-E-CONTINUIDADE.md), [configuração 06](007-06-CONFIGURACAO-DE-PROJETOS-IA.md), [Knowledge 07](007-07-EVOLUCAO-DO-KNOWLEDGE.md) e [documentação 08](007-08-DOCUMENTACAO-E-NOMENCLATURA.md). São desenhos candidatos homologados, ainda não regras vigentes.

| Alternativa | Avaliação |
| --- | --- |
| Aprovação humana para cada ação técnica | Reduz iniciativa do agente e multiplica intervenções sem garantir melhor entrega |
| Autonomia irrestrita após aprovação do objetivo | Confunde escopo, risco, acesso, aceite e operação; não adotar |
| Autonomia delimitada por autorização, risco e evidência | Recomendada; executar o que já está permitido, escalar somente decisão material e preservar gates |

**Princípio:** a autonomia é máxima dentro do escopo autorizado e mínima fora dele. Eficiência é entregar resultado correto, comprovado e aceito com menos esforço evitável, não executar menos testes, gerar mais commits ou reduzir aprovações necessárias.

## 2. Matriz de autoridade e risco

A classificação avalia a ação concreta e seu destino, não o tamanho do arquivo, duração da tarefa ou reputação da ferramenta. Os níveis de formalidade simples/intermediário/crítico já existem em docs 08; os perfis abaixo detalham quando aplicar controles, sem criar novos estados normativos, níveis obrigatórios de gestão ou classificação numérica.

### 2.1 Fatores observáveis

| Fator | Verificar |
| --- | --- |
| Autoridade | Tarefa, decisão, papel competente, restrições e gate já concedido |
| Escopo | Objetivo, critérios, incluído/excluído, comportamento/contratos afetados |
| Destino | Isolado, compartilhado, homologação, produção ou terceiro |
| Dados e acesso | Dados reais/sensíveis, credenciais, permissões, autenticação, autorização |
| Impacto | Reversibilidade, persistência, indisponibilidade, integridade, alcance e dependências |
| Custo e recursos | Orçamento, uso faturável, tempo de executor, criação de recursos e manutenção |
| Incerteza | Identidade/revisão/destino não confirmados, evidência faltante ou conflito |
| Aceite | Dimensões técnicas e não técnicas e decisão humana exigida |

Se um fator material for desconhecido, investigar primeiro de forma segura e autorizada. A falta de evidência não diminui risco nem justifica classificar a ação como baixa. O controle mais restritivo aplicável governa a ação afetada, sem tornar todas as demais ações da tarefa críticas.

### 2.2 Matriz operacional

| Perfil | Ações típicas | Autoridade e controles |
| --- | --- | --- |
| Simples / baixo impacto | Leitura autorizada, diagnóstico focal, correção documental curta, testes isolados, ajuste reversível local | Executar quando inerente à tarefa autorizada e permitido pelas regras; evidência mínima suficiente; revisão/homologação conforme gate existente |
| Intermediário / impacto delimitado | Mudança funcional em branch/ambiente isolado, integração de componentes, pacote de QA, correção inseparável de alcance conhecido | Escopo e critérios explícitos, refs, análise de dependências, regressão/segurança proporcional, evidências e homologação humana; decisões técnicas delegadas não exigem microaprovação |
| Crítico / impacto operacional ou material | Dados reais, produção, migração, autenticação/permissões sensíveis, recursos compartilhados, exclusão material, custo não aprovado ou publicação | Autoridade competente e autorização específica correspondente, runbook, impacto e recuperação, validação especializada conforme risco, evidência pós-operação; parar antes da ação se requisitos faltarem |

Projeto crítico mantém seus controles próprios mesmo para uma ação aparentemente simples. Classificação de risco não substitui autorização. Uma atividade de baixo impacto fora do escopo continua não autorizada; uma atividade de alto impacto pode prosseguir se todos os gates e controles específicos já foram satisfeitos, sem pedir o mesmo aceite novamente.

### 2.3 Decisão por tipo de ação

| Ação | Pode prosseguir sem nova decisão humana? |
| --- | --- |
| Consultar fontes e inspecionar estado relevante | Sim, dentro de acesso, finalidade e limites autorizados |
| Escolher implementação técnica reversível entre alternativas equivalentes | Sim, quando delegada e sem mudança material de requisito, risco, custo ou contrato |
| Corrigir erro da própria implementação/teste no escopo | Sim, respeitando refs, critérios e validação afetada |
| Corrigir pré-requisito inseparável | Sim, somente se cumprir o teste do §3 |
| Agrupar leituras, testes ou ações independentes autorizadas | Sim, se preservar limites, evidências e condições de parada |
| Preparar commit, PR ou artefato de entrega | Sim, se previsto no fluxo e sem publicação ou exposição adicional não autorizada |
| Homologar a própria entrega | Não; decisão do responsável |
| Alterar objetivo, critérios, arquitetura material, contrato ou direção criativa aprovada | Não; decisão competente, ainda que tecnicamente fácil |
| Iniciar nova tarefa ou etapa após gate pendente | Não; não inferir autorização de planejamento ou backlog |
| Merge, publicação, deploy ou migração | Somente quando o gate correspondente e a autorização já cobrem exatamente a ação/destino |
| Excluir dados, histórico, backup, ref ou recurso preexistente/material | Somente conforme autoridade e protocolo 04; limpeza de temporário próprio isolado segue autorização existente |
| Ativar recurso faturável, ampliar permissão ou compartilhar dado restrito | Não por inferência; autorização e política específicas |
| Aceitar risco relevante, dispensar controle obrigatório ou mudar procedimento homologado | Não por conveniência; decisão competente dentro de política e segurança aplicáveis |

Um gate humano pode abranger vários passos ou dimensões explicitamente identificados (artefato e operação, por exemplo), conforme docs 05. Não inventar obrigação de duas aprovações se a decisão já cobre ambas; não usar homologação de artefato para inferir operação. Políticas de plataforma e acesso não são contornadas por autorização do projeto.

## 3. Fronteira da correção inseparável

A arquitetura 03 já definiu a menor correção inseparável. Operacionalizar D-06 mediante cinco perguntas cumulativas:

1. Sem a correção, o critério autorizado não pode ser atendido corretamente ou com segurança?
2. A mudança é a menor necessária, diretamente vinculada ao resultado e demonstrável?
3. Preserva objetivo, requisitos, direção visual, interfaces/contratos, dados, arquitetura material e comportamento não relacionado?
4. Permanece dentro de autoridade, risco, destino, custo, dependências e impacto previamente autorizados?
5. Pode ser evidenciada e testada no mesmo escopo sem dispensar controle ou gate?

Se todas forem satisfeitas, executar e registrar no diff/entrega, sem microaprovação. Se alguma não for satisfeita, tratar como mudança de escopo ou decisão de risco; registrar problema no backlog/tarefa pertinente e solicitar somente a decisão necessária. Quando incerto, investigar antes de escrever. Risco crítico descoberto deve ser comunicado imediatamente e a ação afetada interrompida conforme contrato e docs 12; não transformar descoberta em autorização para reparo amplo.

Exemplos: ajustar importação diretamente necessária após renomear função interna autorizada, corrigir fixture incompatível com contrato comprovado, tratar entrada inválida inseparável do novo endpoint: possíveis no escopo, se as cinco condições forem verificadas. Migrar banco, trocar framework/editor, ampliar privilégios ou alterar fluxo de autenticação para contornar erro: decisões materiais, não correções automaticamente inseparáveis.

## 4. Escalonamento mínimo e comunicação

Antes de pedir intervenção humana, recuperar autorização, decisão, ref/gate e runbook existentes. Confirmar se o agente possui ferramenta e permissão, e se a ação foi delegada. Não transformar dificuldade instrumental em trabalho humano quando alternativa segura autorizada resolve.

| Situação | Comportamento |
| --- | --- |
| Ação delegada e requisitos satisfeitos | Executar e evidenciar, sem pedido intermediário |
| Informação técnica recuperável em fonte autorizada | Consultar seletivamente; não perguntar o que já está registrado |
| Conflito ou falta de prova | Investigar de forma focal; bloquear apenas ação dependente se persistir |
| Alternativas que alteram objetivo, custo, risco ou direção | Apresentar decisão necessária, alternativas, recomendação fundamentada e consequência |
| Gate humano pendente | Apresentar artefato/revisão, critérios, evidências, limitações e objeto do aceite |
| Acesso indispensável não disponível | Solicitar a menor ação ou evidência necessária; não expor credencial nem contornar sandbox |
| Trabalho interrompido | Recuperar checkpoint e preservar material; não repetir operação de efeito desconhecido |

Agrupar providências humanas compatíveis no único bloco terminal AÇÃO SUA, conforme COM-001. Cada uma indica ação, alvo e retorno esperado. Sem providência real, omitir. Decisão independente já autorizada pode continuar se não houver dependência, risco compartilhado ou regra de parada que a proíba. Não avançar para etapa formal seguinte sem gate correspondente; não solicitar novamente decisão comprovada. Uma autorização genérica de continuidade é interpretada no contexto do objeto imediatamente solicitado, não como liberação permanente de etapas futuras.

## 5. Reutilização de evidências e verificações

Evidência só é reutilizável na dimensão e no alcance que realmente comprovou. Reaproveitamento não equivale a novo teste executado. Preservar [Knowledge 07](007-07-EVOLUCAO-DO-KNOWLEDGE.md) e [continuidade 05](007-05-CHATS-E-CONTINUIDADE.md).

### 5.1 Predicado de reutilização

Antes de dispensar repetição, identificar:
- afirmação ou critério que a evidência deve sustentar;
- revisão, arquivos, artefato, configuração, dados, ambiente e dependências relevantes;
- método, resultado, limitações e fonte recuperável;
- delta desde a prova e impacto sobre seus pressupostos;
- gate ou política que exige repetição/independência;
- validade atual, inclusive fatos voláteis e autorização.

Se a prova cobre integralmente a dimensão pretendida, é recuperável, os pressupostos relevantes permanecem válidos e nenhum gate exige nova execução, reutilizar citando origem. Se cobre parcialmente, executar apenas lacuna e verificações afetadas; se mudança pode afetar resultado, revalidar o alcance pertinente; se evidência ausente, contraditória ou insuficiente, executar validação necessária quando autorizada. Não tomar ausência de diff em arquivo isolado como prova de ausência de impacto transitivo.

| Evidência anterior | Reutilização permitida | Revalidação necessária |
| --- | --- | --- |
| Teste unitário em revisão imutável e dependências fixadas | Mesma afirmação e pressupostos | Alteração afetada, requisito de independência ou lacuna de cobertura |
| Build/hash de pacote | Identidade e integridade do artefato correspondente | Artefato reconstruído diferente; instalação e runtime são provas distintas |
| QA visual aprovado | Mesma referência, renderização e condições comprovadas | Mudança visual/UX, viewport relevante, assets ou ambiente afetados |
| Teste parcial com caso negativo pendente | Reusar resultado positivo válido e testar pendência | Não declarar suíte integral aprovada |
| Inventário de backup, serviço ou permissão | Referência histórica e orientação | Confirmar estado atual quando operação depender dele |
| Aprovação humana | Mesmo objeto, revisão/escopo e condição aceitos | Mudança material, ressalva pendente ou gate independente |
| Prova de sandbox/ambiente local | Diagnóstico naquele contexto | Mudança de contexto ou destino real |
| Merge/árvore Git | Conteúdo integrado e correspondência da revisão | Estado de produção, artefatos externos e dados não comprovados |

A prova reutilizada deve ser distinguível de execução nova, de teste não executado e de N/A justificado. Não contar reutilização como nova passagem de teste. A verificação antes de uma mutação e o pós-check correspondente não são redundantes: provam momentos diferentes. Revalidar identidade, destino e condição de segurança imediatamente antes de ação sensível quando necessário. Mudança de gate/ambiente não invalida toda prova indiscriminadamente, mas exige avaliar pressupostos.

## 6. Eficiência de execução e recursos

### 6.1 Sequência preferencial

1. Recuperar tarefa, autorização, critério, fontes, estado e Knowledge pertinentes, sem releitura integral automática.
2. Consultar procedimento existente e identificar o menor caminho seguro. Preferir ferramentas disponíveis e compatíveis, reutilizar script/teste aprovado; não criar método, backup, clone ou dependência novos sem necessidade.
3. Selecionar perfil de risco e verificações suficientes para as dimensões afetadas. Agrupar leituras e verificações independentes; manter operações dependentes em ordem.
4. Executar o escopo autorizado, corrigir falha focal e preservar prova útil. Evitar ciclos de tentativa cega; antes de repetir comando que falhou, verificar causa ou hipótese testável, mudar condição relevante e definir resultado esperado.
5. Em interrupção ou retorno parcial, recuperar estado e ponto pendente; não reexecutar mutação só para obter log perdido. Verificar o estado externo antes de repetir ação de resultado desconhecido.
6. Apresentar evidências proporcionais, distinguir o que foi executado, reutilizado, não testado, homologado e publicado; aplicar verificação final e limpeza quando pertinente.

### 6.2 Agrupamento e divisão

Agrupar ações quando têm mesmo objetivo/gate, autoridade e contexto compatíveis, dependências conhecidas e evidência individual distinguível. Exemplo: ler arquivos canônicos em uma consulta, rodar testes de regressão relacionados em suíte, corrigir conjunto editorial do mesmo estado em um commit. Uma única autorização pode delimitar lote fechado com alvos, condições, limites e critérios; cada item respeita seu preflight e resultado. Não agrupar tarefas que dependem de aceite intermediário, têm responsáveis/destinos incompatíveis, riscos diferentes que exigem controle separado ou mudanças materiais independentes. Não usar paralelismo em escritas que competem pelo mesmo recurso, branch, ambiente ou dado.

Tamanho de tarefa adequado: uma entrega coerente, revisável e com critério verificável. Dividir quando aumenta capacidade de diagnóstico/rollback ou quando decisão humana intermediária muda direção, não para multiplicar IDs, commits, PRs ou chats. Etapa formal e tarefa interna são distintas; preservar granularidade 05. Correções editoriais pós-merge só exigem PR adicional quando houver resíduo real e o fluxo autorizado a previr; não criar fechamento que apenas registra o próprio fechamento.

### 6.3 Escolha de execução e ferramentas

A escolha considera adequação, capacidade real, segurança, isolamento, reprodutibilidade, custo e necessidade de independência. Executar localmente ou em ambiente isolado quando suficiente, respeitando política aplicável. O [perfil do mantenedor QA local-first](../onboarding/PERFIL-MANTENEDOR-VALIDACAO-LOCAL.md) é preferência operacional de escopo declarado, não regra universal. CI/CD obrigatório, revisão independente e compliance do projeto não podem ser dispensados por economia. Runner indisponível não equivale a teste aprovado; alternativa deve cobrir o mesmo critério e ser permitida. Não ativar faturamento, infraestrutura, novos acessos ou serviços sem autoridade e necessidade.

Skills (09A) apoiará escolha de técnica profissional conforme problema, alternativas, esforço, contraindicações e dimensão de aceite; Tools (09B) apoiará execução governada, versão, licença e segurança. Não admitir nenhuma Skill/Tool nesta etapa nem tornar ferramenta dependência obrigatória por preferência. Uma técnica rotineira delegada pode ser escolhida sem microgate; adoção que altera escopo, custo, risco ou direção exige decisão. Nenhuma métrica justifica reduzir segurança, critérios de aceite, acessibilidade ou QA necessário.

## 7. Avaliação mensurável — desenho para etapa 11

O [ROADMAP](../ROADMAP.md) exige matriz/checklist validada em projetos reais para v0.4. Esta etapa define protocolo candidato, não comprova maturidade. Usar a menor coleta útil; não instalar telemetria, criar rastreamento de pessoas ou registrar conteúdo sensível. Definir antes do piloto perguntas, perfil, critérios e comparação. Métricas não são metas individuais ou autorização para omitir trabalho necessário.

### 7.1 Baseline e comparação

- Unidade primária: tarefa autorizada com objetivo, perfil de risco, critérios e gate identificados. Para recuperação de contexto, episódio de retomada. Para reincidência, oportunidade comparável de repetir erro previamente conhecido.
- Baseline: executar/observar fluxo vigente anterior à integração candidata ou recuperar registros históricos suficientes com revisão, escopo, ambiente e fontes. Não usar estimativa retrospectiva não comprovada como medição. Se dados anteriores não existirem, coletar baseline prospectiva em cenário autorizado/isolado antes da variante candidata; nunca desfazer controle vigente ou repetir operação real arriscada só para medir.
- Comparação: tarefas equivalentes por tipo, risco, critérios, ambiente e dependências; fixar quando possível versões de código, ferramenta/modelo, fixtures, acesso, instruções e condições. Separar efeito de mudança de modelo, hardware, rede, fila, aprendizagem e tarefa. Em ensaio pareado, restaurar estado inicial isolado ou usar casos equivalentes e evitar contaminação de conhecimento entre variantes.
- Selecionar ao menos perfis distintos conforme etapa 11: tarefa simples/documental, mudança funcional/integração e caso sensível ou operacional simulado/isolado quando autorizado. Não prometer tamanho amostral, projeto participante ou acesso antes da autorização. Reportar N por perfil e condição, falhas, exclusões justificadas e dados ausentes. Se não houver comparabilidade, apresentar observação descritiva sem atribuir ganho causal.
- Mesmo critério de aceite, segurança e fidelidade nas variantes. Não comparar entrega parcial com homologada. Registrar tarefa incompleta, bloqueada ou rejeitada, sem removê-la do denominador por conveniência. Medir custo de preparação/manutenção do método, não apenas execução final.

### 7.2 Indicadores e definições

| Indicador | Definição e unidade | Fonte / limite |
| --- | --- | --- |
| Tempo ativo do agente | Soma de intervalos de execução/diagnóstico observáveis por tarefa, sem espera humana; minutos | Logs/timestamps disponíveis; se indisponível, não estimar |
| Tempo de ciclo | Início autorizado até gate/encerramento definido, incluindo esperas; minutos/horas | Registro de tarefa/PR e timestamps; declarar definição de fim e casos não encerrados |
| Intervenções humanas necessárias | Episódios de decisão/ação indispensável por tarefa; contar separadamente gates exigidos e pedidos evitáveis | Mensagens/registro de gate; múltiplos itens no mesmo bloco contam como ações distintas se independentes, não contar mensagens repetidas como novos gates |
| Pedidos evitáveis | Solicitações repetidas ou delegadas/recuperáveis que revisão identifica com evidência | Classificação justificada; distinguir falta de acesso legítima |
| Repetição evitável | Verificações ou diagnósticos repetidos sem mudança de pressuposto, lacuna ou exigência de gate / verificações elegíveis observadas | Registro de execução e prova anterior; denominador explícito; não contar pre/pós distintos |
| Reuso correto | Evidências reutilizadas com predicado satisfeito / reutilizações observadas | Registro de origem e revisão de validade; reportar reutilizações indevidas separadamente |
| Recuperação de contexto | Episódios que recuperam identidade, tarefa, autorização, ref, último gate e próxima ação corretos / episódios avaliados; tempo quando medido | Checkpoint e fonte primária; não medir apenas número de arquivos lidos |
| Retrabalho | Tempo ativo de correções decorrentes de erro de execução, perda de contexto ou desvio de critério, separado de evolução legítima de requisito | Evidência de causa, não classificar toda revisão humana como desperdício |
| Reincidência | Erros conhecidos repetidos / oportunidades comparáveis em que aprendizado era aplicável e acessível | Knowledge/troubleshooting e evidência; não supor causalidade se base não consultável |
| Recursos | Tokens, chamadas, minutos de runner, custo real quando disponíveis | Medição fornecida pela plataforma, sem inferir valores ocultos; distinguir unidade e preço |
| Qualidade e segurança | Critérios satisfeitos/previstos, gates cumpridos, defeitos/regressões, violações de escopo e falhas de segurança observadas | Dimensão por tarefa; sem agregação que esconda requisito crítico |
| Encerramento | Inconsistências, resíduos sem justificativa, evidência perdida, ações pendentes não classificadas | Verificação proporcional 04/08; não inventar ausência de resíduos locais |

Relatar contagens e denominadores, mediana e faixa quando N permite, dados ausentes como não medidos (não zero). Para comparação percentual de uma medida menor-é-melhor: (baseline - variante) / baseline × 100, apenas com baseline positiva, unidade e escopo equivalentes; baseline zero não define percentual. Para taxas de qualidade, reportar diferenças em pontos percentuais e contagens. Não combinar medidas heterogêneas em um único “score ÓRBITA” arbitrário; não publicar ganho quando evidência insuficiente.

### 7.3 Registro mínimo do piloto (ilustrativo)

```text
Caso / perfil / objetivo e critérios:
Condição: baseline ou variante; revisão do método, tarefa e ambiente:
Autorizações e gates previstos:
Início/fim observados; tempo ativo/espera (se medidos):
Verificações executadas, reutilizadas, pendentes; referências:
Intervenções necessárias/evitáveis e justificativa:
Retrabalho, falhas, resíduos e limites:
Resultado por dimensão; gate humano e estado real:
Comparabilidade, dados ausentes e evidência:
```

Reutilizar registros existentes; formulário apenas opção para piloto, não obrigação por tarefa. Dados devem ser sanitizados, acesso autorizado e retenção proporcional. Não coletar prompts privados integrais, credenciais ou dados de clientes.

### 7.4 Critério de avaliação

A variante só demonstra eficiência se mantiver critérios/gates e segurança aplicáveis, sem regressão material, e houver melhoria observada em indicador pertinente com comparação válida. Se houver regressão, avaliar causa, corrigir e repetir somente cenário afetado em condições comparáveis; não ocultar falha ou trocar denominador. Se resultados forem inconclusivos, declarar inconclusivos. Qualquer violação de autoridade, exposição indevida, perda de dados ou gate omitido impede tratar o caso como sucesso; analisar com responsável. O responsável humano decide adoção/maturidade após evidências. Não fixar meta percentual universal sem baseline nem alterar estados do roadmap v0.x nesta etapa.

## 8. Walkthroughs documentais

Os casos abaixo confrontam o desenho. Não são testes de execução, pilotos ou medidas de economia.

| Caso | Situação | Resolução esperada |
| --- | --- | --- |
| C01 — leitura focal | Fonte autorizada contém decisão anterior | Recuperar diretamente, não pedir repetição (§4) |
| C02 — ajuste delegado | Correção local reversível atende critério | Executar e evidenciar no escopo (§2) |
| C03 — correção inseparável | Import interno precisa acompanhar mudança autorizada | Aplicar cinco condições; corrigir mínimo (§3) |
| C04 — expansão | Agente propõe refatoração de módulo independente | Registrar fora do escopo; gate próprio (§3) |
| C05 — operação real | Artefato homologado, destino não autorizado | Não implantar; recuperar gate específico (§2) |
| C06 — autorização combinada | Artefato e deploy explicitamente autorizados no mesmo gate | Executar runbook e pós-check sem nova microaprovação (§2) |
| C07 — procedimento existente | Agente tenta substituir instalação por conveniência | Preservar método vigente ou elevar mudança (§§4,6) |
| C08 — risco crítico | Descoberta de falha relevante fora do escopo | Comunicar e parar ação afetada; não reparar amplamente sem decisão (§3) |
| C09 — prova parcial | Caso positivo válido, negativo pendente | Reutilizar prova e executar lacuna (§5) |
| C10 — dependência mudou | Mesmo arquivo de teste, ambiente diferente | Avaliar impacto e revalidar pressupostos (§5) |
| C11 — prova imutável | Hash e conteúdo aprovado permanecem iguais | Reutilizar identidade; não inferir implantação (§5) |
| C12 — teste visual | Build válido, UX rejeitada | Corrigir dimensão exigida, respeitar gate (§§2,5) |
| C13 — runner indisponível | QA local autorizado cobre critérios | Usar alternativa comprovável, declarar limites (§6) |
| C14 — cobrança | Teste exige recurso pago não aprovado | Não ativar; propor alternativa ou decisão (§§2,6) |
| C15 — interrupção | Operação externa terminou sem retorno conhecido | Verificar destino antes de repetir (§6) |
| C16 — lote | Testes independentes com mesma autorização | Agrupar preservando resultados individuais (§6.2) |
| C17 — dependência de gate | Etapa seguinte depende de avaliação humana | Parar; não agrupar além da autorização (§6.2) |
| C18 — limpeza | Temporário próprio isolado, ciclo autorizado | Descartar delimitadamente e verificar; não tocar backup (§2; 04) |
| C19 — encerramento | Resumos coerentes após merge | Não abrir PR adicional apenas por ritual (§6.2) |
| C20 — métrica ausente | Plataforma não informa tokens reais | Não medido, não inventar consumo (§7) |
| C21 — ganho aparente | Variante mais rápida omite teste obrigatório | Não aceitar como melhoria (§7.4) |
| C22 — baseline incomparável | Tarefas de complexidade diferente | Segmentar ou declarar limite; sem percentual causal (§7) |

Os 22 cenários têm tratamento conceitual; não houve teste real em agentes, operação, medição ou classificação quantitativa de eficiência.

## 9. Integração e continuidade

| Diagnóstico | Tratamento candidato | Materialização |
| --- | --- | --- |
| D-03/D-12 | Recuperação seletiva, referências e runbook | 06–08, 10–11 |
| D-05/D-06 | Matriz de autoridade e risco, correção inseparável e escalonamento mínimo | 10–11 |
| D-09 | Reuso de evidências, pre/pós proporcional e encerramento sem ritual | 08, 10–11 |
| D-11/D-13 | Critérios verificáveis, dimensões e autorização operacional | 06/08, 10–11 |
| D-16 | Backlog não é execução; registro sem duplicação | 08, 10–11 |
| D-20/D-26 | Protocolo de baseline, indicadores, qualidade e limites | 11–12 |
| D-24 | Critério de escolha de técnicas sem impor framework | 09A |

Na etapa 10, materializar matriz e critérios nas fontes normativas competentes (docs 02/05/08/12, contrato e templates afetados), preservando protocolo operacional 04, recuperação 05–07, verificação final 08 e COM-001. Evitar duplicar matriz em cada template. Na etapa 11, selecionar pilotos autorizados, registrar baseline e aplicar comparação sem comprometer segurança. A fase v0.4 e eventual publicação permanecem dependentes dos critérios vigentes e de decisão humana.

Critério documental: matriz de risco/autoridade, correção inseparável, escalonamento, predicado de reuso, execução proporcional, agrupamento, indicadores/baseline/guardrails e 22 cenários confrontados; reconciliar README, ROADMAP e PROP-007. 8/14 etapas homologadas até aceite e integração de 09. Nenhuma alteração normativa, configuração aplicada, consumidor, ferramenta, acesso, faturamento, clone, backup, operação ou varredura integral de segredos. PRs #4/#5 e branches documentais preservadas; refs da entrega intencionais. Não criar Knowledge duplicado.

Gate: homologação humana da proposta, integração autorizada, conferência pós-merge e reconciliação documental. Após encerramento comprovado e autorização específica, continuar neste mesmo chat com 09A — ÓRBITA Skills: catálogo profissional, taxonomia, curadoria, ficha, seleção proporcional, fontes primárias, autoria/licença, versões, contraindicações, evidência e piloto candidato UI/UX (Double Diamond e técnicas pertinentes). Distinguir Skill de Knowledge, método e Tool; não impor framework, nem alegar pesquisa/execução sem prova. 09B permanece independente e não autorizada. Não iniciar 09A nesta etapa; integração normativa em 10.
