# Proposta 004 — Gates de fidelidade visual e qualidade artística para entregas 3D

- **Categoria:** extensão proporcional de evidências e homologação para projetos com requisito visual.
- **Registrada em:** 22/10/2026.
- **Origem:** [the-mmo-idea](https://github.com/jotaCorsino/the-mmo-idea), [PR #7 — CHAR-001](https://github.com/jotaCorsino/the-mmo-idea/pull/7) e [PR #10 — VIS-001](https://github.com/jotaCorsino/the-mmo-idea/pull/10).
- **Estado:** proposta em avaliação; **não é regra oficial**.
- **Escopo:** jogos 3D, interfaces, identidades visuais e outros produtos cuja adequação estética faça parte explícita do objetivo.

## 1. Ocorrência

Na CHAR-001 do MMO, o Codex entregou um cavaleiro estático que podia ser aberto no Blender, exportado em FBX e renderizado no Unity, com controles preservados e sem novos erros. **O pipeline técnico funcionou**, porém o resultado visual era composto de formas geométricas simplificadas e foi considerado insuficiente em relação às imagens aprovadas.

Prosseguir diretamente para rigging/animações teria aumentado retrabalho. A equipe passou a exigir uma prova separada de fidelidade 3D, com três PNGs canônicos e a reprodução de um pequeno cenário e cavaleiro. Na VIS-001.1, o primeiro cenário também exibiu estrutura básica reconhecível, mas ainda não tinha acabamento correspondente. A execução foi interrompida por limite do agente, antes da homologação, e o escopo seguinte foi reduzido a **uma única árvore de alta qualidade**.

O erro não foi a ausência de testes de software: foi tomar uma **validação técnica necessária, mas insuficiente**, como evidência de que uma necessidade artística poderia estar satisfeita.

## 2. Distinções necessárias

Para tarefas criativas, diferenciar:

- **Pipeline validado:** arquivo abre, exporta, importa, executa e não quebra funções existentes.
- **Blockout validado:** escala, composição, silhueta geral e distribuição espacial são reconhecíveis.
- **Fidelidade visual validada:** formas, materiais, iluminação, densidade e estilo se aproximam suficientemente da referência aprovada.
- **Asset aprovado para próxima dependência:** o humano aceitou a qualidade exigida para a finalidade (ex.: rigging, publicação, produção em escala).

Esses estados **não devem ser comprimidos em “concluído”**. “Sucesso técnico” não implica “aprovação artística”.

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

Trata-se de um **template opcional e contextual**, não de uma exigência para qualquer bugfix ou projeto sem direção visual crítica.

## 5. Critérios de aceite para o método

- Um agente não poderá relatar “fidelidade aprovada” com base apenas em funcionamento técnico.
- Entregas de demonstração terão prova inequívoca de que são 3D reais e do software-alvo.
- A revisão poderá interromper expansão de escopo sem descartar assets já produzidos.
- O custo burocrático permanecerá proporcional à criticidade visual.
- Homologação e incorporação normativa ocorrerão somente após revisão humana de proposta específica.

## 6. Referências

- [Governança e homologação](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md).
- [Contrato de trabalho](../onboarding/CONTRATO-DE-TRABALHO.md).
- [CHAR-001 — PR #7](https://github.com/jotaCorsino/the-mmo-idea/pull/7).
- [VIS-001 — PR #10](https://github.com/jotaCorsino/the-mmo-idea/pull/10), especialmente `VisualProof/ANALISE-TECNICA-VIS-001.0.md`.
