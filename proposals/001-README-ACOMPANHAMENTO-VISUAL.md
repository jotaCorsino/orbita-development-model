# Proposta 001 — Painel visual de acompanhamento no README de cada projeto

- **Tipo:** melhoria futura do Método ÓRBITA / padrão de documentação.
- **Registrada em:** 09/10/2026.
- **Origem:** revisão da apresentação do projeto [Technolife — Central de Links](https://github.com/jotaCorsino/technolife-downloads-web).
- **Estado:** refinamento metodológico preparado em branch dedicada e **aguardando homologação humana**. Nenhuma mudança foi incorporada à `main` até o momento.
- **Escopo deste registro:** preservar a origem, a motivação, os critérios e a evolução da proposta. A mudança só passa a integrar o método após homologação humana e merge na `main`.

## 1. Problema observado

A versão atual do Método ÓRBITA já recomenda criar `README.md`, roadmap, estados de acompanhamento e critérios de homologação na fundação de cada projeto. Porém, ainda **não explicita a posição da tabela de acompanhamento no README nem uma convenção visual de status**.

Consequência observada: o painel de etapas pode aparecer apenas no fim do README ou somente no roadmap, obrigando o responsável pelo projeto a navegar por arquivos para descobrir o estágio atual. Os estados também podem variar entre projetos.

A visibilidade do estágio de desenvolvimento é especialmente importante na colaboração entre responsável humano, agente de planejamento e agente de implementação.

## 2. Padrão visual proposto

Usar **círculos coloridos acompanhados de texto** (não depender somente das cores) na coluna de status da tabela:

| Indicador | Significado | Relação com o fluxo ÓRBITA |
| --- | --- | --- |
| ⚪ Planejado | Etapa planejada, ainda não autorizada para execução | PLANEJADA |
| ⚪ Autorizado | Etapa autorizada, ainda não iniciada | AUTORIZADA |
| 🟡 Em implementação | Implementação em execução | EM_IMPLEMENTACAO |
| 🔵 Em validação | Implementada e em testes ou revisão técnica | EM_VALIDACAO |
| 🔵 Aguardando homologação | Evidências apresentadas e aguardando decisão humana | AGUARDANDO_HOMOLOGACAO |
| 🟢 Concluído | Etapa aprovada e homologada para o escopo definido | CONCLUIDA |
| 🟠 Pausado | Trabalho suspenso com pendência documentada | Condição excepcional; fora do fluxo normativo |

**Nota:** a cor é apenas uma camada visual. O texto deve preservar o estado real do fluxo. O **verde exige homologação humana**; execução técnica ou testes aprovados, isoladamente, não bastam.

`PAUSADO` pode ser usado como condição excepcional de acompanhamento, mas **não integra o conjunto normativo de estados**.

## 3. Posição recomendada no README

A leitura inicial do repositório deve deixar imediatamente claro **o que o projeto faz e em qual fase se encontra**.

Ordem proposta, adaptável conforme o porte do projeto:

1. **Nome do projeto** (título).
2. **Descrição objetiva** de 1 a 3 frases.
3. **Acompanhamento do desenvolvimento** — tabela com fases e status.
4. Problema, objetivo ou visão geral.
5. Solução, funcionalidades, arquitetura/tecnologias e requisitos.
6. Documentação detalhada, instruções de uso e demais seções pertinentes.

A tabela deve estar **próxima ao início**, após a introdução e antes da descrição extensa. Evitar posicioná-la apenas ao final do README. Em projetos com muitas dezenas de tarefas, apresentar **macroetapas no README** e manter os detalhes no roadmap.

## 4. Estrutura mínima recomendada

```md
# Nome do projeto

Descrição breve do que é e do problema resolvido.

## Acompanhamento do desenvolvimento

**Fase atual:** BOOT-001 — aguardando homologação.

| Ordem | ID | Etapa | Status |
| --- | --- | --- | --- |
| 0 | INIT-001 | Fundação documental | 🔵 Aguardando revisão |
| 1 | BOOT-001 | Bootstrap local | 🔵 Aguardando homologação |
| 2 | FE-001 | Primeira funcionalidade | ⚪ Planejado |

**Legenda:** ⚪ Planejado / autorizado · 🟡 Em implementação · 🔵 Em validação / aguardando homologação · 🟢 Concluído (homologado) · 🟠 Pausado.

Detalhamento: [Roadmap](docs/ROADMAP.md)

## Problema e solução
...
```

Os nomes dos arquivos, IDs e etapas variam de acordo com o projeto. Evitar copiar os exemplos como fatos sobre um novo projeto.

## 5. Regra de atualização proposta

- Ao criar a fundação documental, estabelecer a tabela e a legenda no README.
- Ao autorizar, iniciar, validar, pausar ou homologar uma etapa, **atualizar README e roadmap na mesma mudança documental** (quando ambos acompanham o progresso).
- Manter em ambos a mesma fase atual, status, data relevante e próximo gate; links podem apontar para tarefas detalhadas.
- **Não marcar 🟢** por implementação concluída sem a aprovação prevista no projeto.
- Não remover o histórico e os critérios do roadmap em nome da tabela resumida.
- Não usar percentuais artificiais de conclusão: estado e critério de saída são mais verificáveis.
- O README deve permitir identificar rapidamente o **que foi finalizado, o que está em andamento e o que vem depois**.

## 6. Exemplos observados

- [Project Backlog](https://github.com/jotaCorsino/project-backlog) — legenda `⚪ Não iniciado`, `🟡 Iniciado`, `🔵 Em testes`, `🟢 Concluído`, `🟠 Pausado`.
- [Technolife RustDesk](https://github.com/jotaCorsino/technolife-rustdesk) — quadro de fases e entregas com `🟢`, `🟡` e `⚪`.
- [Technolife Central de Links](https://github.com/jotaCorsino/technolife-downloads-web) — tabela colocada imediatamente após a descrição inicial, com legenda e estados de homologação.

## 7. Incorporação metodológica — aguardando homologação

A proposta foi transformada em refinamentos concretos na branch:

`docs/PROP-001-readme-acompanhamento-visual`

Documentos e artefatos preparados:

- [README-INICIAL-TEMPLATE.md](../templates/README-INICIAL-TEMPLATE.md) — novo template reutilizável com descrição breve, painel de acompanhamento, legenda, vínculo com roadmap e orientações de adaptação;
- [docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md) — passou a definir a estrutura recomendada do README inicial e a relação entre visão rápida e documentação detalhada;
- [onboarding/README.md](../onboarding/README.md) — passou a orientar o agente de planejamento a usar o README como painel rápido quando houver fases ou gates;
- [onboarding/CHECKLIST-NOVO-PROJETO.md](../onboarding/CHECKLIST-NOVO-PROJETO.md) — passou a verificar presença, posição, clareza e coerência do acompanhamento visual quando aplicável;
- [docs/04-FLUXO-DE-DESENVOLVIMENTO.md](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md) — passou a relacionar indicadores visuais aos estados normativos sem alterar o fluxo oficial.

### Decisões adotadas no refinamento

- o padrão é **recomendado e proporcional ao projeto**, não obrigatório em qualquer repositório;
- o README funciona como **visão rápida**, não substituto de roadmap, tarefas, histórico ou critérios de aceite;
- indicadores visuais são apenas uma camada de leitura e devem sempre estar acompanhados de texto;
- `🔵 Em validação` e `🔵 Aguardando homologação` continuam sendo estados diferentes;
- `🟢 Concluído` exige homologação;
- `🟠 Pausado` pode ser usado como condição excepcional de acompanhamento, mas não integra a sequência normativa de estados;
- caminhos e estrutura documental continuam adaptáveis ao porte e à natureza do projeto;
- percentuais artificiais de conclusão não são recomendados.

### Estado atual

O refinamento está **implementado na branch de trabalho e revisado de forma cruzada**, mas ainda depende de homologação humana antes de qualquer merge na `main`.

Enquanto a homologação não ocorrer, esta proposta permanece como referência da motivação, dos critérios e das decisões que originaram o refinamento.

## 8. Critérios para aceitar a melhoria

A proposta poderá ser considerada validada quando:

1. o responsável aprovar a organização visual;
2. a convenção não confundir execução técnica com homologação;
3. os exemplos e templates mantiverem o README como apresentação concisa, não substituto do roadmap;
4. o modelo for testado em pelo menos dois projetos com perfis distintos;
5. o conjunto de documentos oficiais for revisado numa alteração específica, com evidências e homologação.

**Próxima ação para o método:** realizar a homologação humana do conjunto preparado na branch. A publicação deste arquivo, isoladamente, **não** constitui alteração normativa automática.
