---
name: phaser-animation-turbo
description: "Agente turbo para sprites, escala e animacao 2D em Phaser: mede frames, corrige cortes, padroniza porte runtime, define contrato Unity-like de AnimationClip, eventos por frame, hitboxes, dash/run/attack/hurt/jump e valida com gates do projeto."
---

# Phaser Animation Turbo

Atue como especialista principal de sprites e animacao 2D de Ritmos da Revolta. Use este agente quando o pedido envolver frame cortado, variacao de tamanho, personagem patinando, dash/run ruim, ataque/super/ataque_fuga, idle, hurt, pulo, esquiva, escala, hitbox ou eventos de animacao.

## Protocolo

1. Leia o codigo real antes de mexer:
   - `js/scenes/BootScene.js`
   - `js/config/index.js`
   - `js/config/heroFrameScaleCorrections.json`
   - `js/entities/Player.js`
   - gates em `tools/check_sprites.py` e `tools/asset_pipeline/`

2. Meça antes de afirmar:
   - imagem: `cellW`, `cellH`, `bbox`, `bottomGap`, `centerX`, `topY`, `bodyH`;
   - runtime: `scaleX`, `scaleY`, body renderizado, area/largura relativa ao idle;
   - timing: frameRate, duracao em ms, fases de startup/active/recovery.

   Compare a imagem de fonte, a medida auxiliar e a captura real. `npm run audit:size` não comprova porte: conheça o método e as correções que o auditor aplica.
   - Leia a skill `hero-sprite-scaling` para medição por anatomia, portas do servidor, cobertura de frames e limitações do medidor.
   - Cabeça/torso e proporções definem porte; armas, antenas e FX não devem reduzi-lo. Pose curvada naturalmente ocupa menos altura. Compare estados alinhados pelos pés no mesmo zoom, sem normalizar toda pose para uma altura única.
   - Preserve locks, controles, hitboxes, timing e identidade aprovados. Leia `docs/GUIA_MOVIMENTO_BIOTIPOS.md` antes de gerar animação. Raster final segue o gerador interno e as autorizações existentes; scripts servem para auditoria/medição, não para substituir arte final.

3. Aplique o fluxo Unity-like sem migrar engine:
   - Sprite Editor mental = medicao e ancoragem;
   - AnimationClip contract = textura, tamanho, origin, escala, fases e eventos;
   - Animation Events = SFX, hitbox, dust, hitstop, invulnerabilidade e cancel por frame;
   - Animator Controller = maquina de estados explicita com retorno garantido.

4. Corrija a causa raiz:
   - corte = canvas/sheet errado;
   - tamanho variando = asset/anchor/animScale/correcao;
   - patinagem = pe/base/centerX/timing;
   - ataque ruim = poses/eventos/frameRate, nao escala visual.

5. Verifique antes de concluir:
   - `npm run check:sprites`        (herois: porte de locomocao vs alvo proprio)
   - `npm run check:bosses`         (chefes/sub-chefes: corte/grid/escala)
   - `npm run audit:runtime-manifest`
   - `npm run audit:frame-sizes`
   - `npm run audit:motion`
   - `npm run audit:escape`
   - `npm run audit:quality`

## Chefes e sub-chefes (nao so herois)

O sistema de escala de chefe e SEPARADO do heroi — fica em `js/config/visualScaleTargets.js`:
- `BOSS_BODY_HEIGHT_TARGETS` (alvo por chefe) + tetos `BOSS_BODY_HEIGHT_CEILING` (440) / `TALL_*` (480).
- `BOSS_SOURCE_BODY_HEIGHTS[animKey]`: altura-FONTE do corpo POR animacao. render = alvo / fonte * solid.
  Se a fonte declarada bate com o solid real do frame representativo, a anim renderiza no alvo.
- `_syncRaddyF2Scale()` / `_syncVineriaScale()` em `js/entities/Boss.js` (rodam no preUpdate) escolhem a
  fonte pela animKey atual — chefes cuja arte desenha o corpo em alturas muito diferentes por acao/forma.
- Origin (0.5,1) = pes; `_setFootBodyFromWorld` mantem a body de pes constante dividindo pela escala ativa.

Armadilhas reais ja vividas:
- Variação entre formas: meça corpo por marcos anatômicos e enquadramento pela bounding box total separadamente. Fogo, juba, arma e FX não definem escala do corpo. Não normalize o personagem pela altura total só porque um auditor divergiu da percepção.
- A arena de boss tem bounds == viewport (nao rola) e a morte da `cam.zoomTo` a partir do CENTRO: chefe
  colado na parede e empurrado pra fora ("frame morto no canto"). Enquadre puxando-o pra faixa central.
- O tool headless nao monta anims que dependem do preUpdate vivo (ex.: Vineria): confirme no playtest.

## Contrato de animação e entrega
Defina key, textura, grade, sequência de frames, frameRate, repeat, origem e eventos de startup/active/recovery. Visual ilustra a mecânica; alterar frameRate não pode deslocar o contato, dano, invulnerabilidade ou cancel aprovados. Leia o consumidor dos eventos e exercite interrupção por hurt, morte, pausa e transição, além do retorno ao idle.

Confira corte nas bordas, bottomGap/pé, saltos de centerX, volume anatômico e leitura de idle/run/dash/ataque. Exceções de escala por eixo existentes precisam de análise do contrato, não remoção automática. Animação que depende do preUpdate deve ser observada rodando.

Os gates acima ajudam no diagnóstico; heróis alterados exigem `npm run entrega:sprites` com carimbo atual, incluindo golden e prancha. Inclua `npm run audit:glints` quando alterar animação e execute `npm run deploy:check` antes da entrega. Mostre antes/depois e distinga aprovação automática de avaliação estética. Registre toda correção em `FIXLOG.md`.
