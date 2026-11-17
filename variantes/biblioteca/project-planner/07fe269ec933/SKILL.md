---
name: project-planner
description: "Planejar jogos e funcionalidades de jogo com escopo, arquivos responsáveis, dependências, marcos jogáveis e critérios verificáveis. Use para trabalho amplo; correções pequenas não precisam de plano separado."
---

# Project Planner — plano executável de jogo

## TURBO OPERATING PROTOCOL
Aplique `AGENTS.md`. Leia o pedido e decisões anteriores, plano pertinente já existente, specs necessários e comandos reais no `package.json`. Preserve alterações de outras tarefas. Um plano organiza a execução; não impõe aprovação adicional nem troca o modo da sessão.

## Enquadrar sem transformar o jogo em outro produto
Determine gênero, mecânica central, alvo/dispositivo, controles, recursos existentes e resultado solicitado. Android pode ser uma distribuição do mesmo jogo Phaser; não implica reescrever em framework mobile. Também não acrescente backend, contas, banco de dados ou rede sem necessidade do jogo.

Para escolher o especialista, leia o spec `game-build-flow` disponível no roteador. Use somente agentes ativos em `AGENTS.md`; uma referência a agente arquivado é uma dependência inválida. Corrigir um bug conhecido normalmente exige uma tarefa focada, não um novo roteiro de projeto.

## Plano proporcional
Se o usuário pediu análise, entregue análise. Se pediu somente plano, entregue plano. Se pediu construir ou corrigir, planeje o necessário e prossiga com o trabalho autorizado. Reutilize o plano existente; crie um arquivo com nome descritivo somente se a complexidade justificar acompanhamento persistente.

Cada tarefa deve ter:
- Resultado observável e motivo; exemplos: ataque atinge uma vez, pause retém estado, save recupera progresso.
- Responsável dentre os agentes ativos, arquivos sob sua responsabilidade e habilidades necessárias.
- Entrada → saída → verificação: estado inicial, artefato/comportamento final e procedimento que demonstra a mudança.
- Dependências reais, risco principal e forma de reverter apenas a própria alteração.

Ordene por núcleo jogável → encontro completo → conteúdo → apresentação integrada → medição → entrega. Respeite dependências; arte e áudio independentes podem avançar quando o contrato estiver definido. Delegação depende da autorização e ferramentas da sessão, nunca é pré-requisito para começar.

## Critérios de aceite de jogo
Defina antes de implementar, com detalhe proporcional à tarefa:
- **Jogabilidade:** ação central, feedback legível, colisão/dano, vitória/derrota e reinício demonstrados em runtime; diversão depende de playtest, não de uma declaração do agente.
- **Controles:** teclado, gamepad e/ou touch conforme o alvo, incluindo pausa, retomada, perda de foco e eventos efetivamente utilizados pelo jogador.
- **Conteúdo:** assets e chaves reais, contratos de animação, locks preservados e escopo explícito de fases; `fase1`–`fase7` quando pedido o jogo inteiro.
- **Ciclo de vida:** troca contínua de fases e retorno ao jogo sem áudio, listeners, timers, objetos ou overlays duplicados.
- **Desempenho:** dispositivo, cenário, metas e medições A/B comparáveis. Não transformar uma meta de FPS em resultado confirmado.
- **Entrega:** gates, arquivos produzidos e teste no destino quando houver pacote solicitado; limitações de acesso ao dispositivo devem aparecer como não verificadas.

## Verificação e encerramento
Escolha testes pelos arquivos e comportamento tocados, conferindo sua existência no `package.json`. Use `npm run audit:agent-pack` para alterações do pacote; `npm run entrega:sprites` para heróis; `npm run audit:cenario` para cenário; `npm run deploy:check` antes de build/entrega. Runtime precisa de prova em runtime, além de contratos estáticos.

Guarde resultado, código de saída e evidência de cada verificação. Não marque uma tarefa concluída por ter escrito instruções ou por ter iniciado um comando. Distinga aprovado, reprovado e não verificado; atualize o plano utilizado e faça append no `FIXLOG.md` para cada correção. Não empacote ou publique algo que não foi pedido.
