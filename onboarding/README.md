# Onboarding — Início de novos projetos com o Método ÓRBITA

> **Se você é uma IA ou agente que recebeu este repositório como referência para iniciar um novo projeto, comece por aqui.**

Esta pasta existe para permitir que qualquer novo projeto adote o Método ÓRBITA sem que o responsável humano precise reexplicar manualmente o processo de trabalho a cada conversa.

O objetivo é garantir que o agente compreenda **como o projeto será organizado, documentado, implementado, validado e homologado** antes de participar de mudanças.

---

## 1. Papéis fundamentais

O Método ÓRBITA separa quatro responsabilidades:

| Papel | Responsabilidade |
|---|---|
| **Responsável humano** | Define necessidade, prioridades, restrições, decisões e homologação |
| **Agente de planejamento** | Analisa, estrutura, documenta, planeja, decompõe tarefas e revisa evidências |
| **Agente de implementação** | Trabalha na working copy, implementa tarefas autorizadas, testa e produz evidências |
| **Git/GitHub** | Mantém o estado persistente, documentação, histórico e rastreabilidade |

Um exemplo de configuração é:

```text
Responsável humano
        ↓ decide e homologa

Agente de planejamento
        ↓ planeja, documenta e coordena

Agente de implementação
        ↓ implementa e valida tecnicamente

Git / GitHub
        ↓ registra o estado persistente
```

As ferramentas podem mudar. Os papéis e gates continuam válidos.

Na configuração pessoal do autor, **ChatGPT** exerce o papel de planejamento e **Codex** o papel de implementação. Isso é apenas uma preferência pessoal. Claude, Gemini ou outras IAs podem ocupar esses papéis.

Princípio operacional:

> **Planejar → Executar → Evidenciar → Homologar**

---

## 2. Ordem de leitura

Antes de orientar um novo projeto, leia:

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
11. [Identidade e ambiente do projeto](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md)
12. [Inicialização de um novo projeto](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md)
13. [Contrato de trabalho para agentes](CONTRATO-DE-TRABALHO.md)
14. [Checklist de início de projeto](CHECKLIST-NOVO-PROJETO.md)

Templates operacionais:

- [Template de tarefa](../templates/TASK-TEMPLATE.md)
- [Template de implementação](../templates/IMPLEMENTACAO-PROMPT-TEMPLATE.md)
- [Template de bootstrap local](../templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md)
- [Template de homologação](../templates/HOMOLOGACAO-TEMPLATE.md)

---

## 3. Ao receber o Método ÓRBITA em um novo chat

O agente de planejamento deve primeiro compreender o método.

Depois, deve confirmar de forma objetiva que entendeu:

- que a decisão final pertence ao responsável humano;
- que planejamento e implementação são responsabilidades distintas;
- que o repositório é a referência persistente;
- que conversas ajudam a coordenar, mas não substituem documentação;
- que implementação não significa homologação;
- que não existe avanço automático;
- que o escopo não deve crescer silenciosamente;
- que o mesmo projeto deve possuir identidade coerente entre agentes de planejamento e implementação, pasta local e repositório.

Em seguida, deve receber do responsável humano:

1. a ideia do software;
2. o problema que deve resolver;
3. usuários/contexto;
4. restrições conhecidas;
5. nome do projeto;
6. repositório remoto específico do software.

**Não implemente funcionalidades neste momento.**

---

## 4. Fundação documental é responsabilidade do planejamento

Para um projeto novo, o agente de planejamento deve inspecionar o repositório remoto e transformar a ideia inicial em uma base persistente antes do primeiro handoff para implementação.

Quando possuir acesso autorizado ao repositório, deve criar ou organizar diretamente nele, de forma proporcional ao projeto:

- README no padrão do método;
- objetivo e contexto;
- escopo inicial;
- planejamento/roadmap;
- arquitetura inicial quando necessária;
- regras locais;
- estados de acompanhamento;
- critérios de aceite e homologação;
- riscos, restrições e decisões iniciais.

O repositório precisa conter contexto suficiente para que outra sessão ou agente consiga compreender o projeto sem depender exclusivamente da conversa original.

Se o agente não possuir permissão de escrita, deve preparar a fundação para que ela seja persistida antes do avanço.

---

## 5. Cadeia padrão de inicialização

O fluxo esperado de um projeto novo é:

```text
Responsável humano
cria contexto no agente de planejamento
        ↓
inicia conversa + explica a ideia
        ↓
fornece ÓRBITA + repositório do projeto
        ↓
Agente de planejamento
lê o método e estrutura o projeto
        ↓
cria documentação inicial no GitHub
        ↓
confirma fundação e planejamento
        ↓
gera a primeira tarefa do agente de implementação
        ↓
Responsável humano
cria/abre a pasta local no agente de implementação
        ↓
agente de implementação executa BOOTSTRAP
        ↓
Git local ↔ GitHub sincronizados
        ↓
planejamento + implementação + pasta local + repositório
representam o mesmo projeto
        ↓
primeira tarefa funcional
```

A descrição normativa completa está em [Inicialização de um novo projeto](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md).

---

## 6. Primeira tarefa do agente de implementação

Em projeto novo, a primeira tarefa enviada ao agente de implementação deve ser uma tarefa de **bootstrap local**.

O responsável humano já terá criado e aberto a pasta destinada ao projeto.

O agente de implementação deve:

1. confirmar a pasta correta;
2. verificar se Git já existe;
3. inicializar Git somente se necessário;
4. configurar ou validar o remoto `origin`;
5. buscar o repositório remoto;
6. sincronizar a branch principal de forma segura;
7. confirmar que README e documentação inicial estão presentes;
8. verificar remoto, branch, HEAD e `git status`;
9. retornar evidências;
10. parar.

Ele **não deve implementar funcionalidades nessa primeira tarefa**.

Se encontrar conteúdo local conflitante, remoto incorreto, histórico divergente ou necessidade de ação destrutiva, deve parar e relatar.

Use o [template de bootstrap](../templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md).

---

## 7. Depois do bootstrap

Somente quando os ambientes estiverem vinculados começa o ciclo normal:

```text
Necessidade
   ↓
Análise
   ↓
Planejamento
   ↓
Tarefa autorizada
   ↓
Implementação
   ↓
Testes / evidências
   ↓
Revisão
   ↓
Homologação humana
   ↓
Merge / documentação / release
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
- validações;
- evidências esperadas.

---

## 8. Regras que não podem ser interpretadas de forma errada

### Implementação não é aprovação

O agente de implementação apresenta evidências. A homologação pertence ao responsável humano.

### Conversa não é fonte persistente

Decisões relevantes devem convergir para o repositório.

### Capacidade não significa autoridade

Uma ferramenta poder executar uma ação não significa que esteja autorizada a fazê-la.

### Não existe avanço automático

Ao terminar a tarefa autorizada, o agente para no gate correspondente.

### Não existe expansão silenciosa

Nova necessidade deve ser registrada e planejada, não incorporada discretamente.

### Estado atual deve ser verificado

Uma conversa antiga ou working copy local pode estar desatualizada. Para trabalho relevante, consulte o repositório atual.

---

## 9. Segurança e exposição pública

Projetos operacionais, de clientes ou ligados a infraestrutura real devem avaliar privacidade antes da publicação.

Quando apropriado:

```text
projeto operacional privado
        ↓
sanitização
        ↓
case público
```

Não exponha desnecessariamente credenciais, infraestrutura, dados pessoais, dados de clientes, identificadores operacionais ou configurações internas.

---

## 10. Saída esperada do onboarding

Ao terminar a leitura, o agente deve compreender, em essência:

```text
O responsável humano define e homologa.
O planejamento transforma a ideia em documentação e tarefas.
O agente de implementação executa apenas o trabalho autorizado.
O GitHub mantém o estado persistente.
A primeira tarefa de um projeto novo vincula a pasta local ao remoto.
Somente depois começa a implementação funcional.
```

Um prompt reutilizável para iniciar esse processo está em [PROMPT-INICIAL.md](PROMPT-INICIAL.md).
