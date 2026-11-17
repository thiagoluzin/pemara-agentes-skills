---
name: terra-puzzles-progressao
description: "Desenhe e verifique puzzles físicos e grafos de progressão de A Terra Devolve, com pistas justas, atalhos e recuperação sem bloqueio permanente."
---

# Puzzles e progressão

Leia o `AGENTS.md`, `TerraDevolveGodot/README.md`, `ANIMACAO_REQUISITOS.md`, `Docs/README.md`, `01_ESCOPO_GDD.md`, `02_ARQUITETURA_TECNICA.md`, `09_DIRECAO_CRIATIVA_A_TERRA_DEVOLVE.md` e `10_CONTROLES_E_MIRA_FIXA.md`. A skill Gemini Decision 1 do computador permanece obrigatória, sem exigir chamadas para um grafo determinístico.

## Formular o puzzle

Parta da função original do objeto: arquivo, moinho, capela, transporte, ossuário, bomba ou comporta. Defina por que existe aquele mecanismo, que conhecimento falta a Helena e como o jogador pode inferi-lo. Use a materialidade e a descoberta espacial associadas a Tormented Souls; não transplante suas soluções, locais ou símbolos.

Especifique estado inicial, pistas disponíveis, regra inferível, operação, resultado visível, feedback de erro e recuperação. Escreva a solução com todas as pistas necessárias: se o próprio designer precisa de conhecimento não dado ao jogador, falta informação. Evite senhas arbitrárias, itens usados por associação obscura e ordem de fichas que só funciona porque o texto já entregou tudo.

## Verificar o grafo

Represente salas, portas, itens, evidências e operações com IDs estáveis. Cada transição declara pré-condições e efeitos; diferencie item possuído, pista lida, hipótese e mecanismo operado. Consumo deve ocorrer somente depois de validar a transação.

Percorra pelo menos o caminho crítico, a ordem alternativa de coleta e o retorno após erro/carga. Procure chave atrás da própria porta, evidência irrecuperável, item crítico descartável, inventário cheio sem saída, consumo duplicado e flags só na UI. Documentos não ocupam o inventário de recursos; requisitos de oito espaços não podem impedir coletar o item que permite sair.

Teste conceitualmente a rota com munição zero e cura zero. Um puzzle crítico não exige gastar recurso finito sem recuperação prevista. Combate pode tornar a travessia mais segura; desvio viável não significa apagar o valor das armas. Atalhos devem reduzir risco ou distância e manter estado após carga.

## Implementar e revisar

Godot 4.7.2, GDScript tipado, sinais e uma fonte de verdade para progresso. Antes de trocar a condição da porta atual, examine as dependências de `scripts/save_store.gd`: o save v1 depende de chave + aviso para `unlocked`. Não remova a barreira documental sem migração compatível e regressão das partidas antigas.

Para runtime, rode `Testar.ps1` e inspecione logs; teste save/load antes e depois da operação, erro recuperável e revisita sem duplicar itens. Use slot separado. Revise o mecanismo renderizado: estado aberto/fechado, alcance e pista devem ser legíveis. Não ateste justiça por um percurso do próprio autor; registre o que ainda requer jogador novo.
