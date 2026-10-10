# Checklist — Início de um novo projeto

Use este checklist para verificar se um projeto novo foi inicializado corretamente sob o Método ÓRBITA.

## A. Onboarding do método

- [ ] README do Método ÓRBITA lido
- [ ] papéis e responsabilidades compreendidos
- [ ] fluxo e homologação compreendidos
- [ ] identidade e ambientes do projeto compreendidos
- [ ] processo de inicialização compreendido
- [ ] contrato de trabalho para agentes lido
- [ ] baseline de segurança e integridade lido

## B. Contexto e identidade inicial

- [ ] nome canônico do projeto definido
- [ ] contexto próprio no agente de planejamento criado/identificado
- [ ] ideia e problema do software explicados
- [ ] usuários/contexto identificados
- [ ] restrições conhecidas registradas
- [ ] repositório remoto específico do projeto criado/fornecido
- [ ] agente de planejamento confirmou entendimento do método e do projeto

## C. Fundação documental remota

- [ ] repositório remoto foi inspecionado
- [ ] README inicial criado/organizado
- [ ] objetivo e contexto registrados
- [ ] escopo inicial registrado
- [ ] planejamento/roadmap criado
- [ ] arquitetura inicial registrada quando necessária
- [ ] regras locais do projeto registradas
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
- [ ] working copy local está vinculada ao remoto
- [ ] primeira tarefa funcional possui ID
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
