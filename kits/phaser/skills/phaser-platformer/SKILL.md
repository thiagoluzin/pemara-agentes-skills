---
name: phaser-platformer
description: "Implementar e afinar salto, movimento, tilemaps, plataformas de mão única e câmera de platformers Phaser, preservando o design de controle escolhido."
---

# Controlador platformer Phaser

Leia o controlador e o backend físico reais. Escolha Arcade ou Matter pelas colisões necessárias, preservando a engine existente. Confira as APIs da versão instalada; fixedStep reduz dependência do render, mas sozinho não garante determinismo de input, RNG ou ordem de eventos.

Defina unidades: velocidade em pixels/segundo, aceleração em pixels/segundo² e janelas em milissegundos. Não misture delta em segundos com timers em ms. Para picos de delta, escolha pausa, passos limitados ou descarte de tempo conscientemente; clamping indiscriminado pode dessincronizar movimento e cronômetros.

Coyote time, buffer, aceleração, corte de salto e gravidade assimétrica são opções de design. Preserve o controle deliberadamente rígido quando solicitado. Buffer é consumido uma vez; não rearme coyote a partir de contato ainda verdadeiro no frame imediatamente após saltar. Corte de velocidade acontece na borda de soltura ou uma única vez por salto, nunca repetidamente em cada update enquanto o botão está solto.

O [exemplo de janela de salto](scripts/jump-window.mjs) separa essas decisões da física. Precisa de grounded confiável e jumpPressed por borda. É uma referência testada de lógica; não substitui um controlador nem certifica colisão.

Em plataformas de mão única, compare pés anteriores e atuais no espaço do mundo, velocidade relativa e transformação da layer. Teste plataformas móveis, layer deslocada/escalada, alta velocidade, subida por baixo e descida intencional. Um teste com pixelY sem transformação e margem fixa não resolve todos esses casos.

Confirme nomes de tileset, layer e propriedades no carregador; valide camadas ausentes antes de consumir objetos. Dimensione obstáculos pelo alcance medido, com espaço de aterrissagem e recuperação visível.

Para pixel art, nearest e arredondamento de render não exigem arredondar a física. Scale.FIT preserva proporção, mas não assegura escala inteira no CSS/DPR. Observe o canvas no alvo com câmera em movimento.

Exercite salto curto/longo, borda, buffer ao aterrissar, teto, parede, plataforma fina, respawn e perda de foco em taxas de render diferentes. Registre alcance e sensações como evidências distintas.
