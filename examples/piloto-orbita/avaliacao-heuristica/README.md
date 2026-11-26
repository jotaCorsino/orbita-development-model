# Exercício independente — avaliação heurística focal

**Natureza:** protótipo deliberadamente fictício, criado para ensaiar a seleção e aplicação de uma Skill. Não é produto, pesquisa com usuários, teste de acessibilidade integral ou comparação entre agentes. A escolha A (avaliação heurística) foi expressamente aprovada pelo responsável no chat. Fonte metodológica: [ficha](../../../skills/ui-ux/avaliacao-heuristica.md), na revisão `2f82be11e7b9dbe007469aa9f6cf59a1c18796bc`; método Nielsen/Molich conforme referências da própria ficha.

## Escopo e decisão técnica

Fluxo: localizar um título, interpretar a ausência de correspondência, restaurar a lista. Perfil ilustrativo: pessoa que consulta uma coleção de livros; dispositivo de teste desktop, viewport 640 × 320, Chromium 144.0.7559.96, Playwright e Python locais já disponíveis. Sem rede, dados reais, contato, deploy ou orçamento. Comparadas inspeção visual direta (útil para julgamento, menos reproduzível), automação local de interação (evidência de estados e regressão) e integração de ferramenta nova (desnecessária). Escolha delegada: inspeção individual com automação local como instrumento auxiliar, sem admissão de Tool ou instalação. A automação não substitui o julgamento heurístico. Não há teste comparativo de métodos, nem avaliadores independentes.

## Achados e reavaliação

| ID | Localização e observação | Heurística / impacto estimado | Correção isolada |
| --- | --- | --- | --- |
| UX-01 | Botão de submissão “OK” | Correspondência com a linguagem da tarefa; baixo | Rótulo Buscar |
| UX-02 | Busca de título existente retorna lista filtrada, sem mensagem de resultado | Visibilidade do estado; baixo | Contagem de resultados |
| UX-03 | Busca inexistente deixa região vazia, sem explicação | Visibilidade do estado e recuperação; intermediário | Mensagem e orientação de recuperação |
| UX-04 | Sem ação explícita que restaure a lista inteira; limpar campo e reenviar funciona | Controle do usuário; baixo | Botão Limpar busca, restauração e foco |

O impacto é classificação analítica do avaliador único, não medição com participantes. O campo de busca nativo tem controle de limpar em Chromium; não se alegou impossibilidade de limpeza. Os quatro critérios focais falharam na [versão inicial](antes.html) e passaram na [versão corrigida](depois.html). Os demais cinco checks (lista inicial, título existente, ausência real, erros JS, solicitações externas) passaram nas duas versões. Capturas do estado sem resultados foram efetivamente abertas e inspecionadas; registros JSON preservam também o texto e o estado observado. As correções se limitam a defeitos deliberadamente inseridos no laboratório, não autorizam mudança de projeto real ou homologação de UX pelo próprio agente.

## Reprodução

Em cópia isolada e autorizada desta pasta, com Python, Playwright e Chromium locais previamente disponíveis, executar:

```sh
python3 inspecionar.py antes > antes-novo.json
python3 inspecionar.py depois > depois-novo.json
```

O roteiro lê HTML criado para o ensaio e usa set_content; a tentativa inicial de navegação file:// foi bloqueada pela política do navegador, não alterada. A alternativa usa conteúdo sintético próprio e API de teste suportada, sem acessar destino protegido. O parâmetro de inicialização de Chromium reflete o ambiente de laboratório; não aplicar a um ambiente produtivo. O roteiro não é sandbox nem instrumento de segurança universal. O script gera PNGs locais; não baixa dependências. Usar os resultados históricos [antes](antes.json) e [depois](depois.json), preservados byte a byte; arquivos PNG originais não estão incorporados ao Git, mas são reproduzíveis pelo roteiro. As capturas efetivamente geradas foram disponibilizadas no chat, com hashes:

| Captura | SHA-256 |
| --- | --- |
| antes-lista.png | 946bd33ad448f43571ab2c5c27f4090f92cea23a648e9281e7ecaa7b04d6ef9a |
| antes-sem-resultados.png | f661b4993589e09fa17a298adf284b712bfd99e7663926bd6c6373d83f7cb91e |
| depois-lista.png | a36674fae228164899947b75bc8492f5292071fe686b4f353d08090e68bc4c6f |
| depois-sem-resultados.png | 45507a5fb31483781412690ca54ec73ee4b7f36f7e757f8fc0586e4cee0ba0ce |

Os hashes identificam capturas históricas, não garantem reprodução pixel a pixel em ambiente diferente. 5/9 → 9/9 é cobertura dos critérios locais, não uma pontuação de usabilidade ou prova de superioridade do método. A aprovação da abordagem não equivale à homologação visual ou da etapa 11.
