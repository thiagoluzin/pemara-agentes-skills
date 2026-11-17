---
name: phaser-ui
description: "Criar e corrigir menus, HUD e interfaces DOM associadas a jogos Phaser, incluindo foco, navegação por dispositivos e layout responsivo."
---

# Interface de jogos Phaser

Determine se a UI vive no canvas, em Scene paralela ou no DOM. Preserve o padrão existente e a separação entre coordenadas de mundo, câmera, canvas e CSS. Uma mudança no menu não justifica introduzir framework ou substituir HUD inteiro.

Estado de menu precisa ter dono: seleção, confirmação, modal, pausa e retorno. Mouse/touch devem selecionar o alvo tocado antes de confirmar; teclado/gamepad usam a mesma intenção. Evite acionamento simultâneo no overlay e na cena ao fundo. Confira foco, blur, repetição e reabertura.

No DOM, prefira elementos semânticos, botões com nomes claros, labels, foco visível e navegação por teclado. No canvas, avalie a necessidade de equivalente acessível no DOM e instruções compreensíveis. Cor não deve ser o único sinal de perigo ou seleção. Respeite preferências de movimento quando disponíveis.

Teste em resoluções e proporções do alvo, safe area, orientação, zoom e DPR. Alinhe área clicável com a imagem real após escala e letterbox; captura em desktop não certifica hit targets no telefone.

HUD precisa manter hierarquia legível durante combate e efeitos. Não exiba detalhes de implementação ao jogador sem utilidade. Dicas de controle acompanham mapeamento real, incluindo remapeamento e troca de dispositivo.

Listeners DOM, observers e overlays devem ser removidos por quem os criou. Teste menu → gameplay → pausa → opções → retorno → próxima fase na mesma instância, verificando foco, áudio e overlay duplicado.

Use testes de entradas reais e capturas abertas/inspecionadas. Relate qual viewport/dispositivo foi exercitado e limitações de acessibilidade ou hardware não cobertas.
