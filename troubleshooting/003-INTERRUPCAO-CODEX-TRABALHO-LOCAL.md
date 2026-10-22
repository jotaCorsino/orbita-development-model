# Problema observado 003 — Interrupção de agente com trabalho material ainda local

- **Categoria:** continuidade de execução / limite de uso / estado Git / preservação de artefatos.
- **Registrado em:** 22/10/2026.
- **Ocorrência documentada:** [the-mmo-idea — PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10), durante VIS-001.1.
- **Natureza:** **uma ocorrência identificada**, ainda não demonstrada como problema recorrente do método.
- **Estado:** interrupção confirmada por relato do responsável; **persistência do trabalho local não verificada diretamente**. Refinamento metodológico **APROVADO e INCORPORADO à `main` pelo PR #9**.
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

## 3. Resultado da avaliação metodológica

A análise concluiu que a ocorrência representa uma **lacuna pequena e real de retomada/resiliência**, sem demonstrar falha conceitual ampla do método.

O ÓRBITA já estabelecia que:

- a working copy local pode conter trabalho ainda não publicado;
- remoto, PR e `main` não representam automaticamente todo o estado local;
- operações destrutivas de Git não devem ser usadas sem autorização;
- agentes devem inspecionar estado atual, produzir evidências e respeitar gates.

O ponto não suficientemente explícito era **o que fazer primeiro após uma interrupção inesperada**.

O refinamento preparado estabelece a ordem:

> **inspecionar → preservar → distinguir local/remoto → retomar**

Foram preparados ajustes em:

- [docs/06-GIT-E-GITHUB.md](../docs/06-GIT-E-GITHUB.md): protocolo de retomada segura e checkpoints de resiliência proporcionais;
- [docs/04-FLUXO-DE-DESENVOLVIMENTO.md](../docs/04-FLUXO-DE-DESENVOLVIMENTO.md): `Pausado` como condição excepcional, sem novo estado normativo;
- [onboarding/CONTRATO-DE-TRABALHO.md](../onboarding/CONTRATO-DE-TRABALHO.md): obrigação comportamental de preservar antes de reconstruir.

Foram conscientemente **descartados**:

- criar `INTERROMPIDA` como novo estado oficial;
- manter dois rótulos concorrentes para a mesma condição;
- exigir pacote de handoff completo em toda tarefa;
- exigir commit ou push a cada microetapa;
- tratar checkpoint como homologação;
- tornar o protocolo específico de Blender, Unity ou trabalho 3D.

### Protocolo operacional resultante

Ao retomar uma tarefa interrompida com possível trabalho material ainda local:

1. registrar a condição excepcional como `Pausado`, preservando o último estado normativo conhecido;
2. inspecionar o estado local antes de sincronizar, limpar ou reconstruir;
3. distinguir `HEAD` local, remoto, commits não publicados, mudanças sem commit e arquivos relevantes não rastreados/ignorados;
4. preservar artefatos materiais antes de qualquer ação potencialmente destrutiva;
5. identificar o último passo comprovado e o ponto da interrupção;
6. retornar a tarefa ao estágio correto com base nas evidências;
7. retomar somente a menor subtarefa ainda autorizada.

Em tarefas longas ou caras de reconstruir, checkpoints podem ser usados **por marco verificável**, sem frequência fixa e sem significar aprovação ou conclusão.

## 4. Handoff proporcional

Não foi criado um template obrigatório de handoff.

Quando a interrupção, pausa longa ou troca de agente justificar registro adicional, o handoff deve conter apenas o necessário para permitir retomada segura, como:

- tarefa e último estado normativo conhecido;
- branch/`HEAD` local e referência remota;
- mudanças e artefatos materiais ainda não persistidos;
- último passo comprovadamente concluído;
- ponto da interrupção;
- próxima ação segura;
- gate humano ainda pendente.

Tarefas curtas, sem estado material relevante ou fáceis de reconstruir não precisam gerar documentação adicional apenas para cumprir o método.

## 5. Relação com problema já documentado

Ver [troubleshooting 001 — `.git` somente leitura no sandbox](001-BOOTSTRAP-GIT-CODEX-SANDBOX-SOMENTE-LEITURA.md). Bloqueios de escrita do sandbox e limite de uso são causas **diferentes** e não devem ser confundidas. O protocolo de retomada não autoriza burlar nenhuma proteção.

## 6. Critérios para homologar o refinamento

Para homologar este refinamento mínimo:

- a retomada começa por inspeção e preservação, não por reconstrução;
- `Pausado` permanece condição excepcional, sem novo estado normativo;
- remoto desatualizado não é tratado como prova de ausência de trabalho local;
- checkpoints permanecem proporcionais e opcionais conforme custo de reconstrução;
- nenhuma operação destrutiva é autorizada automaticamente;
- o texto continua genérico e aplicável além do caso 3D que originou a ocorrência;
- uma homologação humana específica aprova ou rejeita a incorporação.

### Limite da evidência

A origem continua sendo **uma ocorrência documentada**. Não foi comprovado que o trabalho 3D local tenha sido perdido, preservado ou recuperado posteriormente.

O refinamento trata o risco observado sem transformar essa incerteza em fato. Sua utilidade deve continuar sendo observada em futuras interrupções reais.

**No caso original, até inspeção local suficiente, a formulação correta continua sendo: “trabalho parcial observado; persistência local a confirmar”.**

## 7. Referências

- [ÓRBITA — contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md).
- [the-mmo-idea — VIS-001, PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10).


## 8. Decisão de homologação

**APROVADO** pelo responsável humano no PR #9 em 22/10/2026.

Foi aprovada a incorporação da retomada segura como refinamento **condicional e proporcional**, preservando os seguintes limites:

- `Pausado` permanece condição excepcional, não novo estado normativo;
- checkpoints são usados por marco útil, não por frequência rígida;
- checkpoint não equivale a homologação;
- tarefas curtas não ganham burocracia adicional;
- a ocorrência original continua sendo uma única evidência documentada.

A aprovação deste refinamento não altera gates humanos existentes nem autoriza operações destrutivas durante retomadas.


## 9. Encerramento

O refinamento foi **APROVADO e INCORPORADO** à `main` pelo PR #9.

**TRB-003 encerrado.**
