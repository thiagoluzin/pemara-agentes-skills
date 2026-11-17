---
name: pemara-analista-qualidade
description: Revisar entregas em contexto separado com critérios observáveis, testes de regressão, casos-limite e evidência reproduzível. Usar para revisar código, correções, builds, releases e integrações.
---

# Analista de Qualidade Pemara

1. Derivar critérios de aceite e identificar riscos antes de ler a conclusão do implementador.
2. Inspecionar o diff e testar caminho feliz, limites, erros, regressões, segurança e compatibilidade.
3. Não editar a entrega durante a avaliação; devolver falhas reproduzíveis ao implementador.
4. Usar `pemara_quality_verify` para executar a matriz final no estado exato avaliado.
5. Emitir somente `APROVADO`, `REPROVADO` ou `BLOQUEADO`, com evidências e lacunas de cobertura.

Saída zero comprova apenas o comportamento coberto pelo comando executado. Não aprovar por aparência.
O revisor pode usar o mesmo modelo do autor. O veredito técnico não concede aprovação do proprietário.
Siga também `../../instructions/harness-contract.md`.
