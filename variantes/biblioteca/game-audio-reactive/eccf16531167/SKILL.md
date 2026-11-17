---
name: game-audio-reactive
description: "Implementar áudio reativo Phaser/Web Audio no gerenciador existente: ducking, intensidade, transições e desbloqueio por gesto, com limpeza de recursos. Use para som que responde ao gameplay sem alterar física ou timing de combate."
---

# Game Audio Reactive — integração e ciclo de vida

Aplique `AGENTS.md`. Leia `js/managers/AudioManager.js`, `js/config/audio.js` e os consumidores antes de adicionar nós ou listeners. O projeto já possui controle de música: não crie um segundo player independente na cena.

## Escolha pelo efeito
- Ducking: confira `duckMusic`, `duckMusicHold` e `unduckMusic` existentes e suas unidades. Preserve volumes de preferências e nós de intensidade separados. Eventos sobrepostos precisam restaurar o estado correto, não um volume constante copiado de exemplo.
- Transição: confira `crossfadeMusic`, `setMusicMode` e a resolução de pedidos assíncronos. Um decode antigo não pode vencer o pedido da nova fase; preserve o pedido mais recente e descarte recursos obsoletos.
- Stems: só adicione quando necessários e disponíveis. Duas chamadas consecutivas de play não garantem sincronismo; alinhe duração, loop e início pelo mesmo relógio de áudio.
- Variação: use rate/detune moderado quando fizer sentido para SFX. Confirme a semântica do backend: pitch pode mudar duração e deslocar contato. Não varie sinais musicais ou telegraphs por obrigação.
- Filtro: use roteamento compatível com o backend real, guarde a conexão anterior e limpe nós de sua propriedade. Não desconecte o master global indiscriminadamente.
- Silêncio: escolha pelo momento narrativo e restaure o estado em interrupção/skip; não imponha silêncio a toda fase.

## Fronteira com combate
Sincronize SFX ao evento de contato existente. Áudio não deve chamar pause/resume da física nem criar seu próprio hitstop: isso pode desfazer pausa, morte ou transição. Alteração de timing de impacto pertence ao contrato de combate e animação.

## Ciclo de vida e testes
Defina dono e descarte de cada source, gain, timer, tween e listener. Teste gesto inicial, contexto suspenso, opções/mute, pausa, perda de foco, troca de modo, derrota/reinício e avanço contínuo de fases com a mesma StageScene. Confira se fade/duck pendente afeta a música seguinte.

Use `npm run test:music-mode` e `npm run test:boss-music` conforme a mudança; confira a cobertura real. Ouça/capture a saída em contexto e meça clipping/headroom com `audio-analysis` quando necessário: o master isolado não representa a cadeia de ganho final. Sem escuta, não afirme mix aprovado. Antes de entrega, `npm run deploy:check`; correção registrada no `FIXLOG.md` com estados exercitados e limites.
