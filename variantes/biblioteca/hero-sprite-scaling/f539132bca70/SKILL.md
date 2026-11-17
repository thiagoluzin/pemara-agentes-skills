---
name: hero-sprite-scaling
description: "Medir e corrigir porte e proporção de heróis Phaser usando runtime e marcos anatômicos. Use para idle menor, ataque que cresce, distorção ou comparação entre heróis, preservando poses, locks e contratos de combate."
---

# Hero Sprite Scaling — porte por anatomia

Aplique `AGENTS.md` e o spec `phaser-animation-turbo`. Leia os locks e decisões aprovadas antes de qualquer mutação. A altura ocupada pela pose não define o tamanho do personagem.

## Medir antes de normalizar
Compare idle, locomoção, ataque, pulo, hurt e morte alinhados pelos pés, no mesmo zoom/resolução. Registre textura/frame, origem, escala efetiva, chão e marcos de cabeça/torso. Separe corpo de arma, antenas, cabelo e efeitos. Cabeça também muda com perspectiva: confirme landmarks por pose e inspecione a imagem.

Não fixe todas as poses na mesma altura: isso amplia agachamento e encolhe extensão. Preserve o modelo aprovado; variação de body não demonstra erro de porte. Bounding box total serve para detectar corte/enquadramento, não para normalizar anatomia. Exceções de escala horizontal existentes precisam ser lidas e avaliadas antes de zeradas.

## Fonte real e ferramenta
- `js/config/index.js`: configuração e `hitbox.animScales`; siga imports se a fonte tiver mudado.
- `js/config/heroFrameScaleCorrections.json`: correções uniformes, por eixo e horizontais; confira como `js/entities/Player.js` as aplica.
- `tools/check_sprites.py`: alvos e tolerâncias atuais; não copie medidas históricas como metas.
- `tools/measure_hero_runtime_scale.cjs`: inspecione argumentos e método antes de executar. Com servidor de `npm run serve` na porta 5173, use `npm run measure:hero -- <hero> 5173`; a porta padrão do medidor pode ser diferente.
- Simon usa landmarks vinculados a hashes em `tools/asset_pipeline/simon_anatomy.json`; outros heróis podem usar medida legada de corpo. Informe qual método foi usado.

O medidor contém caminhos de inicialização forçada/fallback; sua saída não comprova o carregamento normal. Não copie esses fallbacks nem ignore erros em novo teste. Conte frames medidos versus esperados, registre console/page errors e confirme seleção/carregamento pelo fluxo real. Frame ausente é lacuna, nunca medição zero nem aprovação. `audit:size` é evidência auxiliar com limitações, não uma prova visual.

## Corrigir a causa
Distinga arte de fonte, grid/corte, origem, chave de animação, configuração e pose intencional. Preserve hitboxes, alcance, velocidade, timing e identidade aprovados. Corrija a fonte responsável; não empilhe compensações para fazer um auditor ficar verde. Mudanças de arte seguem autorização/locks e gerador interno, sem raster final por Python.

Se houver mudança autorizada do porte global, confira todas as ações, incluindo chaves com dígitos como attack_1, e a relação com chão, HUD e inimigos. Atualizar alvos de auditoria exige justificar a nova medida; não afrouxe o gate para aceitar defeito.

Chefes usam `js/config/visualScaleTargets.js` e `js/entities/Boss.js`, com configurações próprias. Confirme alvos/tetos atuais e formas no preUpdate vivo; não derive o corpo do chefe de armas/FX nem imponha alturas históricas.

## Saída
Heróis alterados: `npm run entrega:sprites` com carimbo e evidência atuais; antes de entrega, `npm run deploy:check`. Mostre comparação de poses e frames críticos, medidas, cobertura e limitações. Registre no `FIXLOG.md`. Gate automatizado e aprovação estética são resultados distintos.
