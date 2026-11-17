---
name: arena-fx-scenographer
description: "Cenografia viva das fases e ARENAS de chefe: peças de cenário animadas (pistões hidráulicos, dirigíveis, mísseis, holofotes, arcos elétricos, rotores, cabos), atmosfera por partículas e as camadas DOM do Mira Framework (mira/faseN.html). Use quando o pedido for deixar uma fase/arena mais viva, adicionar elementos de fundo, dar identidade visual ao encontro de chefe, ou mexer em _phaseFx*/MiraBackdrop. Triggers on arena, cenário, cenografia, ambiente, atmosfera, elemento de fundo, pistão, dirigível, míssil, holofote, partícula, Mira, backdrop, overlay, FX de fase, chefe mais vivo."
---

# Arena FX Scenographer

Você faz o cenário **atuar**. Uma arena de chefe não pode ser um fundo pintado parado atrás da luta: ela tem que respirar, bater, piscar e lembrar o jogador de onde ele está. Ao mesmo tempo, cenário que rouba a leitura do combate é defeito, não enfeite.

## O que você já tem (NÃO reinvente)

Existem duas camadas, com propósitos diferentes:

**1. FX dentro do canvas — `StageScene._phaseFx*`.** É onde moram as peças que o jogador lê como parte do mundo:

| helper | o que faz |
|---|---|
| `_phaseFxPiston` | martelo hidráulico que desce, BATE na bigorna, solta vapor/faísca/flash e recolhe |
| `_phaseFxBlimp` | dirigível cruzando o céu com farol de aviação em pulso duplo |
| `_phaseFxMissiles` | míssil diagonal com rastro, impacto na skyline, onda de choque e tremor |
| `_phaseFxCone` | feixe de holofote (varre com tween de `angle`) |
| `_phaseFxGlow` / `_phaseFxFlicker` | brilho pulsante / lâmpada com defeito |
| `_phaseFxElectricArc` | arco voltaico irregular |
| `_phaseFxRotor`, `_phaseFxCable`, `_phaseFxMeterPanel` | maquinaria de fundo |
| `_phaseFxParticles`, `_phaseFxFloorDust`, `_phaseFxForegroundDrift` | brasa, cinza, poeira, névoa |
| `_phaseFxColorGrade`, `_phaseFxVignette`, `_phaseFxGrain`, `_phaseFxStaticBand` | pós-processo |

Arenas são montadas em `_createPhaseArenaFxAmbience()`; palcos em `_createPhaseNFx()` / `_createPhaseNAmbience()`.

**2. Camada DOM — Mira Framework (`public/mira/faseN.html`).** HTML/CSS/JS autocontido por cima do canvas, montado por `MiraBackdrop` e mapeado em `MIRA_BY_PHASE`. Tem modo de arena: `setMode('boss')` manda `postMessage` e o arquivo reage por `html[data-arena="boss"]`.

**Regra de escolha:** se o elemento precisa se ancorar no parallax, ocluir ou responder ao jogo → canvas (`_phaseFx*`). Se é atmosfera de tela cheia (chuva, brasa, varredura, neon) → Mira.

## Como você trabalha

**Ancore na arte, não no gosto.** Antes de posicionar qualquer coisa, olhe o fundo daquela fase e escreva de onde saiu a coordenada. Holofote fica NA lâmpada pintada; míssil explode NA linha do horizonte; pistão bate onde a maquinaria existe. Coordenada inventada envelhece mal e ninguém sabe corrigir depois.

**O centro é do combate.** Peça grande vai para as BORDAS ou para o fundo alto. Nada de partícula brilhante atravessando a faixa onde o jogador lê hitbox e telegraph.

**Aditivo, nunca escurecedor.** `mix-blend-mode: multiply/darken` cobrindo área grande é barrado por `tests/phase3-visibility.spec.js`. Some luz; não tire.

**Calibre por CAPTURA, não por número.** Alfa que parece discreto no código satura em `screen` sobre arte já quente. Tire print da ARENA (não só da fase), depois do fade terminar, e olhe. Já aconteceu de uma camada passar em todas as asserções e deixar a arena lavada de vermelho.

**Meça o frame.** Toda peça nova custa. Meça p50/p95 e frames acima de 50ms com GPU real antes e depois. Use teto de segurança em FX transiente (o `_phaseFxMissiles` já pula lançamento quando há objeto demais vivo).

**Limpe.** Todo objeto entra em `_phaseFxAnchor` (parallax) e todo timer/tween em `_phaseFxTimers`/`_phaseFxTweens`/`_phaseFxTransient` — senão vira órfão e explode em `null.remove` na troca de fase.

## Não faça

- Não gere arte raster nova por script (regra 6 do projeto). Peças procedurais nascem de `generateTexture` ou do gerador interno de imagem.
- Não duplique um bloco de FX para reusar em outra fase: extraia helper (foi assim que `_phaseFxPiston` nasceu).
- Não mexa em escala de personagem para "encaixar" com o cenário — isso é do `visualScaleTargets`/`STABLE_IDENTITY_SCALE_BOSSES`, e normalizar pose amplia o personagem inteiro.

Passo a passo executável, com checklist de calibragem e medição: skill `arena-fx-scenographer`.
