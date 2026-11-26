# Inventário de distribuição independente — etapa 12

**Natureza:** estudo de distribuição independente preservado para eventual necessidade futura; não é pacote produzido, publicado ou requisito da etapa 12. A finalidade esclarecida pelo responsável é uso próprio e portfólio público, sem licença formal. Não materializar este inventário sem autorização específica. Baseline `8c20cddcde82d334ab75bce6667dd504816cc165`. A lista fixa os arquivos e blobs Git da revisão auditada; as reconciliações documentais da etapa 12 e ajustes de distribuição serão verificados contra a revisão de origem efetivamente aprovada. Não transportar histórico, autoria de commits, PRs, logs, hashes históricos ou links para repositório de manutenção no pacote. Não usar este inventário administrativo como conteúdo da distribuição.

## Seleção de origem

46 arquivos do núcleo e adoção como fontes diretas, 22 arquivos de propostas/planejamento como fontes de manutenção e de guias, 17 arquivos de laboratório mantidos fora da edição inicial. Nenhuma exclusão na origem. A lista de origem não é autorização de redistribuição.

| Caminho de origem | Blob Git | Tratamento |
| --- | --- | --- |
| `AGENTS.md` | `55efd3688160a7c44ecb60a8aea0a78c8cc2de4b` | Reconciliar identidade/status e retirar referências administrativas |
| `README.md` | `d7e4631834b12e08c0bfbfb285290ce29ded1dd5` | Reconciliar identidade/status e retirar referências administrativas |
| `ROADMAP.md` | `530728d9d97b1bfaea5670111335906dba12e4c1` | Reconciliar identidade/status e retirar referências administrativas |
| `docs/01-VISAO-GERAL.md` | `2314516a38e6ff3d8169a037072b19d703128a9f` | Preservar conteúdo; rever links, status e direitos |
| `docs/02-PRINCIPIOS.md` | `bb1fdca384228dc1e29589aa35406f7c916e2981` | Preservar conteúdo; rever links, status e direitos |
| `docs/03-PAPEIS-E-RESPONSABILIDADES.md` | `8e2eae5f23f8edc35176d73f3804e6986c5d8087` | Preservar conteúdo; rever links, status e direitos |
| `docs/04-FLUXO-DE-DESENVOLVIMENTO.md` | `1b981672bdefc4e3031e68b20431e65344f80c2d` | Preservar conteúdo; rever links, status e direitos |
| `docs/05-GOVERNANCA-E-HOMOLOGACAO.md` | `831e4e894aaef854c94c74c342f7b1a51db11a97` | Preservar conteúdo; rever links, status e direitos |
| `docs/06-GIT-E-GITHUB.md` | `833cd20e71746a4db85c17790ed817b244599fe8` | Preservar conteúdo; rever links, status e direitos |
| `docs/07-IA-NO-METODO.md` | `11642c06d80726b3536da6b6510b60007ee3c54a` | Preservar conteúdo; rever links, status e direitos |
| `docs/08-APLICACAO-E-EVOLUCAO.md` | `e4c16479880919d4a76814aa2a65419973471365` | Preservar conteúdo; rever links, status e direitos |
| `docs/09-ANTI-PADROES.md` | `b2c2d71f18e665d8fffcc700e6b0800975e91320` | Preservar conteúdo; rever links, status e direitos |
| `docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md` | `4ad47152c4e2bd2659df28d3d558698dc40a58a4` | Preservar conteúdo; rever links, status e direitos |
| `docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md` | `f71da6a838a9a08a6aad3b3cf5ebbaf6e6ef4d78` | Preservar conteúdo; rever links, status e direitos |
| `docs/12-SEGURANCA-E-INTEGRIDADE.md` | `624c56ee40af252ae87e7a70e494dd4f8cc86319` | Preservar conteúdo; rever links, status e direitos |
| `examples/01-APLICACAO-FICTICIA.md` | `8d7b70f8b86e8e82ec0d7641e2d9168e442b7da4` | Preservar conteúdo; rever links, status e direitos |
| `knowledge/README.md` | `b54e22bcad87b5213ee67290c230306a372d67c7` | Preservar conteúdo; rever links, status e direitos |
| `onboarding/CHECKLIST-NOVO-PROJETO.md` | `b248371dd219a79dd60c58f3984b4ccc148a867e` | Preservar conteúdo; rever links, status e direitos |
| `onboarding/CONTRATO-DE-TRABALHO.md` | `daa065865854249f2ea998c892c8d917eaa2f0c2` | Preservar conteúdo; rever links, status e direitos |
| `onboarding/PROMPT-INICIAL.md` | `a2d09d566d6e385a720dbfd503ed3832987c3483` | Preservar conteúdo; rever links, status e direitos |
| `onboarding/README.md` | `92328e39e6c97eb52b67a2fe4fbe5fa5bf4cd3ae` | Preservar conteúdo; rever links, status e direitos |
| `skills/README.md` | `15d1d682c81a22d6bc11f54f9e113f793821ff6c` | Reconciliar identidade/status e retirar referências administrativas |
| `skills/ui-ux/avaliacao-de-acessibilidade.md` | `0684e558899adb41e1fa788277de1725a03a724a` | Preservar conteúdo; rever links, status e direitos |
| `skills/ui-ux/avaliacao-heuristica.md` | `4a968bdd316ad35513c96181a7783ce5134f358f` | Preservar conteúdo; rever links, status e direitos |
| `skills/ui-ux/design-sprint.md` | `89ddbc947b2580776019e6ee490e923540427dbf` | Preservar conteúdo; rever links, status e direitos |
| `skills/ui-ux/design-thinking-ideo.md` | `61b65cee173ee895559ade695ea4f74a64f0a607` | Preservar conteúdo; rever links, status e direitos |
| `skills/ui-ux/double-diamond.md` | `ba729f4eeaed49e71d3b8cd9f5b86e1914af980d` | Preservar conteúdo; rever links, status e direitos |
| `skills/ui-ux/entrevistas-com-usuarios.md` | `1d2ae70936124f7861fe937d4194d3e6fbb123c2` | Preservar conteúdo; rever links, status e direitos |
| `skills/ui-ux/teste-de-usabilidade.md` | `ce892443df4808778427617b7bee7dd74bddb4e9` | Preservar conteúdo; rever links, status e direitos |
| `templates/AGENTS-TEMPLATE.md` | `01087f27f12b8b645c94b988dfbd20e9bb109e7c` | Preservar conteúdo; rever links, status e direitos |
| `templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md` | `aebae506f5baed9b9374d8188cca11904b83d6c0` | Preservar conteúdo; rever links, status e direitos |
| `templates/HOMOLOGACAO-TEMPLATE.md` | `28ba2e1e3aa3f6df87c57dfa62c2368d7fef4a6c` | Preservar conteúdo; rever links, status e direitos |
| `templates/IMPLEMENTACAO-PROMPT-TEMPLATE.md` | `160e5cdd2d4beea74755a084dad207d691a71ecf` | Preservar conteúdo; rever links, status e direitos |
| `templates/KNOWLEDGE-ENTRY-TEMPLATE.md` | `e19392f170583ae5a054264fbb5d96d5c7e0a2dc` | Preservar conteúdo; rever links, status e direitos |
| `templates/KNOWLEDGE-README-TEMPLATE.md` | `b54e22bcad87b5213ee67290c230306a372d67c7` | Preservar conteúdo; rever links, status e direitos |
| `templates/README-INICIAL-TEMPLATE.md` | `c1710b41059de0f3dc9fd0404b788b986881d969` | Preservar conteúdo; rever links, status e direitos |
| `templates/TASK-TEMPLATE.md` | `6468e0d1c714f2661d5340afe0362cfed217f63a` | Preservar conteúdo; rever links, status e direitos |
| `templates/VERIFICACAO-FINAL-TEMPLATE.md` | `94b164a1b241db7c83666af4cb8a8f220256baad` | Preservar conteúdo; rever links, status e direitos |
| `tools/README.md` | `8db9a5ae767722b802bf8d30ab1e688a30d83a4b` | Reconciliar identidade/status e retirar referências administrativas |
| `tools/modelo-de-ficha.md` | `6aa9eff6e8fa2f3249ed022be932b7c00a845806` | Preservar conteúdo; rever links, status e direitos |
| `tools/revisao-de-interfaces.md` | `532a1338e715ac696a2574894b7ddaf666b3ee26` | Reconciliar identidade/status e retirar referências administrativas |
| `troubleshooting/001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md` | `0dfca5e5b2be3a405dc2bc22ab56327f65b3d796` | Preservar conteúdo; rever links, status e direitos |
| `troubleshooting/002-DEPLOY-PREVIEW-FLUXO-OPERACIONAL-NAO-RECUPERADO.md` | `5b28c76ababcdea1120ce8562acc3906ce656f85` | Preservar conteúdo; rever links, status e direitos |
| `troubleshooting/003-INTERRUPCAO-CODEX-TRABALHO-LOCAL.md` | `b2d9bab31bf03864def8bb27bf3d2efef912be98` | Preservar conteúdo; rever links, status e direitos |
| `troubleshooting/004-ENCERRAMENTO-SEM-SINCRONIZACAO-DOCUMENTAL.md` | `13e41cb1b5c75bb5ba31e580509168467ddf1e54` | Preservar conteúdo; rever links, status e direitos |
| `troubleshooting/README.md` | `471673e81645685af51c6dbc68306f8ff0844d55` | Preservar conteúdo; rever links, status e direitos |

## Guias complementares e dependências

Omitir a pasta proposals administrativa do pacote; não eliminar seu conteúdo necessário ao uso. Antes de exportar, inventariar todos os links do núcleo a proposals e transformar as fontes necessárias em guias autônomos, com cobertura semântica e referências profissionais. Em particular:
- eficiência: protocolo de indicadores, baseline e comparação (proposta 007-09, §7);
- documentação: convenções NOM-001 e modelos README A/B (007-08, §§2/4);
- Skills: contrato de curadoria e seleção, complementado pela descoberta proativa de docs 08 (007-09A);
- Tools: contrato de admissão, seleção, consumo, retirada e direitos (007-09B);
- preflight e outras referências pertinentes de troubleshooting: recuperar as regras aprovadas sem origem particular;
- índice de evolução público: explicar como propor melhorias futuras, sem importar o registro administrativo anterior.

Reconciliar README, ROADMAP, AGENTS, índices Skills/Tools, docs e troubleshooting com as fontes finais. Exemplos e guias devem funcionar sem repositório de manutenção, histórico ou dados de consumidor. Não converter referências profissionais em materiais licenciados pelo ÓRBITA. Preservar autoria e direitos de terceiros. Não criar licença formal para o portfólio; qualquer futura distribuição distinta exigirá decisão própria. A lista final de um eventual pacote poderá divergir da seleção de origem, conforme guias e conteúdo efetivamente autorizados.

## Mantidos exclusivamente na manutenção

- `proposals/001-README-ACOMPANHAMENTO-VISUAL.md`
- `proposals/002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md`
- `proposals/003-CONSOLIDACAO-DOCUMENTAL-SEM-PERDA.md`
- `proposals/004-GATES-FIDELIDADE-VISUAL-3D.md`
- `proposals/005-BACKLOG-DE-EVOLUCAO.md`
- `proposals/006-KNOWLEDGE-BASE-DE-CONHECIMENTO-OPERACIONAL.md`
- `proposals/007-01-AUDITORIA-INTEGRAL.md`
- `proposals/007-02-AUDITORIA-HUB-E-PROJETOS.md`
- `proposals/007-03-ARQUITETURA-METODOLOGICA.md`
- `proposals/007-04-LIMPEZA-OPERACIONAL.md`
- `proposals/007-05-CHATS-E-CONTINUIDADE.md`
- `proposals/007-06-CONFIGURACAO-DE-PROJETOS-IA.md`
- `proposals/007-07-EVOLUCAO-DO-KNOWLEDGE.md`
- `proposals/007-08-DOCUMENTACAO-E-NOMENCLATURA.md`
- `proposals/007-09-EFICIENCIA-E-AUTONOMIA.md`
- `proposals/007-09A-ORBITA-SKILLS.md`
- `proposals/007-09B-ORBITA-TOOLS.md`
- `proposals/007-10-INTEGRACAO-METODOLOGICA.md`
- `proposals/007-11-NEUTRALIDADE-E-ISOLAMENTO.md`
- `proposals/007-11-VALIDACAO-PRATICA.md`
- `proposals/007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md`
- `proposals/README.md`
- `examples/piloto-orbita/README.md`
- `examples/piloto-orbita/avaliacao-heuristica/README.md`
- `examples/piloto-orbita/avaliacao-heuristica/antes.html`
- `examples/piloto-orbita/avaliacao-heuristica/antes.json`
- `examples/piloto-orbita/avaliacao-heuristica/depois.html`
- `examples/piloto-orbita/avaliacao-heuristica/depois.json`
- `examples/piloto-orbita/avaliacao-heuristica/inspecionar.py`
- `examples/piloto-orbita/baseline-execution.txt`
- `examples/piloto-orbita/baseline-result.json`
- `examples/piloto-orbita/baseline-setup.jsonl`
- `examples/piloto-orbita/candidata-execution.txt`
- `examples/piloto-orbita/candidata-result.json`
- `examples/piloto-orbita/candidata-setup.jsonl`
- `examples/piloto-orbita/ensaio-isolamento.py`
- `examples/piloto-orbita/negative-result.json`
- `examples/piloto-orbita/pilot.py`
- `examples/piloto-orbita/resultado-isolamento.json`

Não incluir logs, PRs, histórico Git, tags ou branches de origem. O laboratório independente já executado sustenta avaliação interna limitada; não apresentá-lo como estudo de caso de adoção. Se uma edição futura distribuir scripts, revisar direitos e escopo MIT separadamente.

## Critérios de verificação do pacote

- Conteúdo selecionado e mapeamento origem→destino com cobertura das regras e referências; nenhum requisito dependente perdido.
- Varredura textual de identificadores, segredos, dados e URLs históricas; conferência manual de sentido; links relativos/âncoras/contexto gerado; nenhuma referência necessária ao repositório de origem.
- Sete fichas profissionais com autoria, fontes, limites e direitos revistos; Knowledge inicial vazio; catálogo Tools vazio; ISO-001, COM-001/002, NOM-001, Satélites e gates preservados.
- Para eventual distribuição separada: direitos de uso e limites explícitos; árvore inicial independente (sem ancestralidade anterior); manifesto e hashes do pacote final. Não exigir licença padronizada.
- Verificação após publicação no destino real; não declarar limpeza histórica de cópias preexistentes.
