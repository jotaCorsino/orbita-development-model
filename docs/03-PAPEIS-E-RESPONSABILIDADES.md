# 03 — Papéis e responsabilidades

O ÓRBITA trabalha com papéis, não com dependência obrigatória de ferramentas específicas.

## 1. Responsável humano

Responsabilidades:

- definir necessidade e objetivo;
- estabelecer prioridades e restrições;
- aprovar decisões relevantes;
- avaliar resultado funcional;
- homologar ou rejeitar entregas;
- decidir quando o projeto avança.

O humano é o **proprietário da decisão**, não apenas o autor do prompt.

## 2. Agente de planejamento

Responsabilidades:

- transformar necessidades em problemas claros;
- estruturar requisitos;
- criar e manter a fundação documental inicial do projeto no repositório remoto, quando autorizado;
- criar README, visão, planejamento, roadmap e regras proporcionais ao projeto;
- decompor trabalho em tarefas;
- identificar riscos e dependências;
- produzir instruções de implementação;
- gerar a primeira tarefa de bootstrap para vincular a pasta local ao repositório remoto antes da primeira funcionalidade;
- interpretar evidências retornadas;
- revisar coerência entre planejamento e execução;
- manter visão global do projeto.

O agente de planejamento não substitui a homologação humana.

## 3. Agente de implementação

Responsabilidades:

- inspecionar o repositório;
- implementar apenas o escopo autorizado;
- criar ou alterar código;
- executar testes e builds;
- registrar limitações encontradas;
- produzir evidências técnicas;
- preparar commits e Pull Requests conforme o fluxo adotado.

O implementador não deve expandir escopo silenciosamente.

## 4. Git/GitHub

Responsabilidades:

- manter código e documentação;
- registrar evolução;
- sustentar branches, commits e Pull Requests;
- preservar histórico;
- tornar o estado do projeto reconstruível.

## Separação de responsabilidades

A separação é intencional:

**humano decide → planejador estrutura → implementador executa → repositório registra → humano homologa.**

Um mesmo produto de IA pode tecnicamente exercer mais de um papel, mas os papéis devem continuar conceitualmente distintos.

## Papéis e ambientes não são a mesma coisa

O ÓRBITA separa **quem faz o quê** de **onde o trabalho acontece**.

| Ambiente atual | Papel predominante | Observação |
|---|---|---|
| Contexto do agente de planejamento | planejamento e coordenação | pode ser ChatGPT, Claude, Gemini ou outra ferramenta equivalente; não substitui a documentação persistente |
| Contexto do agente de implementação | implementação e validação técnica | pode ser Codex ou outro agente capaz de trabalhar sobre o repositório e o escopo autorizado |
| Pasta local | execução material do projeto | contém a working copy Git sincronizada com o remoto |
| GitHub | registro persistente | é a fonte canônica de código, documentação e histórico |

O mesmo nome de projeto deve ser usado entre esses ambientes sempre que possível.

Essa separação evita dois erros comuns: imaginar que o chat é o próprio projeto ou imaginar que a pasta local, isoladamente, representa o estado oficial do projeto.

## Configuração pessoal do autor

Na aplicação que originou o método, o autor prefere **ChatGPT no papel de planejamento** e **Codex no papel de implementação**. Essa escolha serve como exemplo concreto, não como requisito. Outras ferramentas podem substituir qualquer um dos agentes desde que cumpram as responsabilidades definidas pelo ÓRBITA.
