# 08 — Aplicação e evolução

## Como começar

Uma adoção mínima do ÓRBITA pode usar apenas:

1. um responsável humano;
2. um repositório Git;
3. um agente para planejamento;
4. um agente ou ferramenta para implementação;
5. tarefas com critérios de aceite;
6. validação antes do merge.

## Organização recomendada de um projeto

Na configuração de referência, um projeto novo é inicializado nesta ordem:

1. definir o nome canônico;
2. criar um contexto dedicado no agente de planejamento;
3. apresentar a ideia e os repositórios do ÓRBITA e do novo projeto;
4. o agente de planejamento cria a fundação documental no repositório remoto;
5. o responsável humano cria a pasta local e a abre no ambiente do agente de implementação;
6. o agente de planejamento entrega a primeira tarefa de bootstrap;
7. o agente de implementação inicializa/valida Git e sincroniza a pasta com o remoto;
8. somente depois começa a primeira implementação funcional.

Os quatro ambientes devem permanecer associados pelo mesmo nome sempre que possível.

O repositório continua sendo a referência persistente. Os demais ambientes reduzem troca de contexto e especializam o trabalho.

Essa organização é recomendada, não um requisito tecnológico universal. Se uma ferramenta mudar, o princípio permanece: **um projeto deve ter identidade clara e ambientes de trabalho inequivocamente associados ao mesmo repositório**.

Ver [Inicialização de um novo projeto](11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Níveis de formalidade

### Projeto simples

- tarefa curta;
- implementação;
- teste;
- revisão humana;
- commit.

### Projeto intermediário

- roadmap;
- tarefas identificadas;
- branches;
- testes;
- PR;
- homologação;
- documentação contínua.

### Projeto crítico

O ÓRBITA deve ser complementado por processos formais adequados: revisão especializada, segurança, CI/CD, controle de acesso, QA, compliance e outros requisitos organizacionais.

## Evolução por experiência real

O método deve mudar quando a prática demonstrar necessidade.

Uma nova regra deve responder a pelo menos uma pergunta:

- Qual problema recorrente ela evita?
- Qual decisão torna mais clara?
- Qual risco reduz?
- Qual evidência passa a exigir?
- O ganho justifica a complexidade adicionada?

## Projeto operacional e case público

Um projeto operacional não precisa ser público para demonstrar competência.

Quando o repositório real contém infraestrutura, dados, configurações internas ou detalhes de manutenção desnecessários ao público, o padrão recomendado é:

```text
projeto operacional privado
        ↓
seleção e sanitização
        ↓
case público independente
```

O case público deve priorizar:

- problema;
- arquitetura;
- decisões;
- processo de desenvolvimento;
- testes e evidências;
- segurança;
- resultados;
- aprendizados.

Ele não deve depender da exposição de credenciais, dados reais, caminhos internos, IDs operacionais ou detalhes de infraestrutura.

Esse princípio foi incorporado ao método a partir do estudo de caso [Tickets Recorrentes HESK](../examples/01-TICKETS-RECORRENTES-HESK.md).

## Portfólio

Este repositório também existe para demonstrar uma competência que nem sempre aparece apenas no código final: **capacidade de organizar o processo de engenharia**.

Projetos mostram o que foi construído.

O Método ÓRBITA procura mostrar **como o trabalho é conduzido**.
