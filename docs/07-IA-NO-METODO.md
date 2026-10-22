# 07 — IA no método

## IA como capacidade, não como autoridade

O Método ÓRBITA parte da ideia de que agentes de IA podem ampliar produtividade sem retirar do desenvolvedor a responsabilidade de compreender e governar o projeto.

## Por que separar planejamento de implementação?

Quando o mesmo agente interpreta uma necessidade, escolhe a solução, implementa e declara que terminou, há menos pontos naturais de revisão.

Ao separar funções, cria-se uma cadeia de verificação:

```text
necessidade humana
      ↓
análise e planejamento
      ↓
implementação
      ↓
evidências
      ↓
revisão
      ↓
homologação humana
```

## Ferramentas são substituíveis

O ÓRBITA define funções, não produtos específicos.

- **responsável humano** — decisão, prioridade e homologação;
- **agente de planejamento** — análise, documentação, especificação, coordenação e revisão;
- **agente de implementação** — implementação e validação técnica;
- **repositório Git** — estado persistente e histórico.

Na configuração de referência deste repositório, ChatGPT exerce o papel de planejamento e Codex o papel de implementação. Claude, Gemini ou qualquer combinação equivalente também podem cumprir esses papéis. O método deve sobreviver à substituição de qualquer IA.

## Contextos dedicados por projeto

Cada software deve manter contextos próprios para planejamento e implementação, independentemente da ferramenta escolhida.

O padrão preferido é:

```text
mesmo projeto
├── contexto do agente de planejamento — análise e coordenação
├── contexto do agente de implementação — implementação e validação
├── pasta local — working copy
└── GitHub — estado persistente
```

Usar o mesmo nome entre esses ambientes reduz ambiguidade e facilita a retomada.

Os contextos de IA são úteis para continuidade, mas podem estar incompletos ou desatualizados. Por isso, antes de decisões ou alterações relevantes, o estado atual do repositório deve prevalecer.

## Fundação documental antes da implementação

Em projeto novo, o agente de planejamento deve transformar o contexto inicial em documentação persistente no repositório remoto antes do primeiro trabalho funcional do agente de implementação.

A primeira tarefa do agente de implementação é o bootstrap da working copy local com o repositório já documentado. Somente depois começa a implementação de funcionalidades.

Ver [Inicialização de um novo projeto](11-INICIALIZACAO-DE-NOVO-PROJETO.md).

## Contexto e documentação

O contexto de um agente é temporário. Por isso, decisões importantes não devem permanecer exclusivamente em chats.

Documentação no repositório reduz dependência de memória conversacional e permite que outro humano ou agente retome o projeto com menor perda de contexto.

## Estado integrado e trabalho ativo em revisão

A `main` representa o estado **integrado e deliberadamente aceito** do projeto, mas não deve ser interpretada automaticamente como inventário completo de todo trabalho atualmente relevante.

Projetos podem manter documentação, planejamento ou implementação ainda em revisão em branches e Pull Requests ativos. Nesses casos, antes de concluir que uma decisão, especificação ou conteúdo “não existe”, o agente deve identificar qual conjunto de documentos rege a tarefa atual.

A distinção esperada é:

- **`main`** — estado integrado/homologado;
- **branch ou PR ativo** — trabalho em elaboração ou revisão, ainda não integrado;
- **documentação vigente para a tarefa** — conjunto explicitamente indicado pelo planejamento ou pelas dependências da tarefa, podendo incluir conteúdo ainda em revisão.

Conteúdo de branch ou PR ativo **não se torna canônico apenas por existir**. Sua autoridade depende do escopo, da relação com a tarefa e dos gates definidos pelo projeto.

Quando uma tarefa depender de trabalho ainda não integrado, o agente deve registrar de forma inequívoca a referência relevante — branch, PR, commit ou base — e evitar assumir que a ausência desse conteúdo na `main` significa perda, descarte ou inexistência.

## Consolidação documental sem perda semântica

Organizar documentação não significa reduzir conteúdo a qualquer custo.

Quando uma tarefa envolver **fusão, condensação, reorganização ou remoção de documentação não trivial**, o agente deve preservar o significado das informações ainda vigentes.

Uma consolidação não pode ser considerada bem-sucedida apenas porque:

- o número de arquivos diminuiu;
- links continuam válidos;
- títulos foram reorganizados;
- textos ficaram menores;
- documentos aparentemente duplicados foram unidos.

A validação deve considerar também se foram preservados, quando ainda vigentes:

- fatos e decisões;
- restrições e exceções;
- nomes próprios e relações;
- regras de negócio ou mecânicas;
- contexto necessário para interpretar decisões;
- detalhes únicos que não existam em outro lugar;
- conteúdo ainda em elaboração que não tenha sido explicitamente descartado.

Conteúdo incompleto, provisório ou ainda não homologado **não deve ser removido apenas por não estar finalizado**. Para remover informação material, o agente deve conseguir demonstrar ao menos uma destas condições:

1. ela foi explicitamente substituída por conteúdo identificável;
2. ela é duplicada e não contém informação exclusiva;
3. sua remoção foi autorizada pelo responsável humano.

Quando houver dúvida sobre perda semântica, a ação correta é **preservar e sinalizar a dúvida**, não resumir de forma irreversível.

## Limites

IA pode errar, interpretar requisitos incorretamente, criar código inseguro ou declarar sucesso com validação insuficiente.

O ÓRBITA não elimina esses riscos. Ele cria pontos explícitos para detectá-los e controlá-los.
