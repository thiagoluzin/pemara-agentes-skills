---
name: balance-tuner
description: "Afinar dano, vida, velocidade, recursos e dificuldade de jogos com valores reais, cenários comparáveis e playtest. Use para curvas injustas ou estratégias dominantes; defeitos de colisão e IA exigem diagnóstico de combate."
---

# Balance Tuner — dificuldade demonstrável

Aplique `AGENTS.md`. Preserve a fantasia de poder, controles e timing aprovados. Antes de mudar números, localize a configuração e seus consumidores: dano base, multiplicadores de dificuldade, críticos, invulnerabilidade, acertos múltiplos, cooldown e drops.

## Diagnóstico e experimento
1. Reproduza o encontro com herói, dificuldade, equipamento/recursos e estratégia registrados. Dano duplicado por frame, inimigo que ignora lane ou golpe sem telegraph são defeitos de combate; investigue com `beatemup-combat-designer` antes de compensar com HP.
2. Defina uma hipótese mensurável e o conjunto mínimo de parâmetros relacionados. Registre valor antigo/novo, unidade, motivo e resultado esperado.
3. Estime tempo para matar e golpes necessários. `HP / DPS` é aproximação: confirme startup/active/recovery, taxa real de acerto, alcance e invulnerabilidade. Arredondamento e hits discretos podem mudar o número de golpes mesmo com pequena alteração.
4. Compare baseline e candidato em cenários equivalentes, incluindo estratégia comum e exploração de uma estratégia dominante. Variações grandes podem ajudar em experimento reversível; não dobre/divida a curva inteira como regra.
5. Meça duração de encontro, dano recebido, recursos gastos/ganhos e oportunidades de reação. Simulação não substitui jogadores com níveis diferentes de habilidade.

## Curva e economia
Alterne pressão e recuperação; desafio deve ser legível, não depender só de vida inflada. Confira disponibilidade de cura/recursos em sequência de fases e após derrota. Verifique limites zero/mínimo/máximo, multiplicadores acumulados e arredondamento. Compare heróis afetados sem impor desempenho idêntico a arquétipos diferentes.

Mantenha valores na configuração real; extraia somente os parâmetros que precisam de ajuste, sem migrar toda a arquitetura. Não regenere golden/baseline de combate para esconder regressão.

## Entrega
Execute `npm run test:balance` e os testes do comportamento tocado, conferindo a cobertura no `package.json`. Repita o encontro e o trecho seguinte em runtime; `npm run deploy:check` antes de entrega. Faça append no `FIXLOG.md` com tabela antes/depois, condições, resultados e limites. Distingua números calculados, observados e avaliação humana; não certifique que nenhuma estratégia domina sem tê-las ensaiado.
