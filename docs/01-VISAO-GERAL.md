# 01 — Visão geral

## Definição

O **Método ÓRBITA** é um modelo prático de organização do desenvolvimento de software assistido por IA com governança humana.

Foi criado a partir de uma necessidade prática recorrente: aproveitar agentes de IA sem perder compreensão, rastreabilidade e autoridade humana sobre o processo de desenvolvimento.

## Problema que o método procura resolver

Agentes de IA reduzem o custo de produzir código, documentação e análises. Essa facilidade também pode incentivar alterações extensas sem planejamento suficiente, decisões não registradas, crescimento descontrolado de escopo e dificuldade para compreender por que determinada implementação existe.

O ÓRBITA introduz uma estrutura explícita para esse trabalho.

## Objetivo

O objetivo não é maximizar a quantidade de código gerado. É criar um processo em que:

- objetivos sejam compreendidos antes da implementação;
- mudanças sejam divididas em unidades controláveis;
- responsabilidades sejam claras;
- implementação gere evidências;
- decisões permaneçam rastreáveis;
- a aprovação final continue humana;
- o repositório represente o estado conhecido do projeto;
- o mesmo projeto mantenha identidade e contexto coerentes entre planejamento, implementação, pasta local e GitHub.

## Escopo

O modelo pode ser usado em projetos pessoais, acadêmicos, experimentais ou profissionais, desde que adaptado ao nível de risco e às políticas da organização.

O ÓRBITA não substitui requisitos de segurança, revisão especializada, compliance, QA, gestão de projetos ou processos formais quando estes forem necessários.

## Natureza do método

O ÓRBITA não é apresentado como padrão de mercado ou metodologia universal.

Ele é uma **sistematização pública de um modelo prático de trabalho**, construída a partir de experiência prática e destinada a continuar evoluindo.

## Organização do ambiente de projeto

O método também trata a organização do ambiente como parte da qualidade do processo.

Na configuração de referência, cada software possui, sempre que possível:

- um **contexto próprio no agente de planejamento** com o nome do projeto;
- um **contexto próprio no agente de implementação** com o mesmo nome;
- uma **pasta local no computador** com o mesmo nome, contendo a working copy Git;
- um **repositório GitHub correspondente**, também claramente associado ao projeto.

Essa organização cria uma relação um-para-um entre os contextos usados para pensar, implementar, executar localmente e registrar o projeto.

O GitHub permanece como fonte persistente da verdade. Os agentes de planejamento e implementação mantêm contextos de trabalho especializados, enquanto a pasta local materializa a working copy sincronizada com o remoto.

Ver [10 — Identidade e ambiente do projeto](10-IDENTIDADE-E-AMBIENTE-DO-PROJETO.md).
