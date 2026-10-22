# Proposta 004 — Gates de fidelidade visual e qualidade artística para entregas 3D

- **Categoria:** extensão proporcional de evidências e homologação para projetos com requisito visual.
- **Registrada em:** 22/10/2026.
- **Origem:** [the-mmo-idea](https://github.com/jotaCorsino/the-mmo-idea), [PR #7 — CHAR-001](https://github.com/jotaCorsino/the-mmo-idea/pull/7) e [PR #10 — VIS-001](https://github.com/jotaCorsino/the-mmo-idea/pull/10).
- **Estado:** refinamento metodológico **APROVADO pelo responsável humano no PR #13**, aguardando integração à `main`.
- **Escopo:** jogos 3D, interfaces, identidades visuais e outros produtos cuja adequação estética faça parte explícita do objetivo.

## 1. Ocorrência

Na CHAR-001 do MMO, o Codex entregou um cavaleiro estático que podia ser aberto no Blender, exportado em FBX e renderizado no Unity, com controles preservados e sem novos erros. **O pipeline técnico funcionou**, porém o resultado visual era composto de formas geométricas simplificadas e foi considerado insuficiente em relação às imagens aprovadas.

Prosseguir diretamente para rigging/animações teria aumentado retrabalho. A equipe passou a exigir uma prova separada de fidelidade 3D, com três PNGs canônicos e a reprodução de um pequeno cenário e cavaleiro. Na VIS-001.1, o primeiro cenário também exibiu estrutura básica reconhecível, mas ainda não tinha acabamento correspondente. A execução foi interrompida por limite do agente, antes da homologação, e o escopo seguinte foi reduzido a **uma única árvore de alta qualidade**.

O erro não foi a ausência de testes de software: foi tomar uma **validação técnica necessária, mas insuficiente**, como evidência de que uma necessidade artística poderia estar satisfeita.

## 2. Distinções observadas no caso 3D

No projeto que originou a proposta, foi útil distinguir diferentes **marcos de validação**, sem tratá-los como novos estados normativos do ÓRBITA:

- **pipeline técnico validado:** arquivo abre, exporta, importa, executa e não quebra funções existentes;
- **blockout avaliado:** escala, composição, silhueta geral e distribuição espacial podem ser avaliadas;
- **fidelidade visual avaliada:** formas, materiais, iluminação, densidade e estilo são comparados à referência aprovada;
- **asset aceito para próxima dependência:** o responsável autorizou avanço para a finalidade seguinte, como rigging, publicação ou produção em escala.

Esses marcos pertencem ao contexto visual/3D do projeto. O aprendizado geral é que **sucesso técnico não implica aprovação artística nem autorização automática para avançar**.

## 3. Protocolo proposto

Quando a estética for condição de viabilidade do projeto:

1. **Travar referências:** guardar os arquivos originais com nomes e hashes; registrar quais imagens determinam silhueta, componentes e cenário, e como resolver conflitos entre vistas.
2. **Definir o uso de cada gate:** composição/blockout primeiro, aparência final depois; não modelar o universo inteiro antes de validar um exemplar representativo.
3. **Exigir artefato real:** cenas/editáveis, malhas 3D e capturas diretamente do software-alvo, e não imagens promocionais ou geradas como substitutas.
4. **Comparar sob parâmetros controlados:** câmera, FOV, escala, luz, materiais, resolução e versões; vistas frontal, perfil, costas/alternativas e, quando aplicável, vídeo orbitando o objeto.
5. **Apresentar comparação honesta:** referência 2D lado a lado com captura real, divergências reconhecidas e prioridades de correção. Não prometer igualdade pixel a pixel.
6. **Reduzir escopo diante de dúvida:** se o cenário inteiro está abaixo do padrão, priorizar um só elemento hero (ex.: árvore) e provar qualidade antes de replicar.
7. **Gate explícito do responsável:** autorizar etapa dependente (rig, animação, variações, mundo) somente após aceite visual do asset correspondente.
8. **Regras de custo e licença:** registrar restrições de orçamento, origem de assets e licença; nunca iniciar serviços pagos sem autorização.

## 4. Evidências mínimas sugeridas

| Dimensão | Evidência |
| --- | --- |
| Origem | Imagem canônica, hash e licença/origem quando cabível |
| Geometria | Arquivo editável + cena carregável + ângulos alternativos |
| Acabamento | Close-up de superfície, luz e materiais no software-alvo |
| Comparação | Lado a lado rotulado: conceito **versus** captura real |
| Operação | Versão da ferramenta/engine, logs e limites conhecidos |
| Homologação | Parecer técnico separado do parecer artístico, com decisão humana |

Essas evidências representam apenas um **exemplo contextual do projeto 3D que originou a proposta**. Não constituem template oficial do ÓRBITA e não são exigidas para projetos que não dependam desse tipo de avaliação.

## 5. Separação entre núcleo e protocolo especializado

A avaliação concluiu que apenas o **princípio geral de aceite multidimensional** deve entrar no núcleo do ÓRBITA.

### Pertence ao núcleo

- validação técnica não prova, sozinha, atendimento a critérios não técnicos;
- critérios visuais, artísticos, UX, conteúdo ou equivalentes devem aparecer no aceite quando fizerem parte do objetivo;
- a evidência deve ser compatível com a dimensão avaliada;
- o agente deve distinguir claramente o que foi validado tecnicamente do que ainda depende de avaliação não técnica;
- etapas dependentes não avançam automaticamente quando o gate correspondente continua pendente;
- o template geral de homologação pode registrar dimensões não técnicas de forma opcional.

### Permanece especializado/contextual

Os seguintes controles podem ser úteis em produção visual/3D, mas são específicos demais para o núcleo:

- hashes e versionamento de referências visuais;
- regras fixas de câmera, FOV, escala, iluminação e materiais;
- número obrigatório de vistas ou vídeo orbital;
- exigência genérica de malha, cena ou arquivo editável 3D;
- comparação pixel a pixel ou protocolo visual rígido;
- validação obrigatória de asset hero antes de toda expansão;
- regras particulares de Blender, Unity ou outra ferramenta;
- critérios específicos de licenciamento e orçamento de assets que já sejam tratados pelo projeto.

Essas práticas podem ser documentadas **no próprio projeto** quando necessárias.

Neste momento, o ÓRBITA **não cria um perfil ou template oficial separado de produção visual/3D**. Uma extensão especializada só deve ser considerada futuramente se aplicações reais adicionais demonstrarem recorrência, estabilidade e ganho suficiente para justificar manutenção própria.

## 6. Resultado da avaliação metodológica

A proposta foi reduzida a um princípio geral de **aceite multidimensional**.

Foram preparados ajustes em:

- [Governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md): critérios não técnicos também participam do gate quando fazem parte do objetivo;
- [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md): o agente não pode declarar atendimento com base apenas em sucesso técnico quando restarem dimensões não técnicas a avaliar;
- [Template de homologação](../templates/HOMOLOGACAO-TEMPLATE.md): campos opcionais permitem registrar dimensões não técnicas aplicáveis.

Foram conscientemente **mantidos fora do núcleo**:

- estados ou gates exclusivos de pipeline/blockout/fidelidade;
- protocolo obrigatório de câmera, FOV, iluminação ou número de vistas;
- exigência universal de arquivos 3D editáveis;
- template separado de produção visual/3D;
- regras específicas de Blender, Unity ou qualquer ferramenta;
- critérios universais de asset hero, licenciamento ou orçamento.

### Critérios para homologar o refinamento

- validação técnica e aceite não técnico permanecem conceitualmente distintos;
- a dimensão não técnica só é exigida quando fizer parte dos critérios da tarefa;
- a evidência deve ser proporcional à dimensão avaliada;
- nenhuma nova sequência de estados é criada;
- tarefas puramente técnicas não recebem burocracia visual artificial;
- a incorporação depende de homologação humana explícita.

### Limite da evidência

A proposta deriva de ocorrências documentadas no projeto MMO, especialmente CHAR-001 e VIS-001. O método incorpora o princípio geral demonstrado por esses casos, mas **não transforma o protocolo específico daquele projeto em padrão universal**.

## 7. Referências

- [Governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
- [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md).
- [CHAR-001 — PR #7](https://github.com/jotaCorsino/the-mmo-idea/pull/7).
- [VIS-001 — PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10), especialmente `VisualProof/ANALISE-TECNICA-VIS-001.0.md`.


## 8. Estado de incorporação

O refinamento está preparado na branch `docs/PROP-004-validacao-nao-tecnica`.

A proposta foi **APROVADA** pelo responsável humano no PR #13 em 22/10/2026 e está liberada para integração à `main`.


## 9. Decisão de homologação

**APROVADA** pelo responsável humano no PR #13 em 22/10/2026.

A homologação confirma:

- separação entre validação técnica e critérios não técnicos quando estes fizerem parte do objetivo;
- evidência proporcional à dimensão avaliada;
- ausência de novos estados normativos;
- ausência de gate visual universal;
- manutenção de protocolos 3D específicos no contexto do projeto, e não no núcleo do ÓRBITA;
- uso opcional de campos de aceite não técnico no template de homologação.

A aprovação não transforma tarefas puramente técnicas em processos visuais nem cria protocolo obrigatório de arte/3D.
