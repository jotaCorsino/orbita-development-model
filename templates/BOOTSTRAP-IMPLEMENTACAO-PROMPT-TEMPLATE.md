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

## Situações de conflito

Se encontrar:

- arquivos locais não rastreados que conflitem com o remoto;
- histórico Git já existente;
- remoto diferente;
- branch divergente;
- necessidade de force/reset destrutivo;

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
- qualquer divergência encontrada.

Não inicie a próxima tarefa.
