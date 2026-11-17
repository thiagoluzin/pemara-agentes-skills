---
name: pemara-debugger
description: Reproduzir, diagnosticar e corrigir defeitos por causa raiz, com teste de regressão e evidência. Usar em bugs, erros intermitentes, falhas de build, comportamento inesperado, regressões e incidentes técnicos.
---

# Debugger Pemara

1. Reproduzir o sintoma antes de modificar, preservando logs e condições relevantes.
2. Formular hipóteses falsificáveis e localizar a primeira divergência observável.
3. Confirmar a causa raiz; não tratar correlação ou workaround como diagnóstico.
4. Criar um teste de regressão que falhe antes da correção quando viável.
5. Aplicar a correção mínima e testar caminhos adjacentes.
6. Rodar `pemara_quality_verify` depois da última edição.

Sem reprodução ou prova suficiente, relatar o estado como hipótese ou bloqueio, nunca como correção.
