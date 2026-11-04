# Proposta 006 — Knowledge: base de conhecimento operacional do projeto

- **Categoria:** continuidade operacional / memória externa / eficiência de agentes / prevenção de reincidência.
- **Registrada em:** 04/11/2026.
- **Origem:** necessidade de preservar descobertas reutilizáveis feitas por agentes durante análise, diagnóstico, implementação, homologação e troubleshooting.
- **Estado:** **APROVADA e INCORPORADA à `main` pelo PR #21 em 04/11/2026**.
- **Escopo:** projetos conduzidos pelo Método ÓRBITA.

## 1. Problema observado

O Método ÓRBITA já preserva código, decisões, documentação, troubleshooting, backlog, evidências e histórico de evolução no repositório.

Ainda existe, porém, uma lacuna entre:

1. o conhecimento detalhado produzido durante uma ocorrência ou tarefa; e
2. a informação curta que um agente precisa recuperar rapidamente antes de agir.

Durante uma tarefa, o agente frequentemente descobre fatos relevantes como:

- particularidades reais do ambiente;
- procedimentos que funcionaram ou falharam;
- dependências entre componentes;
- limitações de ferramentas;
- armadilhas que induzem a diagnóstico incorreto;
- condições necessárias para uma operação segura;
- causas já comprovadas de erros;
- diferenças entre estado aparente e estado real do sistema.

Se esse conhecimento permanecer apenas na conversa, em logs extensos ou dentro de um troubleshooting específico, uma sessão futura pode precisar redescobri-lo.

Isso aumenta:

- tempo de diagnóstico;
- repetição de verificações já realizadas;
- risco de reincidência em erros conhecidos;
- dependência de memória de conversa;
- custo de retomada por outro agente.

## 2. Objetivo

Adicionar ao ÓRBITA uma **base de conhecimento operacional persistente**, chamada **Knowledge**, mantida no próprio repositório do projeto.

O objetivo é permitir que agentes futuros consultem conclusões já comprovadas antes de repetir diagnósticos ou decisões.

Princípio:

> **Descobrir uma vez, validar, registrar e reutilizar quando aplicável.**

Knowledge não representa treinamento interno do modelo. É uma memória externa, versionada e recuperável pelo agente.

O ganho esperado é cumulativo: conforme o projeto registra conhecimento útil e validado, novas sessões conseguem iniciar tarefas com menos redescoberta e maior contexto operacional.

## 3. Estrutura proposta

Todo projeto ÓRBITA deve poder possuir:

```text
knowledge/
├── README.md
├── KN-001-descricao-curta.md
├── KN-002-descricao-curta.md
└── ...
```

O `knowledge/README.md` funciona como **índice rápido**.

O agente não deve precisar abrir todos os arquivos de Knowledge em toda tarefa. Primeiro consulta o índice, identifica quais entradas podem afetar o trabalho atual e abre apenas as relevantes.

### Índice mínimo

```md
# Knowledge

Base de conhecimento operacional reutilizável do projeto.

| ID | Categoria | Resumo | Estado | Verificado em | Detalhe |
| --- | --- | --- | --- | --- | --- |
| KN-001 | Ambiente | [resumo objetivo] | Vigente | AAAA-MM-DD | [abrir](KN-001-descricao-curta.md) |
```

## 4. Unidade de conhecimento

Cada entrada recebe um identificador persistente:

```text
KN-001
KN-002
KN-003
```

A numeração identifica a entrada e não representa prioridade.

Uma entrada detalhada deve ser curta e conter somente o necessário para reutilização segura.

Modelo sugerido:

```md
# KN-001 — [Título]

- **Categoria:** [Ambiente / Operação / Pitfall / Integração / Restrição / outra]
- **Estado:** Vigente
- **Verificado em:** AAAA-MM-DD
- **Origem:** [tarefa / PR / troubleshooting / operação / evidência]
- **Escopo:** [onde este conhecimento se aplica]

## Conhecimento

[Conclusão objetiva e comprovada.]

## Aplicação

[Quando esta informação deve alterar diagnóstico, decisão ou procedimento.]

## Evidência / origem

[Referência suficiente para recuperar a comprovação.]

## Revalidar quando

[Condição que pode tornar o conhecimento antigo ou inválido.]
```

## 5. O que deve entrar em Knowledge

Uma informação deve ser candidata a Knowledge quando for:

1. **reutilizável** — pode ajudar mais de uma tarefa ou sessão;
2. **operacionalmente relevante** — pode mudar diagnóstico, decisão, segurança ou procedimento;
3. **não óbvia** — não é apenas informação trivial já evidente no código ou documentação principal;
4. **suficientemente comprovada** — existe evidência para tratá-la como conhecimento, e não apenas hipótese;
5. **compactável** — pode ser resumida sem perder a condição que torna a conclusão válida.

Exemplos:

- determinado deploy homologado depende de um runbook específico;
- o `HEAD` de um checkout não comprova a revisão realmente publicada;
- uma limitação de sandbox pode simular erro de permissão no filesystem real;
- certo módulo depende de outro repositório antes de uma operação;
- determinada sequência de passos já causou falha e possui alternativa comprovada;
- um campo não deve ser operado por determinado painel porque seu tratamento pertence a outro sistema;
- uma versão, configuração ou característica do ambiente altera o procedimento aplicável.

## 6. O que não deve entrar

Knowledge não deve virar depósito de informação.

Não registrar como Knowledge:

- logs brutos;
- transcrições de conversa;
- hipóteses ainda não verificadas;
- tarefas futuras — pertencem ao backlog;
- planejamento — pertence ao roadmap ou tarefa;
- decisões arquiteturais normativas — pertencem à documentação/decisões apropriadas;
- incidentes completos — pertencem ao troubleshooting;
- segredos, tokens, senhas ou dados sensíveis;
- fatos triviais que podem ser obtidos imediatamente do próprio repositório;
- cópias integrais de documentação já canônica.

Critério de controle:

> **Esta informação evitará uma redescoberta, um erro ou uma decisão inadequada em uma tarefa futura?**

Se a resposta for não, provavelmente não pertence ao Knowledge.

## 7. Relação com troubleshooting

Troubleshooting e Knowledge possuem objetivos diferentes.

### Troubleshooting

Preserva:

- ocorrência;
- contexto;
- sintomas;
- investigação;
- hipóteses;
- evidências;
- causa;
- resolução;
- aprendizado completo.

### Knowledge

Preserva:

- a conclusão reutilizável extraída dessa experiência;
- a condição em que ela se aplica;
- o que um agente futuro precisa saber antes de agir.

Exemplo conceitual:

```text
TRB-xxx
  ocorrência completa
        ↓
causa confirmada
        ↓
lição reutilizável
        ↓
KN-xxx
```

Knowledge não substitui o registro de troubleshooting e não precisa repetir todo o incidente.

## 8. Relação com backlog

Os dois mecanismos respondem a perguntas diferentes.

```text
Backlog:
"O que talvez precisemos fazer no futuro?"

Knowledge:
"O que já aprendemos e não queremos ter que descobrir novamente?"
```

Registrar conhecimento não cria tarefa, prioridade ou autorização de implementação.

## 9. Relação com documentação canônica

Knowledge é uma camada de recuperação rápida, não uma fonte paralela de regras.

Se uma informação define:

- contrato;
- arquitetura;
- política;
- regra de segurança;
- procedimento canônico;
- escopo;
- comportamento obrigatório;

ela deve estar no documento canônico apropriado.

O Knowledge pode apontar para esse documento e resumir a consequência operacional, mas não deve criar uma política paralela.

Em caso de conflito entre uma entrada Knowledge e o estado atual comprovado do projeto, o agente deve:

1. não seguir automaticamente a entrada antiga;
2. verificar a fonte canônica e a realidade atual;
3. corrigir ou invalidar a entrada Knowledge.

## 10. Estados de validade

Os estados propostos são independentes dos estados de tarefa do ÓRBITA:

- **Vigente** — conhecimento validado e aplicável dentro do escopo declarado;
- **Revalidar** — existe motivo concreto para confirmar novamente antes de utilizar;
- **Obsoleto** — a condição deixou de existir ou foi substituída.

Esses estados indicam validade do conhecimento, não andamento de trabalho.

Uma entrada obsoleta pode ser removida do índice ativo ou mantida apenas quando houver valor histórico explícito.

## 11. Protocolo antes de agir

Antes de uma tarefa relevante, o agente deve realizar uma consulta proporcional:

1. localizar `knowledge/README.md`, quando existir;
2. verificar rapidamente os resumos e categorias;
3. identificar entradas que possam afetar a tarefa atual;
4. abrir somente as entradas relevantes;
5. conferir se permanecem Vigentes e dentro do escopo;
6. revalidar fatos voláteis quando a tarefa depender deles.

A consulta ao Knowledge não substitui inspeção do estado atual.

Regra:

> **Conhecimento anterior orienta a investigação; evidência atual confirma a decisão.**

## 12. Protocolo após aprender

Durante ou ao final de uma tarefa, o agente deve perguntar:

> **Foi descoberta uma conclusão comprovada, reutilizável e operacionalmente relevante que uma sessão futura provavelmente precisaria redescobrir?**

Se sim:

1. procurar se já existe entrada equivalente;
2. atualizar a existente quando for o mesmo conhecimento;
3. criar nova entrada somente quando representar conhecimento distinto;
4. registrar origem e escopo;
5. indicar condição de revalidação quando houver volatilidade;
6. atualizar o índice;
7. incluir a alteração no mesmo fluxo Git/revisão da tarefa quando apropriado.

Não criar Knowledge apenas para demonstrar atividade documental.

## 13. Aprendizado cumulativo do projeto

O mecanismo cria um ciclo de melhoria operacional:

```text
Consultar Knowledge
        ↓
Executar com contexto acumulado
        ↓
Investigar somente o que ainda é desconhecido
        ↓
Descobrir e validar novo conhecimento
        ↓
Registrar / atualizar Knowledge
        ↓
Próxima sessão começa com mais contexto
```

O agente não se torna intrinsecamente treinado pelo projeto. O que melhora é a **qualidade do contexto recuperável** antes de uma decisão.

Esse efeito pode gerar:

- menor tempo de retomada;
- menor repetição de diagnóstico;
- menor incidência de erros já conhecidos;
- maior consistência entre agentes e sessões;
- melhor transferência de conhecimento entre humano e IA;
- menor dependência de conversas antigas.

## 14. Controle de qualidade

Knowledge possui um risco próprio: conhecimento incorreto ou antigo pode acelerar uma decisão errada.

Por isso:

- hipótese não deve ser promovida a conhecimento validado;
- origem deve ser recuperável;
- escopo deve ser explícito;
- conhecimento volátil deve ter condição de revalidação;
- duplicatas devem ser consolidadas;
- entradas contraditórias devem ser resolvidas;
- informações sensíveis não devem ser armazenadas;
- mudanças no ambiente devem provocar revisão das entradas afetadas quando identificadas.

A velocidade só é ganho se o conhecimento recuperado for confiável.

## 15. Proporcionalidade

Knowledge não deve criar burocracia em toda tarefa.

Uma tarefa simples que não gera descoberta reutilizável pode terminar sem qualquer alteração em `knowledge/`.

Também não é necessário abrir todos os registros em toda execução.

O padrão é:

```text
índice rápido
   ↓
seleção por relevância
   ↓
somente entradas aplicáveis
```

Isso preserva o benefício de contexto sem aumentar desnecessariamente o custo de leitura do agente.

## 16. Mudanças propostas no Método ÓRBITA

Se homologada, esta proposta deve gerar alterações proporcionais em:

- `docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md` — criar `knowledge/` na fundação padrão;
- `docs/08-APLICACAO-E-EVOLUCAO.md` — definir memória operacional e ciclo de aprendizagem;
- `onboarding/CONTRATO-DE-TRABALHO.md` — consulta prévia e captura posterior de conhecimento;
- `templates/` — adicionar template de índice e de entrada Knowledge;
- `templates/README-INICIAL-TEMPLATE.md` — apontar para a base de conhecimento quando aplicável;
- verificação final — verificar se surgiu aprendizado reutilizável que merece Knowledge;
- README do Método ÓRBITA — registrar a nova camada de continuidade operacional.

## 17. Critérios para homologação

A proposta pode ser incorporada se:

1. Knowledge permanecer distinto de backlog, troubleshooting, roadmap e documentação normativa;
2. apenas conhecimento comprovado for tratado como Vigente;
3. a consulta for proporcional e orientada pelo índice;
4. o mecanismo reduzir redescoberta sem exigir leitura integral da base;
5. conhecimento antigo puder ser marcado para revalidação ou obsolescência;
6. a origem das conclusões permanecer recuperável;
7. Knowledge não puder substituir evidência atual quando o estado for volátil;
8. não houver armazenamento de segredos ou dados sensíveis;
9. o agente puder registrar aprendizado no fluxo normal da tarefa sem criar um processo paralelo pesado;
10. a base permaneça simples o suficiente para ser útil também em projetos pequenos.

## 18. Resultado esperado

Com Knowledge, o repositório passa a preservar quatro dimensões distintas de continuidade:

```text
README / docs
    = o que o projeto é e como funciona

Backlog
    = o que talvez faremos

Troubleshooting
    = o que aconteceu e como foi investigado

Knowledge
    = o que aprendemos e devemos reutilizar
```

O efeito desejado é transformar experiência operacional acumulada em contexto reutilizável para agentes futuros.

## 19. Estado da avaliação

A proposta foi **APROVADA pelo responsável humano em 04/11/2026**.

A homologação confirma:

- `knowledge/` como base padrão de conhecimento operacional reutilizável;
- `knowledge/README.md` como índice rápido;
- entradas `KN-xxx` criadas somente quando houver conhecimento real;
- consulta proporcional antes de tarefas relevantes;
- captura posterior de conclusões comprovadas e reutilizáveis;
- estados de validade `Vigente`, `Revalidar` e `Obsoleto`;
- separação entre Knowledge, backlog, troubleshooting e documentação canônica;
- proibição de promover hipótese a Knowledge Vigente;
- revalidação de conhecimento volátil;
- proibição de segredos e dados sensíveis.

A incorporação normativa foi concluída na `main` pelo PR #21 em 04/11/2026. A verificação pós-merge confirmou a presença da base `knowledge/`, dos templates, da consulta pré-tarefa e da captura pós-aprendizado.

**PROP-006 encerrada.**
