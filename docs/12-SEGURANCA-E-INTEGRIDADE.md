# 12 — Segurança e integridade do projeto

## Objetivo

No Método ÓRBITA, segurança não é uma revisão opcional realizada apenas quando o software está pronto.

> **Segurança é uma restrição transversal presente no planejamento, implementação, evidência e homologação.**

O nível de profundidade deve ser proporcional ao risco do projeto. Um protótipo local, um site institucional e um sistema empresarial com autenticação e dados pessoais não exigem os mesmos controles.

O objetivo deste documento é estabelecer um **baseline mínimo de preocupação**, sem substituir análise especializada, normas internas, compliance, threat modeling formal ou revisão profissional quando necessários.

---

## 1. Responsabilidade compartilhada

### Responsável humano

Decide:

- nível de risco aceitável;
- dados e ambientes que podem ser utilizados;
- visibilidade pública ou privada;
- exceções relevantes;
- necessidade de revisão especializada;
- homologação final.

### Agente de planejamento

Deve:

- identificar superfícies sensíveis antes da implementação;
- registrar requisitos de segurança relevantes;
- incluir critérios de aceite e validações compatíveis com o risco;
- considerar privacidade, exposição pública, autenticação, autorização, dados e dependências;
- transformar riscos descobertos em tarefas ou decisões rastreáveis.

### Agente de implementação

Deve:

- implementar com defaults seguros;
- não introduzir segredos ou dados sensíveis no repositório;
- validar entradas e fronteiras de confiança quando aplicável;
- preservar autenticação e autorização;
- aplicar menor privilégio;
- evitar exposição excessiva em erros e logs;
- revisar dependências e configurações relevantes;
- executar testes e verificações de segurança proporcionais à mudança;
- relatar riscos encontrados.

O agente de implementação não deve interpretar "não foi pedido" como autorização para ignorar um risco de segurança relevante.

Também não deve expandir silenciosamente o escopo para corrigir qualquer problema encontrado. Deve **registrar, evidenciar e elevar o risco** para decisão humana, salvo correções inseparáveis da própria tarefa autorizada.

---

## 2. Segurança do software

Durante planejamento e implementação, avaliar quando aplicável:

- validação de entradas;
- codificação/escape de saídas;
- autenticação;
- autorização e controle de acesso;
- gestão de sessão;
- princípio do menor privilégio;
- tratamento seguro de erros;
- logs sem dados sensíveis;
- uso seguro de arquivos e caminhos;
- consultas parametrizadas e acesso seguro a banco;
- chamadas externas e integrações;
- uploads e downloads;
- execução de comandos;
- configurações de rede;
- proteção de endpoints administrativos;
- criptografia utilizando bibliotecas e padrões estabelecidos;
- atualização e procedência de dependências.

Esta lista não é exaustiva. O agente deve raciocinar sobre os riscos específicos da arquitetura e da tarefa.

---

## 3. Segurança da informação

Informações sensíveis devem ser minimizadas.

Não versionar deliberadamente:

- senhas;
- tokens;
- API keys;
- chaves privadas;
- credenciais de banco;
- arquivos `.env` reais;
- certificados privados;
- dumps ou bancos de produção;
- backups com dados reais;
- dados pessoais desnecessários;
- dados de clientes;
- informações operacionais internas sem necessidade.

Quando possível, usar:

- placeholders;
- variáveis de ambiente;
- secret managers;
- arquivos de exemplo;
- dados fictícios;
- ambientes de teste;
- exemplos sanitizados.

Se um segredo real for encontrado versionado ou exposto, o agente deve **parar a ação relacionada, reportar claramente e recomendar revogação/rotação**, além da correção no repositório. Remover o texto do arquivo atual não garante que o segredo tenha desaparecido do histórico.

---

## 4. Git e GitHub

O repositório também é parte da superfície de segurança.

Boas práticas esperadas, quando aplicáveis:

- `.gitignore` compatível com a tecnologia;
- não versionar segredos, builds locais, bancos, dumps ou artefatos sensíveis;
- revisar arquivos staged/diff antes do commit;
- commits pequenos e coerentes;
- branches específicas para mudanças relevantes;
- Pull Requests revisáveis;
- evitar force push, reset destrutivo ou reescrita de histórico sem autorização;
- proteger a branch principal conforme a criticidade;
- restringir permissões de repositório ao necessário;
- revisar exposição antes de tornar um repositório público;
- habilitar recursos de análise de dependências/segredos quando disponíveis e apropriados;
- manter dependências e workflows de CI sob revisão.

Um repositório público deve conter apenas o que é aceitável expor publicamente.

Projetos operacionais podem permanecer privados e produzir cases públicos sanitizados separados.

---

## 5. Testes e segurança

Testes já são parte fundamental do ÓRBITA.

Para segurança, o princípio é:

> **quanto maior o risco, mais explícita deve ser a validação de segurança.**

Além dos testes funcionais normais, considerar conforme o projeto:

- testes negativos;
- entradas inválidas e limites;
- tentativas de acesso não autorizado;
- diferenças entre perfis/permissões;
- regressão de controles de segurança;
- comportamento de erros;
- manipulação de dados sensíveis;
- integração com serviços externos;
- dependências e configurações relevantes.

Testes automatizados são evidência importante, mas **não provam ausência de vulnerabilidades**.

Por isso, segurança também pode exigir revisão de código, inspeção de configuração, análise de dependências, ferramentas automatizadas, testes manuais ou revisão especializada.

---

## 6. Evidências de segurança

Conforme o risco da tarefa, uma entrega pode precisar informar:

- riscos considerados;
- controles alterados;
- testes de segurança executados;
- cenários negativos testados;
- resultado de análise de dependências;
- resultado de análise de segredos;
- alterações em autenticação/autorização;
- mudanças de permissões;
- dados sensíveis utilizados;
- limitações conhecidas;
- riscos ainda não tratados.

"Não encontrei problemas" só é útil quando acompanhado de **como a verificação foi feita**.

---

## 7. Gate de segurança

Uma tarefa não deve ser homologada apenas porque:

- compilou;
- passou nos testes funcionais;
- funcionou no ambiente do agente.

Antes da homologação, riscos de segurança relevantes para o escopo devem estar:

- tratados;
- aceitos conscientemente pelo responsável humano;
- ou registrados como pendência com impacto conhecido.

Um risco crítico descoberto durante a tarefa deve ser comunicado imediatamente e pode justificar interromper o avanço até decisão humana.

---

## 8. Publicação e portfólio

Antes de publicar código, documentação, logs, screenshots ou exemplos:

1. revisar segredos;
2. revisar dados pessoais e de clientes;
3. revisar URLs e infraestrutura;
4. revisar IDs e nomes internos;
5. revisar caminhos de servidor;
6. revisar configurações e permissões;
7. avaliar se o projeto operacional deveria permanecer privado.

A demonstração pública de competência não exige exposição do ambiente real.

---

## 9. Regra para agentes

O comportamento esperado pode ser resumido assim:

```text
antes de implementar
    ↓
identificar riscos relevantes
    ↓
implementar com defaults seguros
    ↓
testar funcionalidade + controles sensíveis
    ↓
revisar exposição, dependências e Git
    ↓
evidenciar riscos e validações
    ↓
homologação humana
```

Segurança deve acompanhar o ciclo:

> **Planejar com segurança → Executar com segurança → Evidenciar segurança → Homologar conscientemente.**
