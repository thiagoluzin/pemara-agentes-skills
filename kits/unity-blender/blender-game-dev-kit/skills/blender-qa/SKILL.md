---
name: blender-qa
description: "Auditar geometria e validar round-trip Blender."
---

# blender-qa

Use [audit_scene.py](scripts/audit_scene.py) para relatório sem salvar ou alterar a cena. A contagem usa mesh avaliada com modificadores e libera temporários. Relate UV ausente, escala negativa e materiais vazios como achados contextuais. Rode `tests/blender_smoke.py` na raiz do kit completo somente em processo Blender --background --factory-startup: ele cria fixtures, exporta e reimporta FBX em diretório temporário. Testes não aprovam arte.

## Entrega

Informe o problema, a alteração ou diagnóstico, a evidência executada e os limites observados. Respeite a versão e as decisões do projeto. Esta especialidade não inicia outros agentes automaticamente.
