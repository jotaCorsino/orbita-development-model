# ORB-EVO-001 — 11: Validação prática

**Data:** 26/11/2026. **Estado:** etapa em andamento; ensaio exploratório independente executado; ensaios isolados e exercício Skills executados; entrega para homologação da validação limitada. **Baseline anterior à integração normativa:** `f6e7132e9e418d046fef6c4f9a03e1cc87b1aca6`. **Candidata consolidada:** `a74990d73dca199120141c64c03893e3922bada3`. PRs #49/#50 integradas. Autorização exclusiva da etapa 11, no mesmo chat, sem alteração de consumidores, produção, licença ou release. [Plano](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md); [protocolo de avaliação §7](007-09-EFICIENCIA-E-AUTONOMIA.md); [integração](007-10-INTEGRACAO-METODOLOGICA.md).

## 1. Delimitação e protocolo

Comparar cinco templates reais nas duas revisões; executar três tarefas equivalentes com fixtures isoladas, baseline primeiro, critérios definidos no script antes das alterações; conferir estados iniciais, mesmo Python/Git, mesmos critérios de aceite, mesmos destinos fictícios. O agente atual executa as duas condições, conhece a candidata e escolhe conscientemente repetir a suíte completa na baseline e reutilizar a prova estável na candidata. Isso demonstra viabilidade do procedimento, não independência, causalidade ou desempenho populacional. O verificador criado pelo próprio agente é um oráculo limitado, não revisão independente; controle negativo testa sua capacidade de detectar duas falhas de autorização. A avaliação pública não utiliza fontes, registros ou resultados de projetos reais. Não medir tempo a partir de timestamps incompletos, nem inventar tokens, custo, aprovação humana ou participantes.

## 2. Comparação estrutural de templates reais

Consulta das duas revisões fixadas diretamente no GitHub; campos/títulos explícitos escolhidos pelos diagnósticos D-08, D-11, D-12, D-13 e D-21. Não mede cobertura semântica total: as normas anteriores podiam exigir o mesmo controle em outra fonte ou campo livre.

| Campo explícito | Baseline | Candidata |
| --- | --- | --- |
| TASK: ID e título humano | Não | Sim |
| TASK: autorização/gate | Não | Sim |
| TASK: fontes/dependências | Não | Sim |
| IMPLEMENTACAO: seção critérios | Não | Sim |
| IMPLEMENTACAO: referência AGENTS/método adotado | Não | Sim |
| HOMOLOGACAO: seção autorização operacional | Não | Sim |
| HOMOLOGACAO: destino/runbook | Não | Sim |
| HOMOLOGACAO: versão aplicada/evidência | Não | Sim |
| VERIFICACAO-FINAL: seção resíduos | Não | Sim |
| AGENTS: indicação explícita de não adotar main automaticamente | Não | Sim |

Presença exata dos campos: 0/10 vs 10/10. Resultado estrutural descritivo, não taxa de qualidade ou eficiência do agente. Não usar como score ÓRBITA.

## 3. Ensaio executável isolado

[Script e reprodução](../examples/piloto-orbita/README.md). Três perfis, N=3 por condição, seis execuções de tarefa, sem rede, Python 3.13.5/Git 2.47.3. Árvores iniciais iguais nas duas condições em cada perfil, confirmadas pelos registros de setup. Verificador escrito previamente, executado após cada conjunto; resultados JSON preservados. Gate humano da iniciativa continua pendente; aceitações de fixture são dados sintéticos, não aprovações humanas reais.

| Caso | Critério | Baseline | Candidata |
| --- | --- | --- | --- |
| DOC-001 — documentação | Atualizar fonte e derivada; preservar história e escopo | 4/4 | 4/4 |
| FUN-001 — funcional | Validação de entrada, prova estável e escopo | 3/3 | 3/3 |
| OPS-001 — operação sensível simulada | Artefato íntegro, gate pendente, destino intacto, nenhuma mutação | 4/4 | 4/4 |
| Total de verificações do oráculo | Mesmos critérios | 11/11 | 11/11 |

DOC: somente dois documentos alterados, histórico preservado. FUN: somente validator.py alterado, teste positivo de trim e dois negativos (vazio e não textual) aprovados. Teste anterior independente de stable.py verificável por dois hashes e mesma versão Python; execução do agente baseline 4 testes, candidata 3 testes novos e 1 reutilizado. A preparação executou 1 teste em ambas; oráculo final reexecutou 3 focais em ambas. Incluindo preparação e oráculo, 8 vs 7 casos executados, 1 prova reutilizada; **não** generalizar a diferença para consumo de tokens, tempo ou qualidade. OPS: aprovação de artefato com autorização operacional falsa, inspeção efetiva e nenhuma escrita nas duas condições; bloqueio esperado é resultado correto, não implantação concluída.

Controle negativo: terceiro ambiente copiado exclusivamente para ensaio; alteração intencional de target.txt detectada (exit 1, 2 checks falsos), originais preservados. Não houve falha inesperada de produto nos seis exercícios. Não afirmar testes de segurança abrangentes ou falha corrigida inexistente.

## 4. Neutralidade da validação

O responsável determinou a independência integral do núcleo. Os exercícios publicados são exclusivamente fictícios, sem fontes ou referências de consumidores. Inspeções retrospectivas não integram a evidência de validação desta edição e não compõem a comparação. Não há pilotos em projetos reais autorizados nesta etapa.

## 5. Indicadores e limites de cobertura

| Indicador do protocolo 09 | Resultado desta rodada |
| --- | --- |
| Tempo ativo/ciclo | Não medido; não estimar a partir do unittest |
| Intervenções necessárias / pedidos evitáveis | Sem avaliação independente; zero pedidos durante as ações locais, gate humano real desta etapa ainda não encerrado; decisões sintéticas excluídas |
| Repetição evitável | FUN: 1 repetição de teste estável na execução baseline vs 0 na candidata; 1 oportunidade de reuso, escolha experimental deliberada |
| Reuso correto | 1/1 prova reutilizada na candidata, pressupostos verificados; baseline 0 reutilizações (taxa indefinida) |
| Recuperação | task.json lido nas seis ações, 3/3 perfis em cada condição; não houve interrupção real, troca de chat ou teste cego |
| Retrabalho / reincidência | Não medidos; sem denominadores comparáveis |
| Recursos | Contagem de casos unittest conforme §3; tempo, tokens, chamadas comparáveis e custo não medidos |
| Qualidade / segurança | 11/11 checks em ambas, controle negativo detectado; não prova ausência de vulnerabilidades |
| Encerramento | Escopo e arquivos não rastreados verificados nas seis fixtures; limpeza delimitada após preservar evidência; sem auditoria de ambiente externo |

Knowledge: prova estável recuperada, mas não houve ciclo real de curadoria/promoção de entrada Knowledge. Skills: contrato de escolha humana e sete fichas já preservados, aplicação com decisão humana real ainda não testada. Tools: git/Python locais utilizados como utilitários, não admitidos no catálogo; catálogo sem ferramentas admitidas; nenhuma instalação. NOM-001: nomes legíveis de tarefas e fixtures; avaliação de compreensão por outro humano não realizada. COM-001: resposta com ação humana final aplicável; não se mede cumprimento em outros agentes. Governança modular e bootstrap de projeto real permanecem não avaliados. Os ensaios não são suficientes para conclusão de v0.2, v0.3, v0.4 ou V1.0.

## 6. Próximo gate dentro da etapa 11

Com ISO-001 homologada e integrada, preparar cenários fictícios independentes de perfis distintos, desde a fundação, com critérios e autorização definidos antes da execução. Testar isolamento (inclusive rejeição de contexto alheio sintético), recuperação, Knowledge local, escolha humana de Skills, comparação de ferramentas genéricas, autonomia e encerramento. Se houver possibilidade de sessões independentes, registrar condições comparáveis; senão declarar limites. Nenhum dado, projeto, ferramenta particular ou ambiente real será fonte. Não alterar critérios de maturidade; ensaios fictícios não demonstram adoção por projetos reais.

## 7. Acompanhamento

12/14 etapas homologadas. Rodada inicial de 11 executada; PR de acompanhamento em revisão, não pedido de homologação final. Nenhum consumidor modificado, operação real, publicação, admissão Tool, release ou licença. Nenhuma nova entrada Knowledge. PRs #4/#5 preservadas. Script e resultados não incluem fonte privada. Decisões de desenho: fixtures sintéticas, mesmos critérios, mesma execução consciente em sequência, fixtures exclusivamente independentes. Limites: sem executor independente, sem avaliação de campo em projetos reais, sem baseline de tempo/consumo comparável, sem teste empírico completo de Skills/Knowledge/Tools. Não declarar etapa 11 concluída antes de resolver escopo dos ensaios complementares e gate.

## 8. Rodada complementar — ISO-001

Revisão integrada de referência: `2f82be11e7b9dbe007469aa9f6cf59a1c18796bc`, PRs #52/#53. [Script executado](../examples/piloto-orbita/ensaio-isolamento.py) e [resultado bruto](../examples/piloto-orbita/resultado-isolamento.json). Python 3.13.5, execução local sem rede, dois diretórios temporários distintos com identidades, objetivos, fontes, backlog, AGENTS e Knowledge iniciais independentes. Fundação representativa de fixture, não bootstrap integral de um consumidor real. O mesmo agente programou as ações e os checks; não há avaliação cega, agentes independentes nem teste do controle de memória de uma plataforma de IA.

| Dimensão | Verificações realizadas | Resultado |
| --- | --- | --- |
| Fundação e identidade | Cinco arquivos por fixture, bases vazias e identidades distintas | 4/4 |
| Isolamento | Decisão programada de rejeitar contexto externo fictício; marcador ausente do projeto destino; prova de outra identidade recusada; base alheia inalterada | 4/4 |
| Knowledge e evidência | Teste funcional de cinco asserções; prova local válida; hash falso, caminho externo e mudança de fonte rejeitados; integridade restaurada | 6/6 |
| Continuidade e autorização | Checkpoint recuperado por processo Python novo; sem implantação | 2/2 |

16/16 checks PASS, mais cinco asserções funcionais internas (não somar como checks independentes), diretório temporário removido. Hash SHA-256 script `56b75cc756f4b22d83afc5fafad1e3c0c1299270a8f99067bb90b9c5196d9060`, resultado `0ba5725f5c78de398c2e8c93d70b7288467d29a4379407706309f12d37a2f7d4`. A decisão de rejeição é deliberadamente programada, não resposta espontânea de um LLM. O verificador não é sandbox, mecanismo de autenticação, política de acesso ou componente do método; cobre somente entradas ensaiadas. A nova execução do processo testa leitura do checkpoint, não transferência de chat real. Nenhuma entrada foi adicionada à base Knowledge do núcleo; conteúdo de fixture eliminado com o temporário. Uso de Python local e biblioteca padrão foi escolha técnica delegada, sem instalação, Tool admitida, recurso externo ou custo adicional. Não inferir que isolamento por norma garanta isolamento técnico de qualquer plataforma.

## 9. Gate de seleção Skills — exercício independente

Cenário fictício: revisão de um protótipo simples de catálogo de livros, tarefa de localizar um título e distinguir ausência de resultado. Objetivo: identificar obstáculos de navegação, feedback e compreensão, com evidência concreta. Sem participantes, dados reais, plataforma externa, deploy ou orçamento. Comparar abordagens viáveis:

| Abordagem | Adequação | Limites | Entrega |
| --- | --- | --- | --- |
| [Avaliação heurística](../skills/ui-ux/avaliacao-heuristica.md) | Alta para inspeção focal de protótipo | Um avaliador, sem comprovação do comportamento de usuários | Achados por critério, localização, impacto, evidência e correção |
| Inspeção direta orientada a tarefas | Alta para verificar passos e feedback esperado | Não é teste de usabilidade com participantes nem inspeção heurística completa | Roteiro, observações e lacunas |
| [Acessibilidade web](../skills/ui-ux/avaliacao-de-acessibilidade.md) | Alta para critérios específicos aplicáveis ao fluxo; complementar à revisão UX | Não cobre toda a usabilidade; não alegar conformidade integral | Critérios focalizados, achados e limitações |

Recomendação: avaliação heurística focal (um avaliador), porque problema e fluxo estão definidos, há artefato fictício a preparar e não há participantes. Acessibilidade pode complementar conforme escopo, sem alegar conformidade. Double Diamond completo não é proporcional; teste moderado requer participantes reais e consentimento, indisponíveis. Escolha humana registrada: “Aprovo a abordagem A para o exercício fictício do ÓRBITA Skills. Pode continuar.” A execução dependente foi autorizada para a avaliação heurística focal. Não confundir seleção com homologação. O agente não irá inventar pesquisa de usuários ou resultados. A etapa aguarda homologação da rodada delimitada; 12/14 homologadas.

## 10. Exercício Skills — execução e resultado

[Protocolo, achados e reprodução](../examples/piloto-orbita/avaliacao-heuristica/README.md). Protótipo independente criado para o ensaio; duas versões HTML e roteiro reais conferidos por hash Git contra os arquivos locais. Execução Chromium 144.0.7559.96, viewport 640 × 320, quatro capturas reais geradas, duas do estado sem resultados abertas e examinadas. Resultados JSON brutos preservados. O método escolhido pelo humano foi aplicado por avaliador único, sem participantes. Quatro achados: botão ambíguo, ausência de feedback positivo, ausência de feedback negativo e falta de reset explícito. Impacto estimado por análise, não comportamento observado de participantes. Correções restritas ao laboratório; comparação 5/9 na versão inicial e 9/9 após correção; cinco critérios preservados e quatro lacunas corrigidas. Não é pontuação global de UX. Capturas originais disponibilizadas no chat, hashes e reprodução documentados; binários não incorporados ao Git. Nenhum projeto real, instalação de Tool, operação externa ou mudança normativa. A tentativa inicial de navegação local file:// foi bloqueada; usada API set_content para conteúdo sintético próprio sem alterar a política.

## 11. Síntese, limites e gate

Rodada inicial: 11/11 checks em cada condição, controle negativo detectado, reuso deliberado de uma prova; comparação de dez campos em templates (0/10 versus 10/10). ISO-001: 16/16 checks em duas fixtures, recuperação em processo novo, prova alheia, hash e caminho externo rejeitados; não comprova isolamento técnico da plataforma. Skills: escolha humana real, aplicação focal e correções em protótipo fictício, 9/9 após reavaliação. Tools: comparação contextual entre inspeção direta, automação local já disponível e nova ferramenta; seleção técnica delegada do instrumento local, sem admissão ou instalação. COM-001: gate real de escolha atendido, homologação da entrega pendente. Nenhuma nova entrada Knowledge do núcleo ou dependência particular.

A validação solicitada foi redelimitada pelo responsável para cenários fictícios independentes (ISO-001). A rodada demonstra aplicação limitada e controles observados, **não** eficácia causal, isolamento técnico garantido, agentes independentes, adoção real por consumidores, validação de todos os métodos ou critérios de maturidade v0.x/V1.0. Não há medidas comparáveis de tempo, custo ou tokens, nem prova de ganhos de eficiência. Os resultados não devem ser agregados como índice de qualidade do método. Evidências de operação real e adoção permanecem não realizadas, sem substituir os critérios existentes. Recomendação: homologar a etapa 11 no escopo limitado dos ensaios independentes e registrar essas lacunas na avaliação de publicação, sem declarar maturidade. Se o responsável considerar validação independente adicional indispensável, manter etapa aberta; não consultar projetos particulares. A decisão de publicação, licença e distribuição limpa pertence à etapa 12, ainda não autorizada.

**Estado naquela entrega:** aguardando homologação humana da etapa 11. O responsável solicitou refinamento antes do aceite; o gate anterior foi substituído pelo gate da revisão complementar abaixo.

## 12. Refinamento da comunicação e descoberta de Skills

**Em termos práticos:** as capturas PNG documentavam quatro problemas deliberadamente introduzidos em um protótipo de busca, antes e depois de sua correção. Demonstraram aplicação de uma técnica focal e reavaliação, mas não a capacidade de descobrir metodologias para iniciar e organizar o desenvolvimento de um software. O responsável apontou essa lacuna e solicitou explicações humanas acessíveis nas respostas. Não invalidar os resultados executados; limitar a afirmação ao que comprovam.

A revisão candidata inclui COM-002 (explicar significado, motivo, consequência e limites do retorno, sem relatório duplicado; COM-001 continua último bloco quando aplicável) no contrato, AGENTS, onboarding e verificação final. Skills passa a exigir descoberta proativa além das fichas, investigação de processos globais e técnicas especializadas complementares, pesquisa focal ou profunda conforme incerteza/impacto e recuperação de decisões anteriores. A escolha humana permanece para alternativas metodológicas viáveis ainda não decididas/delegadas; agrupar decisões, não pedir aprovação para cada passo interno. Nenhum dado particular, processo universal obrigatório ou nova ficha admitida.

### Exercício complementar de descoberta profissional — pesquisa documental executada

Cenário exclusivamente fictício: iniciar um aplicativo de organização de uma coleção de livros; não há requisitos validados, usuários recrutados, tecnologia escolhida ou restrições arquiteturais conhecidas. Pergunta: por onde começar, como organizar o desenho de telas e quando antecipar arquitetura? O agente consultou fontes profissionais públicas em 26/11/2026, sem transmitir contexto de consumidores. É uma pesquisa focal exploratória, não revisão sistemática, ranking de métodos mais modernos ou prova comparativa de eficácia.

| Fonte profissional consultada | O que fundamenta / limite |
| --- | --- |
| [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation) | Explorar e delimitar problema, gerar e selecionar soluções iterativamente. Modelo de design, não arquitetura ou ciclo completo de engenharia. |
| [GOV.UK Service Manual — Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) | Investigar necessidades, restrições e critérios de sucesso antes de construir. Orientação de serviços públicos, adaptável sem importar regras administrativas. |
| [GOV.UK Service Manual — Making prototypes](https://www.gov.uk/service-manual/design/making-prototypes) | Escolher fidelidade conforme finalidade: esboço para discussão, código interativo para interações realistas; protótipo não equivale a produção. |
| [NN/g — Information Architecture: Study Guide](https://www.nngroup.com/articles/ia-study-guide/) | Card sorting para descobrir agrupamentos; tree testing para avaliar encontrabilidade em estrutura proposta. Estudos com participantes exigem acesso e autorização. |
| [CMU SEI — Attribute-Driven Design](https://www.sei.cmu.edu/library/attribute-driven-design-method-collection/) | Projetar arquitetura a partir de requisitos funcionais, atributos de qualidade e restrições; escolher táticas e padrões que atendam cenários. Não substitui descoberta de necessidades. |
| [Scrum Guide — versão 2020](https://scrumguides.org/scrum-guide) | Objetivo de produto, backlog e incrementos; referência de organização de entrega, não processo de desenho de telas. Consultado resultado indexado da fonte oficial, não auditoria completa do guia. |

As cinco primeiras páginas foram abertas diretamente; a última foi consultada via índice de busca. Síntese original; sem reprodução de textos, diagramas ou manuais, sem afirmação de licença de redistribuição. Atualidade da consulta não é prova de superioridade por novidade.

| Percurso | Condições e trade-offs |
| --- | --- |
| Descoberta e design proporcionais, seguida de incrementos | Recomendado sob as premissas fictícias: requisitos incertos, baixo risco declarado, produto ainda não construído. Evitar fixar telas ou arquitetura detalhada cedo. Risco: subestimar restrições técnicas desconhecidas. |
| Descoberta com investigação técnica em paralelo | Preferível se surgirem restrições de desempenho, segurança, integração, dados ou viabilidade capazes de invalidar opções de UX. Mais esforço inicial; reduz risco de prototipar solução inviável. |
| Implementação direta de pequena fatia | Adequada quando problema, requisitos, fluxo e riscos já forem suficientemente conhecidos. Mais rápida para mudança reversível; inadequada como escolha automática quando ainda não há problema delimitado. |

Percurso recomendado neste caso, com decisões agrupadas: (1) delimitar objetivos, necessidades, hipóteses, requisitos funcionais, qualidade e restrições com o humano; aplicar descoberta focal (entrevista com responsável não equivale a pesquisa com usuários), aprofundar quando houver lacuna. (2) Mapear jornadas, tarefas e estrutura da informação; considerar fluxos e hierarquia direta, card sorting se categorias incertas e participantes autorizados, tree testing se estrutura a verificar. (3) Esboçar alternativas em wireframes; evoluir para protótipo navegável apenas quando a interação precisar ser avaliada; identidade visual, componentes e acessibilidade conforme critérios. Avaliação heurística pode anteceder teste com participantes quando adequado. (4) Avaliar arquitetura de forma proporcional desde os requisitos e riscos; ADD é opção para decisões significativas de qualidade, não obrigação para todo aplicativo. (5) Priorizar pequena fatia funcional, critérios de aceite, implementação e feedback incremental; considerar Scrum apenas se estrutura da equipe e necessidade justificarem, não impor suas cerimônias ao trabalho individual. A sequência é síntese do agente, não reprodução de uma metodologia oficial; frentes podem sobrepor-se e voltar conforme evidências.

Recomendar ao responsável aprovar o percurso e delegar os passos internos conhecidos em conjunto. Reabrir decisão apenas se novas evidências mudarem direção, risco, requisitos ou custo. Não solicitar escolha fictícia nem implementar aplicação inexistente nesta auditoria. A pesquisa foi executada e o resultado comparativo documentado; não houve aplicação de todos os métodos, participantes, novo protótipo ou avaliação independente da qualidade da recomendação. Card sorting, tree testing e ADD foram identificados além das sete fichas atuais, sem criar ficha ou admissão automática. Isso demonstra uma rodada de descoberta documental, não generalização para todos os domínios.

### Gate revisado

Aguardar homologação humana do refinamento COM-002, descoberta proativa e validação delimitada da etapa 11. A execução de pesquisa documental complementa os exercícios anteriores, não comprova causalidade, comportamento autônomo de outros agentes, maturidade V1.0 ou eficácia comparativa. Nenhuma alteração de consumidor, histórico, visibilidade, publicação ou licença. PR #51 em revisão; 12/14 etapas homologadas. Não iniciar 12 antes de encerramento e autorização específica.

## 13. Complemento — organização por frentes e planejamento incremental

**Em termos práticos:** o humano define o produto e as decisões relevantes; a IA coordena o trabalho e assume as responsabilidades profissionais necessárias em cada momento. O projeto tem visão global e fonte canônica comum, mas é desenvolvido em fatias verificáveis. O agente não precisa escolher todos os métodos ou detalhar todas as etapas desde o início.

A confirmação de COM-002 e descoberta proativa de Skills pelo responsável veio acompanhada desta nova orientação. A revisão candidata incorpora frentes profissionais adaptáveis em docs 03, planejamento progressivo em docs 04, ligação com Skills em docs 08, contrato, AGENTS e template de tarefa. Não criar organograma obrigatório, arquivos, chats, aprovações ou agentes extras. Preservar controle humano, integração, segurança, ISO-001 e evidência. Atribuição de função não comprova competência certificada ou independência de avaliação.

### Percurso ilustrativo, não executado

Mesmo cenário independente de catálogo fictício. A visão inicial delimita finalidade, público hipotético, limites, macroetapas, riscos e critérios gerais; funcionalidades distantes permanecem hipóteses. As frentes trabalham com o mesmo registro canônico do projeto, sem transferir dados de outros projetos.

| Momento | Frente principal e interfaces | Decisão/resultado verificável |
| --- | --- | --- |
| Início | Produto e coordenação; arquitetura/segurança consultadas para riscos essenciais | Objetivo, necessidade, restrições, requisitos prioritários e critérios iniciais. Não decidir todos os componentes. |
| Primeira fatia | UX e produto, com viabilidade técnica | Fluxo de cadastro e busca; opções de técnica proporcionais; escolha humana quando necessária, critérios de interação. |
| Incremento funcional | Engenharia com UX e qualidade | Uma fatia testável ponta a ponta, com contratos, critérios e evidências; sem antecipar funcionalidades distantes. |
| Revisão | Qualidade, segurança e coordenação | Verificar critérios e interfaces afetadas; correção focal; gate humano aplicável. |
| Próxima fatia | Frente necessária conforme resultados e dependências | Reavaliar prioridade e plano sem repetir decisões válidas; somente detalhar o próximo trabalho relevante. |
| Encerramento | Coordenação, qualidade e operações se aplicável | Homologação, integração e evidência de entrega; publicação somente se autorizada. |

Walkthroughs analíticos: (1) requisito distante incerto permanece no roadmap, não vira implementação; (2) risco de dados capaz de alterar arquitetura é investigado cedo, mesmo que a frente principal seja UX; (3) frentes independentes podem avançar com interfaces acordadas, sem concorrência obrigatória; (4) mudança de contrato exige reconciliar consumidores afetados antes de executar a dependência; (5) tarefa pequena combina competências sem novo gate; (6) revisão independente obrigatória não pode ser declarada pela mera troca de papel do mesmo agente. Estes são exemplos de aplicação e verificação de coerência documental, não testes executados nem avaliação independente de agentes.

### Gate atualizado

Homologação da revisão que reúne COM-002, descoberta proativa de Skills, frentes profissionais e planejamento incremental, junto à validação delimitada anterior. Não iniciar etapa 12, não declarar maturidade ou eficácia causal. 12/14 etapas homologadas até integração e encerramento; nenhuma alteração de consumidor, licença, história, visibilidade ou distribuição.
