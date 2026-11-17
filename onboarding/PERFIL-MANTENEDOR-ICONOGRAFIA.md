# Perfil do mantenedor — iconografia de interfaces (ICON-001)

**Decisão do responsável:** 17/11/2026. **Aplicação:** projetos de sites, sistemas e interfaces desenvolvidos sob direção do mantenedor deste repositório. Este é um **perfil de preferência de projeto**, **não uma obrigação genérica do Método ÓRBITA para terceiros**. Sua adoção passa a valer em cada repositório após a integração da referência correspondente.

## Decisão canônica

- **Fonte preferencial para pesquisar e selecionar ícones:** [Iconify](https://iconify.design/) e [catálogo de coleções](https://icon-sets.iconify.design/).
- **Coleção de interface inicialmente preferida:** [Tabler Icons](https://icon-sets.iconify.design/tabler/) (`tabler:`, MIT). **Alternativa:** [Phosphor](https://icon-sets.iconify.design/ph/) (`ph:`, MIT), quando justificada pela identidade visual. Registrar coleção, variante e versão/forma de obtenção por projeto.
- **Não desenhar ícones por IA**, nem misturar bibliotecas arbitrariamente, quando existir um recurso adequado e licenciado. Exceções: identidade de marca/logotipo, símbolos próprios do produto e lacunas comprovadas no catálogo; a exceção exige justificativa.
- **Consistência por interface:** manter uma coleção principal, variante de peso/traço coerente, escala, grid, tamanho óptico e alinhamento; cor por tokens CSS (`currentColor` quando aplicável), estados consistentes e contraste suficiente. Um ícone não substitui rótulo textual quando este é necessário para clareza.
- **Publicação:** preferir SVGs revisados armazenados/versionados no projeto ou ícones incluídos no build (apenas os utilizados). API externa sob demanda só quando houver necessidade concreta (por exemplo, catálogo dinâmico), com avaliação de performance, disponibilidade, cache e política de segurança. Não incorporar uma dependência externa obrigatória à execução do site sem decisão explícita.
- **Licenças:** verificar a licença da coleção efetivamente utilizada. A licença da plataforma/ferramenta Iconify **não** substitui a licença dos ícones. Preservar atribuição e termos quando exigidos, e registrar origem no projeto.
- **Acessibilidade:** ícones decorativos com `aria-hidden="true"`; botões só com ícone devem possuir nome acessível; avaliar foco, área de toque, estados, contraste e responsividade.
- **Segurança:** utilizar recursos do catálogo oficial ou pacotes confiáveis, revisar SVG antes da incorporação e evitar SVG arbitrário recebido de usuários como HTML executável.

## Uso operacional por agentes

1. Antes de desenhar ícone, buscar um equivalente no Iconify e conferir compatibilidade de estilo e licença.
2. Registrar no projeto a **coleção escolhida** e um mapa semântico mínimo quando houver vários ícones (ex.: `navegação/início → tabler:home`, `serviço/servidor → tabler:server`). Registrar identificadores, não duplicar SVGs completos na documentação.
3. Selecionar implementação proporcional à stack: exportação SVG local para WordPress/HTML, ícones importados seletivamente no build para React/Vue e outros frameworks. A API `https://api.iconify.design/tabler/home.svg` é uma fonte possível de obtenção, não um requisito de carregamento em produção.
4. No QA, verificar legibilidade, alinhamento, coerência visual, acessibilidade e comportamento em desktop/tablet/celular.
5. Migrações de iconografia **não são retroativas automaticamente**: não substituir ícones de sites publicados ou componentes homologados fora de tarefa autorizada; preservar evidências, versões, testes e eventual rollback.

## Adoção e limites

- O repositório de cada software deve **referenciar este perfil** em suas instruções de agentes/decisões de UI quando a regra for adotada. A referência evita repetir e desalinhar várias cópias da especificação.
- A escolha da coleção principal é **padrão inicial**, não impeditivo para identidades visuais já aprovadas ou conjuntos com exigências técnicas específicas.
- Este perfil não altera o núcleo metodológico, não altera projetos de terceiros que usem ÓRBITA e não autoriza merges, deploys ou intervenções em produção.

## Referências técnicas consultadas em 17/11/2026

- [Documentação Iconify](https://iconify.design/docs/)
- [Dados de ícones e diferenças entre API e build local](https://iconify.design/docs/icons/icon-data.html)
- [API SVG](https://iconify.design/docs/api/svg.html)
- [Conceito de coleção/licença](https://iconify.design/docs/icons/icon-set-basics.html)
- [Coleção Tabler](https://icon-sets.iconify.design/tabler/)
- [Coleção Phosphor](https://icon-sets.iconify.design/ph/)
