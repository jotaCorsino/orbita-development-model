# ORB-EVO-001 — 11: Validação prática

**Data:** 26/11/2026. **Estado:** etapa em andamento; ensaio exploratório executado e inspeção retrospectiva somente leitura concluídos; validação de campo ainda pendente. **Baseline anterior à integração normativa:** `f6e7132e9e418d046fef6c4f9a03e1cc87b1aca6`. **Candidata consolidada:** `a74990d73dca199120141c64c03893e3922bada3`. PRs #49/#50 integradas. Autorização exclusiva da etapa 11, no mesmo chat, sem alteração de consumidores, produção, licença ou release. [Plano](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md); [protocolo de avaliação §7](007-09-EFICIENCIA-E-AUTONOMIA.md); [integração](007-10-INTEGRACAO-METODOLOGICA.md).

## 1. Delimitação e protocolo

Comparar cinco templates reais nas duas revisões; executar três tarefas equivalentes com fixtures isoladas, baseline primeiro, critérios definidos no script antes das alterações; conferir estados iniciais, mesmo Python/Git, mesmos critérios de aceite, mesmos destinos fictícios. O agente atual executa as duas condições, conhece a candidata e escolhe conscientemente repetir a suíte completa na baseline e reutilizar a prova estável na candidata. Isso demonstra viabilidade do procedimento, não independência, causalidade ou desempenho populacional. O verificador criado pelo próprio agente é um oráculo limitado, não revisão independente; controle negativo testa sua capacidade de detectar duas falhas de autorização. A inspeção de registros de dois projetos reais é somente retrospectiva: não é aplicação nova da candidata nesses projetos. Não medir tempo a partir de timestamps incompletos, nem inventar tokens, custo, aprovação humana ou participantes.

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

## 4. Inspeção de evidências de projetos reais (somente leitura)

Fontes privadas S1/S4 da auditoria HUB [02](007-02-AUDITORIA-HUB-E-PROJETOS.md), PRs específicas recuperadas diretamente pelo conector em 26/11/2026. Identificadores privados, conteúdo operacional, caminhos, dados e hashes privados não publicados. Nenhuma ação em consumidor nem nova execução dos testes relatados. Duas inspeções atuais de registros históricos; não são dois estudos de caso completos, nem baseline quantitativa pareada.

| Perfil | Observado diretamente no GitHub | Relatado na fonte, não reexecutado | Decisão sob candidata |
| --- | --- | --- | --- |
| S1 — evolução funcional e operação sensível | PR fechada, merged=true, 44 arquivos; corpo inclui cronologia de gates e encerramento restrito ao Git | QA isolado 15/15 suítes e 1.853 asserções reportadas; recuperação operacional e quatro ciclos naturais posteriores ao restauro; revisão inicial não demonstrava cronologia, complementada por inspeção focal | Não inferir implantação a partir do merge; reutilizar prova de QA somente na revisão e dependências correspondentes; não repetir operação concluída nem reabrir migração sem gate |
| S4 — integração de sistema existente | PR aberta, merged=false, 23 arquivos; corpo registra falhas, correções e próximo teste negativo pendente | Compilação/selftests, comparação de engines, criação/edição isoladas e falha de efeito secundário; prova posterior de ordem/contadores não estabelece snapshot anterior exato; novo teste negativo preparado, não executado no registro | Preservar falha histórica e evidências parciais; não repetir escrita já comprovada; executar somente lacuna autorizada quando agente do projeto estiver habilitado; não homologar writer/produção |

As fontes demonstram relevância prática de gates, escopo, evidência, continuidade, preservação e correção focal; os resultados anteriores antecedem ou são independentes da integração candidata. Não alegar que esta evolução causou aqueles resultados. Não substituir o fluxo operacional dos projetos ou divulgar conteúdo. Não duplicar os registros nas bases Knowledge.

## 5. Indicadores e limites de cobertura

| Indicador do protocolo 09 | Resultado desta rodada |
| --- | --- |
| Tempo ativo/ciclo | Não medido; não estimar a partir do unittest |
| Intervenções necessárias / pedidos evitáveis | Sem avaliação independente; zero pedidos durante as ações locais, gate humano real desta etapa ainda não encerrado; decisões sintéticas excluídas |
| Repetição evitável | FUN: 1 repetição de teste estável na execução baseline vs 0 na candidata; 1 oportunidade de reuso, escolha experimental deliberada |
| Reuso correto | 1/1 prova reutilizada na candidata, pressupostos verificados; baseline 0 reutilizações (taxa indefinida) |
| Recuperação | task.json lido nas seis ações, 3/3 perfis em cada condição; não houve interrupção real, troca de chat ou teste cego |
| Retrabalho / reincidência | Não medidos; históricos S1/S4 não fornecem denominadores comparáveis |
| Recursos | Contagem de casos unittest conforme §3; tempo, tokens, chamadas comparáveis e custo não medidos |
| Qualidade / segurança | 11/11 checks em ambas, controle negativo detectado; não prova ausência de vulnerabilidades |
| Encerramento | Escopo e arquivos não rastreados verificados nas seis fixtures; limpeza delimitada após preservar evidência; sem auditoria de ambiente externo |

Knowledge: prova estável recuperada, mas não houve ciclo real de curadoria/promoção de entrada Knowledge. Skills: contrato de escolha humana e sete fichas já preservados, aplicação com decisão humana real ainda não testada. Tools: git/Python locais utilizados como utilitários, não admitidos no catálogo; ferramenta restrita não instalada. NOM-001: nomes legíveis de tarefas e fixtures; avaliação de compreensão por outro humano não realizada. COM-001: resposta com ação humana final aplicável; não se mede cumprimento em outros agentes. Governança modular e bootstrap de projeto real permanecem não avaliados. Os ensaios não são suficientes para conclusão de v0.2, v0.3, v0.4 ou V1.0.

## 6. Próximo gate dentro da etapa 11

Recomendação: **dois pilotos de campo em cópias isoladas de projetos reais, sem alteração do consumidor canônico ou produção**. S4 e S1 são candidatos por perfis diferentes; usar revisão imutável e fixture sanitizada, sem reaproveitar tarefas ativas ou repetir operação real. Alternativa: aplicar em novas tarefas reais autorizadas nos projetos, sem duplicar trabalho apenas para medir; maior validade externa, mais dependências e risco de interferir no trabalho corrente. Comparação de mesmo agente consciente tem baixo poder causal; se possível, separar sessões de execução com instruções da baseline e da candidata e mesma versão de modelo/ambiente, avaliação com oráculo e revisão humana. Se independência ou comparabilidade não for possível, relatar descritivamente. Nenhum comando de deploy, escrita em repositório consumidor, dados reais, instalação ou despesa sem autorização específica.

Critérios de campo: recuperação de contexto por checkpoint real; seleção entre alternativas metodológicas com recomendação e escolha humana; reuso de conhecimento/prova; seleção de Tool elegível ou bloqueio restrito; execução de tarefa delimitada e verificação de impacto/encerramento, registro de falhas e correção proporcional. Usar fonte de registro existente. Definir autorização, casos, revisões, dados e critérios antes da execução; medir apenas dados disponíveis. Não abrir novo chat de coordenação por etapa; sessões de executor independentes são distintas. O aceite desta rodada não encerra etapa 11, não libera etapa 12 nem altera estados do roadmap v0.x.

## 7. Acompanhamento

12/14 etapas homologadas. Rodada inicial de 11 executada; PR de acompanhamento em revisão, não pedido de homologação final. Nenhum consumidor modificado, operação real, publicação, admissão Tool, release ou licença. Nenhuma nova entrada Knowledge. PRs #4/#5 preservadas. Script e resultados não incluem fonte privada. Decisões de desenho: fixtures sintéticas, mesmos critérios, mesma execução consciente em sequência, dois registros reais somente leitura. Limites: sem executor independente, sem piloto em projeto real sob nova revisão, sem baseline de tempo/consumo comparável, sem teste empírico completo de Skills/Knowledge/Tools. Não declarar etapa 11 concluída antes de resolver escopo de campo e gate.
