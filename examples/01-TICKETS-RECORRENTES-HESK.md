# Estudo de caso 01 — Tickets Recorrentes HESK

## Projeto

**Case público sanitizado:** [jotaCorsino/hesk-recurring-tickets](https://github.com/jotaCorsino/hesk-recurring-tickets)

O projeto desenvolve uma camada externa de automação para criação de chamados recorrentes em uma instalação HESK, com persistência própria, scheduler, segurança contra duplicidade, processamento em lote e painel administrativo.

Este estudo de caso não pretende expor o ambiente operacional completo. Seu objetivo é mostrar **como os princípios do Método ÓRBITA aparecem em um desenvolvimento real** por meio de uma representação pública sanitizada.

## Projeto operacional e representação pública

Durante a evolução do projeto ficou claro que um sistema operacional real não precisa permanecer público para servir como evidência de portfólio.

A estratégia adotada passou a separar:

```text
projeto operacional
privado
        ↓
sanitização
        ↓
case público
        ↓
arquitetura + decisões + processo + resultados
```

O case público utiliza dados, caminhos, hosts, identificadores e exemplos genéricos ou fictícios. Detalhes necessários apenas à operação real permanecem fora da representação pública.

### Princípio demonstrado

**Demonstrar competência não exige expor infraestrutura ou dados operacionais desnecessários.**

## 1. Necessidade antes da implementação

A necessidade inicial poderia ter sido resumida como:

> “Criar tickets recorrentes automaticamente no HESK.”

Em vez de transformar essa frase diretamente em uma implementação extensa, o projeto foi decomposto em etapas progressivas.

Entre elas:

```text
BASE-001  → baseline manual
POC-001   → prova de conceito
CFG-001   → persistência
SCH-001   → scheduler
SAFE-001  → segurança/idempotência
BATCH-001 → processamento em lote
ERR-001   → erros operacionais
UI-001    → interface administrativa
DEP-001   → implantação
OPS-001   → operação
```

Essa decomposição é um exemplo direto do princípio **Blocos incrementais**.

## 2. Baseline antes da automação

Antes de automatizar o processo, foi criado e validado manualmente um ticket de referência.

Essa baseline serviu como comportamento esperado para a prova de conceito.

### Princípio demonstrado

**Planejar antes de executar.**

A automação não deveria apenas “criar algum ticket”; ela deveria reproduzir um resultado conhecido.

## 3. Prova de conceito isolada

A POC validou primeiro a capacidade de criar um único ticket usando o mecanismo correto do HESK.

Somente depois dessa capacidade ter sido demonstrada o projeto avançou para persistência e recorrência.

### Princípio demonstrado

**Uma hipótese técnica importante deve ser validada antes de construir camadas que dependem dela.**

## 4. Persistência sem antecipar execução

A etapa de persistência criou o modelo de recorrências e sua administração sem, naquele momento, gerar tickets automaticamente.

Isso permitiu validar separadamente estrutura, migrations, datas, integridade e operações básicas.

### Princípio demonstrado

**Uma tarefa deve possuir escopo controlável e evidência própria.**

## 5. Scheduler separado do worker

O scheduler foi homologado inicialmente produzindo executions pendentes, sem criar tickets reais.

Dessa forma, cálculo de recorrência e materialização do chamado não ficaram acoplados em uma única etapa impossível de observar separadamente.

### Princípio demonstrado

**Separar responsabilidades também se aplica à arquitetura do software, não apenas aos agentes.**

## 6. Segurança antes de escala

Antes da geração de lotes, uma etapa específica tratou claim, lease, heartbeat, retry e proteção contra processamento concorrente.

Só então o sistema avançou para criação de múltiplos tickets.

### Princípio demonstrado

**A próxima capacidade só é adicionada quando a fundação da anterior está homologada.**

## 7. Evidências de homologação

As etapas registram evidências como:

- testes automatizados;
- validações no ambiente real;
- bancos isolados para homologação;
- estado antes e depois;
- prevenção de efeitos colaterais;
- commits e branches;
- limitações não reproduzidas manualmente;
- status explícito da tarefa.

Um detalhe importante é que limitações também são evidência.

Quando determinado cenário permaneceu coberto apenas por teste automatizado e não por reprodução manual, isso foi registrado em vez de apresentado como validação equivalente.

### Princípio demonstrado

**Evidenciar não é apenas listar sucessos; é registrar o que foi e o que não foi validado.**

## 8. Gates humanos

O roadmap do projeto utiliza estados de trabalho e a implementação deve parar em **AGUARDANDO_HOMOLOGACAO**.

A próxima tarefa não deve começar automaticamente apenas porque o agente terminou a implementação.

### Princípio demonstrado

**Aprovação antes do avanço.**

## 9. O papel de cada participante

Na condução desse projeto:

| Participante | Papel |
|---|---|
| **João Corsino** | define necessidade, avalia comportamento, aprova direção e homologa |
| **ChatGPT** | auxilia análise, planejamento, decomposição, revisão e instruções |
| **Codex** | trabalha sobre o repositório, implementa, testa e apresenta evidências |
| **GitHub** | preserva código, documentação, commits, branches, PRs e estado aprovado |

Essa composição corresponde diretamente aos papéis descritos no Método ÓRBITA.

## 10. O que este caso ensinou ao método

A experiência reforçou seis regras:

1. **Homologação real precisa ser distinguida de teste automatizado.**
2. **Bancos e ambientes isolados reduzem risco durante validações.**
3. **Registrar limitações aumenta a confiança no processo.**
4. **Tarefas intermediárias de segurança podem ser necessárias antes de funcionalidades visíveis.**
5. **Documentação atualizada permite retomar o desenvolvimento sem depender integralmente do histórico das conversas.**
6. **Projeto operacional e case público podem — e às vezes devem — ser artefatos separados.**

## Conclusão

O projeto Tickets Recorrentes HESK funciona como uma evidência de que o ÓRBITA não foi definido apenas de forma teórica.

O método é, em grande parte, uma **formalização posterior de práticas que já estavam sendo usadas para manter um projeto assistido por IA compreensível e controlado**.

Essa relação é importante:

> o projeto não foi adaptado para parecer seguir o ÓRBITA; o ÓRBITA foi extraído e organizado a partir de práticas que já demonstravam utilidade no desenvolvimento real.
