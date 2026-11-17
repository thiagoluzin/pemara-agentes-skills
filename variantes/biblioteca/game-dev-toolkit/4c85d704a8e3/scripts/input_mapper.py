import json
import argparse
import os

def generate_phaser(actions):
    lines = [
        "// ── INPUT MANAGER (Phaser 3) ─────────────────────────────────",
        "export class InputManager {",
        "  constructor(scene) {",
        "    this.scene = scene;",
        "    this.keys = scene.input.keyboard.addKeys({"
    ]
    for a in actions:
        name = a['name'].lower().replace(" ", "_").replace("ã", "a").replace("ç", "c")
        key = a['key']
        pk = "SPACE" if key == "space" else "ENTER" if key == "return" else "ESC" if key == "escape" else key.upper()
        lines.append(f"      {name}: Phaser.Input.Keyboard.KeyCodes.{pk},")
    
    lines.append("    });")
    lines.append("    this._timers = {};")
    lines.append("  }")
    lines.append("  _debounce(name, ms) {")
    lines.append("    const now = Date.now();")
    lines.append("    if ((now - (this._timers[name]||0)) >= ms) { this._timers[name]=now; return true; }")
    lines.append("    return false;")
    lines.append("  }")
    lines.append("  update() {")
    lines.append("    return {")
    
    for a in actions:
        name = a['name'].lower().replace(" ", "_").replace("ã", "a").replace("ç", "c")
        db = f" && this._debounce('{name}', {a['debounce']})" if a.get('debounce', 0) > 0 else ""
        expr = ""
        if a['type'] == "press":
            expr = f"Phaser.Input.Keyboard.JustDown(this.keys.{name}){db}"
        elif a['type'] == "held":
            expr = f"this.keys.{name}.isDown"
        elif a['type'] == "release":
            expr = f"Phaser.Input.Keyboard.JustUp(this.keys.{name}){db}"
            
        lines.append(f"      {name}: {expr},")
    
    lines.append("    };")
    lines.append("  }")
    lines.append("}")
    return "\n".join(lines)

def run_mapper(input_json, engine, out_file):
    try:
        with open(input_json, 'r', encoding='utf-8') as f:
            actions = json.load(f)
    except Exception as e:
        print(f"Erro ao ler JSON: {e}")
        return

    code = ""
    if engine == "phaser":
        code = generate_phaser(actions)
    else:
        print(f"Engine {engine} não implementada no script básico. Apenas phaser suportado.")
        return

    os.makedirs(os.path.dirname(os.path.abspath(out_file)), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(code)
    
    print(f"Gerado mapeamento para {engine} em {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Arquivo JSON de ações")
    parser.add_argument("--engine", default="phaser", choices=["phaser", "godot", "pygame"], help="Engine destino")
    parser.add_argument("--out", required=True, help="Arquivo de saída JS/GD/PY")
    args = parser.parse_args()
    
    run_mapper(args.input, args.engine, args.out)
