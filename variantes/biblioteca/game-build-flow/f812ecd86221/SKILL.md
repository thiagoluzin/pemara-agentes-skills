---
name: game-build-flow
description: "Fluxo orquestrado para construir um jogo (especialmente platformer Phaser 16-bit/HD remix) amarrando os especialistas na ordem certa, com checkpoints entre etapas. Use quando o pedido for \"fazer um jogo X\" do conceito ao jogável. Triggers on fazer um jogo, criar jogo, pipeline de jogo, do conceito ao jogável, orquestrar jogo, game flow."
---

# Game Build Flow — orquestração de jogo

Você conduz a construção de um jogo do conceito ao jogável, **amarrando os especialistas** e validando entre etapas. Regra Miyamoto: o núcleo precisa ser divertido **antes** de arte e áudio.


## O pipeline (com checkpoints)

| # | Etapa | Especialista | Entrega | ✅ Checkpoint pra avançar |
|---|-------|--------------|---------|---------------------------|
| 1 | Conceito & roteiro | `creative-director` | fun-core (1 frase), 3 pilares, loop de 30s, escopo MVP | Conceito empolga em 1 parágrafo? |
| 2 | Núcleo jogável | `phaser-platformer-architect` | controller + 1 sala de teste (16-bit ou HD remix) | **Os primeiros 8s são divertidos?** (Miyamoto) |
| 2b | Fases & balanço | `level-designer` + `balance-tuner` | layout que ensina + curva justa | Ensina antes de cobrar; dificuldade justa |
| 3 | Animação | `animation-engineer` | máquina de estados + juice | Transições legíveis, sem travar, 60fps |
| 4 | Áudio | `game-audio-designer` | som reativo + mix | Áudio reage ao estado; silêncio usado |
| 5 | Performance | `performance-optimizer` | 60fps no alvo fraco | Frame budget mantido c/ FX |
| 6 | Verificação | `pack-doctor` / `qa-automation-engineer` | smoke-test jogável | Roda do início ao fim sem quebrar |

**Ordem importa:** trave o **feel (etapa 2)** antes de investir em arte/áudio. Arte linda em cima de pulo ruim é dinheiro jogado fora.

## Hand-off (contrato entre etapas)
Cada etapa entrega pra próxima: **o que está pronto**, **o que falta**, **arquivos/keys de assets**, **decisões tomadas**. Sem hand-off claro, a próxima etapa adivinha — e adivinhar custa retrabalho e cota.

## Loop de feedback
Após etapa 4, faça um **playtest** mental/real do primeiro minuto. Se o feel regrediu, **volte à etapa 2** antes de seguir. Registre ajustes no `FIXLOG.md`.

## Quando me usar
- "Faz um jogo X" / "monta o esqueleto jogável de Y"
- Coordenar conceito → core → animação → áudio → perf → teste
