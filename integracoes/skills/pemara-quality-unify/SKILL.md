---
name: pemara-quality-unify
description: Audita projetos, plugins, instaladores e pacotes de skills/agentes; valida UTF-8, detecta mojibake, confere frontmatter, manifests, checksums, arquivos ausentes e segredos acidentais. Use antes de instalar, publicar ou distribuir, ao conferir a qualidade Pemara, ao diagnosticar caracteres como "Ã"/"â", ou quando pedirem quality check, health check, conferidor, validação ou correção segura de Unicode.
---

# Pemara Quality Unify

## Fluxo obrigatório

1. Resolver a raiz exata que o usuário colocou em escopo.
2. Executar a varredura determinística antes de afirmar que está íntegro:

```powershell
$env:PYTHONUTF8 = "1"
python scripts/quality_unify.py scan --root <caminho> --report <relatorio.json>
```

3. Tratar erros antes dos avisos. Corrigir a causa raiz quando a alteração estiver autorizada.
4. Para mojibake, primeiro simular a reparação; aplicar somente quando a pontuação melhorar sem perda:

```powershell
python scripts/quality_unify.py repair-unicode --root <caminho>
python scripts/quality_unify.py repair-unicode --root <caminho> --apply --backup-root <backup>
```

5. Repetir `scan` após as correções. Não aprovar com erro remanescente.
6. Para bundles Pemara, passar também o manifesto:

```powershell
python scripts/quality_unify.py scan --root <bundle> --manifest <bundle>\manifest\packages.json --fail-on-warning
```

## Portões

- `PASS`: zero erros; avisos documentados ou zero avisos em modo estrito.
- `FAIL`: UTF-8 inválido, mojibake, manifesto inválido, checksum divergente, skill quebrada, caminho ausente ou segredo incluído.
- Nunca regravar arquivo inválido silenciosamente.
- Nunca alterar binários nem arquivos fora da raiz informada.
- Reparação Unicode sempre cria backup fora da árvore reparada.
- Em PowerShell, usar `-Encoding UTF8` ou APIs .NET com `UTF8Encoding`; não depender do padrão do Windows PowerShell 5.1.

Consulte [quality-gates.md](references/quality-gates.md) para códigos, escopo e formato do relatório.

## Saída

Informar contagens, caminhos exatos, achados por severidade, correções realizadas, verificações repetidas e o que exige julgamento humano. Não confundir integridade determinística com qualidade subjetiva das respostas dos agentes.
