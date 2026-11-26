# ORB-EVO-001 — 02: Avaliação da composição metodológica

**Estado:** etapa documental homologada e integrada. Esta edição substitui o inventário de fontes particulares por uma síntese autônoma de requisitos e riscos metodológicos. Os identificadores E-01 a E-22 abaixo servem somente para manter continuidade lógica com propostas posteriores; não identificam projeto, organização, repositório, fonte ou ocorrência recuperável. Não são dados de piloto nem comprovação empírica.

| Tema | Princípio ou risco a verificar |
| --- | --- |
| E-01 | Composição explícita de núcleo, HUB e métodos; autoridade por assunto, não por associação de conta. |
| E-02 | Distinguir versão da origem, artefato, pin, destino e prova de instalação. |
| E-03 | Limpeza deve ter alvo, autorização, proteção de dependências e pós-verificação. |
| E-04 | Recuperar procedimento aprovado antes de operar; resultado de comando não demonstra runtime. |
| E-05 | Código, dados persistidos, artefato, instalação e aceite são dimensões distintas. |
| E-06 | Reconciliar status de fontes derivadas sem reescrever histórico. |
| E-07 | Inspecionar trabalho ativo e refs; não presumir que main contenha a última decisão. |
| E-08 | Recuperar instruções da tarefa e gate vigente sem refazer etapas encerradas. |
| E-09 | Aceite com ressalva transfere condição explicitamente, não dispensa teste exigido. |
| E-10 | Preservar falha e evidência parcial; corrigir somente lacuna comprovada; não repetir mutações. |
| E-11 | Ensaiar migração e recuperação; não presumir rollback de operação não transacional. |
| E-12 | Distinguir backup histórico de snapshot atual; preservar dados e validar efeito de operações. |
| E-13 | Preservar trabalho e separar pós-check estrutural de QA funcional. |
| E-14 | Backup legível não é recuperação demonstrada. |
| E-15 | Validação técnica não substitui avaliação visual e critérios humanos. |
| E-16 | Metodologias profissionais devem ser selecionadas de acordo com necessidade e evidência. |
| E-17 | Critérios de qualidade precisam corresponder a contexto, domínio e artefato. |
| E-18 | Testes e avaliação especializada não podem ser inferidos de build aprovado. |
| E-19 | Preservar fontes, escopo e direitos sem transferir contexto particular. |
| E-20 | Checkpoint recuperável deve identificar estado local, remoto e última ação comprovada. |
| E-21 | Interrupção exige recuperação seletiva e preservação antes de repetir ação. |
| E-22 | Segurança, privacidade e separação de ambientes devem ser verificadas proporcionalmente. |

## Aplicação e limites

A composição do método é opcional e governada por assunto. Um projeto parte do zero e adota apenas fontes escolhidas pelo responsável. A validação pública utiliza cenários fictícios e independentes; resultados de projeto ficam no próprio projeto. Nenhuma organização, caso, ferramenta particular ou contexto de consumidor constitui referência do núcleo. Consulte [matriz de diagnóstico](007-01-AUDITORIA-INTEGRAL.md), [integração](007-10-INTEGRACAO-METODOLOGICA.md) e ISO-001 em docs 12. As etapas 03–10 materializaram os controles; validade prática ainda depende dos gates da iniciativa. Não atribuir ganhos causais ou maturidade com base neste registro.
