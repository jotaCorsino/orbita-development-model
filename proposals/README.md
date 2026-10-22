# Proposals — melhorias candidatas

Esta pasta reúne propostas de evolução do Método ÓRBITA derivadas de uso real, análise ou experimentação.

Uma proposta **não é regra oficial** enquanto não for analisada, homologada e integrada à `main`.

## Identificação

IDs numéricos como `PROP-001`, `PROP-002` e seguintes são canônicos somente quando atribuídos contra a `main` atual.

Em branches paralelas, use temporariamente um identificador inequívoco, por exemplo:

```text
PROP-DRAFT-AAAAMMDD-descricao-curta
```

Antes da integração:

1. consultar as propostas já presentes na `main`;
2. identificar o próximo número livre;
3. verificar outros PRs/branches ativos que também adicionem propostas;
4. atribuir o número canônico;
5. renomear arquivo, título e referências internas;
6. revisar links antes da homologação.

A numeração identifica o registro; **não expressa prioridade, maturidade ou obrigatoriedade**.

## Avaliação

Uma proposta deve deixar claro:

- qual problema ou oportunidade a motivou;
- o que já é coberto pelo método atual;
- qual lacuna permanece;
- qual mudança é sugerida;
- onde a mudança seria aplicada;
- qual custo ou burocracia adicional ela cria;
- como validar se o ganho justifica essa complexidade.

Sempre que possível, prefira mudanças proporcionais e condicionais em vez de transformar toda ocorrência em nova regra transversal.
