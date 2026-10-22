# Troubleshooting — registros de ocorrências

Esta pasta preserva problemas, limitações e falhas observadas durante a aplicação prática do Método ÓRBITA.

Um registro de troubleshooting documenta evidência e aprendizado. Ele **não altera automaticamente** as regras normativas do método.

## Identificação

IDs numéricos como `TRB-001`, `TRB-002` e seguintes são canônicos somente quando atribuídos contra a `main` atual.

Em branches paralelas, use temporariamente um identificador inequívoco, por exemplo:

```text
TRB-DRAFT-AAAAMMDD-descricao-curta
```

Antes da integração:

1. consultar os registros já presentes na `main`;
2. identificar o próximo número livre;
3. verificar outros PRs/branches ativos que também adicionem troubleshooting;
4. atribuir o número canônico;
5. renomear arquivo, título e referências internas;
6. revisar links antes da homologação.

Se dois registros concorrentes tiverem usado o mesmo número antes desta convenção, a ordem de criação comprovável pode ser usada como critério neutro para saneamento.

## Conteúdo esperado

Sempre que possível, registrar:

- contexto e sintoma;
- fatos confirmados;
- hipóteses separadas dos fatos;
- impacto ou risco;
- conduta segura;
- aprendizado;
- relação com regras existentes;
- possível avaliação metodológica;
- estado de homologação.

Uma ocorrência pode resultar em:

- nenhuma mudança no método, quando houver apenas erro de execução;
- esclarecimento operacional de regra existente;
- proposta de melhoria;
- mudança normativa homologada.

A decisão pertence ao responsável humano.
