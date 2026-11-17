---
name: phase-art-music-review
description: "Revisar e melhorar a APARENCIA das fases e o casamento entre trilha e jogo em Ritmos da Revolta: capturar gameplay real por fase, diagnosticar profundidade/valor/matiz do fundo, medir BPM real x tabela do jogo, offset da primeira batida, true peak das musicas, e aplicar FX de chao/primeiro plano. Use quando o pedido falar em deixar o jogo mais bonito, analisar background, fase feia/escura/chapada, ritmo fora da musica, batida, BPM, clipping, headroom, letreiro de fase, profundidade, parallax ou primeiro plano."
---

# Skill: Revisão de arte de fase e trilha (Ritmos da Revolta)

> Origem: varredura 2026-07-29 (fases 1-7 + 13 faixas). Antes dela, "deixar mais bonito"
> era chute: ninguém olhava o jogo rodando e ninguém tinha medido a trilha.

## REGRA DE OURO — olhe o jogo rodando, meça a faixa tocando
Arte não se julga pelo PNG do asset (o jogo compõe 4 camadas, FX, vinheta, grade e HUD por
cima), e trilha não se julga de ouvido. **Capture o frame real e meça o arquivo real.**
Ferramentas prontas — não reescreva:

```bash
npm run serve                                    # noutro terminal
node tools/capture_phase_art_review.cjs 1,2,3    # frames reais; 7 liga ?fase7=1 sozinho
py -3 tools/asset_pipeline/audit_music_true_peak.py        # --fix aplica ganho
```

O capturador espera `_stageReady` + cena povoada e **oculta o letreiro (depth >= 2900) só na
foto** — sem isso você fotografa a tela coberta e conclui besteira.

## A Fase 7 está fora do escopo da demo
`DEMO_SCOPE.maxPhase = 6` é regra de PRODUTO e é travada por `test:demo-scope`. Para
inspecionar a Fase 7 use a flag `?fase7=1`, que move só `assetMaxPhase()` (carregamento /
animação / FX). **Nunca mexa em `DEMO_MAX_PHASE` para "ver a fase 7".**

## Diagnóstico de fundo — o que realmente estava errado
Cheque nesta ordem; os quatro primeiros valem para TODAS as fases:

1. **Emenda fundo↔chão reta.** Corte horizontal perfeito achata a profundidade (lê como
   duas faixas coladas). → `_phaseFxGroundSeam` (ancora em `floorTopY`, que sai da ARTE via
   `background_config.json`; nunca um Y chutado).
2. **Terço inferior morto.** Faixa jogável em textura chapada. → `_phaseFxFloorDust`.
3. **Separação de VALOR entre planos.** Se a faixa média e o chão têm o mesmo valor, colam
   (era o caso da fase 3, quase preta). → seam extra em `SCREEN` levantando o pé do fundo.
4. **Contraste de MATIZ.** Fase monocromática vira massa única (fase 4, toda marrom). →
   injete o complementar da paleta (ciano contra marrom/laranja), alpha baixo.
5. **Primeiro plano ausente.** Nenhuma camada passa NA FRENTE do jogador, então a cena
   inteira acontece "atrás de um vidro". → `_phaseFxForegroundDrift` (versão sem arte) ou
   uma layer 0 desenhada (mais forte, custa arte).

Régua de qualidade do elenco de fases: **a fase 5** (paleta complementar + acentos
emissivos + três planos legíveis). A fase 7 é a de identidade mais forte e a mais carente
de acento emissivo.

### Não repita o que já foi decidido
- **Lights2D foi testado e REPROVADO** pelo usuário (`StageScene._enableLights`, atrás de
  `?lights=1`): a arte já é pintada com luz embutida, e luz dinâmica por cima escurece.
- Glow de Filter em GPU real é assunto sensível (`?glow=1`); não ligue por padrão.
- O mira emissivo já cobre glow guiado pela arte (`mira_emissive.json`). Complemente, não
  duplique.

### Armadilhas de FX medidas na prática
- **Massa escura sobre fundo escuro é invisível.** Numa fábrica o que se vê é o VAPOR
  claro pegando a luz, não a fuligem.
- **Primeiro plano precisa de duas passadas**: massa clara média (atmosfera) + massa grande
  ESCURA e bem mais rápida (é essa que o olho lê como "entre a câmera e a ação").
- Depth do primeiro plano: **acima do jogador** (`setDepth(this.y)`, até `floorBottomY`) e
  **abaixo da HUD** (2000). 1200 é seguro.
- Partícula que nasce e morre fora de quadro **não precisa de curva de alpha** — alpha
  constante, sem custo por frame.
- Scrim de letreiro: gradiente radial (`fx_glow` tingido de preto), não retângulo chapado.
  Espalhar demais a altura enfraquece o NÚCLEO e a tagline some em fundo movimentado.

## Trilha — o que medir e onde
### BPM: a tabela do jogo mentia
`GAME_BALANCE.combat2.phaseBpm` alimenta `CombatRhythmSystem`, o `_onBeatSpark` e o pulso
do retrato na HUD. Meça sempre; não confie na tabela.

- Meça por **dois métodos** (`librosa.beat.beat_track` + tempograma) e refine pela média dos
  intervalos entre batidas. Faixas de DAW caem em valores redondos (140/120/150/135) — se o
  seu número é redondo, provavelmente está certo.
- O extrator erra oitava (metade/dobro): compare candidatos antes de aceitar.
- **BPM certo não basta.** Nenhuma faixa começa em cima da 1ª batida: sem `beatOffsetMs` o
  desalinho fica em 78-161 ms, acima da janela de 72 ms. Ache o offset varrendo o período
  em 1 ms e minimizando o desalinho circular.
- **Ancore no relógio do áudio**, não em `scene.time.now`: `AudioManager.getMusicPosition()`
  usa o `AudioContext.currentTime`, imune a decode/gate/crossfade.
- **Chefe tem andamento próprio** → `bossBpm` / `bossBeatOffsetMs` (fase 4: fase 150, chefe 172,3).
- **Limite conhecido:** fases 3, 6, 7 e boss 4, 5 têm andamento VARIÁVEL; nenhuma grade de
  BPM constante as representa (p95 de 104 a 261 ms no melhor ajuste). Só um beat map resolve.

Alvo de qualidade: desalinho médio < 40 ms e p95 dentro de `perfectBeatWindowMs`.

### Loudness: meça na CAMADA CERTA
21 das 26 faixas de runtime passam de −1 dBTP e a pior chega a +4 dBTP. **Isso não quer
dizer que o jogo clipa.** O caminho de saída é
`musicVolume (0,75) × track.volume (0,7) × _intensityMult (até 1,18)` ≈ −4,15 dB — no volume
padrão a pior faixa sai a −0,12 dBTP. Clipa só acima do padrão.

- Rebaixar master é o conserto ERRADO: degrada arquivo (MP3 seria reencodado duas vezes) e
  muda o equilíbrio com os SFX.
- O certo é o **limiter no barramento de música** (`AudioManager._ensureMusicLimiter`),
  que protege todas as faixas e as futuras. Guarde contra contexto sem
  `createDynamicsCompressor` (os contratos usam stub).
- Pico de amostra NÃO vê inter-sample peak. Use reamostragem polifásica em blocos; FFT da
  faixa inteira mede certo mas leva minutos e não serve para gate.

## Medição de performance é só A/B
Os números do profiler saem de SwiftShader (software) e a máquina varia 2x entre execuções.
**Nunca compare com um número de outra sessão.** Ligue/desligue o efeito e meça em seguida,
na mesma sessão. Se o "sem o efeito" sair mais lento que o "com", o custo está abaixo do
ruído — diga isso, não invente ganho.

## Checklist de saída
1. Frames reais capturados nas fases tocadas, antes e depois.
2. `ERROS: nenhum` no capturador (ele lê `pageerror`).
3. Gates conforme o que você tocou: `test:balance` (BPM vive em GAME_BALANCE),
   `test:performance`, `test:demo-scope`, `test:background-config`, `test:music-mode`.
4. Alinhamento de batida medido e reportado (médio/p95), incluindo as faixas que NÃO alinham.
5. Entrada no `FIXLOG.md` por correção.
