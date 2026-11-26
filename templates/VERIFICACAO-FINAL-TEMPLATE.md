# Verificação final — encerramento de mudança

Use este checklist **somente na extensão necessária ao impacto da mudança**.

Ele não cria novo estado no fluxo do ÓRBITA e não exige varredura integral do repositório para toda tarefa.

## Identificação

- **Tarefa / registro:**
- **Branch / PR:**
- **Responsável pela revisão:**
- **Superfícies derivadas esperadas:** [README / roadmap / índice / tabela / changelog / documentação / nenhuma / outras]

## A. Antes da integração

- [ ] artefato ou registro canônico identificado;
- [ ] branch comparada com a `main` atual;
- [ ] diff permanece no escopo autorizado;
- [ ] arquivos derivados relevantes identificados;
- [ ] IDs, nomes, títulos e estados relacionados conferidos;
- [ ] links/caminhos afetados conferidos;
- [ ] busca por referências antigas relacionadas à mudança executada quando aplicável;
- [ ] nenhuma inconsistência conhecida ficou ocultada antes da homologação.

### Evidências / observações

[registrar somente o necessário]

## B. Depois do merge ou aplicação (sem PR, confirmar fonte/destino final)

- [ ] PR confirmado como mergeado quando houver; sem PR, registro/artefato final comprovado;
- [ ] commit de integração identificado;
- [ ] arquivos canônicos verificados diretamente na linha integrada ou destino pertinente;
- [ ] README/roadmap/índices/painéis relevantes conferidos quando aplicável;
- [ ] busca por estados ou referências antigas repetida quando aplicável;
- [ ] links/caminhos principais afetados continuam válidos;
- [ ] nenhum resumo contradiz o estado integrado;
- [ ] necessidades futuras relevantes descobertas durante o ciclo foram registradas no backlog quando aplicável;
- [ ] nenhum item de backlog foi tratado como autorização implícita para nova implementação;
- [ ] conclusões comprovadas, reutilizáveis e operacionalmente relevantes descobertas no ciclo foram registradas ou atualizadas em `knowledge/` quando aplicável;
- [ ] nenhuma hipótese não confirmada foi promovida a Knowledge Vigente.

## C. Resíduos operacionais (quando aplicável)

- [ ] alvos inventariados/classificados, identidade e dependências verificadas;
- [ ] autoridade, preservação e recuperação adequadas; não excluir por nome/idade/merge;
- [ ] pós-check confirma resultado e preservação dos demais recursos;
- [ ] exceções/falhas parciais registradas com responsável, risco e condição de saída;
- [ ] sem PR adicional por ritual quando não há resíduo; mudança material retorna ao gate.

## Verificação de comunicação — COM-001

- [ ] se a resposta final atribui uma ação ao responsável humano, existe **um único bloco terminal `AÇÃO SUA`** com ação e retorno claros;
- [ ] se a resposta não requer providência humana, o bloco foi omitido;
- [ ] as autorizações previamente dadas não foram solicitadas novamente; nenhuma ação sensível foi apresentada como executada sem evidência.

## Resultado do encerramento

Escolha um:

- [ ] **CONSISTENTE — encerramento confirmado**
- [ ] **RESÍDUO DOCUMENTAL — correção curta necessária**
- [ ] **INCONSISTÊNCIA MATERIAL — retornar ao fluxo normal de revisão/homologação**

## Regra prática

Pergunta de controle:

> **Que outros lugares podem continuar contando a versão anterior desta mesma informação?**

A resposta define o alcance proporcional da verificação.
