# Checklist — Início de um novo projeto

Use este checklist para verificar se um projeto novo foi inicializado corretamente sob o Método ÓRBITA.

## A. Onboarding do método

- [ ] README do Método ÓRBITA lido
- [ ] papéis e responsabilidades compreendidos
- [ ] fluxo e homologação compreendidos
- [ ] identidade e ambientes do projeto compreendidos
- [ ] processo de inicialização compreendido
- [ ] contrato de trabalho para agentes lido
- [ ] regra COM-001 de fechamento **AÇÃO SUA** compreendida pelos agentes de planejamento e implementação
- [ ] baseline de segurança e integridade lido

## B. Contexto e identidade inicial

- [ ] nome canônico do projeto definido
- [ ] contexto próprio no agente de planejamento criado/identificado
- [ ] ideia e problema do software explicados
- [ ] usuários/contexto identificados
- [ ] restrições conhecidas registradas
- [ ] repositório remoto específico do projeto criado/fornecido
- [ ] revisão adotada do ÓRBITA, fontes e domínios aplicáveis registrados
- [ ] agente de planejamento confirmou entendimento do método e do projeto

## C. Fundação documental remota

- [ ] repositório remoto foi inspecionado
- [ ] README inicial criado/organizado
- [ ] quando aplicável, o README apresenta o acompanhamento do desenvolvimento próximo ao início
- [ ] quando aplicável, a tabela resume fase atual, etapas relevantes e próximo gate sem substituir o roadmap
- [ ] quando usados, indicadores visuais estão acompanhados de texto e preservam a distinção entre validação, homologação e conclusão
- [ ] README e roadmap estão coerentes quanto ao estado atual do projeto
- [ ] objetivo e contexto registrados
- [ ] escopo inicial registrado
- [ ] planejamento/roadmap criado
- [ ] backlog de evolução criado no README
- [ ] `knowledge/README.md` criado como índice inicial, mesmo sem entradas
- [ ] arquitetura inicial registrada quando necessária
- [ ] regras locais do projeto registradas
- [ ] `AGENTS.md` criado a partir do [template oficial](../templates/AGENTS-TEMPLATE.md) ou equivalente e contém COM-001 (fechamento `AÇÃO SUA` quando houver tarefa humana)
- [ ] estados de acompanhamento definidos
- [ ] critérios de aceite/homologação definidos
- [ ] riscos de segurança/publicação avaliados
- [ ] fundação documental confirmada ao responsável humano

## D. Preparação local e agente de implementação

- [ ] pasta local com o nome do projeto criada pelo responsável humano
- [ ] pasta aberta no ambiente do agente de implementação
- [ ] primeira tarefa gerada pelo agente de planejamento é uma tarefa de bootstrap
- [ ] tarefa de bootstrap identifica projeto, remoto e branch principal

## E. Bootstrap local

- [ ] agente de implementação confirmou a pasta correta
- [ ] Git foi detectado ou inicializado somente se necessário
- [ ] `origin` corresponde ao repositório remoto correto
- [ ] estado remoto foi buscado
- [ ] branch principal foi sincronizada de forma segura
- [ ] README e documentação inicial estão presentes localmente
- [ ] branch, HEAD e `git status` foram reportados
- [ ] nenhuma funcionalidade foi implementada durante o bootstrap
- [ ] nenhuma ação destrutiva foi executada silenciosamente
- [ ] quando houve bloqueio de escrita ou acesso em `.git`, ele foi diagnosticado antes de alterar o workspace
- [ ] quando aplicável, restrições do sandbox/ambiente foram distinguidas das permissões reais da pasta
- [ ] quando aplicável, a pasta canônica original foi priorizada antes da criação de outra working copy

## F. Gate para primeira funcionalidade

- [ ] agente de planejamento, agente de implementação, pasta local e repositório representam inequivocamente o mesmo projeto
- [ ] documentação inicial existe no repositório
- [ ] base `knowledge/` existe e pode ser consultada por agentes
- [ ] working copy local está vinculada ao remoto
- [ ] primeira tarefa funcional possui ID e título humano
- [ ] abordagem metodológica escolhida pelo humano quando houver alternativas pertinentes e decisão não registrada; Tool e versão/autorizações quando aplicáveis
- [ ] objetivo está claro
- [ ] escopo incluído e excluído estão claros
- [ ] critérios de aceite estão definidos
- [ ] validações/evidências esperadas estão definidas
- [ ] tarefa foi autorizada pelo responsável humano

## G. Segurança

- [ ] riscos de segurança proporcionais ao projeto foram identificados
- [ ] autenticação/autorização foram avaliadas quando aplicáveis
- [ ] tratamento de entradas e dados sensíveis foi avaliado
- [ ] nenhum segredo foi versionado
- [ ] `.gitignore` e arquivos versionados foram revisados
- [ ] dados reais só serão usados quando necessários e autorizados
- [ ] dados fictícios/ambiente isolado foram considerados
- [ ] dependências/configurações sensíveis foram consideradas
- [ ] testes negativos ou de controles sensíveis foram definidos quando necessários
- [ ] visibilidade pública ou privada do projeto foi avaliada
- [ ] case sanitizado separado foi considerado quando aplicável

## Gate

Em projeto novo, a implementação funcional só começa depois que a **fundação documental remota** e o **bootstrap local** estiverem concluídos.

## ISO-001 — Contexto independente

Usar apenas o núcleo metodológico e as fontes explicitamente adotadas/autorizadas para este projeto. Não recuperar, carregar, inferir requisitos ou importar dados, código, decisões, preferências, Knowledge ou referências de outros projetos por semelhança, titularidade, memória, acesso técnico ou associação de conta. Novo projeto inicia com Knowledge vazio, salvo conclusões produzidas nele. Perfis e dependências são escolhas locais; exemplos do núcleo são fictícios. Conteúdo alheio encontrado involuntariamente não é fonte de decisão. A regra canônica está em docs/12-SEGURANCA-E-INTEGRIDADE.md do método adotado.
