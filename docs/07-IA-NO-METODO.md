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

## Uso atual de ferramentas

Na implementação original do método:

- **João Corsino** — responsável e homologador;
- **ChatGPT** — planejamento, análise, especificação e revisão;
- **Codex** — implementação e validação técnica;
- **GitHub** — estado canônico e histórico.

Essa composição pode mudar. O método deve sobreviver à substituição de qualquer ferramenta.

## Contextos dedicados por projeto

Na aplicação prática atual, João mantém um contexto próprio para cada software tanto no ChatGPT quanto no Codex.

O padrão preferido é:

```text
mesmo projeto
├── Projeto no ChatGPT — planejamento, análise e coordenação
├── Projeto/workspace no Codex — implementação e validação
├── pasta local — working copy
└── GitHub — estado persistente
```

Usar o mesmo nome entre esses ambientes reduz ambiguidade e facilita a retomada.

Os contextos de IA são úteis para continuidade, mas podem estar incompletos ou desatualizados. Por isso, antes de decisões ou alterações relevantes, o estado atual do repositório deve prevalecer.

## Contexto e documentação

O contexto de um agente é temporário. Por isso, decisões importantes não devem permanecer exclusivamente em chats.

Documentação no repositório reduz dependência de memória conversacional e permite que outro humano ou agente retome o projeto com menor perda de contexto.

## Limites

IA pode errar, interpretar requisitos incorretamente, criar código inseguro ou declarar sucesso com validação insuficiente.

O ÓRBITA não elimina esses riscos. Ele cria pontos explícitos para detectá-los e controlá-los.
