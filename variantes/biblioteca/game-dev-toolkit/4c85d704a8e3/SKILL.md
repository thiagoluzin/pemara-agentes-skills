---
name: game-dev-toolkit
description: "Ferramentas autônomas de Game Dev (Sprite Cutter, Input Mapper) convertidas da UI do Toolkit Pro."
---

# Game Dev Toolkit

Esta skill provê ferramentas de automação para tarefas comuns no desenvolvimento do jogo, baseadas na API do Toolkit Pro.

## Scripts Disponíveis

### 1. Sprite Cutter (`sprite_cutter.py`)
Fatia uma spritesheet em frames individuais e salva em um diretório.
**Uso:**
```bash
python .agent/skills/game-dev-toolkit/scripts/sprite_cutter.py --input <arquivo> --tw <largura> --th <altura> --out <pasta_destino>
```
Exemplo: `python .agent/skills/game-dev-toolkit/scripts/sprite_cutter.py --input assets/sprites/sheet.png --tw 16 --th 16 --out assets/sprites/cortados/`

### 2. Input Mapper (`input_mapper.py`)
Lê um JSON contendo o mapeamento de teclas e gera o código nativo (Phaser, Godot ou Pygame).
**Uso:**
```bash
python .agent/skills/game-dev-toolkit/scripts/input_mapper.py --input <actions.json> --engine <phaser|godot|pygame> --out <arquivo_saida>
```
Exemplo do `actions.json`:
```json
[
  { "id": 1, "name": "Mover Esquerda", "key": "a", "type": "held", "debounce": 0 }
]
```

## Como Usar
- Se o usuário pedir para fatiar ou extrair frames de uma imagem, crie a pasta destino se não existir, e rode o `sprite_cutter.py`.
- Se o usuário pedir para gerar a classe de Input ou atualizar os controles, rode o `input_mapper.py`.
