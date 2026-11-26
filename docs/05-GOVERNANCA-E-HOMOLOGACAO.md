# 05 — Governança e homologação

## Governança humana

Governança, no ÓRBITA, significa que capacidade técnica do agente não equivale a autoridade decisória.

O responsável humano controla:

- início de mudanças relevantes;
- alteração de escopo;
- aceitação de trade-offs;
- homologação funcional;
- merge ou liberação de etapas sensíveis.

## Gates

Um **gate** é uma condição que precisa ser satisfeita antes do próximo estágio.

Exemplos:

- requisitos compreendidos antes de implementar;
- testes aprovados antes do PR;
- revisão antes do merge;
- validação funcional antes da release;
- riscos de segurança relevantes tratados, aceitos conscientemente ou registrados antes do avanço.

## Homologação do artefato e autorização operacional

A aprovação de código, documentação ou artefato **não autoriza automaticamente sua implantação em um ambiente operacional**.

São decisões relacionadas, mas distintas:

- **homologação do artefato** — confirma que a mudança atende ao objetivo e pode integrar o estado aprovado do projeto;
- **autorização operacional** — permite aplicar essa mudança em um ambiente real, seguindo o procedimento, dependências e controles daquele ambiente.

A distinção é de responsabilidade e evidência, não uma exigência de duas aprovações formais em todos os casos. Quando a tarefa, o runbook e o gate já autorizarem explicitamente a implantação, a homologação e a autorização operacional podem ser registradas no mesmo fluxo de decisão.

Quando houver deploy, migração, atualização de preview, servidor, CMS, integração ou infraestrutura compartilhada, o gate operacional deve considerar, de forma proporcional:

- procedimento ou runbook vigente;
- destino real e estado existente;
- integrações e módulos que precisam ser preservados;
- dependências entre projetos ou responsáveis;
- backup, rollback ou dry-run quando aplicáveis;
- evidência da versão ou artefato efetivamente implantado;
- verificações pós-operação e limitações ainda não comprovadas.

Um commit homologado na origem não demonstra, isoladamente, qual versão está instalada no destino. A evidência operacional deve registrar a revisão ou artefato efetivamente aplicado.

Se o procedimento canônico do ambiente não estiver disponível ou seu status não puder ser confirmado, a ausência de contexto **não deve ser tratada como autorização para inventar um novo fluxo de implantação**.

## Segurança no gate

Uma tarefa não deve ser homologada apenas porque compilou ou porque os testes funcionais passaram.

Quando a mudança tocar superfícies sensíveis, o gate deve considerar evidências proporcionais ao risco, como:

- testes negativos;
- autenticação/autorização;
- análise de segredos;
- dependências;
- permissões;
- exposição de dados;
- configuração;
- riscos ainda não tratados.

Um risco crítico descoberto durante a tarefa deve ser comunicado antes do avanço.

Ver [Segurança e integridade](12-SEGURANCA-E-INTEGRIDADE.md).

## Evidência antes de confiança

O agente implementador deve demonstrar o que fez.

Dependendo da tarefa, evidências podem incluir:

- arquivos alterados;
- resumo do diff;
- testes executados;
- quantidade de testes aprovados/falhos;
- resultado do build;
- logs relevantes;
- commit SHA;
- branch;
- Pull Request;
- limitações ou pontos não validados;
- riscos de segurança relevantes e verificações executadas, quando aplicável.

## Dimensões de aceite além da validação técnica

Validação técnica e atendimento ao objetivo não são necessariamente a mesma coisa.

Quando uma tarefa possuir critérios relevantes que não sejam puramente técnicos — por exemplo, **fidelidade visual, qualidade artística, experiência de uso, clareza de conteúdo, identidade visual ou outra dimensão explicitamente exigida** — o gate deve avaliar também essa dimensão.

Nesses casos:

- build, testes, exportação, importação ou execução sem erros continuam sendo evidências necessárias quando aplicáveis;
- essas evidências **não demonstram, sozinhas, que o resultado atende ao objetivo não técnico**;
- os critérios de aceite devem indicar quais dimensões precisam ser avaliadas;
- a evidência apresentada deve permitir comparar o resultado real com a referência, requisito ou intenção aprovada;
- o responsável humano pode impedir o avanço para uma etapa dependente mesmo quando a implementação estiver tecnicamente funcional.

Exemplo conceitual:

```text
pipeline técnico validado
        ≠
qualidade visual homologada
        ≠
autorização automática para a próxima dependência
```

O método não cria estados normativos separados para cada dimensão. A distinção existe nos **critérios, evidências e gates** aplicáveis à tarefa.

## Homologação

**Homologar não significa apenas confirmar que o código compila.**

A homologação responde se a mudança atende ao objetivo esperado pelo responsável pelo projeto.

Possíveis resultados:

- **Aprovado** — pode avançar;
- **Aprovado com ressalvas** — avança com pendências registradas;
- **Correção necessária** — retorna à implementação;
- **Replanejamento necessário** — a solução ou requisito precisa ser revisto.

O template está em [../templates/HOMOLOGACAO-TEMPLATE.md](../templates/HOMOLOGACAO-TEMPLATE.md).

## Autoridade e risco — matriz operacional

Classificar ação concreta por autoridade/escopo, destino, dados e acesso, reversibilidade, persistência, indisponibilidade, dependências, custo, incerteza e dimensões de aceite. Investigar desconhecidos de forma segura; controle mais restritivo aplicável governa a ação afetada, não todas as demais. Os níveis de formalidade de projeto permanecem distintos.

| Impacto | Controle |
| --- | --- |
| Baixo | Consulta autorizada, diagnóstico focal, ajuste reversível e teste isolado inerentes ao escopo: executar e evidenciar sem microaprovação, preservando gate previsto |
| Intermediário | Mudança funcional, integração isolada, pacote de QA: escopo, refs, critérios, dependências, regressão/segurança e homologação proporcionais |
| Crítico/material | Produção, dados reais, migração, permissões sensíveis, exclusão material, custo não aprovado ou publicação: autorização específica competente, preflight/runbook, recuperação e pós-check; parar se faltar requisito |

Baixo risco fora do escopo não é autorização. Alto impacto já explicitamente autorizado e com controles cumpridos não exige novo aceite redundante. Autorizações identificam objeto, revisão, destino e condições; um gate pode cobrir artefato e operação se explícito. Agente pode escolher implementação técnica equivalente delegada, corrigir a própria falha, agrupar ações independentes e preparar entrega no fluxo autorizado. Não altera requisito, arquitetura material, direção criativa, contrato, custo, segurança, destino, direitos ou gate por conveniência. Aprovação com ressalva identifica pendência, impacto, responsável, condição de avanço e gate posterior; não dispensa requisito crítico ou obrigatório.

### Correção inseparável

Somente quando todas as condições forem satisfeitas: necessária ao critério autorizado; menor mudança demonstrável; preserva objetivo, contratos, direção e comportamento alheio; permanece no risco, destino, custo e autoridade concedidos; pode ser testada e evidenciada sem dispensar controles. Registrar no diff/entrega. Caso contrário, registrar necessidade fora do escopo e elevar decisão material. Risco crítico exige comunicação imediata e interrupção da ação afetada conforme segurança.

### Reutilização de evidência

Identificar afirmação/critério, revisão, artefato, ambiente, dados, configuração, dependências, método, resultado, limitações, fonte e delta desde a prova. Reutilizar apenas quando cobertura e pressupostos permanecem válidos, prova recuperável e gate não exige independência/repetição. Cobertura parcial: executar lacuna; mudança relevante: revalidar alcance afetado. Distinguir executado agora, reutilizado, não testado e não aplicável com justificativa. Hash não prova instalação ou segurança; pré e pós-operação comprovam momentos diferentes. Evidência técnica não substitui aceite visual/UX nem homologação. Não contar reutilização como nova execução.

Para desempenho, consultar [protocolo de avaliação da etapa 09](../proposals/007-09-EFICIENCIA-E-AUTONOMIA.md) §7: baseline comparável, tempo ativo/ciclo, intervenções necessárias/evitáveis, repetição, reuso, retomada, retrabalho, reincidência, recursos, qualidade/segurança e encerramento. Dados ausentes não são zero; não alegar ganho sem comparação válida nem omitir controles para melhorar métricas.
