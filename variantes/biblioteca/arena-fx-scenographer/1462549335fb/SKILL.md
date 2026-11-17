---
name: arena-fx-scenographer
description: "Passo a passo para adicionar ou ajustar cenografia viva numa fase ou ARENA de chefe: escolher entre FX de canvas (_phaseFx*) e camada Mira (mira/faseN.html), ancorar na arte, calibrar por captura de tela e medir o custo em frame. Use ao deixar uma arena mais viva, colocar pistão/dirigível/míssil/holofote no fundo, criar uma camada Mira nova, ou investigar FX que sumiu, saturou a cor ou derrubou o fps."
---

# Arena FX Scenographer — execução

## 1. Antes de escrever qualquer coisa: olhe a fase

```bash
ls assets/backgrounds/fase<N>/
```

Rode a fase e tire uma captura da **arena** (não só do palco). O `devSkipToBoss: true` no `scene.start` leva direto ao chefe:

```js
game.scene.start('StageScene', { phase: 6, hero: 'oren', lives: 9, difficulty: 'normal',
                                 devSkipToBoss: true, save: { character: 'oren', currentPhase: 6 } });
```

Escreva, em uma linha, **de onde saiu cada coordenada** que você for usar ("holofote em 408,98 = lâmpada pintada no teto"). Sem isso ninguém corrige depois.

## 2. Escolha a camada

| pergunta | resposta |
|---|---|
| Precisa acompanhar o parallax ou ser ocluído pela arte? | canvas: `_phaseFx*` |
| Precisa reagir ao jogo (batida, impacto, tremor)? | canvas |
| É atmosfera de tela cheia (brasa, chuva, varredura, neon)? | Mira (`public/mira/faseN.html`) |

## 3. Canvas — onde mexer

- Arena: `StageScene._createPhaseArenaFxAmbience()`, ramo `this.phase === N`.
- Palco: `_createPhaseNFx()` / `_createPhaseNAmbience()`.

Reuse os helpers (lista completa no spec do agente). Exemplos reais:

```js
// dirigível cruzando atrás das janelas + míssil caindo na skyline
this._phaseFxBlimp({ y0: 150, speed: 13, amplitude: 7, depth: -26, scale: 1.25, phase: 0 });
this._phaseFxMissiles({ depth: -25.8, skyMinY: 60, skyMaxY: 150, impactMinY: 300, impactMaxY: 400 });

// martelo hidráulico nas laterais (centro fica livre para o combate)
this._phaseFxPiston({ x: 232, anvilY: 545, scale: 1.05, layer: 0, delay: 900, depthBase: -19.9 });
```

`depthBase`/`depth` mudam entre palco e arena: o palco tem parallax em camadas (-27.x fica atrás da maquinaria do layer3), a arena não. Confira contra o que já existe no ramo daquela fase.

**Registre tudo:** objeto em `_phaseFxAnchor`, timer em `_phaseFxTimers`, tween em `_phaseFxTweens`, transiente em `_phaseFxTransient`. Tween infinito precisa de `.stop()` antes do `destroy()`.

## 4. Mira — camada nova

Copie a estrutura de `public/mira/fase4.html` (a mais simples) ou `fase5.html` (a mais completa, com modo de arena). Obrigatório:

- `<html data-arena="stage">` e regras `html[data-arena="boss"] .x { … }` para o modo arena;
- listener de `message` com `event.data.type === 'mira-mode'`;
- `background: transparent`, tudo em `mix-blend-mode: screen`;
- registrar no `MIRA_BY_PHASE` do `StageScene._mountMiraBackdrop()`.

**Comece com metade do alfa que você acha certo.** Sobre arte quente, `screen` satura rápido.

## 5. Calibrar — por captura, não por número

Tire print **da arena, depois do fade**, e compare com o print de antes. Perguntas:

- A cor da arte ainda lê, ou virou um banho de uma cor só?
- Dá para ver o personagem, a hitbox e o telegraph do chefe?
- O elemento parece parte do mundo ou colado por cima?

Audite as camadas proibidas (mesmo contrato de `tests/phase3-visibility.spec.js`): nenhuma com `multiply`/`darken` cobrindo mais de 25% da tela.

## 6. Medir o frame — obrigatório

GPU real (headless mede errado). Meça 12s na arena, antes e depois:

```
p50, p95, pico, frames > 50ms
```

Referência saudável nesta base: p50 ≈ 16,7ms e p95 abaixo de ~25ms. Se o p95 passar de 35ms ou aparecerem frames acima de 100ms, corte quantidade ou frequência — e lembre que a variação entre corridas engana: alterne A/B em vez de confiar numa medição só (regra 8 do projeto).

## 7. Fechar

- Entrada no `FIXLOG.md` com o que foi medido dos dois lados.
- `npm run test:contracts` **sozinho** (browser concorrente derruba teste por timing e você lê como falha real).
