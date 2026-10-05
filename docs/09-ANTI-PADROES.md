# 09 — Anti-padrões

O ÓRBITA também é definido pelo que procura **evitar**.

Os itens abaixo não representam proibições absolutas. São sinais de que o processo pode estar perdendo clareza, rastreabilidade ou governança.

## 1. Prompt-to-production

### Sintoma

Uma necessidade ampla é entregue diretamente a um agente e a resposta resultante segue para produção sem decomposição, revisão ou validação intermediária.

### Risco

Uma alteração grande pode misturar decisões de arquitetura, requisitos presumidos, correções paralelas e novas funcionalidades, tornando difícil identificar onde surgiu um erro.

### Resposta ÓRBITA

Transformar a necessidade em tarefas menores com critérios de aceite e gates proporcionais ao risco.

---

## 2. Autoaprovação do agente

### Sintoma

O mesmo agente interpreta a necessidade, escolhe a abordagem, implementa e conclui que o resultado está correto.

### Risco

A cadeia não possui um ponto independente de questionamento.

### Resposta ÓRBITA

Separar conceitualmente planejamento, execução, evidência e homologação, mesmo quando a mesma ferramenta técnica é usada em mais de um papel.

---

## 3. Chat como banco de conhecimento

### Sintoma

Decisões importantes existem apenas no histórico de uma conversa.

### Risco

O contexto pode ser perdido, resumido ou ficar inacessível para outro colaborador ou agente.

### Resposta ÓRBITA

Mover decisões que precisam persistir para o repositório: documentação, código, issues, commits ou Pull Requests.

---

## 4. Escopo silencioso

### Sintoma

Durante uma tarefa, o agente começa a corrigir ou melhorar componentes não solicitados sem registrar a ampliação.

### Risco

A revisão deixa de saber quais mudanças eram necessárias e quais foram oportunistas.

### Resposta ÓRBITA

Manter escopo explícito. Necessidades novas tornam-se nova tarefa, salvo quando forem pré-requisitos inevitáveis e devidamente registrados.

---

## 5. “Passou no teste, então terminou”

### Sintoma

Uma tarefa é considerada concluída apenas porque compilou ou os testes automatizados passaram.

### Risco

Validação técnica não garante que a necessidade funcional foi atendida.

### Resposta ÓRBITA

Distinguir **validação técnica** de **homologação**.

---

## 6. Próxima tarefa antes da homologação

### Sintoma

O desenvolvimento continua acumulando novas funcionalidades enquanto a etapa anterior ainda não foi avaliada.

### Risco

Uma decisão errada no início pode contaminar várias etapas seguintes.

### Resposta ÓRBITA

Usar gates e manter tarefas relevantes em `AGUARDANDO_HOMOLOGACAO` até a decisão humana.

---

## 7. Repositório que não representa o projeto

### Sintoma

Código, documentação, status e decisões contam histórias diferentes.

### Risco

Ninguém consegue determinar com segurança qual é o estado real do sistema.

### Resposta ÓRBITA

Tratar o repositório como referência persistente e atualizar documentação e status junto das mudanças que alteram o estado do projeto.

---

## Regra de leitura

Quanto mais desses anti-padrões aparecem ao mesmo tempo, maior a necessidade de aumentar a formalidade do processo.
