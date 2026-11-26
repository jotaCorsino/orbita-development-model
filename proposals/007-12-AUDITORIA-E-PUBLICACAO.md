# ORB-EVO-001 — 12: Auditoria final e publicação

**Estado:** em andamento — auditoria da baseline e proposta de distribuição para homologação. **Data:** 26/11/2026. **Baseline:** `8c20cddcde82d334ab75bce6667dd504816cc165`, árvore `fe88066dc556208da91c4495b8b2d719f70f2b29`. PRs #51/#54 integradas. A etapa 12 foi autorizada, mas licenciamento, mudança de visibilidade, criação de destino e publicação são decisões próprias. [Plano](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## Em termos práticos

O método está documentado e foi validado em exercícios limitados. A versão atual está adequada para preparar uma edição experimental, não para declarar maturidade V1.0. O repositório existente é público e contém histórico de desenvolvimento; a distribuição deve ter histórico independente e não encaminhar usuários para o histórico anterior. Não há licença registrada. O titular precisa decidir os direitos que concederá e autorizar o destino antes da publicação.

## 1. Auditoria da revisão

| Controle | Resultado |
| --- | --- |
| Main e integração de 11 | Baseline idêntica, PRs #51/#54 integradas |
| Inventário | 85 arquivos, árvore recursiva não truncada |
| Identidade dos blobs lidos | 85/85 correspondentes à árvore em cinco lotes |
| Varredura textual focal | Nenhuma ocorrência dos identificadores particulares conhecidos, perfis retirados, caminhos /home/ pesquisados, padrões de chave privada/token GitHub pesquisados |
| Links relativos Markdown | 453 ocorrências verificadas quanto à existência de caminho; 451 resolvidas diretamente, duas exceções de contexto já conhecidas: ficha Knowledge fictícia em exemplo e Knowledge relativo à raiz de README gerado |
| Vínculos com repositório anterior | 13 documentos contêm URL do repositório histórico; outros contêm números de PR, referências administrativas e hashes históricos |
| Knowledge, Skills e Tools | Base inicial vazia; sete fichas profissionais preservadas; zero ferramentas admitidas; licenças de materiais externos não integralmente auditadas |
| Repositório de desenvolvimento | Visibilidade pública, sem licença registrada, zero releases retornadas, 55 branches no inventário, zero forks no metadado consultado |
| Tags | Endpoint de listagem recusado pelo conector; inventário não comprovado |

A varredura não é auditoria integral de segredos, titularidade, âncoras, links externos, histórico, comentários, forks, caches ou cópias. Uma tentativa de agrupar dois lotes excedeu o limite do conector; o lote seguinte foi consultado separadamente. Nenhum recurso externo foi alterado. Encontradas duas inconsistências textuais de estado/neutralidade na especificação atual: aviso de versão no README anterior ao fechamento de 11 e formulações genéricas de sanitização/promoção em docs 12. A revisão desta PR as reconcilia com ISO-001 já homologada, sem novo requisito ou mudança de gate. Verificação final do delta na PR.

## 2. Maturidade — critérios existentes do ROADMAP

| Marco | Situação demonstrada | Decisão |
| --- | --- | --- |
| v0.1 Fundação | Documentação fundamental homologada | Preservar concluída |
| v0.2 Aplicação prática | Ensaios fictícios; não há dois estudos de caso reais admissíveis como evidência | Em andamento |
| v0.3 Kit operacional | Templates e onboarding ampliados; comparação estrutural e ensaios limitados, não teste em projetos reais de perfis distintos | Manter pendente |
| v0.4 Avaliação | Protocolo e indicadores definidos; não matriz validada em projetos reais, sem baseline causal de eficiência | Manter pendente |
| v1.0 Modelo estável | Especificação candidata consolidada; falta avaliação suficiente de adoção externa, kit, eficácia e direitos de distribuição | Manter pendente |

Não alterar os critérios ou usar 13/14 etapas como porcentagem de maturidade. A política ISO-001 proíbe importar casos reais ao núcleo, inclusive anonimizados. Uma avaliação futura pode ocorrer no próprio contexto do adotante, com comprovação independente de critério do método sem transferência de dados ou referências; nenhum critério é considerado atingido por essa possibilidade. Recomenda-se rótulo de pré-lançamento **v0.2.0-preview.1**, se aprovado: indica trabalho em direção à v0.2, não conclusão de seu gate. Alternativa: não publicar até v1.0. Não atribuir tag agora.

## 3. Licenciamento — decisão do titular

Fontes oficiais consultadas em 26/11/2026: [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br), [BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br), [FAQ Creative Commons](https://creativecommons.org/faq/), [MIT — Open Source Initiative](https://opensource.org/license/mit), [GitHub — licenciamento](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

| Opção documental | Direitos principais | Trade-off |
| --- | --- | --- |
| CC BY 4.0 | Compartilhar/adaptar inclusive comercialmente, crédito, licença e indicação de mudanças | Adoção ampla; não obriga derivação distribuída a manter licença |
| CC BY-SA 4.0 | Direitos semelhantes e licença igual/compatível para adaptações compartilhadas | Reciprocidade; maior restrição para redistribuição de adaptações |
| Reservar direitos / licença específica | Permissões dependem de autorização e termos definidos pelo titular | Menor abertura; não declarar open source ou livre reutilização |

Recomendação condicional à intenção de adoção ampla, inclusive em projetos comerciais: **CC BY 4.0 para textos, fichas próprias e templates; MIT para código próprio efetivamente distribuído, com delimitação explícita dos arquivos e trechos**, preservando avisos e atribuições. CC não é recomendada para software; MIT permite uso, modificação e distribuição com manutenção do aviso de licença. Licença pública não revogável para quem cumpre termos; não publicar sem confirmar titularidade e intenção. Não aplicar a marcas/logos, materiais de terceiros, dependências, direitos não controlados ou projetos criados usando o método. O método não exige que produtos independentes adotem a mesma licença; reprodução de materiais protegidos continua sujeita aos termos aplicáveis. Administração GitHub não prova titularidade. Direitos e atribuições nas fichas devem ser conferidos na preparação do pacote; síntese própria e referência não equivalem a permissão de republicar materiais externos. Sem licença não presumir permissões gerais; repositório público admite visualização/fork conforme termos da plataforma. Nenhum LICENSE criado ou direito concedido. Não é parecer jurídico.

## 4. Estratégia de distribuição

| Alternativa | Avaliação |
| --- | --- |
| Publicar release diretamente no repositório atual | Rejeitada: histórico e PRs antigos continuam acessíveis |
| Reescrever histórico | Não recomendada: risco de romper refs, cópias, diffs e evidências; não garante remoção de exposição |
| Repositório novo, independente, com origem vazia | Recomendada: preservar desenvolvimento e iniciar distribuição somente com conteúdo revisado e sem ancestralidade antiga |

Proposta: manter repositório de desenvolvimento existente como fonte de manutenção, restringir sua visibilidade mediante autorização específica, criar repositório público independente de nome sugerido **orbita** (disponibilidade não verificada), inicialmente vazio/privado para preparação e homologação. Não fork, clone com .git, espelhamento ou importação de histórico. A mudança de visibilidade não retira cópias já obtidas. GitHub [documentação de visibilidade](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility). O conector disponível não oferece ações de criar repositório, alterar visibilidade ou publicar release/tag; preparar conteúdo via Git quando destino autorizado e acessível, e executar as operações restantes por fluxo explícito do titular, sem contornar permissões.

[Inventário de distribuição](007-12-INVENTARIO-DE-DISTRIBUICAO.md) delimita a exportação. Preservar conteúdo normativo e orientações complementares, retirar status administrativo, links a histórico, refs antigas e relatórios de execução do kit público. Não simplesmente copiar toda main. Materializar fontes de apoio em guias independentes, conferir cobertura e redirecionar links. Não usar dados de consumidor, nem mesmo anonimizados. Base Knowledge vazia, catálogo Tools sem ferramentas admitidas. Manter Skills profissionais com autoria, fonte e limites. A autoria do método já aparece no README; confirmar titularidade e crédito para licenciamento; não incluir identificadores de projetos, registros de conversas ou contas de terceiros.

## 5. Gate e verificação final da publicação

Após aprovação: (1) confirmar direitos e destinação, nome/visibilidade e permissões; (2) materializar pacote independente a partir de inventário com alterações documentadas e revisão de guias/links/atribuições; (3) verificar conteúdo, manifesto, integridade, ausência de vínculos antigos, referências transitivas, templates gerados e árvore inicial sem pai histórico; (4) apresentar árvore/pacote e licença exatos para homologação; (5) publicar somente revisão homologada e confirmar destino, visibilidade, conteúdo, versão/release e licença; (6) reconciliar roadmap, manter histórico de manutenção autorizado e não declarar maturidade não demonstrada. Nenhuma exclusão de refs, alteração de visibilidade, mudança de consumidor, licença ou release nesta rodada. 13/14 etapas homologadas. Etapa 12 continua aberta.
