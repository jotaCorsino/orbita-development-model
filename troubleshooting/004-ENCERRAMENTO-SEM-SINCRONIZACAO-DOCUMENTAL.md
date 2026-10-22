# Problema observado 004 — Encerramento sem sincronização documental final

- **Categoria:** encerramento / consistência documental / rastreabilidade.
- **Registrado em:** 22/10/2026.
- **Origem:** evolução do próprio repositório do Método ÓRBITA após a incorporação de TRB-001 a TRB-003 e PROP-001 a PROP-004.
- **Estado:** ocorrência confirmada; refinamento metodológico em preparação.
- **Impacto:** documentação resumida permaneceu desatualizada apesar de os registros canônicos já estarem homologados e incorporados.

## 1. Ocorrência

Após a incorporação de vários refinamentos metodológicos, o `README.md` principal continuava apresentando informações antigas:

- TRB-001 ainda aparecia como avaliação metodológica pendente;
- TRB-002 e TRB-003 não apareciam na visão geral;
- PROP-001 ainda era apresentada como proposta não oficial;
- PROP-002, PROP-003 e PROP-004 não apareciam no índice resumido.

Os registros canônicos e seus PRs estavam corretos. A falha ocorreu na **documentação derivada de visão geral**, que não foi incluída em uma verificação final de consistência.

## 2. Diagnóstico

O fluxo atual já prevê revisão, homologação, merge e atualização documental. Porém, não existe uma rotina explícita para verificar, ao encerrar uma mudança, se o novo estado foi refletido em todos os pontos derivados relevantes.

O problema não exige:

- novo estado normativo;
- novo gate universal separado;
- atualização obrigatória de todo arquivo do repositório;
- checklist pesado para mudanças pequenas.

A lacuna é operacional: falta uma **varredura final proporcional de consistência**.

## 3. Refinamento proposto

Aplicar duas passagens quando uma mudança alterar estado, identidade, referência, índice, roadmap, documentação agregadora ou informação reproduzida em mais de um lugar.

### Passagem A — antes da integração

Verificar, proporcionalmente:

1. quais arquivos são canônicos para a mudança;
2. quais superfícies derivadas podem repetir ou resumir essa informação — por exemplo README, roadmap, índices, tabelas de acompanhamento, changelog ou documentação de navegação;
3. se branch e PR continuam baseados na `main` esperada e sem mudanças estranhas ao escopo;
4. se IDs, nomes, links, títulos e estados estão coerentes;
5. se permanecem referências claramente obsoletas, como “pendente”, “não oficial”, “aguardando homologação” ou nome de branch antiga, quando já não correspondem ao resultado pretendido.

### Passagem B — depois do merge

Verificar o estado **diretamente na `main`**, e não apenas na branch que foi integrada:

1. confirmar que o PR foi mergeado e identificar o commit resultante;
2. abrir na `main` os registros canônicos afetados;
3. conferir os resumos/índices derivados relevantes;
4. repetir uma busca por status ou referências antigas relacionadas à mudança;
5. validar que links e caminhos principais continuam resolvendo;
6. registrar e corrigir resíduos puramente documentais antes de considerar o encerramento completo.

Se a correção pós-merge for somente de status ou fechamento documental, ela pode ser feita em PR pequeno e isolado. Se a inconsistência alterar significado, regra ou escopo homologado, deve voltar ao fluxo normal de revisão e homologação.

## 4. Regra de proporcionalidade

A verificação final não deve se transformar em varredura integral obrigatória do repositório para qualquer alteração.

Exemplos:

- correção local simples: conferir o arquivo alterado e referências diretamente relacionadas;
- mudança de status/tarefa: conferir registro canônico + README/roadmap ou painel que reproduza o status;
- mudança metodológica ou estrutural: conferir documentação normativa, registros de origem e superfícies de apresentação/índice;
- renomeação/movimentação: conferir links, referências e caminhos afetados.

A pergunta prática é:

> **“Que outros lugares podem continuar contando a versão anterior desta mesma informação?”**

## 5. Objetivo do refinamento

Evitar que uma mudança tecnicamente e metodologicamente correta termine com o repositório apresentando estados contraditórios.

O encerramento deve confirmar não apenas que o artefato foi integrado, mas que a documentação relevante **descreve corretamente o estado que agora existe na `main`**.

## 6. Estado da avaliação

Este registro documenta uma ocorrência real no repositório do próprio Método ÓRBITA.

O refinamento ainda depende de revisão e homologação humana antes de se tornar regra oficial.
