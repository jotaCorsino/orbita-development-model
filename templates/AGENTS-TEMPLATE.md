# AGENTS — [NOME DO PROJETO]

**Escopo:** [descrever o software e limites em uma ou duas frases]. **Fonte metodológica:** [URL do ÓRBITA e revisão adotada (tag/commit); caminho do contrato nessa revisão]. **HUB/métodos aplicáveis:** [fonte, revisão, domínio ou nenhum]. Não adotar main automaticamente; se legado desconhecido, registrar e regularizar com responsável.

## Leitura inicial obrigatória

1. `README.md` — objetivo, status, pendências e próximo passo;
2. roadmap/planejamento canônico e última homologação;
3. branch/PR ativa e estado do repositório;
4. índice `knowledge/README.md`, entradas relevantes e condição de validade;
5. procedimentos e dependências específicos, Skills/Tools pertinentes, quando aplicáveis;
6. tarefa autorizada, ref, critérios, último gate e restrições. Recuperar seletivamente na continuidade; preservar estado local antes de sincronizar. Não confundir revisão do AGENTS com configuração efetivamente carregada.

Nenhum agente deve presumir estado de produção, autorização ou progresso a partir de memória de conversa.

## Limites e continuidade

Um chat por iniciativa enquanto suficiente; não por etapa. Agir dentro de autorização; comparar métodos viáveis, recomendar e aguardar decisão humana salvo escolha/delegação registrada. Reutilizar prova válida, preservar gates, aplicar NOM-001 e limpeza proporcional. Referenciar fontes competentes; não armazenar segredos, status volátil ou duplicar método.

## COM-001 — Regra absoluta de comunicação ao responsável

**Toda resposta deste projeto, seja de planejamento, implementação, revisão ou manutenção, deve seguir a regra abaixo.** Não há exceções de estilo.

**Se existir uma providência efetivamente destinada ao responsável humano**, o **último trecho da resposta** deve ser um único bloco:

```text
**AÇÃO SUA**
[Descreva objetivamente o que você precisa fazer: ação, objeto e resultado que deve me informar/enviar, quando aplicável.]
```

Exemplos de gatilho: instalar/testar pacote, executar comando, aprovar gate ou PR, fornecer informação necessária, optar por uma alternativa, enviar evidência, realizar publicação autorizada.

- O bloco `AÇÃO SUA` deve aparecer **uma única vez e por último**, mesmo se houver mais de uma ação humana.
- **Sem ação destinada ao responsável: omitir totalmente o bloco**. Não criar tarefas artificiais.
- Não transferir para o responsável tarefas que o próprio agente consegue e está autorizado a executar.
- Não pedir novamente autorização já registrada; ações sensíveis continuam exigindo os gates do projeto.
- Conservar no corpo da resposta os resultados do agente, evidências e limitações; `AÇÃO SUA` contém somente providências humanas.

**Verificação final antes de cada resposta:** `Houve algo que o responsável precisa fazer?` Se sim, terminar com `AÇÃO SUA`; se não, encerrar normalmente.

## Regras e gates específicos do projeto

[Completar somente com regras reais de tecnologia, segurança, documentação e aprovação do projeto. Não remover nem enfraquecer COM-001.]

---

> **Antes de publicar no repositório:** substituir placeholders; preservar a referência metodológica. Este template é para a fundação de novos projetos, não é permissão de alterar ambientes.
