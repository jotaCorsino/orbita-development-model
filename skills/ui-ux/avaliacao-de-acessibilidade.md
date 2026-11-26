# Avaliação de acessibilidade web — WCAG

**Estado:** ficha candidata — revisão documental inicial; não homologada como Skill vigente. **Tipo:** Técnica de avaliação orientada por padrão. **Competência:** UI/UX. **Revisão da ficha:** inicial (26/11/2026); versão persistente pelo Git.

## Finalidade e seleção

Avaliar critérios de acessibilidade definidos para o escopo, combinando verificações automatizadas e humanas.

**Quando usar:** Interfaces web com requisitos de acessibilidade; teste de fluxos, estados e regressão.

**Limites e contraindicações:** Scanner isolado não prova conformidade; inspeção parcial não é certificação. Não tratar requisitos legais/contratuais como opções descartáveis.

**Alternativas e complementos:** Verificações focais para regressão versus avaliação de conformidade abrangente; [teste de usabilidade](teste-de-usabilidade.md) e [heurística](avaliacao-heuristica.md) complementam, não substituem exigências.

**Esforço:** Varia conforme cobertura, estados, tecnologias assistivas e escopo. Estimativa contextual, não SLA.

## Aplicação — síntese operacional ÓRBITA

**Insumos:** Escopo, nível/versão exigidos, páginas e estados, tecnologia, critérios e capacidade de avaliação humana.

1. Definir escopo, padrão e nível aplicáveis.
2. Selecionar fluxos/estados e critérios, incluindo teclado, foco, semântica e reflow quando pertinentes.
3. Executar verificações automáticas e manuais adequadas; registrar não testado e não aplicável com razão.
4. Consolidar achados por critério e corrigir/reavaliar alcance afetado.

**Entregáveis:** Matriz de critérios por escopo, evidências, falhas, lacunas e relatório de avaliação.

**Evidência:** Versão do padrão, artefato e ambiente, critério, método, resultado e cobertura. Conformidade só se demonstrar todos os requisitos aplicáveis ao escopo declarado.

**Gate:** Manter exigências contratuais/legais e decisão humana; não trocar por avaliação heurística ou preferência. Consulte [contrato de seleção](../../proposals/007-09A-ORBITA-SKILLS.md). Se houver abordagens metodológicas viáveis, apresente opções e recomendação fundamentada; aguarde escolha humana. Não repetir decisão já aprovada nem abrir microgate para passos internos delegados.

## Fontes, autoria e validade

W3C, WCAG 2.2 — https://www.w3.org/TR/wcag/ ; Understanding Conformance — https://www.w3.org/WAI/WCAG22/Understanding/conformance ; Conformance Evaluation and Reports — https://www.w3.org/WAI/test-evaluate/conformance/

WCAG 2.2 Recommendation e orientação WAI consultadas em 26/11/2026; fixar versão/revisão aplicável no projeto. WCAG-EM é metodologia distinta; não declarar aplicação integral sem executá-la.

Termos específicos de reprodução W3C não avaliados integralmente; referência ao padrão e síntese própria, sem reproduzir texto normativo. Esta ficha é síntese própria do ÓRBITA, não tradução integral, certificação ou material oficial dos autores. Reavaliar ao mudar fonte, versão, aplicabilidade, direitos ou evidência contraditória; a revisão documental não prova eficácia em projetos. Consulte [índice](../README.md).
