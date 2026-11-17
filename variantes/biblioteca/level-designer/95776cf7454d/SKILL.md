---
name: level-designer
description: "Criar e revisar fases, arenas e ondas de beat-em-up ou platformer, com aprendizado, ritmo, legibilidade e progressão sem softlock. Preserve o formato de conteúdo e o moveset existentes; Tiled só quando usado pelo projeto."
---

# Level Designer — espaço e encontros jogáveis

Aplique `AGENTS.md`. Leia o moveset, câmera, área caminhável, dados de fase e gatilhos reais antes de desenhar desafios. Neste projeto, investigue `js/managers/WaveManager.js` e o caminho de progressão em `js/scenes/StageScene.js`; siga os imports até a fonte dos dados.

## Escolher pelo gênero
- Beat-em-up: trabalhe lanes X/Y, profundidade útil, posição de spawn, limites da câmera, gate de ondas e transição para arena. Combine funções de inimigos sem bloquear todas as saídas ou esconder telegraphs atrás do HUD.
- Platformer: dimensione alcance e altura pelo controlador real, pontos de aterrissagem visíveis, recuperação, hazards e checkpoints. Use Tiled e nomes de camadas somente se o carregador já os consome.
- Reutilize o formato existente. Um encontro melhor não exige introduzir editor, tilemap, rotas alternativas ou mecânica nova.

## Construção
Defina o objetivo do trecho, o que ensina, a pressão, o respiro e a condição de liberação. Ensine uma mecânica em condição segura, pratique e combine sob pressão. Use landmarks e contraste para orientar; segredos precisam de pista e só entram quando cabem no escopo.

Para cada encontro, anote composição, posições válidas, gatilho de início/fim, comportamento na derrota/reinício e relação com o encontro seguinte. Encaminhe IA, hitbox e gates de ataque para `beatemup-combat-designer`; valores de HP/dano para `balance-tuner`. Ajustar layout não autoriza alterar controles ou porte dos personagens.

## Verificação
Jogue do encontro anterior até o seguinte na mesma instância. Verifique inimigo fora dos limites, inimigo morto ainda contado, último spawn inacessível, saída bloqueada, câmera prendendo o jogador e retomada por checkpoint/save. Morte, pausa e reinício não podem duplicar ondas ou liberar progressão cedo.

Use `npm run test:encounters` quando aplicável e confirme quais situações cobre; complete com reprodução real e capturas. Cenário modificado exige `npm run audit:cenario`; antes da entrega, `npm run deploy:check`. Para revisão global, registre fase1 a fase7 individualmente. Entregue arquivos reais, intenção de cada trecho, evidência de progressão e observações de playtest no `FIXLOG.md`. Simulação mental não comprova ausência de softlock nem diversão.
