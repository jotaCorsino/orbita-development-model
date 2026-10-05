# 10 — Identidade e ambiente do projeto

## Objetivo

O Método ÓRBITA não organiza apenas tarefas. Ele também organiza **onde cada projeto existe**.

A experiência prática mostrou que um desenvolvimento assistido por IA fica mais previsível quando planejamento, implementação, working copy local e repositório remoto possuem uma relação clara e reconhecível.

Por isso, o método adota o conceito de **identidade única do projeto**.

## Regra principal

> **Um projeto deve ser reconhecível como o mesmo projeto em todos os ambientes usados para trabalhá-lo.**

Na configuração de referência, o padrão preferido é:

```text
NOME_DO_PROJETO
│
├── Contexto do agente de planejamento
├── Contexto do agente de implementação
├── Pasta local no computador
└── Repositório no GitHub
```

Sempre que possível, os quatro usam o mesmo nome.

## Ferramentas de referência

O método não exige ChatGPT, Codex ou qualquer fornecedor específico. Na configuração pessoal que originou o ÓRBITA, o autor usa **ChatGPT para planejamento** e **Codex para implementação**. Outros usuários podem adotar Claude, Gemini ou ferramentas diferentes, desde que preservem os mesmos papéis e vínculos.

## Os quatro espaços

### 1. Contexto do agente de planejamento

Função principal:

- compreender a necessidade;
- discutir produto e arquitetura;
- planejar;
- decompor tarefas;
- revisar evidências;
- acompanhar decisões;
- ajudar na administração do projeto.

O contexto do agente de planejamento fornece continuidade para análise e coordenação, mas **não substitui a documentação persistente do repositório**.

Uma decisão que precisa sobreviver a sessões, agentes ou ferramentas deve ser registrada no projeto técnico.

### 2. Contexto do agente de implementação

Função principal:

- trabalhar sobre o repositório do software;
- implementar tarefas autorizadas;
- executar testes e builds;
- produzir evidências;
- preparar branches, commits e Pull Requests quando aplicável.

O agente de implementação deve receber o mesmo nome/contexto do software para reduzir a chance de misturar projetos.

Antes de alterar, deve verificar o estado atual do repositório e as regras locais do projeto.

### 3. Pasta local

A pasta local é a working copy material do projeto no computador.

Padrão preferido:

```text
<diretorio-de-projetos>/
└── NOME_DO_PROJETO/
```

Essa pasta deve estar vinculada ao repositório remoto correspondente por Git.

O nome local deve coincidir com o nome do projeto/repositório quando isso for tecnicamente razoável.

A pasta local não é uma fonte independente de verdade. Ela pode conter trabalho ainda não publicado, branches locais ou estado temporário. Por isso, sua relação com Git deve estar sempre clara.

### 4. Repositório GitHub

O GitHub é a referência persistente do projeto.

Ele deve permitir recuperar, conforme a complexidade do software:

- código;
- documentação;
- decisões;
- roadmap;
- tarefas;
- branches;
- commits;
- Pull Requests;
- releases;
- evidências;
- estado homologado.

Conversas ajudam a pensar. O repositório permite reconstruir o projeto.

## Relação entre os espaços

```text
Agente de planejamento
planejamento / revisão
        │
        ▼
Repositório GitHub ◄────────────┐
fonte persistente               │
        │                       │
        ▼                       │
Pasta local                     │
working copy Git                │
        │                       │
        ▼                       │
Agente de implementação         │
implementação / testes ─────────┘
```

O desenho não significa que toda troca precise passar manualmente pelo GitHub a cada mensagem.

Significa que **o conhecimento relevante e o estado técnico devem convergir para o repositório**.

## Nome canônico

No início de um projeto deve existir um nome canônico.

Exemplo:

```text
Projeto: exemplo-projeto

Planejamento: exemplo-projeto
Implementação: exemplo-projeto
Pasta local: exemplo-projeto/
GitHub: organizacao/exemplo-projeto
```

Para ferramentas que usam nomes de projeto mais legíveis que o slug técnico, pequenas diferenças são aceitáveis, desde que não criem ambiguidade.

Exemplo aceitável:

```text
Nome humano: Exemplo Projeto
Slug técnico: exemplo-projeto
```

O importante é existir uma associação inequívoca.

## Ordem de vinculação em projeto novo

Em projeto novo, os quatro espaços não surgem todos ao mesmo tempo.

A ordem padrão é:

1. contexto dedicado criado no agente de planejamento;
2. repositório remoto do projeto fornecido ao agente de planejamento;
3. fundação documental criada no repositório remoto;
4. pasta local criada pelo responsável humano;
5. pasta aberta no ambiente do agente de implementação;
6. primeira tarefa do agente de implementação inicializa/valida Git e sincroniza a pasta com o remoto;
7. somente então começa a primeira implementação funcional.

Essa sequência é detalhada em [11 — Inicialização de um novo projeto](11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Regra para projetos existentes

Quando o software já possui repositório e histórico:

1. considerar o repositório existente como referência inicial de identidade;
2. inspecionar antes de renomear;
3. alinhar os contextos dos agentes e a pasta local ao projeto existente;
4. evitar criar um novo projeto apenas para reorganizar aparência;
5. documentar qualquer transição necessária.

## Sincronização antes de trabalhar

Antes de planejamento ou implementação relevante:

- confirmar que está no projeto correto;
- verificar o repositório remoto correto;
- consultar documentação e estado atuais;
- sincronizar a working copy quando a tarefa for implementada localmente;
- não confiar apenas no que uma conversa antiga afirma sobre o estado do código.

## Por que esse padrão é importante

### Menos troca de contexto

O mesmo nome em todas as ferramentas torna mais fácil localizar o ambiente certo.

### Menos risco operacional

Reduz a chance de executar uma tarefa no repositório errado ou usar uma pasta local incorreta.

### Melhor retomada

Uma nova sessão ou um novo agente consegue relacionar rapidamente conversa, implementação e repositório.

### Separação clara de função

O agente de planejamento não vira armazenamento de código. O agente de implementação não vira gestor do projeto. A pasta local não vira documentação oficial. GitHub não precisa substituir o espaço de raciocínio.

### Escalabilidade pessoal

Conforme o número de projetos cresce, a padronização reduz o custo mental de administrá-los.

## Regra de encerramento

Quando um projeto for abandonado, arquivado, substituído ou concluído, essa decisão também deve ficar clara.

Não manter múltiplos ambientes ativos com nomes parecidos sem saber qual é o canônico.

Se existir sucessor:

- indicar o sucessor no repositório antigo;
- arquivar ou tornar privado quando apropriado;
- alinhar os novos ambientes ao projeto canônico.

## Resumo

A organização recomendada pode ser expressa assim:

> **um software, uma identidade, quatro espaços complementares e um repositório persistente como referência.**

Esse padrão é parte importante da aplicação prática do Método ÓRBITA.
