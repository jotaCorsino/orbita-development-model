# Problema recorrente 001 — `.git` somente leitura no sandbox do Codex

- **Categoria:** bootstrap local / Git / ambiente de implementação.
- **Primeiro registro documentado aqui:** 09/10/2026.
- **Estado do problema:** recorrente; solução comprovada em um dos ambientes.
- **Estado metodológico:** observação registrada. **Nenhuma mudança normativa do Método ÓRBITA aprovada ou aplicada por este registro.**
- **Projetos com ocorrência identificada:** `scripts-action1` (08/10/2026) e `technolife-downloads-web` (09/10/2026).

## 1. Sintoma

Durante o primeiro bootstrap Git de um projeto, o agente Codex encontra um diretório `.git` vazio ou inacessível, aparentemente **somente leitura**, e não consegue executar `git init`, concluir um clone ou consultar `git status` como repositório válido.

A mensagem de falha pode induzir o planejamento a concluir que o diretório local do usuário não permite Git. Essa conclusão é prematura: o problema pode estar **apenas na visão do filesystem imposta pelo sandbox do Codex**, e não nas permissões reais da pasta no sistema operacional.

## 2. Evidências de recorrência

| Data | Projeto | Evidências | Resultado conhecido |
| --- | --- | --- | --- |
| 08/10/2026 | `scripts-action1` | `.git` vazio; `git init -b main` falhou ao criar `.git/branches/`; `.git` identificado como `tmpfs` montado `ro` (modo `555`), embora o diretório pai estivesse em `ext4` gravável | Um clone funcionou em pasta de trabalho alternativa. A limitação foi atribuída ao sandbox, não a uma incapacidade do Git |
| 09/10/2026 | `technolife-downloads-web` | Codex viu `.git` como montagem `tmpfs` somente leitura; `git status` retornou `fatal: not a git repository`; documentação ainda ausente no ambiente local | Execução **autorizada fora do sandbox** confirmou a pasta original vazia/gravável e clonou a `main` diretamente nela, **sem mover o projeto** |

### Evidência de conclusão da BOOT-001 em 09/10/2026

Segundo o relatório do agente executor para `technolife-downloads-web`:

- diretório original preservado: `~/Projetos/technolife-downloads-web`;
- remoto `origin`: `https://github.com/jotaCorsino/technolife-downloads-web.git`;
- branch e upstream: `main` / `origin/main`;
- HEAD local e remoto: `fc42b74c6b3d4cdea11586dbca383a77a64e8d28`;
- `git status`: `working tree clean`, atualizado com `origin/main`;
- README, documentação e tarefa BOOT-001 presentes;
- nenhuma funcionalidade implementada.

**Atenção:** essas evidências são provenientes do relatório do Codex; a homologação humana do bootstrap é um gate separado.

## 3. Causa técnica identificada

No sandbox do Codex, o caminho `.git` podia ser apresentado como uma **montagem `tmpfs` com opção `ro`**. A falta de escrita nessa montagem impedia a inicialização ou atualização dos metadados do Git, mesmo quando a pasta real do projeto, fora do sandbox, era gravável.

Não confundir:

- **permissão POSIX no filesystem real**, que pode estar correta;
- **montagem ou política do sandbox**, que pode tornar somente leitura o caminho observado pelo agente.

Um `chmod` ou `chown` não resolve necessariamente uma montagem `ro`. Não apagar ou desmontar `.git` por tentativa e erro.

## 4. Procedimento de diagnóstico recomendado (lição operacional, ainda não incorporada ao método)

Antes de propor outro diretório ou recriar o projeto:

1. Confirmar o caminho da pasta, arquivos existentes e remoto desejado.
2. Verificar `ls -ld . .git` e `git status`, **sem modificar nada**.
3. Verificar o tipo/opções de montagem de `.git` com `findmnt -T .git` (quando disponível) e comparar com o diretório pai.
4. Diferenciar explicitamente: bloqueio do **sandbox do Codex** versus permissões da **pasta real** no notebook.
5. Se houver restrição do sandbox, verificar se o ambiente oferece um procedimento legítimo de **execução fora do sandbox mediante autorização humana**, mantendo a **mesma pasta original**.
6. Na execução autorizada, inspecionar novamente se a pasta real está vazia ou já possui arquivos/Git antes de inicializar ou clonar.
7. Para remoto que já contém documentação e pasta original comprovadamente vazia, `git clone <URL_REMOTA> .` é uma forma possível de trazer o projeto **para o diretório atual**, se não houver conteúdo conflitante.
8. Confirmar `origin`, branch, upstream, HEAD, documentação e `git status`. Encerrar o bootstrap sem implementar funcionalidades.

**Regra de segurança:** não contornar o sandbox sem o mecanismo formal de autorização. Não executar `sudo`, `chmod -R`, `rm -rf .git`, desmontagens, `reset --hard` ou mudanças de workspace como reação automática. Se o acesso necessário não for autorizado ou a situação não estiver clara, interromper e registrar o bloqueio.

## 5. Falha de orientação identificada

Na ocorrência de 09/10, a primeira recomendação foi **criar um clone em outra pasta** antes de confirmar se a restrição era apenas do sandbox. Essa orientação era inadequada ao objetivo de manter a identidade única entre repositório, working copy e contexto de implementação, e poderia gerar pastas duplicadas desnecessárias.

**Aprendizado:** identificar a camada responsável pela restrição antes de recomendar reorganizar diretórios. Soluções alternativas devem ser consideradas **após** diagnosticar o ambiente, não como primeira reação.

## 6. Critério de resolução da ocorrência

A ocorrência de 09/10 ficou **tecnicamente resolvida** quando o Git foi clonado no diretório original e o Codex relatou o remoto correto, `main` sincronizada, documentação presente e working tree limpa. A conclusão definitiva da tarefa BOOT-001 depende da homologação do responsável humano no repositório do projeto.

Não foi demonstrado que a política do sandbox deixou de impor a montagem somente leitura; resolveu-se o bootstrap por execução autorizada **fora** dele.

## 7. Avaliação futura do Método ÓRBITA — pendente

Avaliar **em outro momento**, com decisão humana explícita, se o método precisa incorporar:

- um diagnóstico de montagem e permissões ao [template de bootstrap](../templates/BOOTSTRAP-IMPLEMENTACAO-PROMPT-TEMPLATE.md);
- uma orientação para distinguir filesystem real e sandbox na [inicialização de novos projetos](../docs/11-INICIALIZACAO-DE-NOVO-PROJETO.md);
- um item na [checklist de onboarding](../onboarding/CHECKLIST-NOVO-PROJETO.md) relativo a bloqueios `.git` e à autorização necessária;
- a preferência pela **pasta original** antes de oferecer outro workspace, preservando a identidade do projeto.

**Não alterar agora** esses documentos. Este registro reúne evidências e proposta de investigação, não uma atualização já aprovada do Método ÓRBITA.

## 8. Referências de projeto

- [Método ÓRBITA — onboarding](../onboarding/README.md)
- [Technolife — Central de Links](https://github.com/jotaCorsino/technolife-downloads-web)
- [BOOT-001 — bootstrap local](https://github.com/jotaCorsino/technolife-downloads-web/blob/main/tasks/BOOT-001-BOOTSTRAP-LOCAL.md)

Quando uma nova ocorrência for encontrada, acrescentar data, repositório, ambiente, diagnóstico e solução validada, distinguindo fatos observados de hipóteses.
