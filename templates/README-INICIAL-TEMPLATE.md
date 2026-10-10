# [NOME_DO_PROJETO]

[Descrição objetiva em 1 a 3 frases: o que é o projeto, qual problema resolve e para quem existe.]

## Acompanhamento do desenvolvimento

> Use esta seção quando o projeto possuir fases, tarefas ou gates que precisem ser acompanhados ao longo do desenvolvimento.
>
> Para repositórios muito simples, bibliotecas pequenas ou projetos sem evolução por etapas, adapte ou omita esta tabela. O objetivo é dar visibilidade ao estado real do projeto, não criar burocracia artificial.

**Fase atual:** [ID / etapa atual — estado textual]

| Ordem | ID | Etapa | Status |
| --- | --- | --- | --- |
| 0 | INIT-001 | Fundação documental | ⚪ Planejado |
| 1 | BOOT-001 | Bootstrap local | ⚪ Planejado |
| 2 | [ID] | [Próxima etapa relevante] | ⚪ Planejado |

**Legenda:** ⚪ Planejado / autorizado · 🟡 Em implementação · 🔵 Em validação / aguardando homologação · 🟢 Concluído (homologado) · 🟠 Pausado.

> **Importante:** o texto do status preserva o estado real do fluxo. `🔵 Em validação` e `🔵 Aguardando homologação` usam o mesmo indicador visual, mas representam gates diferentes.
>
> O indicador 🟢 só deve ser usado quando a etapa estiver homologada para o escopo definido. Implementação concluída ou testes aprovados, isoladamente, não significam conclusão homologada.
>
> `Pausado` representa uma condição excepcional de acompanhamento e não adiciona um novo estado ao fluxo normativo do Método ÓRBITA.

**Detalhamento:** [Roadmap]([CAMINHO_DO_ROADMAP])

## Problema / contexto

[Descreva a necessidade que motivou o projeto, o contexto de uso e o problema que precisa ser resolvido.]

## Objetivo

[Declare o resultado que o projeto pretende alcançar.]

## Escopo inicial

### Incluído

- [item];
- [item].

### Fora do escopo

- [item];
- [item].

## Solução

[Explique de forma objetiva como o software pretende resolver o problema.]

## Arquitetura / tecnologias

[Inclua apenas o nível de detalhe necessário para compreender a solução. Projetos simples podem reduzir ou omitir esta seção.]

## Segurança e restrições

- [riscos, dados sensíveis, autenticação/autorização, exposição pública, dependências ou outras restrições relevantes];
- [indicar explicitamente quando não houver superfície sensível conhecida nesta fase].

## Documentação

- [Roadmap]([CAMINHO_DO_ROADMAP])
- [Arquitetura]([CAMINHO_DA_ARQUITETURA])
- [Outros documentos relevantes]

## Método ÓRBITA

Este projeto utiliza o **Método ÓRBITA — Desenvolvimento de Software Assistido por IA com Governança Humana**.

Princípio operacional:

**Planejar → Executar → Evidenciar → Homologar**

---

## Orientações para adaptar este template

Este arquivo é uma referência inicial, não um formulário rígido.

Ao utilizá-lo:

1. mantenha no início o **nome**, a **descrição objetiva** e, quando o projeto exigir acompanhamento por etapas, o **painel de desenvolvimento**;
2. mostre no README apenas macroetapas suficientes para entender rapidamente o estado atual;
3. mantenha tarefas, critérios, histórico e detalhes no roadmap e nos documentos próprios;
4. mantenha README e roadmap coerentes quando o estado de uma etapa mudar;
5. use os indicadores visuais sempre acompanhados de texto;
6. não use percentual artificial de conclusão quando não existir uma métrica objetiva;
7. adapte nomes de arquivos, IDs e seções ao porte e à natureza do projeto;
8. remova exemplos e placeholders antes de publicar o README real.
