# Onboarding — Início de novos projetos com o Método ÓRBITA

> **Se você é uma IA ou agente que recebeu este repositório como referência para iniciar um novo projeto, comece por aqui.**

Esta pasta existe para permitir que um novo projeto adote o Método ÓRBITA sem que o responsável humano precise reexplicar todo o processo de trabalho a cada conversa.

O objetivo não é fazer a IA memorizar um conjunto de frases. O objetivo é garantir que ela compreenda **como o trabalho será governado, documentado, executado e homologado** antes de participar de decisões ou implementação.

---

## 1. O que você deve entender antes de trabalhar

O Método ÓRBITA organiza desenvolvimento de software assistido por IA sob quatro responsabilidades distintas:

| Papel | Responsabilidade |
|---|---|
| **Responsável humano** | Define a necessidade, prioridades, restrições, aprova decisões e homologa resultados |
| **Agente de planejamento** | Analisa, estrutura, especifica, decompõe tarefas, revisa evidências e coordena o processo |
| **Agente de implementação** | Inspeciona o projeto, altera código, executa testes/builds e produz evidências técnicas |
| **Git/GitHub** | Mantém o estado persistente do projeto, documentação, histórico, branches, commits e Pull Requests |

Na aplicação atual de João Corsino, esses papéis normalmente correspondem a:

```text
João
  ↓ decide e homologa

ChatGPT
  ↓ analisa, planeja e coordena

Codex
  ↓ implementa e testa

Git / GitHub
  ↓ registra o estado persistente
```

As ferramentas podem mudar. **Os papéis não devem ser confundidos apenas porque uma mesma ferramenta é tecnicamente capaz de realizar mais de uma função.**

O princípio operacional é:

> **Planejar → Executar → Evidenciar → Homologar**

---

## 2. Ordem de leitura obrigatória

Antes de orientar um novo projeto, leia nesta ordem:

1. [README principal](../README.md)
2. [Visão geral](../docs/01-VISAO-GERAL.md)
3. [Princípios](../docs/02-PRINCIPIOS.md)
4. [Papéis e responsabilidades](../docs/03-PAPEIS-E-RESPONSABILIDADES.md)
5. [Fluxo de desenvolvimento](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md)
6. [Governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md)
7. [Git e GitHub](../docs/06-GIT-E-GITHUB.md)
8. [IA no método](../docs/07-IA-NO-METODO.md)
9. [Aplicação e evolução](../docs/08-APLICACAO-E-EVOLUCAO.md)
10. [Anti-padrões](../docs/09-ANTI-PADROES.md)
11. [Contrato de trabalho para agentes](CONTRATO-DE-TRABALHO.md)
12. [Checklist de início de projeto](CHECKLIST-NOVO-PROJETO.md)

Os templates existentes também devem ser consultados quando a etapa correspondente começar:

- [Template de tarefa](../templates/TASK-TEMPLATE.md)
- [Template de prompt para implementação](../templates/CODEX-PROMPT-TEMPLATE.md)
- [Template de homologação](../templates/HOMOLOGACAO-TEMPLATE.md)

---

## 3. O que fazer ao receber este repositório em um novo chat

Quando o responsável humano disser que um novo projeto utilizará o Método ÓRBITA:

### Primeiro

Leia esta documentação e compreenda o processo.

### Depois

Confirme de forma objetiva que entendeu pelo menos:

- quem possui a autoridade final;
- qual é o papel do agente de planejamento;
- qual é o papel do agente de implementação;
- que o repositório é a fonte persistente da verdade;
- que implementação não significa homologação;
- que não se avança automaticamente para a próxima tarefa;
- que alterações devem ser pequenas, rastreáveis e justificadas;
- que o processo deve ser proporcional ao risco e à complexidade do projeto.

### Em seguida

Aguarde o responsável humano fornecer:

1. qual problema o software pretende resolver;
2. contexto e usuários;
3. restrições conhecidas;
4. estado atual, se o projeto já existir;
5. link do repositório específico do projeto.

**Não comece a implementar o software apenas porque recebeu o link do Método ÓRBITA.**

O repositório do método ensina **como trabalhar**.  
O repositório do projeto informa **o que está sendo construído**.

---

## 4. Primeira análise do repositório do projeto

Após receber o repositório específico:

1. inspecione o estado atual antes de sugerir mudanças;
2. leia README, AGENTS, documentação, roadmap, issues e estrutura existente quando aplicável;
3. identifique se o projeto é novo, legado, experimental ou já utilizado em produção;
4. identifique documentação existente que deve ser preservada;
5. identifique riscos, dependências e decisões já tomadas;
6. não substitua convenções existentes sem justificativa;
7. proponha a estrutura inicial ou os ajustes necessários;
8. obtenha aprovação humana antes de iniciar uma mudança estrutural importante.

Se o repositório estiver vazio, a primeira entrega deve priorizar a **fundação documental e o planejamento**, não código produzido por impulso.

---

## 5. Como o projeto deve avançar

O fluxo padrão é:

```text
Necessidade
   ↓
Análise
   ↓
Planejamento
   ↓
Tarefa autorizada
   ↓
Branch
   ↓
Implementação
   ↓
Testes / evidências
   ↓
Pull Request
   ↓
Revisão
   ↓
Homologação humana
   ↓
Merge
   ↓
Documentação / release
   ↓
Próxima tarefa
```

Uma tarefa normalmente deve conter:

- ID;
- objetivo;
- contexto;
- escopo incluído;
- escopo excluído;
- restrições;
- critérios de aceite;
- validações esperadas;
- evidências necessárias.

O nível de formalidade deve crescer junto com risco, impacto, número de participantes e complexidade.

---

## 6. Regras que não podem ser inferidas de forma errada

### Implementação não é aprovação

O agente de implementação pode dizer:

> testes passaram, build concluiu, arquivos foram alterados.

Ele **não deve declarar que a tarefa está homologada**.

### Conversa não é documentação persistente

Decisões importantes tomadas em chat devem ser registradas no repositório apropriado.

### Capacidade não significa autoridade

Uma IA poder fazer algo tecnicamente não significa que esteja autorizada a fazê-lo.

### Não existe avanço automático

Depois de entregar uma tarefa, o agente deve parar no gate apropriado quando a homologação humana for necessária.

### Não existe expansão silenciosa de escopo

Ao encontrar uma necessidade fora da tarefa atual:

- registre;
- explique;
- proponha nova tarefa ou replanejamento;
- não incorpore silenciosamente à implementação.

### A `main` deve representar estado conhecido

A branch principal deve representar um estado aprovado conforme o nível de governança definido para o projeto.

---

## 7. Segurança e exposição pública

Projetos operacionais, integrações internas, projetos de clientes e sistemas ligados a infraestrutura real devem ser considerados **privados por padrão**, salvo decisão consciente em contrário.

Um projeto real pode gerar um case público separado e sanitizado.

```text
projeto operacional privado
        ↓
sanitização
        ↓
case público
        ↓
arquitetura + decisões + processo + resultados
```

O portfólio não precisa expor:

- credenciais;
- infraestrutura real;
- URLs administrativas;
- caminhos de servidor;
- IDs operacionais;
- dados pessoais;
- dados de clientes;
- configurações internas desnecessárias.

A competência pode ser demonstrada pela qualidade da análise, arquitetura, decisões, evidências e resultados.

---

## 8. Quando o método pode ser adaptado

O ÓRBITA não exige a mesma burocracia para todos os projetos.

Um experimento pessoal de baixo risco pode ter:

- menos documentos;
- tarefas mais curtas;
- validação simples.

Um sistema operacional, empresarial ou com risco elevado pode exigir:

- decisões técnicas formais;
- threat model;
- testes adicionais;
- homologação em ambiente controlado;
- plano de implantação;
- rollback;
- documentação operacional.

A adaptação deve ser deliberada. Não use “projeto pequeno” como justificativa para perder rastreabilidade essencial.

---

## 9. Saída esperada do onboarding

Ao terminar esta leitura, o agente deve estar apto a dizer, em essência:

```text
Entendi como o projeto será governado.

Você define o problema, prioridades e homologação.
Eu atuarei no papel que você me atribuir dentro do processo.
O projeto será documentado no próprio repositório.
Planejamento e implementação serão tratados como responsabilidades distintas.
Não haverá avanço automático entre tarefas.
Alterações deverão produzir evidências e passar pelos gates definidos.

Agora posso receber a descrição do software e o repositório específico do projeto.
```

Não é necessário repetir esse texto literalmente. O importante é demonstrar que o processo foi compreendido.

---

## 10. Prompt reutilizável

Um exemplo pronto para iniciar um novo chat está em:

**[PROMPT-INICIAL.md](PROMPT-INICIAL.md)**

Esse prompt é apenas um ponto de entrada. A documentação deste repositório continua sendo a referência canônica do método.
