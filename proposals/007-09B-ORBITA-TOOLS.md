# ORB-EVO-001 — 09B: ÓRBITA Tools

**Data:** 26/11/2026. **Estado:** catálogo e contrato de admissão candidatos homologados documentalmente, integrados pela PR #47 e verificados na main; ainda não vigentes como norma geral. **Baseline:** `c1ffeaf98205d2c058ad585f5ed077c62db353f3`, PRs #45/#46 integradas; etapas 01–09A encerradas. **Autorização:** etapa 09B exclusivamente, no mesmo chat da iniciativa. [Plano aprovado](007-ORB-EVO-001-PLANO-DE-EVOLUCAO.md).

## 1. Fundamento e decisão

D-25 da [auditoria integral](007-01-AUDITORIA-INTEGRAL.md) aponta a ausência planejada de catálogo de ferramentas; D-01/D-04/D-05/D-08/D-13/D-19/D-21/D-23/D-26/D-27 delimitam autoridade, estado, proporcionalidade, limpeza, operação, versões, nomenclatura, avaliação e privacidade. A [auditoria HUB](007-02-AUDITORIA-HUB-E-PROJETOS.md) documenta E-01/E-02/E-04/E-15/E-16/E-17/E-22: fontes independentes, pins e evidências de integração, desvio de runbook, ferramenta de revisão e checker especializado. Não inferir uso ou eficácia universal.

Preservar [arquitetura 03](007-03-ARQUITETURA-METODOLOGICA.md), [limpeza 04](007-04-LIMPEZA-OPERACIONAL.md), [continuidade 05](007-05-CHATS-E-CONTINUIDADE.md), [configuração 06](007-06-CONFIGURACAO-DE-PROJETOS-IA.md), [Knowledge 07](007-07-EVOLUCAO-DO-KNOWLEDGE.md), [NOM-001/08](007-08-DOCUMENTACAO-E-NOMENCLATURA.md), [autonomia 09](007-09-EFICIENCIA-E-AUTONOMIA.md), [Skills 09A](007-09A-ORBITA-SKILLS.md), [dependências entre projetos](../docs/10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md), [governança](../docs/05-GOVERNANCA-E-HOMOLOGACAO.md), [segurança](../docs/12-SEGURANCA-E-INTEGRIDADE.md) e [PROP-002](002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md). A árvore da baseline não contém diretório tools/. Nenhuma ferramenta se torna obrigação metodológica por estar registrada.

| Alternativa | Avaliação |
| --- | --- |
| Concentrar código e instaladores de todas as ferramentas no núcleo | Duplica propriedade, versões, responsabilidades e risco de exposição; rejeitada |
| Catálogo de links sem critérios | Baixa manutenção inicial, mas insuficiente para adoção segura e rastreável |
| Catálogo governado com referência à fonte e contrato de consumo, código independente | Recomendada; reuso controlado, direitos, versão, QA e responsabilidade explícitos |

O primeiro piloto será **documental**, em [tools/README.md](../tools/README.md), com um exemplo fictício de categoria de ferramenta de revisão de interfaces e um modelo adaptável de admissão. Código de ferramentas permanece nas fontes competentes, não no núcleo. Não criar instalador, gerenciador, automação de atualização, repositório externo ou cópia de ativos.

## 2. Arquitetura e classificação

| Capacidade | Responde à pergunta |
| --- | --- |
| Método / núcleo / HUB | Quais regras, etapas, papéis e limites se aplicam? |
| Skills | Qual técnica profissional convém ao problema? |
| Knowledge | Qual aprendizado comprovado é reutilizável nestas condições? |
| Tools | Qual instrumento pode executar ou apoiar a atividade autorizada? |
| Projeto | Qual requisito, ambiente, decisão e evidência são próprios do produto? |

Uma Tool pode ser software, script, biblioteca auxiliar, plugin, checker, CLI ou serviço externo com uso governado. O catálogo não é inventário de toda dependência transitiva nem marketplace. Ferramenta especializada pode ficar no método/HUB/projeto competente; só promover ao núcleo quando houver utilidade transversal, direitos e segurança. Ferramenta comercial pode ser referenciada mediante permissão aplicável; referência não concede licença. Tool não é agente, papel, Skill, conhecimento local ou gate.

Categorias candidatas por finalidade: revisão visual/UX; QA e validação; diagnóstico; documentação; automação de engenharia; segurança; infraestrutura/operações; dados/análise. Acrescentar apenas quando houver ficha útil. Usar nome humano e slug estável, identidade e versão na fonte; sem IDs artificiais ou pastas vazias. Separar catálogo público de registros privados; um índice organizacional restrito pode apontar para fonte real sem divulgar nomes, SHAs, contratos privados ou dados de clientes no núcleo público.

| Responsável | Competência |
| --- | --- |
| Titular / licenciante | Autorizar usos e distribuição conforme direitos demonstrados |
| Mantenedor da ferramenta | Código, versões, correções, dependências, documentação e suporte declarado |
| Curador do catálogo | Avaliar e manter ficha, classificar limitações, evidência e revisão |
| Responsável do projeto/método consumidor | Selecionar/autorizar adoção, compatibilidade, requisitos e versão adotada |
| Dono do ambiente/dados | Autorizar execução operacional, destino, acesso, dados, custos e recuperação |
| Agente | Pesquisar, comparar, recomendar, executar no escopo autorizado e demonstrar; não auto-homologar |

Permissão administrativa de repositório, autoria de commits, posse de cópia, publicação anterior ou licença de uma dependência não bastam para demonstrar todos os direitos de exploração, derivação ou redistribuição. Não concluir titularidade jurídica a partir desses sinais. Exigir evidência proporcional para o uso pretendido; se faltar, manter candidatura restrita e não copiar/distribuir código.

## 3. Admissão e manutenção

### 3.1 Ficha mínima

Usar [modelo de ficha](../tools/modelo-de-ficha.md) como referência adaptável, não formulário obrigatório para toda dependência. Campos essenciais: identidade, finalidade/tipo, fonte competente e acesso, proprietário/licenciante e mantenedor, escopo de direitos, versão/canal/revisão/artefato, requisitos e dependências, compatibilidade comprovada e lacunas, instalação/configuração/remoção, dados/permissões/rede/custo, testes/evidência, gate, manutenção e alternativas. Referenciar manual oficial sem duplicá-lo. Separar fonte viva de versão adotada e versão observada.

Rótulos editoriais (não novos estados normativos): **candidata** (em avaliação, não disponível para adoção automática), **admitida para escopo declarado** (critérios suficientes e aceite competente registrados), **restrita** (uso limitado por licença, acesso, ambiente ou lacuna), **retirada de consulta** (substituição ou fim de manutenção justificado, histórico preservado). Candidata restrita é possível. Admissão não homologa instalação, não instala, não aprova atualização, não define versão de consumidor. Uma ferramenta admitida pode ter versões candidatas ou obsoletas; não inferir que todas são adequadas.

### 3.2 Critérios de avaliação

| Critério | Evidência ou condição mínima |
| --- | --- |
| Utilidade e alternativas | Problema recorrente/pertinente, comparar ferramenta existente, opção direta e desenvolvimento próprio quando realmente viáveis |
| Origem e direitos | Fonte canônica, acesso, titular/licença/termos, componentes de terceiros; uso e redistribuição distinguidos |
| Versão e integridade | Revisão/canal/pacote aprovado, hashes ou assinatura quando aplicável; cadeia de origem identificável |
| Compatibilidade | Stack, SO, navegador, versão, formato/contrato, dependências e condições reais; não generalizar de um piloto |
| Segurança e dados | Permissões mínimas, entrada/saída, segredos, destino, rede, dados, exposição, atualização e vulnerabilidades; risco proporcional |
| Operação e recuperação | Procedimento existente, escopo de instalação, efeitos, reversão, preservação de dados, desativação e remoção |
| Qualidade | Testes pertinentes e evidências de limitações; não confundir QA da origem com QA do consumidor |
| Custo e manutenção | Custo real ou limite declarado, responsável, revisão por mudança/incidente, alternativas se descontinuada |

Todos os critérios relevantes devem estar satisfeitos **para o escopo de admissão pretendido**, com lacunas explícitas e decisão competente. Não impor auditoria integral de código ou SBOM formal em toda ferramenta simples; exigir inventário de dependências e direitos na extensão necessária. Se a ferramenta manipular dados sensíveis, executar código de terceiros, operar produção ou afetar segurança, elevar profundidade conforme 09 e docs 12. Se direitos, integridade, segurança ou autorização indispensáveis não estiverem demonstrados, bloquear a ação dependente; não aceitar risco por conveniência.

Reavaliar quando mudar versão, contrato, dependências, licença, titularidade, mantenedor, segurança, destino, custo ou evidência. Não obrigar atualização automática nem fixar calendário universal. Mantenedor pode anunciar correção; consumidor avalia impacto, gate e pin adotado. Vulnerabilidade crítica exige comunicação e contenção autorizada; não ignorar por estar pinado nem atualizar cegamente. Descontinuação: identificar consumidores/dependências, alternativas e plano de saída, preservar versão/evidência quando autorizadas, não excluir fonte/artefatos ou revogar acesso de terceiros automaticamente.

## 4. Seleção e decisão humana

1. Recuperar objetivo, tarefa autorizada, método escolhido, ambiente e restrições; consultar índice Tools e procedimento existente seletivamente.
2. Identificar ferramenta já adotada e válida. Evitar desenvolver substituta, atualizar ou instalar nova dependência sem necessidade. Conferir versão real e condições quando a tarefa depender delas.
3. Quando houver escolha relevante de instrumento, apresentar alternativas viáveis e condicionais (reutilizar, ferramenta existente distinta, abordagem manual/direta, criar nova somente se necessário). Comparar cobertura, compatibilidade, segurança, direitos, esforço, custo total, manutenção, evidência e dependências. Recomendar justificadamente; não inventar alternativas.
4. A seleção rotineira entre utilitários equivalentes já delegados é decisão técnica (09); **escolha de metodologia continua humana** (09A). Se a seleção da ferramenta definir metodologia, alterar arquitetura/contrato, custo, risco, acesso, licença, destino ou direção material, solicitar escolha/aceite do responsável competente antes da adoção. Respeitar decisão já registrada, sem microgate.
5. Registrar fonte, versão, autorização e limites no registro existente; referenciar a ficha e runbook. Usar COM-001 para intervenção real. Não confundir disponibilidade do conector/CLI com capacidade de acesso ou autorização.

## 5. Contrato de consumo e integração

O núcleo registra finalidade e condição de uso; a fonte da Tool detém o contrato do componente, e o projeto consumidor detém adaptação, ambiente, dependências e implantação. O [preflight operacional](002-PREFLIGHT-OPERACIONAL-E-DEPENDENCIAS-ENTRE-PROJETOS.md) e regras de segurança vigentes prevalecem.

### 5.1 Dimensões de versão e estado

| Dimensão | Prova |
| --- | --- |
| HEAD observado na origem | Referência Git naquele momento; não é versão aprovada |
| Versão/release aprovada na origem | Manifesto/tag/revisão e evidência do fornecedor, incluindo ressalvas |
| Artefato obtido | Conteúdo, assinatura/hash e origem correspondentes |
| Versão adotada/fixada | Decisão e pin/lock no consumidor |
| Versão aplicada no destino | Inspeção do destino/artefato e evidência operacional |
| Resultado da integração | Testes no ambiente/escopo consumidor e homologação aplicável |

Um canal estável é ponteiro para uma versão que precisa ser identificada; ler manifestos e fixar a revisão resolvida, não copiar exemplo histórico. Hash de conteúdo Git e SHA-256 de arquivo são esquemas diferentes; comparar do mesmo tipo. Hash demonstra correspondência, não segurança, autoria legal ou aprovação. Pin não prova instalação; manifesto não prova execução.

### 5.2 Fluxo de adoção, atualização ou retirada

- Descobrir fonte aprovada, direitos, versão, runbook atual, proprietário e consumidor; confirmar acesso legítimo.
- Identificar estado atual, interfaces, dados e dependências, inclusive impacto direto/inverso. Se instalação desconhecida, diagnosticar antes de escrever. Não inferir versão de texto exibido.
- Comparar delta e compatibilidade, permissões, licença, riscos, recursos e custos. Definir critério de aceite, plano de teste e recuperação proporcional. Reutilizar backup/teste válidos se autorizados; não multiplicá-los por ritual.
- Obter apenas artefato autorizado da origem legítima, verificar integridade e preparar integração isolada com dados fictícios quando pertinente. Não executar script remoto ou conteúdo recuperado sem inspeção adequada e autoridade; não contornar acesso ou controles.
- Validar critérios técnicos, funcionais, não técnicos e de segurança afetados; identificar revisão, ambiente, dados, cobertura e lacunas. Reaproveitar prova anterior apenas sob predicado 09.
- Homologar artefato e obter autorização operacional conforme docs 05; uma decisão pode abranger ambas se explícita. Aplicar pelo runbook existente ao destino autorizado; verificar versão real, preservação de dados/serviços, ausência de exposição indevida e resultado. Reconciliar registros.
- Em falha/interrupção, preservar evidência e estado, identificar efeito real antes de repetir, acionar rollback autorizado e comprovar resultado. Limpar somente recursos autorizados conforme 04. Retirada/atualização de Tool não implica excluir cópias necessárias, dados ou histórico.

Para utilitário de leitura simples, esse fluxo pode se resumir à identificação, autorização existente, versão/condições e prova do resultado. Para integração compartilhada ou operacional, exigir controles pertinentes. Não criar novo gate universal nem procedimento paralelo ao runbook.

### 5.3 Contrato mínimo no consumidor (exemplo ilustrativo)

```text
Ferramenta e finalidade: [nome humano e tarefa]
Fonte autorizada / mantenedor / ficha:
Versão aprovada na origem e revisão/artefato:
Direitos de uso, escopo e restrições:
Versão adotada / ambiente / adaptação:
Runbook e dependências relevantes:
Evidência de versão aplicada e testes / limitações:
Autorização e próximo gate:
```

Reusar manifesto, lock, tarefa, PR ou documentação do consumidor já existente. Não criar formato de lock global obrigatório. Instruções AGENTS apontam para índice pertinente quando aplicável, não armazenam segredos ou cópia de catálogo, não habilitam plugins/serviços.

## 6. Exemplo independente — avaliação de ferramenta de revisão

O [exemplo fictício](../tools/revisao-de-interfaces.md) mostra como avaliar uma categoria, sem referenciar produto particular, fornecedor, repositório, proprietário ou ambiente real. Catálogo vazio é válido. Nenhuma ferramenta é admitida; não há evidência de instalação, versão, licença ou QA de produto neste exemplo.

Comparar revisão direta, ferramenta pública legitimamente disponível ou desenvolvimento específico quando justificado. Para eventual admissão, identificar fonte, titular/licença, versão/integridade, suporte, compatibilidade, segurança, dados, custo, teste e autorização. Não importar informações ou ferramentas de outro projeto por associação de conta; aplicar ISO-001. Ferramentas particulares não pertencem ao núcleo, ainda que sob alias ou com acesso restrito. Preservar código, dados e decisões na fonte competente. O exemplo não autoriza distribuição ou execução.

## 7. Walkthroughs documentais

| Caso | Situação | Resolução esperada |
| --- | --- | --- |
| C01 — ferramenta existente | Projeto já usa utilitário compatível autorizado | Recuperar procedimento e versão; não recriar (§4) |
| C02 — alternativas | Nova escolha material entre duas ferramentas | Comparar e recomendar; decisão humana (§4) |
| C03 — utilitário delegado | Leitura/diagnóstico já autorizado e equivalente | Executar sem microgate (§4) |
| C04 — escolha metodológica | Ferramenta impõe nova metodologia | Aplicar 09A; humano escolhe (§4) |
| C05 — privado | Fonte inacessível sem autorização | Não copiar de outro consumidor nem contornar acesso (§5) |
| C06 — propriedade incerta | Repositório administrado pelo responsável, licença geral não demonstrada | Candidatura restrita; não redistribuir (§2) |
| C07 — terceiro | Ícones com licença permissiva, código próprio sem licença confirmada | Avaliar direitos separadamente (§3) |
| C08 — HEAD versus release | Main mudou depois do canal estável | Resolver versão aprovada; não instalar HEAD automaticamente (§5) |
| C09 — hash divergente | Pacote obtido não coincide com manifesto | Bloquear uso, recuperar origem legítima (§5) |
| C10 — pin | Lock aponta revisão sem prova de instalação | Verificar destino antes de declarar aplicada (§5) |
| C11 — QA de origem | Teste isolado aprovado em stack diferente | Validar compatibilidade consumidor (§5) |
| C12 — produção | Tool restrita a preview privado | Não publicar em produção (§6) |
| C13 — backend | Atualizar UI sem autorização de mudança SMTP | Preservar backend; gate independente (§6) |
| C14 — envio incerto | Operação externa sem resultado confirmado | Verificar recibo/estado antes de repetir; preservar notas (§5) |
| C15 — despesa | Serviço exige plano pago | Não contratar por inferência (§4) |
| C16 — vulnerabilidade | Dependência pinada recebe alerta relevante | Comunicar, avaliar impacto e correção autorizada (§3) |
| C17 — descontinuação | Tool sem manutenção, consumidores ativos | Planejar saída e preservar dados/refs; sem exclusão automática (§3) |
| C18 — produto independente | Projeto comercial referencia módulo homologado | Direitos e QA próprios; não presumir migração (§6) |
| C19 — registro público | Fonte privada com detalhes operacionais | Sanitizar e manter referência restrita competente (§2) |
| C20 — falta de necessidade | Tarefa simples sem benefício demonstrável de ferramenta | Usar abordagem direta, não instalar por catálogo (§4) |

20 cenários confrontados analiticamente; nenhum teste de execução ou medição de ganho.

## 8. Integração e continuidade

D-25 atendido documentalmente, não empiricamente. Etapa 10 integrará roteamento para Tools, direitos/versões/autoridade e contrato de consumo nas fontes competentes (docs 03/05/08/10/12, contrato, onboarding e templates pertinentes), sem duplicar runbooks, sem tornar ferramentas universais e preservando seleção de 09A. Etapa 11 poderá testar seleção, evidência, bloqueios e integração em caso autorizado com baseline 09; nenhuma ferramenta será implantada sem cumprir gates. Etapa 12 avaliará licença e publicação do núcleo separadamente dos direitos das ferramentas. Não alegar maturidade v1.0.

Critério de saída: índice navegável, modelo de ficha, exemplo fictício independente, matriz de admissão, versionamento e contrato de consumo, exemplo fictício independente, alternativas com recomendação e 20 walkthroughs, reconciliação README/ROADMAP/PROP-007. 11/14 etapas homologadas após aceite e integração de 09B. Nenhuma alteração normativa, Tool admitida, código copiado/publicado/migrado, repositório externo criado, consumidor alterado, credencial divulgada, execução/implantação ou exclusão. Sem varredura integral de segredos ou licenças. PRs #4/#5 e branches documentais preservadas; refs intencionais. Não criar Knowledge duplicado.

Gate: homologação humana e integração comprovadas, conferência pós-merge e reconciliação registradas no encerramento abaixo. Após encerramento comprovado e autorização específica, continuar neste mesmo chat com 10 — Integração metodológica: materializar as decisões candidatas 03–09B nas fontes normativas e templates existentes, reconciliar divergências, preservar cobertura semântica, autoria, estado e limites, elaborar matriz de rastreio e validar documentação. Não confundir versão candidata integrada com release/publicação ou piloto empírico; etapas 11/12 independentes. Não iniciar 10 nesta etapa.

## 9. Encerramento da etapa 09B

- Homologação humana registrada na [PR #47](https://github.com/jotaCorsino/orbita-development-model/pull/47#issuecomment-7196418806): “aprovado pode continuar”, em resposta direta ao pedido de homologação e integração. Aceite documental do catálogo, contrato de admissão e consumo e ficha ilustrativa (substituída na neutralização posterior), limitado à integração e ao encerramento de 09B.
- Entrega aprovada: `ccf57d8a299fc0d071d857c9f0ee71c06db2ec68`; merge squash confirmado: `5bed7334bfe0a531b2ed7dfc852dca95c6ba326d`. Árvore Git `4845bb184fd4e82ba80ba07ab139faab67fb9c65` idêntica à entrega aprovada; os sete arquivos relidos diretamente na main correspondem aos blobs verificados. Preservados os 20 walkthroughs, os critérios de admissão, o contrato de consumo, a seleção metodológica humana, a independência do código e as 14 etapas.
- Fechamento editorial isolado conforme TRB-004: README, ROADMAP, PROP-007, relatório e índice Tools reconciliados. Modelo de ficha preservado. O material particular da edição anterior foi retirado da árvore candidata por decisão posterior de neutralidade. Nenhuma ferramenta admitida, código transferido, uso novo autorizado, consumidor alterado, implantação ou teste operacional. Nenhuma autorização de distribuição particular foi concedida; nenhuma alteração normativa antecipada. Nenhum temporário local criado; PRs #4/#5 e branches documentais preservadas intencionalmente.
- Etapa 09B encerrada no escopo documental. Etapa 10 não iniciada; prosseguir neste mesmo chat somente após autorização específica. Conferir pós-merge da alteração editorial na respectiva PR, sem abrir novo ciclo apenas para registrar seu próprio SHA.
