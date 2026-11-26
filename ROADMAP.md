# Roadmap — Método ÓRBITA

Este roadmap acompanha a evolução do próprio método.

O objetivo não é criar complexidade por antecipação. Cada nova camada deve surgir porque resolve um problema observado na prática.

## Acompanhamento

| Versão / Etapa | Objetivo | Status | Critério de saída |
|---|---|---|---|
| **v0.1 — Fundação** | Definir identidade, princípios, papéis, fluxo, governança e anti-padrões | CONCLUÍDA | Documentação fundamental revisada e homologada |
| **v0.2 — Aplicação prática** | Registrar estudos de caso e confrontar o modelo com projetos reais | EM_ANDAMENTO | Pelo menos dois estudos de caso com aprendizados registrados |
| **v0.3 — Kit operacional** | Ampliar templates e regras de adoção | PENDENTE | Templates testados em projetos de perfis diferentes |
| **v0.4 — Avaliação** | Definir sinais de saúde e critérios para avaliar aplicação do método | PENDENTE | Checklist ou matriz de avaliação validada em projetos reais |
| **v1.0 — Modelo estável** | Consolidar uma especificação pública estável | PENDENTE | Conceitos, exemplos e ferramentas suficientemente maduros para adoção externa |

## Iniciativa transversal ORB-EVO-001

[Plano de evolução (PROP-007)](proposals/007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md): 14 etapas previstas e homologadas (iniciativa concluída); [etapa 01 — auditoria integral](proposals/007-01-AUDITORIA-INTEGRAL.md) concluída e integrada pela PR #27. [Etapa 02 — avaliação da composição metodológica](proposals/007-02-AUDITORIA-HUB-E-PROJETOS.md) concluída, homologada e integrada pela PR #29; [etapa 03 — arquitetura metodológica](proposals/007-03-ARQUITETURA-METODOLOGICA.md) concluída, homologada como arquitetura candidata e integrada pela PR #31; [etapa 04 — limpeza operacional](proposals/007-04-LIMPEZA-OPERACIONAL.md) concluída, homologada como protocolo candidato e integrada pela PR #33; [etapa 05 — chats e continuidade](proposals/007-05-CHATS-E-CONTINUIDADE.md) concluída, homologada como protocolo candidato e integrada pela PR #35; [etapa 06 — configuração de projetos IA](proposals/007-06-CONFIGURACAO-DE-PROJETOS-IA.md) concluída, homologada como configuração candidata e integrada pela PR #37; [etapa 07 — evolução do Knowledge](proposals/007-07-EVOLUCAO-DO-KNOWLEDGE.md) concluída, homologada como refinamento candidato e integrada pela PR #39; [etapa 08 — documentação e nomenclatura](proposals/007-08-DOCUMENTACAO-E-NOMENCLATURA.md) concluída, homologada como refinamento candidato e integrada pela PR #41; [etapa 09 — eficiência e autonomia](proposals/007-09-EFICIENCIA-E-AUTONOMIA.md) concluída, homologada como refinamento candidato e integrada pela PR #43; [etapa 09A — ÓRBITA Skills](proposals/007-09A-ORBITA-SKILLS.md) concluída, homologada documentalmente e integrada pela PR #45; [etapa 09B — ÓRBITA Tools](proposals/007-09B-ORBITA-TOOLS.md) concluída, homologada documentalmente e integrada pela PR #47; [etapa 10 — integração metodológica](proposals/007-10-INTEGRACAO-METODOLOGICA.md) concluída, homologada documentalmente e integrada pela PR #49; etapa 11 — validação prática — concluída no escopo limitado; ISO-001 homologada e integrada pela PR #52; [validação prática independente](proposals/007-11-VALIDACAO-PRATICA.md) homologada e integrada pela PR #51, incluindo COM-002, descoberta proativa de Skills, Satélites e planejamento incremental; [etapa 12 — auditoria final e publicação](proposals/007-12-AUDITORIA-E-PUBLICACAO.md) concluída, homologada e integrada pela PR #55; revisão disponibilizada no repositório público atual. Abrange governança modular, limpeza, chats, configuração de agentes, Knowledge, documentação, eficiência, Skills e Tools. Contribui para v0.2–v0.4 e avaliação da V1.0, sem substituir os critérios existentes nem declarar nova versão.

## v0.1 — Fundação

Inclui:

- definição do Método ÓRBITA;
- motivação;
- princípios O-R-B-I-T-A;
- papéis;
- ciclo de desenvolvimento;
- gates;
- homologação;
- uso de Git/GitHub;
- papel da IA;
- anti-padrões;
- primeiros templates operacionais;
- onboarding mínimo para adoção do método em novos projetos;
- identidade e ambiente padronizados por projeto entre planejamento, implementação, working copy e GitHub;
- protocolo de inicialização de novo projeto: fundação documental remota → bootstrap local → primeira funcionalidade;
- baseline transversal de segurança de software, informação e Git/GitHub.

### Gate

A fundação v0.1 foi **homologada** e está pronta para publicação.

## v0.2 — Aplicação prática

Objetivos:

- documentar aplicações reais;
- comparar teoria e prática;
- registrar onde o método precisou ser adaptado;
- identificar regras que realmente agregam valor e regras que geram burocracia desnecessária.

Material ilustrativo: [exemplo fictício de adoção](examples/01-APLICACAO-FICTICIA.md). Não constitui estudo de caso real nem altera os critérios de maturidade; aplicações de campo podem ser avaliadas no contexto de seus responsáveis, sem que o núcleo incorpore dados ou referências de projetos.

## v0.3 — Kit operacional

O onboarding mínimo já existe desde a fundação. Esta etapa deverá ampliar o kit com artefatos operacionais mais especializados.

Itens candidatos:

- template de planejamento;
- template de decisão técnica;
- template de Pull Request;
- checklist de início de tarefa;
- checklist de entrega do agente;
- checklist de homologação;
- exemplo completo de prompt de implementação.

## Avaliação da versão candidata ORB-EVO-001

O [protocolo de eficiência](proposals/007-09-EFICIENCIA-E-AUTONOMIA.md) §7 define baseline, comparação, indicadores, dados ausentes e condições de qualidade para pilotos autorizados na etapa 11. Nenhuma melhoria quantitativa, maturidade v0.2–v0.4 ou V1.0 é inferida da integração documental. A etapa 12 homologou e integrou a revisão de portfólio; a iniciativa ORB-EVO-001 está concluída. Release formal, licença padronizada e distribuição separada não são requisitos dessa finalidade.

## v0.4 — Avaliação

Possíveis dimensões:

- clareza de escopo;
- rastreabilidade;
- cobertura de evidências;
- quantidade de retrabalho;
- aderência entre implementação e requisito;
- atualização documental;
- tempo entre implementação e homologação.

Essas métricas não devem ser adotadas apenas porque são mensuráveis. Precisam demonstrar utilidade prática.

## v1.0 — Modelo estável

A versão 1.0 deverá representar o ponto em que o Método ÓRBITA deixa de ser apenas uma documentação inicial de um processo prático e passa a possuir uma especificação pública consistente, exemplos suficientes e um kit de adoção utilizável por terceiros.
