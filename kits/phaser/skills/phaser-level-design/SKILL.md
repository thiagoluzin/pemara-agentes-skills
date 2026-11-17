---
name: phaser-level-design
description: "Construir encontros, layouts e curvas de dificuldade para jogos Phaser, medindo progressão, recursos e situações de softlock."
---

# Fases e balanceamento Phaser

Leia moveset, câmera, área navegável, dados de fase e gatilhos. Reutilize o formato existente: Tiled só quando necessário ou já consumido. Dimensione obstáculos pelo alcance observado e encontros pelas regras de combate, sem mudar controles para acomodar o layout.

Defina objetivo do trecho, mecânica ensinada, pressão, recuperação e liberação. Ensine em condição segura antes de combinar exigências. Spawn e saída devem estar acessíveis no espaço do mundo e legíveis com HUD/FX ativos. Segredos precisam de pistas quando pertencem ao escopo.

Balanceamento começa por distinguir bug de regra e ajuste numérico. Acerto duplicado, inimigo fora da lane e telegraph ausente exigem correção de comportamento; reduzir dano pode apenas esconder o defeito.

Registre condições comparáveis: personagem, dificuldade, recursos, equipamento e estratégia. Mude o conjunto mínimo de parâmetros que testa a hipótese. Anote unidades, multiplicadores, arredondamentos e antes/depois. HP/DPS é uma estimativa; janelas de acerto, movimento e invulnerabilidade alteram a duração real.

Compare duração do encontro, dano recebido, recurso gasto/ganho, chances de reação e estratégia dominante. Preservar arquétipos não exige desempenho idêntico. Use playtest com habilidades diferentes quando houver acesso, distinguindo cálculo, simulação e experiência humana.

Teste da fase anterior até a seguinte sem voltar ao menu: último inimigo morto ainda contado, spawn fora dos limites, portão que abre cedo, derrota/reinício duplicando ondas, checkpoint e save. Confira economia em sequência, não só num encontro abastecido artificialmente.

Liste a cobertura real por fase/encontro. Amostra não comprova jogo inteiro. Entregue dados alterados, intenção, medidas, evidência de progressão e questões de dificuldade ainda subjetivas.
