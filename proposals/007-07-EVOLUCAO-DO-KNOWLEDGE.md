# ORB-EVO-001 — 07: Evolução do Knowledge

**Data:** 26/11/2026. **Estado:** refinamento candidato para homologação documental; não integrado nem vigente como norma geral. **Baseline:** `e9d598c6bb067461a455198cfeacdffeb11c4197`, PRs #37/#38 integradas; etapas 01–06 encerradas. **Autorização:** etapa 07 exclusivamente, no mesmo chat da iniciativa. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Fundamento e decisão

A [PROP-006](006-KNOWLEDGE-BASE-DE-CONHECIMENTO-OPERACIONAL.md) foi homologada e incorporada pela PR #21 em 04/11/2026. Preservar integralmente seu fundamento: memória operacional externa e versionada, índice rápido, registro de conclusões comprovadas e reutilizáveis, consulta proporcional, três estados de validade, revalidação de fatos voláteis e distinção de fontes. Knowledge melhora o contexto recuperável; não treina o modelo nem autoriza ações.

A [auditoria integral](007-01-AUDITORIA-INTEGRAL.md) identificou D-15 (maturidade, não ausência), D-03/D-12 (recuperação e aplicação), D-16 (fronteira com backlog), D-27 (exposição) e D-26 (ausência de métrica). A [auditoria HUB](007-02-AUDITORIA-HUB-E-PROJETOS.md) traz E-04/E-10/E-12/E-14/E-19/E-22: perda de procedimento vigente, reutilização de evidência anterior, distinção entre fatos históricos e atuais, backup ausente apesar de registro antigo e limites de compartilhamento. São evidências documentadas de problemas e práticas pertinentes, não demonstração de adoção da estrutura KN em todos os consumidores ou de economia mensurada.

Na baseline da etapa 07, a árvore Git não truncada contém apenas knowledge/README.md sob knowledge/; seu blob é idêntico ao template de índice. Zero entradas não é defeito por si só. Nenhum consumidor foi reinspecionado nesta etapa. Não inventar aprendizados para preencher a base.

| Alternativa | Avaliação |
| --- | --- |
| Manter a base sem detalhar evidência, escopo e promoção | Preserva simplicidade, mas deixa margem para reutilização fora da condição comprovada |
| Criar banco vetorial, memória global automática e ingestão de logs | Complexidade, custo, risco de exposição e propagação de erros sem benefício demonstrado |
| Evoluir o índice e a ficha existentes com critérios operacionais, revalidação por evento e promoção controlada | Recomendada; amplia confiabilidade sem exigir infraestrutura, nova taxonomia rígida ou novo gate universal |

**Princípio:** descobrir uma vez, comprovar, registrar, recuperar seletivamente e revalidar quando necessário. A base deve reduzir redescoberta, não substituir julgamento, autorização ou inspeção do estado real.

## 2. Escopo, responsabilidade e fronteiras

Segundo a [arquitetura candidata](007-03-ARQUITETURA-METODOLOGICA.md), Knowledge pode existir no escopo do projeto, método especializado, HUB ou núcleo. Cada base responde a seu responsável e à visibilidade da fonte. Não há obrigação de criar repositório separado nem de manter cópias em todos os níveis.

| Escopo | Conteúdo apropriado | Limite |
| --- | --- | --- |
| Projeto | Particularidades comprovadas do produto, ambiente, dependências, diagnóstico, limitações | Não generalizar ambiente local nem expor dados |
| Método especializado | Aprendizados comprovados no domínio e condições de aplicação | Não transformar experiência de um consumidor em regra universal |
| HUB opcional | Conhecimento compartilhável entre projetos vinculados, no alcance da organização | Não presumir acesso cruzado, titularidade ou autorização |
| Núcleo ÓRBITA | Aprendizados metodológicos generalizáveis, sanitizados e aprovados | Não incorporar configuração, caso privado, regra local ou procedimento específico como universal |

| Fonte | Pergunta respondida |
| --- | --- |
| README/docs/decisão/runbook canônico | O que o produto é, qual regra vale e como operar? |
| Tarefa, roadmap e backlog | O que está autorizado, planejado ou apenas identificado para o futuro? |
| Troubleshooting/evidência | O que ocorreu, como foi investigado e o que ficou comprovado? |
| Knowledge | Qual conclusão observada é reutilizável, em quais condições e com quais limites? |
| Skills | Qual técnica profissional pode ser selecionada para resolver o problema? |
| Tools | Qual instrumento pode apoiar a tarefa autorizada? |

Se um aprendizado mudar contrato, requisito, procedimento ou política, a alteração deve ocorrer na fonte competente mediante gate aplicável; Knowledge apenas aponta a consequência operacional comprovada. Não duplicar o runbook nem transformar Knowledge em catálogo de Skills/Tools. Hipóteses e testes pendentes permanecem na investigação/tarefa; não criar quarto estado para acomodá-los.

## 3. Admissão e qualidade da evidência

Manter os critérios da PROP-006: reutilizável, operacionalmente relevante, não trivial, suficientemente comprovada e compactável. Antes de registrar, responder:

1. Qual decisão, diagnóstico, erro ou procedimento futuro esta conclusão pode influenciar?
2. Qual evidência sustenta exatamente a afirmação e quais dimensões ela não prova?
3. Em que versão, ambiente, condição e escopo a conclusão vale?
4. Existe entrada equivalente ou documentação canônica que torna a nova entrada redundante?
5. A informação pode ser preservada com segurança, sem credenciais, dados sensíveis ou detalhe privado desnecessário?

### 3.1 Força e alcance da prova

Não criar notas numéricas de confiança ou hierarquia universal de evidências. A prova deve corresponder à natureza da conclusão.

| Tipo de evidência | Pode sustentar | Não sustenta sozinha |
| --- | --- | --- |
| Código, contrato ou configuração em revisão identificada | Comportamento especificado ou propriedade estática observável | Execução real ou implantação |
| Teste reproduzível no ambiente identificado | Resultado e condições efetivamente testados | Outros ambientes, casos não testados ou causa não isolada |
| Inspeção direta e resultado operacional datado | Estado observado no destino e momento verificados | Permanência futura ou ausência de risco |
| Relato registrado de responsável ou executor | Ocorrência relatada, com limites explicitados | Estado técnico diretamente inspecionado pelo agente |
| Documentação de fornecedor | Comportamento documentado na versão e condições descritas | Compatibilidade no consumidor ou resultado local |
| Hipótese ou inferência sem comprovação suficiente | Próximo diagnóstico a realizar | Knowledge Vigente |

Uma tentativa que falhou pode produzir aprendizado sobre o erro **observado**; não atribuir causa se não foi isolada. Um teste sintético pode sustentar uma conclusão sintética, não produção. Uma evidência parcial pode sustentar afirmação parcial, desde que a limitação seja explícita. Distinguir evidência primária, relato e conclusão inferida, conforme a afirmação. Se a informação existir apenas em memória de chat, recuperar prova persistente ou registrar a limitação na tarefa; não promovê-la por conveniência.

## 4. Organização e ficha candidata

Preservar a estrutura atual:

```text
knowledge/
├── README.md
└── KN-xxx-descricao-curta.md
```

Usar nome humanizado, ID persistente e unicidade no escopo da base; identificar origem/base ao compartilhar IDs entre projetos. Categoria serve à busca, não à autoridade. Aproveitar categorias existentes (Ambiente, Operação, Pitfall, Integração, Restrição ou outra); usar rótulo legível equivalente, por exemplo Armadilha, sem renomear registros existentes em massa. Acrescentar categoria somente se melhorar recuperação real. Não exigir subpastas, tags, banco de dados, índice vetorial ou taxonomia universal. Se uma base crescer a ponto de dificultar consulta, subdividir/filtrar o índice sob autorização, mantendo ponto de entrada estável e referências válidas.

O índice deve permanecer compacto: ID, categoria, resumo discriminante, estado, última verificação e link, como atualmente. Se houver necessidade demonstrada, resumo pode indicar escopo breve ou condição; não adicionar colunas obrigatórias para todos. O índice é derivado e precisa corresponder à entrada. A entrada é canônica para a conclusão Knowledge, mas não para normas ou estado operacional.

### 4.1 Ficha candidata (extensão da ficha vigente)

```markdown
# KN-[NNN] — [Título humano]

- Categoria: [categoria existente ou necessária]
- Estado: [Vigente / Revalidar / Obsoleto]
- Verificado em: [AAAA-MM-DD; data da evidência, não da edição]
- Origem: [tarefa / PR / troubleshooting / fonte]
- Escopo: [projeto/domínio, versão/ambiente e condições relevantes]

## Conhecimento
[Uma conclusão comprovada e reutilizável, com limite explícito.]

## Aplicação
[Quando consultar, como influencia a ação e o que não autoriza.]

## Evidência / origem
[Referência recuperável e revisão; o que foi observado/testado,
ambiente e limitações. Relato identificado como relato, se aplicável.]

## Revalidar quando
[Evento, condição, mudança de versão/ambiente ou fato volátil.]

## Relações (somente quando necessárias)
[Entrada equivalente, substituição, fonte compartilhada ou promoção.]
```

A ficha é candidata à revisão do [template existente](../templates/KNOWLEDGE-ENTRY-TEMPLATE.md), não uma nova estrutura normativa. Campos atuais continuam suficientes para caso simples; detalhar condições e limites no conteúdo existente, sem obrigar metadados redundantes. Não criar logs de utilização individuais por toda consulta. Alterações materiais seguem revisão normal da tarefa, sem homologação separada para cada registro rotineiro; promoção entre escopos ou mudança normativa requer decisão competente.

## 5. Validade e revalidação

Preservar os estados homologados. Revalidar é conhecimento anteriormente comprovado cuja aplicabilidade atual se tornou incerta; não é categoria para hipótese jamais validada.

| Estado | Condição | Uso |
| --- | --- | --- |
| Vigente | Prova suficiente e condições conhecidas no escopo | Orientar ação se pressupostos ainda válidos; confirmar fato volátil quando necessário |
| Revalidar | Mudança relevante, evidência contraditória, perda de acesso à prova necessária ou condição incerta | Usar como pista; não como conclusão atual antes da confirmação pertinente |
| Obsoleto | Condição extinta, substituição comprovada ou conclusão refutada para o escopo | Não aplicar; preservar referência histórica quando útil |

Transições: Vigente → Revalidar quando condição relevante muda ou fica desconhecida; Revalidar → Vigente quando nova comprovação sustenta a conclusão no escopo; Vigente/Revalidar → Obsoleto quando substituição ou perda de validade é demonstrada. Conhecimento obsoleto pode voltar a ser aplicável se o contexto retornar e houver nova prova, preservando histórico; não reativar por mera edição. Se apenas uma parte da conclusão mudar, delimitar novo escopo ou separar conhecimento realmente distinto. Registrar motivo e evidência na alteração; reconciliar índice. Não substituir data de verificação apenas por consulta ou edição de texto.

### Gatilhos proporcionais

| Gatilho | Conduta |
| --- | --- |
| Mudança de versão, configuração, dependência, ambiente ou procedimento | Reavaliar somente entradas afetadas |
| Estado volátil: existência de arquivo, backup, serviço, permissão, versão instalada | Confirmar no destino quando a decisão depender do fato |
| Evidência contraditória ou falha em aplicação previamente válida | Suspender uso automático, investigar causa e registrar discrepância |
| Fonte inacessível ou removida | Distinguir indisponibilidade da prova de refutação; não presumir falsidade nem validade atual |
| Mudança de política, licença, autoridade ou acesso | Recuperar fonte competente; entrada não concede autorização |
| Prazo técnico/operacional realmente relevante | Usar prazo da fonte ou política do projeto; não impor vencimento universal por idade |

Uma prova estável fixada a revisão imutável não exige repetição integral a cada tarefa. Se pressuposto mudou, revalidar o efeito relevante; se validação indispensável não puder ser feita, registrar bloqueio da ação dependente. Não executar alteração, restauração ou teste invasivo apenas para atualizar uma ficha sem autorização. Evitar cron obrigatório de revisão de toda a base; revisar por evento, uso ou manutenção proporcional autorizada.

## 6. Fluxo operacional de consulta e captura

### Antes de tarefa relevante
1. Identificar projeto, tarefa, assunto, componente, ambiente e autoridade; recuperar instruções conforme [configuração 06](007-06-CONFIGURACAO-DE-PROJETOS-IA.md).
2. Consultar índice local quando existir; selecionar por problema, categoria e escopo. Usar índices externos apenas se a composição adotada e o assunto justificarem acesso.
3. Abrir somente entradas pertinentes; conferir estado, conclusão, evidência, versão, limites e condição de revalidação.
4. Cruzar com documentação canônica e realidade atual quando necessário. A entrada não revoga norma, gate ou decisão homologada.
5. Reutilizar aprendizado e evidência válidos; não repetir diagnóstico sem mudança de pressuposto. Se não houver entrada aplicável, prosseguir pelo fluxo autorizado sem inventar conhecimento.

### Durante ou após a tarefa
1. Separar ocorrência, hipótese, evidência, conclusão e decisão. Preservar prova no registro competente, sanitizada quando necessário.
2. Aplicar critérios de admissão; procurar equivalência na base pertinente antes de criar.
3. Atualizar entrada equivalente, criar entrada distinta ou corrigir estado/escopo quando comprovado; se não houver aprendizado reutilizável, não alterar a base.
4. Reconciliar índice e referência de origem no fluxo Git/revisão existente. Se aprendizado surgir após merge, persistir pela menor alteração autorizada pertinente; não abrir PR suplementar apenas para cumprir ritual.
5. Na verificação final, registrar apenas aprendizado material e pendências relevantes. A limpeza operacional não pode descartar evidência única necessária à conclusão.

Se a entrada contradisser fato atual ou fonte canônica, interromper sua aplicação automática, confirmar condição e classificar a discrepância. Não resolver por “mais recente vence” sem verificar assunto, alcance e prova. Corrigir/inativar no escopo autorizado ou encaminhar ao responsável; preservar fonte histórica. Quando duas entradas forem equivalentes, manter a referência estável, indicar substituição e verificar links antes de retirar duplicata do índice ativo. Não apagar histórico ou informação material sem autorização conforme [limpeza 04](007-04-LIMPEZA-OPERACIONAL.md).

## 7. Promoção controlada entre escopos

A promoção é extração e validação de aprendizado transferível, não replicação automática da base de um projeto. O fluxo não exige subir por todas as camadas intermediárias; escolher o destino competente, conforme arquitetura 03.

| Passagem | Critério |
| --- | --- |
| Descoberta no projeto | Evidência suficiente no escopo de origem |
| Seleção de aprendizado transferível | Utilidade fora do caso, condições explicitadas, sem generalização indevida |
| Revisão de segurança e direitos | Autoridade de acesso, divulgação, titularidade/licença e sanitização |
| Validação no destino | Responsável do método/HUB/núcleo avalia relevância, prova e limites; testar condições adicionais quando necessárias |
| Aceite e persistência | Registrar conclusão no destino, escopo, origem permitida e referência/revisão; preservar registro original |
| Manutenção | Mudança/refutação comunicada a destinos relevantes conforme fluxo autorizado; não atualizar automaticamente consumidores |

Um único caso pode sustentar aprendizado condicional, não frequência universal ou garantia de resultado. Generalizar somente o que a evidência permite. Não exigir replicação do incidente em produção quando uma prova analítica ou ensaio seguro é suficiente para a afirmação. Se a prova necessária só existe em fonte restrita, manter aprendizado no escopo permitido ou produzir evidência independente sanitizada e verificável; não publicar detalhe restrito para satisfazer rastreabilidade. Identificadores sanitizados podem apontar para mapeamento privado autorizado; não inventar verificabilidade pública.

Ao consumir conhecimento compartilhado, verificar vínculo, origem, versão, validade, escopo e diferenças locais. Preferir referência ao registro mantido pelo responsável em vez de cópia; se adaptação local for necessária, registrar somente conclusão/condição local distinta e relação com a origem. Revogação ou obsolescência da fonte compartilhada exige avaliação da aplicabilidade, não propagação cega. Knowledge não é distribuição de credenciais, dados, comandos executáveis ou autorização entre agentes.

## 8. Exemplos de aplicação (ilustrativos, não entradas reais)

| Situação | Afirmação admissível | Afirmação indevida |
| --- | --- | --- |
| Ensaio isolado recupera predicado válido para dado observado (E-10) | Sob a semântica e revisão ensaiadas, o predicado retornou resultado esperado; investigação secundária ainda pendente | Plataforma inteira validada ou causa secundária resolvida |
| Snapshot anterior à migração (E-12) | O inventário documenta o estado naquele momento | A mesma quantidade e conteúdo existem hoje |
| Backup com hash e sem restauração (E-14) | Integridade em relação à referência verificada no escopo informado | Recuperação garantida |
| Procedimento de instalação homologado (E-04) | Consultar runbook canônico vigente antes da operação | Copiar o procedimento para KN e executá-lo sem gate |
| Discussão de técnica profissional | Evidência de uso local comprovado pode gerar lição condicional | Registrar técnica de mercado não aplicada como aprendizado observado |

Esses exemplos remetem a evidências sanitizadas das auditorias ou situações ilustrativas; não foram reexecutados nem constituem novas fichas. Conclusões que apenas repetem regras já homologadas devem permanecer nas fontes normativas. Não criar KN artificial para mostrar atividade.

## 9. Walkthroughs documentais

Confronto analítico do desenho, sem teste em agentes/consumidores.

| Caso | Situação | Tratamento esperado |
| --- | --- | --- |
| C01 — base vazia | Nenhuma conclusão distinta comprovada | Preservar índice vazio (§§1,6) |
| C02 — aprendizado novo | Falha reproduzida com condição isolada e evidência recuperável | Registrar conclusão delimitada, se não redundante (§3) |
| C03 — hipótese | Causa presumida sem prova | Manter em troubleshooting/tarefa, não KN (§§2–3) |
| C04 — prova parcial | Teste isolado positivo, fluxo secundário não testado | Registrar apenas dimensão comprovada (§3.1; E-10) |
| C05 — duplicata | Entrada existente já contém mesma conclusão | Atualizar referência/evidência se necessário; não criar ID novo (§6) |
| C06 — regra canônica | Entrada tenta substituir runbook homologado | Recuperar runbook; tratar divergência no fluxo competente (§§2,6) |
| C07 — fato volátil | Registro antigo aponta backup que pode não existir | Confirmar presença no destino antes da ação (§5; E-14) |
| C08 — versão diferente | Dependência mudou e pressuposto não está demonstrado | Revalidar entrada afetada, sem repetir toda a base (§5) |
| C09 — revisão imutável | Prova estática continua válida na mesma revisão | Reutilizar sem reexecutar por reflexo (§5) |
| C10 — fonte inacessível | Evidência necessária não pode ser consultada | Declarar limite e revalidar/bloquear ação dependente conforme risco (§5) |
| C11 — promoção | Lição local tem potencial uso em outros projetos | Avaliar alcance, direitos, sanitização e aceite no destino (§7) |
| C12 — informação privada | Entrada contém detalhes de cliente ou segredo | Não publicar; recuperar fonte restrita somente se autorizado (§§3,7) |
| C13 — conflito | Nova prova contradiz conclusão vigente | Suspender uso automático, investigar, atualizar estado e índice (§§5–6) |
| C14 — base cresce | Índice começa a dificultar recuperação | Ajustar organização proporcionalmente, preservar ponto de entrada (§4) |
| C15 — obsolescência | Dependência removida e entrada substituída | Obsoleto; preservar referência histórica útil e verificar links (§§5–6) |
| C16 — aprendizado sem norma | Técnica funcionou em um projeto, sem validade universal demonstrada | Manter condicional/local; não criar obrigação global (§§2,7) |

Os 16 cenários têm tratamento conceitual. Nenhuma entrada real foi criada, atualizada, promovida ou excluída; nenhuma métrica de recuperação ou reincidência foi medida.

## 10. Integração futura e avaliação

| Fonte vigente | Refinamento candidato na etapa 10 |
| --- | --- |
| [Docs 08 — aplicação](../docs/08-APLICACAO-E-EVOLUCAO.md) | Fonte normativa de admissão, evidência, escopo, validade, revalidação e promoção |
| [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md) | Consulta/captura proporcional, conflito com fonte atual e fronteira de acesso |
| [Docs 11 — inicialização](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md) | Preservar fundação com índice vazio permitido |
| [Template de entrada](../templates/KNOWLEDGE-ENTRY-TEMPLATE.md) | Explicitar condições, limites, evidência recuperável e relações condicionais |
| [Template do índice](../templates/KNOWLEDGE-README-TEMPLATE.md) e [índice real](../knowledge/README.md) | Manter formato compacto e coerente; sem fichas fictícias |
| [Verificação final](../templates/VERIFICACAO-FINAL-TEMPLATE.md) | Capturar aprendizado material, reconciliar entrada/índice e preservar prova sem gate adicional |
| Configuração 06 e continuidade 05 | Referência ao índice e recuperação seletiva, não cópia do conteúdo em prompts |

D-15: evoluir base existente e avaliar uso acumulativo; D-03/D-12: recuperar seletivamente; D-16: preservar fronteira de backlog; D-27: sanitização e acesso; D-26: mensuração futura. Etapa 09 deverá definir indicadores de eficiência; etapa 11 poderá testar casos autorizados com baseline (recuperação correta, falsas aplicações, revalidações justificadas, repetição evitada com prova, esforço de manutenção, intervenções e reincidência comparável). Nenhuma meta de volume de entradas, ganho percentual ou prazo universal de validade nesta etapa. Não confundir número de consultas com benefício real.

Critério de saída documental: preservar PROP-006, detalhar admissão e qualidade de prova, classificação e ficha compacta, estados/gatilhos, consulta/captura, resolução de conflito, promoção e privacidade, confrontar 16 cenários e reconciliar referências. 6/14 etapas homologadas até aceite e integração de 07. Nenhuma alteração normativa, entrada real, consumidor, ferramenta de memória, banco vetorial, clone, backup ou operação externa executada. Não houve varredura integral de segredos, teste empírico ou inspeção física. PRs #4/#5 e branches documentais preservadas; novos refs intencionais. Não criar Knowledge duplicado para proposta candidata.

## 11. Continuidade condicional — etapa 08

Gate: homologação humana da proposta, integração autorizada, conferência pós-merge e reconciliação documental. Após encerramento comprovado e autorização específica, continuar no mesmo chat com 08 — Documentação e nomenclatura, recuperando NOM-001, diagnósticos D-02/D-09/D-10/D-11/D-12/D-14/D-16/D-17/D-18/D-19/D-22/D-23/D-28 e fontes pertinentes. Preservar registros históricos e contratos técnicos; definir fontes canônicas e derivadas, convenções humanizadas, consolidação sem perda e verificação proporcional. Não alterar normas/consumidores antecipadamente nem iniciar 08 nesta etapa.
