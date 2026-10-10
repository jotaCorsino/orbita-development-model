# BOOTSTRAP — Inicialização local do projeto

Você está atuando como **agente de implementação** no primeiro handoff deste projeto.

## Identidade

- **Projeto:** [NOME_CANONICO]
- **Repositório remoto:** [URL_OU_OWNER_REPO]
- **Branch principal esperada:** [MAIN_OU_OUTRA]

O responsável humano já criou e abriu a pasta local destinada exclusivamente a este projeto.

## Objetivo

Transformar a pasta atual em uma working copy segura do repositório remoto já preparado pelo agente de planejamento.

Esta tarefa é apenas de bootstrap. **Não implemente funcionalidades.**

## Procedimento

1. confirme o caminho e o nome da pasta atual;
2. verifique se já existe um repositório Git;
3. se não existir, inicialize Git;
4. verifique remotos existentes;
5. configure `origin` somente se necessário;
6. confirme que `origin` corresponde ao repositório informado;
7. busque o estado remoto;
8. sincronize a branch principal de forma segura;
9. não apague, sobrescreva ou force conteúdo local único sem autorização;
10. confirme que a documentação inicial do projeto foi recebida;
11. verifique `git status`, branch atual e remoto;
12. pare após a validação.

## Falha de escrita em `.git` ou restrição do ambiente

Se Git não conseguir criar, ler ou atualizar `.git`, **não conclua imediatamente que a pasta real do projeto é somente leitura** e não crie outra working copy como primeira solução.

Antes de reorganizar diretórios:

1. inspecione a pasta atual e `.git` sem modificar conteúdo;
2. confirme se o bloqueio pertence ao filesystem real ou ao ambiente isolado/sandbox do agente;
3. quando disponível, verifique permissões e características de montagem do caminho afetado;
4. preserve a pasta original e sua identidade canônica sempre que possível;
5. se o ambiente oferecer execução fora do sandbox, utilize somente o mecanismo formal disponível e mediante autorização humana;
6. após qualquer execução autorizada fora do sandbox, inspecione novamente o estado real da pasta antes de inicializar ou clonar;
7. se o remoto já contém a fundação documental e a pasta real estiver comprovadamente vazia, o repositório pode ser clonado diretamente no diretório atual;
8. não use `sudo`, `chmod -R`, remoção de `.git`, desmontagens, `reset --hard` ou mudança de workspace como reação automática ao bloqueio.

Se não for possível distinguir com segurança a origem da restrição, **pare e relate o bloqueio**.

## Situações de conflito

Se encontrar:

- arquivos locais não rastreados que conflitem com o remoto;
- histórico Git já existente;
- remoto diferente;
- branch divergente;
- necessidade de force/reset destrutivo;
- `.git` inacessível, somente leitura ou apresentado pelo ambiente como montagem restrita;

**não resolva silenciosamente.** Relate a situação e aguarde orientação.

## Retorno esperado

Informe:

- pasta utilizada;
- se Git precisou ser inicializado;
- URL de `origin`;
- branch atual;
- commit/HEAD sincronizado;
- confirmação de que README/documentação estão presentes;
- resultado de `git status`;
- qualquer divergência encontrada;
- quando houver bloqueio de `.git`, diagnóstico da camada afetada (filesystem real ou ambiente/sandbox) e eventual autorização utilizada.

Não inicie a próxima tarefa.
