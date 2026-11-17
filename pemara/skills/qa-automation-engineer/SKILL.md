---
name: qa-automation-engineer
description: "Automação de testes ponta a ponta. Comece por um fluxo completo relevante ao usuário e defina a condição observável de sucesso."
---

# Automação de testes ponta a ponta

Comece por um fluxo completo relevante ao usuário e defina a condição observável de sucesso. Utilize um ambiente de testes, identidades fictícias e dados que a suíte consiga criar e remover.

Escolha seletores por papel ou contrato acessível. Espere eventos observáveis em vez de atrasos fixos. Em falhas intermitentes, preserve traços da navegação e compare o primeiro evento divergente.

Separe a suíte rápida de smoke das regressões mais longas da CI. Para funções ou contratos isolados, encaminhe a [test-engineer](../test-engineer/SKILL.md).
