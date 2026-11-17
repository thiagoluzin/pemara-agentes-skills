---
name: blender-export
description: "Exportar FBX Blender com seleção explícita para Unity."
---

# blender-export

Use [export_selection.py](scripts/export_selection.py) a partir de script Blender com lista explícita de objetos e arquivo novo. O helper recusa arquivo existente, cena fora de Object Mode e seleção vazia; restaura seleção e objeto ativo mesmo em falha. O preset estático usa -Z forward, Y up e não exporta animação. Para rigs animados crie configuração específica; não prometa que preset estático resolve Avatar. Reimporte e confira dimensões e hierarquia no Unity.

## Entrega

Informe o problema, a alteração ou diagnóstico, a evidência executada e os limites observados. Respeite a versão e as decisões do projeto. Esta especialidade não inicia outros agentes automaticamente.
