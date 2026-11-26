# TRB-001 — Git somente leitura em ambiente isolado

**Natureza:** diagnóstico genérico, independente de projeto. Refinamento metodológico homologado na evolução do ÓRBITA; exemplo não comprova recorrência ou solução em ambiente específico.

## Sintoma e diagnóstico

Um agente não consegue inicializar ou consultar .git. Distinguir permissões do sistema de arquivos real, montagem somente leitura e política de sandbox. Inspecionar diretório, estado Git, montagem e autoridade sem alterar ou contornar controles. Não concluir que a pasta do usuário está quebrada com base apenas na visão isolada.

## Procedimento

1. Confirmar projeto, pasta canônica, remoto e material local existente.
2. Diagnosticar erros de acesso e estado de Git em leitura; distinguir restrição do ambiente de permissões reais.
3. Preservar pasta original, arquivos e trabalho não publicado. Se a ação depender de ambiente autorizado diferente, solicitar somente a intervenção necessária ao responsável; nunca burlar sandbox.
4. Inicializar ou sincronizar somente quando autorizado e sem sobrescrever material; verificar branch, upstream, HEAD, documentação e working tree.
5. Registrar evidência e pendência; bootstrap não autoriza funcionalidade ou homologação automática.

Referências normativas: [inicialização](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md), [bootstrap](../templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md), [segurança](../docs/12-SEGURANCA-E-INTEGRIDADE.md). Novas ocorrências e evidências pertencem à base local do projeto.
