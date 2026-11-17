# Perfil do mantenedor — QA local-first e uso excepcional de GitHub Actions

**Decisão do mantenedor: 17/11/2026.** Este documento expressa **preferência operacional do mantenedor** nos projetos que ele dirige. Não é obrigação universal para outros adotantes do Método ÓRBITA.

## Princípio

**Manter testes e homologação obrigatórios, mas independentes da disponibilidade de GitHub-hosted runners.** O GitHub conserva código, histórico, PRs e fontes de verdade. Os testes devem rodar primeiro em working copy isolada, com resultado reproduzível e evidência verificável. O GitHub Actions é **opcional** e reservado a necessidade concreta, com orçamento aprovado.

### Política prática

1. **Padrão:** Python/PHP/Node/testes do stack executados localmente no ambiente de desenvolvimento ou ambiente isolado de agente, sem dependência do GitHub Actions.
2. **Evidência:** identificar commit, branch, comandos, ambiente, resultado, logs sanitizados e hashes dos arquivos; confirmar que o conteúdo testado coincide com o proposto. Relatórios de execução ficam fora do Git por padrão, exceto resumo técnico sanitizado aprovado.
3. **QA proporcional:** testes unitários/negativos, smoke, segurança e integração conforme risco. Código não executado ou falhando continua bloqueado; validação estática sozinha não substitui execução exigível.
4. **Actions por exceção:** usar `workflow_dispatch` sob aprovação para matrizes de compatibilidade, testes independentes críticos e releases relevantes. Não configurar gatilhos automáticos repetitivos sem benefício comprovado, orçamento e controles.
5. **Sem despesas implícitas:** não alterar budgets, cadastrar método de pagamento ou ativar recursos faturáveis por iniciativa do agente.
6. **Self-hosted:** alternativa possível somente quando houver necessidade real e revisão de segurança do runner, acesso a repositórios e isolamento de segredos.
7. **Governança:** PR revisada, aceite humano, merge, preview e produção mantêm gates independentes. Bloqueio externo de runner não implica aprovação automática do código.
8. **Aplicação gradual:** mudanças em workflows/regras de outros repositórios exigem branches/PRs próprias. Não cancelar execuções, desativar proteções nem modificar projetos não autorizados de maneira global.

## Evidência de origem

Em 17/11/2026, o painel pessoal de budgets indicou **Actions US$ 0 / 0, Usage blocked**. Foram observados jobs com `runner_id=0` e zero etapas executadas no Hub, Setup Sites, Modo Revisão e site Technolife. Isso é evidência de indisponibilidade para essas execuções, **não** prova isolada de cota gratuita esgotada ou causa única. A [DEP-001 no Hub](https://github.com/jotaCorsino/technolife-hub/pull/30) serve de primeiro caso de adaptação para QA local e workflow de disparo manual.

## Contrato para agentes

Ao iniciar tarefa no projeto deste mantenedor, verificar os comandos locais em seu próprio repositório, executar testes em escopo seguro, produzir resultado e hashes sanitizados, indicar claramente o que não foi testado e **não bloquear o progresso apenas pela ausência de GitHub Actions**. Não chamar de homologação um teste que não executou, nem remover checks obrigatórios sem gate próprio.
