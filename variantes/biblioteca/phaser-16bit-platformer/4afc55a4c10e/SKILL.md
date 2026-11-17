---
name: phaser-16bit-platformer
description: "Battle-tested, copy-ready recipes for 16-bit-style platformers in Phaser 3 — pixel-perfect boot config, framerate-independent loop, full game-feel player controller (coyote/buffer/variable-jump/asymmetric gravity), Tiled tilemap + one-way platforms, pooled projectiles, parallax, save system, and a 60fps checklist. Pair with the phaser-platformer-architect agent. Verify the installed Phaser version before applying — these are Phaser 3 patterns."
---

# Plataforma 16-bit em Phaser

Use a versão e a configuração física do jogo. Para o controle principal, defina quais estados recebem entrada, quando começa um salto e em que momento o herói volta a aceitar outro. Meça tolerância à borda, comando antecipado e altura variável em tempo de jogo para que respondam de forma previsível em taxas de quadros diferentes.

Valide a colisão com piso, paredes e plataformas unidirecionais em ascensão e queda, inclusive em velocidade máxima. Confira a câmera em diferentes tamanhos de tela, com escala inteira quando o estilo pixel art exigir. Teste o retorno pelo checkpoint, a reinicialização de estados e a reutilização de projéteis nos mapas que o projeto suporta.

A implementação pode seguir a [skill de plataforma do kit Phaser](../../../../kits/phaser/skills/phaser-platformer/SKILL.md). A direção de nível define legibilidade e ritmo; a revisão em gameplay confirma o controle.
