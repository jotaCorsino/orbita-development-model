# TRB-002 — Operação de preview sem recuperação do fluxo existente

**Natureza:** cenário fictício e procedimento genérico; refinamento metodológico homologado no ÓRBITA. Não é registro de ambiente real.

## Sintoma e risco

Um ambiente de prévia fictício possui integração auxiliar, autenticação e arquivos próprios. O agente propõe cópia direta de uma nova versão sem recuperar runbook. Isso pode remover recursos, sobrescrever configuração, expor dados ou invalidar rollback. Script experimental não equivale a procedimento homologado. Uma referência Git não demonstra versão publicada.

## Diagnóstico e retomada

1. Identificar ambiente, fonte e responsável, estado observado, versão de origem, artefato publicado e dependências autorizadas. Consultar documentação e runbook do próprio projeto; não buscar outros projetos por semelhança.
2. Se faltar acesso ou contexto indispensável, permanecer em diagnóstico não destrutivo e encaminhar somente a decisão necessária. Não substituir procedimento por comandos improvisados.
3. Recuperar procedimento aprovado, critérios, proteção e recuperação; distinguir evidência de preflight, teste parcial, implantação e homologação.
4. Após autorização específica, preparar artefato e executar controles proporcionais. Confirmar versão/destino real, autenticação e funcionalidades afetadas, preservar configuração e evidência; não repetir operação externa com resultado incerto.
5. Reconciliar registros e classificar resíduos. Relatos e evidências operacionais ficam no projeto que os produziu.

[Preflight](../proposals/002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md), [identidade](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md), [governança](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
