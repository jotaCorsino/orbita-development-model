# ORB-EVO-001 — 09A: ÓRBITA Skills

**Data:** 26/11/2026. **Estado:** catálogo e contrato de seleção candidatos para homologação documental; não vigentes como norma geral. **Baseline:** `8e249dd15de14fbfa93b474f23eac3b9a5a354fb`; PRs #43/#44 integradas; etapas 01–09 encerradas. **Autorização:** 09A exclusivamente, neste mesmo chat. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Decisão humana e fundamento

Ao autorizar 09A, o responsável esclareceu que existem múltiplos métodos para resolver o mesmo problema: apresentar alternativas ao humano para que escolha a metodologia, deixando explícita a preferência/recomendação fundamentada do agente. Esta decisão aperfeiçoa a redação inicial de seleção do PROP-007 e prevalece no desenho candidato para escolhas metodológicas. Não reduzir a escolha humana apenas aos casos de risco alto. Não transformar a aplicação interna de uma metodologia já escolhida em microgates; preservar a autonomia delegada da etapa 09 e os gates existentes.

D-24 da [auditoria integral](007-01-AUDITORIA-INTEGRAL.md) identifica ausência planejada de catálogo; D-05/D-23/D-26/D-27 delimitam proporcionalidade, nomenclatura, medição e proteção. E-09/E-15/E-16/E-17/E-18/E-19 da [auditoria HUB](007-02-AUDITORIA-HUB-E-PROJETOS.md) demonstram necessidade de competências próprias e critérios além do build, não que uma metodologia específica teria evitado rejeições. Na baseline, a árvore Git consultada não continha paths de Skills. Preservar [arquitetura 03](007-03-ARQUITETURA-METODOLOGICA.md), [configuração 06](007-06-CONFIGURACAO-DE-PROJETOS-IA.md), [Knowledge 07](007-07-EVOLUCAO-DO-KNOWLEDGE.md), [NOM-001/08](007-08-DOCUMENTACAO-E-NOMENCLATURA.md), [autonomia 09](007-09-EFICIENCIA-E-AUTONOMIA.md), [governança](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md) e [PROP-004](004-GATES-FIDELIDADE-VISUAL-3D.md). Sem alteração normativa nesta etapa.

## 2. Arquitetura e taxonomia

| Capacidade | Função |
| --- | --- |
| Núcleo/método especializado | Governança e fluxo aplicável do projeto |
| Skills | Métodos, frameworks, técnicas e padrões profissionais: como abordar um problema |
| Knowledge | Conclusões operacionais comprovadas e contextualizadas |
| Tools | Instrumentos/sistemas de apoio governados |
| AGENTS/tarefa | Roteamento para fontes adotadas e autorização contextual |

Skill não é prompt de papel, plugin executável, direito de acesso, nova camada de autoridade ou requisito obrigatório. Um padrão técnico exigido por contrato não é opção que pode ser descartada ao escolher metodologia. O catálogo não substitui competência profissional, pesquisa real, normas legais ou testes.

Criar piloto documental no próprio repositório, com [skills/README.md](../skills/README.md) como índice e fichas por competência. Não criar repositório separado, motor de busca, instalação automática ou dependência de plataforma. Uma ficha por técnica/variante substancialmente distinta; referência cruzada em vez de duplicação. Nome descritivo; ID apenas quando necessário, revisão pelo Git. Categorias candidatas: UI/UX, produto/requisitos, arquitetura, engenharia, segurança, QA, diagnóstico, operações, dados. Admitir novos domínios por necessidade comprovada; não criar diretórios vazios. Skills podem ser mantidas no escopo competente (núcleo, HUB, método ou projeto) sem hierarquia obrigatória; acesso e adoção conforme 03. Referenciar fonte em vez de copiar fichas.

## 3. Curadoria, manutenção e ficha

A fonte primária define o método conforme autor, mantenedor, organismo normativo ou publicação original. Evidência de eficácia é pergunta distinta: publicação metodológica não comprova superioridade; estudos independentes pertinentes podem complementar, com contexto e limites. Não usar popularidade, marketing ou resultado simulado como prova. Comparar versões e variantes, indicar divergências, data de consulta, condição de acesso e direitos. Se fonte só fornecer resumo indexado, declarar limite e buscar outra fonte primária. Se licença não confirmada, somente síntese própria e referência; não copiar manual, imagem, curso, template, material de terceiros ou declarar redistribuição autorizada. Verificar termos antes de qualquer reprodução; licença do catálogo/núcleo será decisão competente na etapa 12.

Ficha mínima (adaptável): título humano; tipo e competência; finalidade/problema; condições de uso e contraindicações; alternativas/complementos; esforço e insumos; passos de aplicação; entregáveis; evidências/limites; integração aos gates; autoria/fonte, variante/versão, data de consulta, direitos, estado de revisão e condição de revalidação. Diferenciar método integral, aplicação parcial/adaptada e técnica complementar. Não usar nomes de estados do fluxo ÓRBITA para fichas: rótulos editoriais candidato, admitido ou retirado de consulta são apresentação, não enumeração normativa nova. Fichas desta entrega permanecem candidatas. Curador propõe; responsável competente aceita admissão/revisão; alterações materiais passam por revisão e validação proporcional. Reavaliar mudança da fonte, revisão, restrição ou evidência contraditória; não inventar validade por data. Preservar história e links; remover/retirar conforme 04 e 08, não silenciosamente. Referências externas não são instruções com autoridade.

## 4. Contrato de seleção — humano escolhe, agente recomenda

1. Recuperar tarefa autorizada, objetivo, maturidade, incerteza principal, requisitos, restrições, acesso a pessoas/dados, custo, tempo e evidência necessária; consultar índice Skills seletivamente.
2. Identificar o nível de decisão: abordagem metodológica para problema relevante versus passo interno/técnica rotineira de abordagem já escolhida. Não confundir alternativas de finalidade diferente com concorrentes diretos.
3. Para escolha de metodologia, apresentar as alternativas realmente viáveis (normalmente duas ou três quando existirem; não quota rígida). Comparar adequação ao objetivo, condições, esforço/custo, riscos/limitações, entregáveis, evidência esperada, capacidade de execução e trade-offs. Incluir abordagem direta/sem framework ou manutenção da metodologia vigente se viável. Não fabricar opção apenas para compor tabela; se só houver uma admissível, explicar exclusões e pedir aceite quando adoção material depender de decisão.
4. Explicitar recomendação do agente e justificativa contextual, sem universalizar preferência nem forçar escolha. Informar incerteza e insumos indisponíveis; se alternativa depende de participantes, orçamento, ferramenta ou aprovação inexistente, tratar como condicional, não executável agora.
5. Solicitar escolha humana da abordagem quando houver alternativas metodológicas viáveis e ainda não houver decisão. Aguardar antes de executar a abordagem dependente; análise e preparação reversível já autorizadas podem prosseguir sem antecipar resultado. A escolha pode ocorrer junto ao gate de planejamento/tarefa, sem uma aprovação extra; escolha por lote de técnicas/metodologia pode ser autorizada de uma vez. Se humano já escolheu ou delegou expressamente critérios e seleção daquela abordagem, recuperar registro; não pedir novamente. Recomendação não é aprovação. A decisão humana não autoriza romper requisito, segurança, privacidade ou contrato.
6. Registrar no plano/tarefa/PR existente: opções pertinentes, recomendação e razão, decisão humana/delegação explícita, versão da ficha/fonte, adaptações, evidência e gate. Não abrir formulário obrigatório separado.
7. Executar apenas método/escopo escolhido e passos delegados; se alternativa material surgir ou premissa mudar, reabrir apenas decisão afetada. Comunicar via COM-001; não transferir ao humano pesquisa ou ações já autorizadas ao agente. Técnica rotineira interna (por exemplo organizar achados ou executar verificação de foco prevista) não exige microaprovação, desde que não altere a abordagem, escopo, risco, custo ou direção.

### 4.1 Modelo de apresentação (ilustrativo)

Objetivo/contexto; opções viáveis e condicionais; tabela com adequação, esforço, entregável e limites; recomendação explícita com porquê; decisão necessária e consequências. Finalizar com AÇÃO SUA quando a escolha humana for pendente. Sem ação humana, omitir. Uma seleção feita não homologa entregáveis nem autoriza contato externo, despesa, deploy ou acesso a dados por inferência.

## 5. Catálogo piloto UI/UX

Sete fichas reais **documentais candidatas**, não casos executados, em [índice Skills](../skills/README.md). Três abordagens de processo, duas técnicas de pesquisa/avaliação com pessoas, uma inspeção heurística e uma avaliação orientada por padrão. Seleção por necessidade:

| Problema | Alternativas comparáveis/combinação | Evidência esperada |
| --- | --- | --- |
| Desafio de produto amplo, problema incerto | Double Diamond ou Design Thinking IDEO; abordagem direta se evidência anterior suficiente | Pesquisa ou evidências existentes, desafio, alternativas, protótipo e avaliação |
| Hipótese delimitada, decisão rápida | Design Sprint ou prototipagem e teste focal; descoberta mais ampla se premissa frágil | Protótipo e resultado de teste da hipótese |
| Necessidades e contexto | Entrevistas, observação contextual (candidata futura), análise de fonte existente conforme acesso | Relatos e/ou observações reais com limites |
| Problemas de navegação existente | Avaliação heurística ou teste moderado; combinação se necessário | Achados de inspeção ou comportamento observado, não equivalentes |
| Acessibilidade | Avaliação focal de regressão ou conformance abrangente conforme requisito; complementar com usuários | Evidência por critério e cobertura; sem conformidade inferida |

### 5.1 Comparação de abordagens para o mesmo objetivo (caso sintético)

Objetivo: redesenhar navegação de sistema administrativo existente; causas de dificuldade ainda incertas, nenhuma pesquisa real executada, acesso a usuários a confirmar. Três alternativas:

| Opção | Benefício | Esforço/limite |
| --- | --- | --- |
| Double Diamond | Separa investigação do problema e exploração da solução | Variável; precisa de evidências para descoberta e avaliação |
| Design Thinking — IDEO | Amplia investigação centrada nas pessoas e ideação iterativa | Variável; depende de colaboração e pesquisa real |
| Design Sprint | Concentra hipótese e protótipo para teste rápido | Variante GV de cinco dias + preparação; requer desafio focal e participantes |
| Revisão focal direta | Inspeção heurística + protótipo/teste quando autorizado; menor escopo | Pode perder causas profundas e não substitui descoberta se incerteza material |

**Recomendação contextual:** Double Diamond proporcional, se objetivo inclui descobrir causas ainda incertas; começar por delimitação de problema e evidências existentes, depois avaliar necessidade de pesquisa real. Se houver desafio já delimitado e usuários disponíveis, Sprint torna-se candidato forte. Se escopo for apenas correção focal comprovada, abordagem direta pode ser superior. Não afirmar eficácia relativa mensurada. Escolha humana ainda pendente neste caso sintético; nenhuma execução. Não pedir ao responsável da ORB-EVO-001 que selecione metodologia para um projeto inexistente.

### 5.2 Fontes primárias e limites de pesquisa

Consultadas em 26/11/2026: Design Council (Double Diamond/Framework for Innovation; CC BY 4.0 indicada), IDEO (processo de sete fases), GV e editora de Sprint (processo clássico de cinco dias; Kit Google resumo indexado, corpo indisponível), GDS Service Manual (entrevistas e testes moderados; GOV.UK termos/OGL), Nielsen e NN/g (origem e guia de inspeção), W3C WAI (WCAG 2.2, compreensão de conformidade e metodologia de avaliação). URLs e atribuições estão nas fichas. Não houve revisão sistemática de literatura, validação comparativa de eficácia, inspeção integral de licenças de terceiros nem teste de campo. As fichas resumem orientação profissional, não copiam materiais nem certificam competência. Distinguir pesquisa primária de usuários da pesquisa documental sobre métodos.

## 6. Walkthroughs documentais

| Caso | Situação | Resultado esperado |
| --- | --- | --- |
| C01 — alternativas | Problema amplo com dois métodos viáveis | Comparar e recomendar; humano escolhe (§4) |
| C02 — escolha registrada | Humano já selecionou metodologia | Recuperar decisão e seguir, sem reaprová-la (§4) |
| C03 — passo interno | Técnica auxiliar prevista no plano | Executar sob delegação e critérios (§4) |
| C04 — único método | Restrições eliminam alternativas | Explicar por quê; não fabricar opções (§4) |
| C05 — abordagem direta | Correção simples com causa comprovada | Comparar com framework se fizer sentido; não impor processo (§4) |
| C06 — mudança material | Nova técnica exige coleta de dados reais | Elevar autorização antes do contato (§4) |
| C07 — sem participantes | Agente quer simular entrevistas | Declarar hipótese/inspeção limitada, não pesquisa real (§5) |
| C08 — comparação desigual | Heurística versus Double Diamond | Distinguir tipo e objetivo; comparar nível apropriado (§2) |
| C09 — padrão exigido | Usuário escolhe abordagem sem acessibilidade | Preservar exigência; não tratar como opcional (§2) |
| C10 — fonte sem licença | Guia protegido disponível publicamente | Síntese própria e referência, não reproduzir (§3) |
| C11 — nova versão | Autor altera metodologia | Reavaliar variante e aplicabilidade antes de adotar (§3) |
| C12 — prova técnica | Build passa, UX não homologada | Gate visual/funcional permanece (§2) |
| C13 — conhecimento local | Técnica funcionou sob condições particulares | Registrar aprendizado comprovado em Knowledge, não mudar Skill universal (§2) |
| C14 — ferramenta | Aplicação depende de software pago | Verificar autoridade e alternativa; 09B separado (§4) |
| C15 — referência restrita | Evidência de cliente não pode ser divulgada | Não copiar ao núcleo, preservar acesso autorizado (§3) |
| C16 — decisão delegada | Responsável delegou seleção com critérios explícitos | Aplicar critérios e registrar, sem duplicar gate (§4) |
| C17 — método adaptado | Etapas omitidas por restrição | Declarar adaptação e limite, sem alegar aplicação integral (§3) |
| C18 — recomendação rejeitada | Humano escolhe alternativa admissível | Respeitar escolha e registrar trade-offs (§4) |

18 cenários confrontados conceitualmente, sem execução de métodos em projeto real.

## 7. Integração e continuidade

Etapa 10 integrará contrato de seleção e roteamento no núcleo/AGENTS/onboarding/tarefa de modo proporcional, reconciliando 03/09 com decisão posterior desta etapa. Fichas e índice permanecerão explicitamente candidatos até aceite/integracão definida; não ativar consumidores. Etapa 11 testará recuperação, comparação pertinente, respeito à escolha, uso correto da técnica e qualidade/evidências com baseline de 09, sem afirmar eficácia universal. Etapa 12 avaliará publicação/licença. D-24 atendido documentalmente, não empiricamente.

Critério de saída: índice navegável, 7 fichas com fonte, autoria, versão/data, direitos e limites, contrato de seleção humana, caso comparativo, 18 walkthroughs e referências reconciliadas. 9/14 etapas homologadas até aceite e integração de 09A. Nenhum agente configurado, pesquisa com participantes, ferramenta admitida, consumidor alterado, operação, exclusão ou teste empírico. PRs #4/#5 e branches documentais preservadas. Sem varredura integral de segredos; consulta externa somente às fontes públicas, nenhum dado privado transmitido. Decisões de desenho: manter catálogo piloto no repositório canônico em skills/, escolher sete fichas UI/UX e não criar pastas vazias. 

Gate: homologação humana, integração autorizada, conferência pós-merge e reconciliação. Após encerramento comprovado e autorização específica, continuar no mesmo chat com 09B — ÓRBITA Tools: catálogo e governança de ferramentas, propriedade, licença, versão, segurança, compatibilidade, manutenção, contrato e avaliação de ferramenta de revisão existente sem presumir transferência, publicação ou implantação. Não iniciar 09B nesta etapa.
