# 04 — Fluxo de desenvolvimento

## Preparação de um novo projeto

Antes do primeiro ciclo normal de desenvolvimento, um projeto novo passa por uma etapa própria de inicialização.

A ordem padrão é:

1. o responsável humano define um **nome canônico**;
2. cria um **contexto próprio no agente de planejamento** com esse nome;
3. inicia uma conversa de planejamento e apresenta a ideia do software;
4. fornece o repositório do **Método ÓRBITA** e o **repositório remoto do novo projeto**;
5. o agente de planejamento lê o método, compreende a ideia e inspeciona o repositório do projeto;
6. o agente de planejamento cria no repositório remoto a **fundação documental inicial**: README, visão, planejamento, roadmap, regras, critérios e demais documentos proporcionais ao projeto;
7. o agente confirma ao responsável humano o que foi criado;
8. o responsável humano cria uma **pasta local** com o mesmo nome e abre essa pasta no **ambiente do agente de implementação**;
9. o agente de planejamento gera a **primeira tarefa do agente de implementação**, dedicada exclusivamente ao bootstrap local;
10. o agente de implementação inicializa Git se necessário, conecta a pasta ao repositório remoto, sincroniza a branch principal com segurança, valida documentação/remoto/HEAD e para;
11. somente depois dessa cadeia estar vinculada começa a primeira tarefa funcional.

A primeira tarefa do agente de implementação em projeto novo, portanto, **não é implementar funcionalidade**. É estabelecer com segurança a working copy local do repositório já documentado.

A especificação completa está em [11 — Inicialização de um novo projeto](11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Planejamento progressivo e entrega incremental

Manter uma visão de começo, desenvolvimento e encerramento do projeto, com objetivo, resultado esperado, limites, macroetapas, Satélites pertinentes, dependências, riscos relevantes e critérios de sucesso. A visão global orienta o percurso e não exige decidir todos os detalhes antecipadamente. Distinguir decisão tomada, hipótese, opção futura e pendência; roadmap não é autorização de execução.

Detalhar a etapa atual e as próximas dependências suficientemente próximas para decidir com segurança; manter as etapas distantes em nível de objetivo, resultados e condições de entrada/saída. Antecipar investigação de risco, arquitetura, segurança, contratos, dados, interfaces e restrições irreversíveis quando puderem invalidar escolhas próximas. Não adiar requisito essencial sob pretexto de agilidade, nem desenhar o produto inteiro por especulação. Revisar o plano diante de evidência nova, preservando decisões ainda válidas.

Decompor cada etapa em problemas, Satélites, fatias e tarefas com resultado verificável. Fatia é unidade de valor, redução de risco ou aprendizado verificável, não necessariamente uma tela, arquivo ou camada isolada. Preferir pequenos incrementos coerentes que integrem os Satélites necessários, inclusive ponta a ponta quando isso demonstrar valor e reduzir risco; uma investigação, protótipo ou decisão de arquitetura pode ser fatia quando resolve incerteza real. Evitar tanto tarefas amplas demais para testar e homologar quanto fragmentação em operações triviais.

Para selecionar o próximo trabalho, recuperar estado e dependências comprovados, identificar o problema pendente de maior relevância e competência necessária, consultar Skills conforme a lacuna, propor alternativas e recomendar quando houver escolha metodológica ainda não decidida/delegada. Definir escopo, insumos, resultado, critérios, responsável funcional, restrições e interfaces necessárias no registro existente. Executar dentro da autorização, integrar evidências, obter o gate aplicável e avançar a partir do resultado. A autorização de uma etapa não implica autorização automática das seguintes; um gate pode cobrir conjunto coerente explicitamente autorizado.

Satélites podem avançar em paralelo ou alternar quando as dependências, autoridade, recursos, interfaces e critérios permitirem; não exigir cascata rígida nem concorrência artificial. Mudança material em um contrato ou decisão deve ser reconciliada com Satélites afetados antes de executar o trabalho dependente. Não criar novas sessões, cerimônias, aprovações ou entregas documentais por fragmentação do trabalho. Um chat de coordenação por iniciativa continua sendo o padrão enquanto suficiente.

## Ciclo padrão

1. **Necessidade** — surge um problema, melhoria ou funcionalidade.
2. **Análise** — o contexto é compreendido antes da alteração.
3. **Planejamento** — a mudança é decomposta, seus critérios são definidos e riscos relevantes de segurança são considerados.
4. **Tarefa** — uma unidade de trabalho recebe objetivo, escopo e aceite.
5. **Branch** — quando aplicável, a mudança é isolada da versão homologada.
6. **Implementação** — o agente executor trabalha no escopo autorizado.
7. **Validação técnica** — testes, build, verificações de segurança proporcionais ao risco e demais validações são executados.
8. **Evidências** — resultados e alterações são apresentados.
9. **Pull Request** — a mudança torna-se revisável e comparável.
10. **Revisão** — coerência técnica e aderência ao objetivo são avaliadas.
11. **Homologação humana** — o responsável aceita ou solicita correções.
12. **Merge** — o estado aprovado passa a integrar a linha principal.
13. **Documentação/Release** — registros são atualizados quando necessário.
14. **Próxima tarefa** — somente então o ciclo recomeça.

## Preflight condicional para operações em ambientes existentes

O ciclo padrão não ganha uma nova etapa obrigatória. Porém, quando a tarefa envolver **deploy, migração, atualização de preview, servidor, CMS, integração ou infraestrutura compartilhada**, a fase de análise deve incluir uma verificação operacional antes de qualquer comando de escrita.

Essa verificação deve confirmar, de forma proporcional ao risco:

1. qual é a origem e a revisão/artefato aprovado;
2. qual é o destino real e o estado já existente;
3. qual procedimento ou runbook mantém esse ambiente e se ele está homologado ou ainda é experimental;
4. quais módulos, repositórios auxiliares, integrações ou responsáveis participam da operação;
5. quais ações podem ser executadas somente em leitura e quais dependem de autorização, backup, rollback ou outro gate;
6. quais evidências pós-operação demonstrarão a versão realmente implantada e a preservação das integrações.

Se essas informações não puderem ser recuperadas com segurança, a tarefa permanece em **análise/diagnóstico**. A ausência de contexto operacional não autoriza avançar para execução nem substituir o fluxo existente por um procedimento criado ad hoc.

A homologação do artefato de origem e a autorização para operar o ambiente são responsabilidades distintas, mas podem estar cobertas pelo mesmo gate quando a tarefa e o procedimento já autorizarem explicitamente a implantação. O ciclo continua o mesmo; apenas os critérios do gate se tornam mais específicos quando existe risco operacional.

## Verificação final de consistência

O ciclo padrão não ganha um novo estado. Porém, antes de considerar uma mudança completamente encerrada, deve existir uma **verificação final proporcional** quando o trabalho alterar informações reproduzidas em mais de um lugar — por exemplo status, IDs, nomes, referências, índices, roadmap, README, documentação agregadora ou registros de evolução.

A verificação ocorre em duas passagens:

### Antes da integração

1. identificar o registro ou artefato canônico da mudança;
2. identificar quais superfícies derivadas podem repetir ou resumir a mesma informação;
3. comparar a branch com a `main` atual quando houver integração Git e confirmar que a alteração permanece no escopo; sem PR, conferir origem, autorização e alteração prevista;
4. conferir IDs, nomes, links, títulos e estados relacionados;
5. procurar referências claramente obsoletas relacionadas à mudança.

### Depois do merge ou aplicação autorizada (quando não houver PR)

1. confirmar o PR efetivamente mergeado e o commit resultante, quando houver; sem PR, confirmar o registro/artefato final e o destino real pertinente;
2. verificar os arquivos relevantes diretamente na linha integrada aplicável, ou o destino final quando não houver integração Git;
3. conferir os resumos, índices e painéis derivados aplicáveis;
4. repetir a busca por status ou referências antigas relacionadas à alteração;
5. validar links e caminhos principais afetados;
6. verificar se a execução revelou necessidades futuras relevantes fora do escopo corrente e, quando houver, registrá-las no backlog do README;
7. corrigir resíduos documentais antes de considerar o encerramento completo.

Essa verificação não exige varredura integral do repositório para mudanças pequenas. O escopo deve acompanhar o risco e a quantidade de lugares que reproduzem a informação alterada.

Registrar uma necessidade no backlog não autoriza sua implementação. O backlog apenas preserva evolução potencial; qualquer item selecionado retorna ao fluxo normal de análise, planejamento, tarefa e homologação.

Se a correção pós-merge for apenas de status ou fechamento documental, ela pode ocorrer em PR curto e isolado. Se modificar significado, regra ou escopo homologado, retorna ao fluxo normal de revisão e homologação.

O checklist reutilizável está em [../templates/VERIFICACAO-FINAL-TEMPLATE.md](../templates/VERIFICACAO-FINAL-TEMPLATE.md).

## Estados normativos

```text
PLANEJADA
   ↓
AUTORIZADA
   ↓
EM_IMPLEMENTACAO
   ↓
EM_VALIDACAO
   ↓
AGUARDANDO_HOMOLOGACAO
   ↓
CONCLUIDA
```

Quando uma validação falha, a tarefa retorna ao estágio adequado.


### Dimensões do estado

Preservar os seis estados oficiais. Planejamento, autorização, implementação, teste, homologação, integração e publicação são evidências/dimensões distintas, não novos estados. Registrar aceite humano e ressalvas com revisão e escopo; quando integração/verificação for exigida, manter explícito “homologado — integração/encerramento pendente” sem declarar encerramento completo. Só marcar CONCLUIDA quando gate definido e ações de encerramento exigidas estiverem satisfeitos. Main, artefato aprovado e destino real podem divergir; não inferir publicação do merge.

### Interrupção e retomada

Uma interrupção inesperada, pausa longa ou troca de agente **não cria um novo estado normativo** no fluxo.

Nesses casos, o acompanhamento pode usar a condição excepcional **Pausado** para comunicar que a execução foi suspensa, mantendo registrado qual era o último estado normativo conhecido da tarefa.

Exemplo:

```text
Estado normativo: EM_IMPLEMENTACAO
Condição: PAUSADO — execução interrompida antes de persistir toda a evidência
```

Ao retomar:

1. não presumir que a tarefa voltou automaticamente a `EM_IMPLEMENTACAO`;
2. inspecionar e preservar o estado local antes de qualquer reconstrução;
3. identificar o último passo comprovado e o trabalho ainda não persistido;
4. retornar a tarefa ao estágio adequado do fluxo com base nas evidências encontradas;
5. manter o gate humano original quando ainda estiver pendente.

A condição excepcional `Pausado` desaparece quando a tarefa é retomada com estado novamente conhecido. Ela serve apenas para comunicar suspensão e incerteza operacional; **não substitui os estados oficiais nem altera a sequência normativa**.



### Indicadores visuais de acompanhamento

Os estados acima são a referência normativa do fluxo. Projetos podem usar indicadores visuais no README para facilitar a leitura, desde que **o texto do status preserve o estado real**.

| Indicador | Texto recomendado | Estado relacionado |
| --- | --- | --- |
| ⚪ | Planejado | `PLANEJADA` |
| ⚪ | Autorizado | `AUTORIZADA` |
| 🟡 | Em implementação | `EM_IMPLEMENTACAO` |
| 🔵 | Em validação | `EM_VALIDACAO` |
| 🔵 | Aguardando homologação | `AGUARDANDO_HOMOLOGACAO` |
| 🟢 | Concluído | `CONCLUIDA` |

A cor é apenas uma camada visual. Ela **não substitui o nome do estado, não altera gates e não cria transições novas**.

Regras:

- `🔵 Em validação` e `🔵 Aguardando homologação` usam o mesmo indicador visual, mas continuam sendo estados diferentes;
- `🟢 Concluído` só pode representar `CONCLUIDA` depois da homologação prevista para o escopo;
- `🟠 Pausado` pode ser usado no acompanhamento de um projeto para indicar suspensão excepcional, mas não integra a sequência normativa de estados acima;
- indicadores devem estar acompanhados de texto para não depender exclusivamente de cor.


## Tarefas

Uma boa tarefa deve responder, no mínimo:

- O que deve mudar?
- Por que isso é necessário?
- O que está dentro do escopo?
- O que não deve ser alterado?
- Como saberemos que terminou?
- Quais evidências devem ser retornadas?
- Quais riscos de segurança, dados ou exposição precisam ser considerados?

O template oficial está em [../templates/TASK-TEMPLATE.md](../templates/TASK-TEMPLATE.md).

Encerramento inclui [limpeza proporcional](06-GIT-E-GITHUB.md) e preservação de evidências. Correção editorial só requer PR adicional se houver resíduo real e o fluxo exigir; não criar ciclo para registrar o próprio SHA. Em tarefas independentes, agrupar ações autorizadas quando não houver gate intermediário, conflito de recursos ou risco incompatível.
