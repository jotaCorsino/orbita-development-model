# ORB-EVO-001 — 11: Validação prática

**Data:** 26/11/2026. **Estado:** etapa em andamento; ensaio exploratório independente executado; validação complementar pendente de correção ISO-001. **Baseline anterior à integração normativa:** `f6e7132e9e418d046fef6c4f9a03e1cc87b1aca6`. **Candidata consolidada:** `a74990d73dca199120141c64c03893e3922bada3`. PRs #49/#50 integradas. Autorização exclusiva da etapa 11, no mesmo chat, sem alteração de consumidores, produção, licença ou release. [Plano](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md); [protocolo de avaliação §7](007-09-EFICIENCIA-E-AUTONOMIA.md); [integração](007-10-INTEGRACAO-METODOLOGICA.md).

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

Knowledge: prova estável recuperada, mas não houve ciclo real de curadoria/promoção de entrada Knowledge. Skills: contrato de escolha humana e sete fichas já preservados, aplicação com decisão humana real ainda não testada. Tools: git/Python locais utilizados como utilitários, não admitidos no catálogo; ferramenta restrita não instalada. NOM-001: nomes legíveis de tarefas e fixtures; avaliação de compreensão por outro humano não realizada. COM-001: resposta com ação humana final aplicável; não se mede cumprimento em outros agentes. Governança modular e bootstrap de projeto real permanecem não avaliados. Os ensaios não são suficientes para conclusão de v0.2, v0.3, v0.4 ou V1.0.

## 6. Próximo gate dentro da etapa 11

Após homologar e integrar ISO-001, preparar cenários fictícios independentes de perfis distintos, desde a fundação, com critérios e autorização definidos antes da execução. Testar isolamento (inclusive rejeição de contexto alheio sintético), recuperação, Knowledge local, escolha humana de Skills, comparação de ferramentas genéricas, autonomia e encerramento. Se houver possibilidade de sessões independentes, registrar condições comparáveis; senão declarar limites. Nenhum dado, projeto, ferramenta particular ou ambiente real será fonte. Não alterar critérios de maturidade; ensaios fictícios não demonstram adoção por projetos reais.

## 7. Acompanhamento

12/14 etapas homologadas. Rodada inicial de 11 executada; PR de acompanhamento em revisão, não pedido de homologação final. Nenhum consumidor modificado, operação real, publicação, admissão Tool, release ou licença. Nenhuma nova entrada Knowledge. PRs #4/#5 preservadas. Script e resultados não incluem fonte privada. Decisões de desenho: fixtures sintéticas, mesmos critérios, mesma execução consciente em sequência, fixtures exclusivamente independentes. Limites: sem executor independente, sem avaliação de campo em projetos reais, sem baseline de tempo/consumo comparável, sem teste empírico completo de Skills/Knowledge/Tools. Não declarar etapa 11 concluída antes de resolver escopo dos ensaios complementares e gate.
