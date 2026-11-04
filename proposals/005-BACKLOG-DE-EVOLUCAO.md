# Proposta 005 — Backlog de evolução do projeto

- **Categoria:** evolução contínua / gestão de escopo / rastreabilidade.
- **Registrada em:** 04/11/2026.
- **Origem:** necessidade observada na evolução contínua de projetos que utilizam o Método ÓRBITA.
- **Estado:** **AGUARDANDO_HOMOLOGACAO**.
- **Escopo:** projetos mantidos pelo Método ÓRBITA, independentemente da tecnologia utilizada.

## 1. Problema observado

Durante desenvolvimento, homologação, troubleshooting, operação e uso contínuo surgem necessidades que não pertencem ao escopo corrente, mas possuem valor futuro:

- novas funcionalidades;
- melhorias de UX/UI;
- upgrades tecnológicos;
- refatorações;
- otimizações;
- integrações;
- melhorias de segurança;
- automações;
- débitos técnicos;
- necessidades identificadas por usuários ou operação.

Sem um mecanismo padrão, essas necessidades tendem a seguir um de três caminhos inadequados:

1. entram silenciosamente no escopo atual;
2. ficam dispersas em conversas, issues avulsas ou anotações;
3. são esquecidas após o encerramento da tarefa que as revelou.

O primeiro caso cria **scope creep**. Os demais reduzem continuidade e rastreabilidade.

## 2. Objetivo

Adicionar ao ÓRBITA um mecanismo simples e persistente de **backlog de evolução**, permitindo registrar necessidades futuras sem convertê-las automaticamente em trabalho autorizado.

O backlog deve servir como memória operacional da evolução potencial do projeto.

Princípio:

> **Registrar no backlog não significa autorizar implementação.**

## 3. Posição canônica

Todo projeto que utiliza o ÓRBITA deve possuir, por padrão, uma seção **Backlog** no `README.md`.

O README é escolhido porque funciona como superfície de entrada do projeto e permite que responsáveis humanos e agentes identifiquem rapidamente:

- o que o projeto faz;
- em qual estado está;
- quais evoluções futuras já foram identificadas.

O backlog do README não substitui roadmap, issue tracker, tarefas, PRs ou documentação técnica detalhada.

Projetos extremamente simples podem manter a seção vazia até que exista uma necessidade futura registrada, mas a presença da seção deve ser o padrão do template inicial.

## 4. Modelo proposto

Modelo mínimo:

```md
## Backlog

Necessidades identificadas para evolução futura do projeto.
A inclusão de um item neste backlog não autoriza sua implementação.

| ID | Tipo | Item | Prioridade | Origem | Status |
| --- | --- | --- | --- | --- | --- |
| BL-001 | Feature | [descrição curta] | Média | Homologação | Backlog |
```

### Campos

**ID**  
Identificador persistente do item no projeto, no formato `BL-001`, `BL-002` e seguintes.

**Tipo**  
Classificação curta para facilitar leitura e agrupamento. Exemplos:

- Feature;
- Melhoria;
- Upgrade;
- Correção;
- Refatoração;
- Segurança;
- Infra;
- Débito técnico.

A lista não deve ser tratada como enumeração rígida quando o projeto exigir outra categoria.

**Item**  
Descrição curta, objetiva e suficiente para reconhecer a necessidade.

**Prioridade**  
Ordem relativa de atenção. Padrão sugerido:

- Alta;
- Média;
- Baixa.

A prioridade representa intenção de análise, não compromisso de execução ou prazo.

**Origem**  
Contexto em que a necessidade foi identificada. Exemplos:

- desenvolvimento;
- homologação;
- troubleshooting;
- operação;
- cliente;
- auditoria;
- segurança.

Esse campo preserva rastreabilidade sem exigir documentação extensa dentro do README.

**Status**  
Estado mínimo do item no backlog.

## 5. Estados do backlog

O backlog não deve replicar o fluxo completo de tarefas do ÓRBITA.

Estados propostos:

- **Backlog** — necessidade registrada, ainda não selecionada;
- **Selecionado** — item escolhido para virar planejamento/tarefa;
- **Concluído** — necessidade atendida e encerrada;
- **Descartado** — item avaliado e deliberadamente não será executado.

Quando um item passa para **Selecionado**, a execução deixa de ser controlada pelo backlog e passa a seguir o fluxo normal do ÓRBITA:

```text
Backlog
   ↓
Selecionado
   ↓
Análise / planejamento
   ↓
Tarefa
   ↓
Branch
   ↓
Implementação
   ↓
Evidências
   ↓
Homologação
   ↓
Merge
```

Por isso, o backlog não precisa duplicar estados como:

- Em implementação;
- Em validação;
- Aguardando homologação;
- Em revisão.

Esses estados pertencem ao acompanhamento da tarefa, não ao backlog.

## 6. Relação entre backlog, escopo e roadmap

Os três conceitos devem permanecer distintos.

### Escopo atual

Define o que está autorizado para a entrega corrente.

### Roadmap

Organiza etapas ou objetivos já planejados para evolução do projeto.

### Backlog

Registra necessidades candidatas que ainda não precisam fazer parte do planejamento ativo.

Fluxo conceitual:

```text
necessidade identificada
        ↓
pertence ao escopo atual?
   ┌───────────┴───────────┐
  sim                     não
   ↓                       ↓
tarefa atual             backlog
                            ↓
                     seleção futura
                            ↓
                         análise
                            ↓
                        roadmap /
                         tarefa
```

O backlog funciona como área de captura. O roadmap representa planejamento. A tarefa representa execução autorizada.

## 7. Pontos de captura

Uma necessidade futura deve ser considerada para registro no backlog quando surgir durante:

- análise;
- desenvolvimento;
- testes;
- homologação;
- troubleshooting;
- uso em produção;
- auditoria;
- feedback do usuário;
- manutenção;
- verificação final.

Antes de encerrar uma tarefa, o responsável pela coordenação deve responder, proporcionalmente:

> **Foi identificada alguma necessidade futura relevante que não pertence ao escopo atual e ainda não está registrada no backlog?**

Se sim, o item deve ser registrado antes do encerramento.

Isso evita que aprendizados do ciclo atual desapareçam sem expandir silenciosamente o escopo.

## 8. Seleção de um item para desenvolvimento

Selecionar um item do backlog não significa implementá-lo diretamente.

O fluxo recomendado é:

1. revisar o item;
2. confirmar que ainda é relevante;
3. definir prioridade real;
4. esclarecer necessidade e critérios;
5. decidir se entra no roadmap ou vira tarefa direta;
6. criar a unidade de trabalho correspondente;
7. vincular ou citar o ID do backlog quando útil;
8. seguir o fluxo normal do ÓRBITA.

Se a necessidade mudou substancialmente, o item pode ser atualizado antes da seleção.

## 9. Encerramento de itens

Quando a necessidade for atendida, o item pode permanecer no README como `Concluído` enquanto houver valor de rastreabilidade.

Quando o volume histórico tornar o README pesado, itens concluídos antigos podem ser movidos para documentação histórica, desde que o backlog ativo continue simples e legível.

Itens descartados devem registrar apenas informação suficiente para deixar claro que a decisão foi deliberada. O README não deve acumular justificativas extensas.

## 10. Regra de proporcionalidade

O backlog deve ser leve.

Ele **não exige**, por padrão:

- estimativa em horas;
- sprint;
- data obrigatória;
- responsável individual;
- story points;
- dependências detalhadas;
- especificação completa;
- critérios de aceite;
- criação imediata de issue.

Essas informações pertencem ao planejamento e à tarefa quando o item for selecionado.

O objetivo do backlog é **capturar e organizar evolução potencial**, não transformar o README em ferramenta pesada de gestão.

## 11. Mudanças propostas no método

Se homologada, esta proposta deve gerar ajustes em:

- `docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md` — incluir backlog na fundação documental padrão;
- `templates/README-INICIAL-TEMPLATE.md` — adicionar seção Backlog;
- `docs/08-APLICACAO-E-EVOLUCAO.md` — definir backlog como mecanismo de captura de evolução;
- fluxo de encerramento/verificação final — incluir captura de necessidades futuras identificadas no ciclo;
- `README.md` do próprio Método ÓRBITA — refletir a nova prática na documentação de adoção quando aplicável.

A incorporação deve evitar duplicar mecanismos já cobertos por roadmap, tarefas ou issues.

## 12. Critérios para homologação

A proposta pode ser incorporada se:

1. separar claramente backlog de escopo autorizado;
2. separar backlog de roadmap e acompanhamento de tarefas;
3. manter o backlog no `README.md` por padrão;
4. permitir captura rápida de necessidades futuras;
5. impedir que o registro de um item implique autorização de implementação;
6. evitar duplicação do fluxo completo de estados do ÓRBITA;
7. permanecer leve o suficiente para projetos pequenos;
8. conectar o encerramento de tarefas à captura de evolução futura;
9. permitir rastreabilidade sem transformar o README em um sistema de gestão complexo.

## 13. Resultado esperado

Com o mecanismo incorporado, o ciclo do ÓRBITA passa a preservar não apenas a entrega corrente, mas também necessidades descobertas durante sua execução:

```text
Planejar
   ↓
Executar
   ↓
Evidenciar
   ↓
Homologar
   ↓
Verificar
   ↓
Capturar evolução futura
   ↓
Encerrar
```

O backlog alimenta ciclos posteriores:

```text
Backlog
   ↓
Priorização
   ↓
Planejamento
   ↓
Nova tarefa
   ↓
Fluxo ÓRBITA
```

## 14. Estado da avaliação

Esta proposta permanece em **AGUARDANDO_HOMOLOGACAO**.

Até sua aprovação e integração à `main`, o backlog não constitui regra normativa do Método ÓRBITA.
