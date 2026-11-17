---
name: unity-tooling
description: "Auditar assets Unity e automatizar tarefas de Editor."
---

# unity-tooling

O recurso [GameDevKitAudit.cs](scripts/GameDevKitAudit.cs) pode ser copiado para Assets/Editor/GameDevKit. Execute GameDevKit.Audit.Run em batch ou pelo menu Tools/Game Dev Kit/Audit assets. O relatório Library/GameDevKit/audit.json inventaria cenas habilitadas, modelos e materiais; warnings pedem revisão, não reparação automática. RunSelfTest verifica contagem geométrica em objeto temporário e depois executa o inventário. Preserve .meta em atualizações. Automação deve usar Undo em edições interativas e evitar AssetDatabase.Refresh repetido em loops.

## Entrega

Informe o problema, a alteração ou diagnóstico, a evidência executada e os limites observados. Respeite a versão e as decisões do projeto. Esta especialidade não inicia outros agentes automaticamente.
