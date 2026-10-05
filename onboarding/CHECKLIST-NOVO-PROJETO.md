# Checklist — Início de um novo projeto

Use este checklist como referência ao iniciar um software sob o Método ÓRBITA.

## A. Onboarding do método

- [ ] Li o README do Método ÓRBITA
- [ ] Li a visão geral
- [ ] Li os princípios
- [ ] Entendi papéis e responsabilidades
- [ ] Entendi o fluxo de desenvolvimento
- [ ] Entendi os gates e a homologação
- [ ] Entendi o papel do Git/GitHub
- [ ] Entendi as regras para agentes de IA
- [ ] Li os anti-padrões
- [ ] Li o contrato de trabalho desta pasta

## B. Contexto do novo software

- [ ] Problema que o software resolve foi explicado
- [ ] Usuários/público foram identificados
- [ ] Objetivo inicial está claro
- [ ] Restrições conhecidas foram registradas
- [ ] Riscos relevantes foram identificados
- [ ] Foi informado se o projeto é novo, legado ou evolução de outro sistema
- [ ] O repositório específico do projeto foi fornecido

## C. Inspeção do repositório

- [ ] README lido
- [ ] AGENTS/regras locais lidos, quando existirem
- [ ] Documentação existente lida
- [ ] Roadmap/status verificado
- [ ] Estrutura do código inspecionada
- [ ] Branch principal e estado atual identificados
- [ ] Issues/PRs relevantes verificados quando aplicável
- [ ] Decisões existentes preservadas até revisão explícita

## D. Fundação do projeto

Para projeto novo:

- [ ] visão/objetivo registrados no repositório
- [ ] escopo inicial definido
- [ ] arquitetura inicial registrada na profundidade necessária
- [ ] regras do projeto definidas
- [ ] roadmap ou backlog inicial criado
- [ ] estados de tarefa definidos
- [ ] convenção de branches definida
- [ ] critérios de homologação definidos
- [ ] riscos de segurança/publicação avaliados

Para projeto existente:

- [ ] lacunas documentais identificadas
- [ ] proposta de organização feita sem destruir histórico útil
- [ ] diferenças entre estado real e documentação registradas
- [ ] plano de transição aprovado

## E. Antes da primeira implementação

- [ ] tarefa possui ID
- [ ] objetivo está claro
- [ ] escopo incluído está claro
- [ ] escopo excluído está claro
- [ ] critérios de aceite estão definidos
- [ ] testes/validações esperados estão definidos
- [ ] tarefa foi autorizada pelo responsável humano
- [ ] agente de implementação sabe onde deve parar

## F. Segurança

- [ ] nenhum segredo será versionado
- [ ] dados reais são necessários para o teste?
- [ ] é possível usar dados fictícios ou ambiente isolado?
- [ ] projeto deve ser público ou privado?
- [ ] se for operacional, um case público separado seria mais apropriado?

## Gate

Somente depois destes pontos estarem suficientemente resolvidos para o nível de risco do projeto a implementação deve começar.
