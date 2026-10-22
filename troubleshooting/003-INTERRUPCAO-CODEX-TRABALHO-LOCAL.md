# Problema observado 003 — Interrupção de agente com trabalho material ainda local

- **Categoria:** continuidade de execução / limite de uso / estado Git / preservação de artefatos.
- **Registrado em:** 22/10/2026.
- **Ocorrência documentada:** [the-mmo-idea — PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10), durante VIS-001.1.
- **Natureza:** **uma ocorrência identificada**, ainda não demonstrada como problema recorrente do método.
- **Estado:** interrupção confirmada por relato do responsável; **persistência do trabalho local não verificada diretamente**. Problema ainda sem procedimento homologado.
- **Escopo:** diagnóstico de continuidade e retomada segura, não alteração normativa automática.

## 1. Sintoma

Uma execução longa do Codex, usando Blender e Unity para construir o campo de treino 3D, foi interrompida pelo **limite de uso do agente**. O responsável apresentou uma captura do cenário parcial: terreno, duas árvores, cerca, muro, alvo e costa, mas ainda longe da referência artística.

Na consulta remota feita na mesma sequência, o [PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10) ainda mostrava somente **cinco arquivos** de documentação/referências, sem os assets 3D demonstrados na captura. O HEAD remoto registrado era `900f38e`.

**Conclusão sustentada:** a captura não estava acompanhada de publicação remota do trabalho 3D. **Não foi demonstrado** se os arquivos locais haviam sido salvos, commitados localmente, modificados sem commit ou apenas gerados temporariamente. Não afirmar perda de trabalho ou integridade local sem inspeção.

## 2. Impacto e risco

- Se a sessão for reiniciada sem inspecionar a working copy, pode haver recriação ou sobrescrita desnecessária de assets.
- O planejamento pode confundir **“PR atualizado”** com **“trabalho preservado”** quando a execução ocorreu só no disco local.
- Limites de uso podem interromper operações antes de captura de evidência, gravação do `.blend` ou validação de exportação.
- A recuperação depende de saber com clareza **qual foi a última operação comprovada**, não de supor que o agente concluiria sozinho.

Este evento não prova falha do Git, do Unity ou do Blender; o gatilho relatado foi limite de uso do agente.

## 3. Protocolo de retomada sugerido

**Antes de continuar uma tarefa interrompida:**

1. Registrar o motivo e marcar a tarefa **INTERROMPIDA/PAUSADA**, sem declará-la “concluída”.
2. Inspecionar, sem sobrescrever, `pwd`, branch, HEAD, `git status`, `git diff --stat` e `git lfs status` quando tecnicamente possível; registrar as restrições de sandbox sem contorná-las.
3. Inventariar arquivos **rastreados, não rastreados e ignorados** relevantes, incluindo `.blend`, `.blend1`, `.fbx`, cenas, texturas, scripts de geração e evidências locais.
4. Verificar que arquivos importantes **abrem** em Blender/Unity e identificar seu último estado conhecido; preservar backup antes de novas gerações ou reconstruções.
5. Diferenciar `HEAD local`, `origin/branch`, commits não publicados e mudanças sem commit; nunca usar `reset --hard`, `clean -fdx`, force push ou descartar alterações como reflexo automático.
6. Preparar um **checkpoint seguro autorizado** contendo fontes editáveis, scripts e relatório de estado, com Git LFS e verificação de segredos/licenças quando aplicável. Se a sessão/sandbox não permitir escrever `.git`, relatar bloqueio e solicitar via legítima; não forçar.
7. Somente então retomar **a menor subtarefa aprovada**, evitando expansão automática de escopo.

**Durante tarefas longas**, registrar checkpoints pequenos após etapas verificáveis, sem transformar qualquer estado parcial em homologação. Ex.: composição → malha hero → material → integração Unity → evidência. Se não houver autorização para publicar a cada checkpoint, ao menos salvar localmente de forma segura e relatar o estado.

## 4. Pacote mínimo de handoff sugerido

```text
Tarefa: VIS-001.1
Branch/HEAD local:
Origin/HEAD remoto:
Arquivos novos/modificados/ignorados relevantes:
Arquivos que abriram com sucesso:
Evidências locais disponíveis:
Último passo comprovadamente concluído:
Passo interrompido:
Riscos de sobreposição e dependências:
Próxima ação segura:
Gate humano pendente:
```

Não exigir esse protocolo em toda tarefa curta. Aplicá-lo quando houver **interrupção inesperada, pausa longa ou mudança de agente** com alterações materiais não confirmadas no remoto.

## 5. Relação com problema já documentado

Ver [troubleshooting 001 — `.git` somente leitura no sandbox](001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md). Bloqueios de escrita do sandbox e limite de uso são causas **diferentes** e não devem ser confundidas. O protocolo de retomada não autoriza burlar nenhuma proteção.

## 6. Critérios para considerar a ocorrência resolvida

- Inventário local reproduzível, com confirmação do que foi salvo, testado e publicado;
- arquivos Blender e cena Unity abertos com sucesso após a interrupção;
- checkpoint persistido sem perda ou sobrescrita;
- estado de PR, branch, arquivos e gate condizente com as evidências;
- avanço à próxima etapa somente por autorização/homologação humana apropriada.

**Até essas verificações, o estado correto é “trabalho parcial observado; persistência local a confirmar”.**

## 7. Referências

- [ÓRBITA — contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md).
- [the-mmo-idea — VIS-001, PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10).
