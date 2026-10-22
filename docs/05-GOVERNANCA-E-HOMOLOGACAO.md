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

## Homologação

**Homologar não significa apenas confirmar que o código compila.**

A homologação responde se a mudança atende ao objetivo esperado pelo responsável pelo projeto.

Possíveis resultados:

- **Aprovado** — pode avançar;
- **Aprovado com ressalvas** — avança com pendências registradas;
- **Correção necessária** — retorna à implementação;
- **Replanejamento necessário** — a solução ou requisito precisa ser revisto.

O template está em [../templates/HOMOLOGACAO-TEMPLATE.md](../templates/HOMOLOGACAO-TEMPLATE.md).
