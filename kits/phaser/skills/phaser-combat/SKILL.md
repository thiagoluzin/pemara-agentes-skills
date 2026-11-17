---
name: phaser-combat
description: "Criar e corrigir combate 2D em Phaser, incluindo beat-em-up com lanes, hitboxes, telegraphs, IA, invulnerabilidade e interrupções."
---

# Combate Phaser

Leia a autoridade de dano e os estados antes de alterar números. Registre unidades e fases do golpe: startup, janela ativa, recovery, cancel e cooldown. A animação ilustra o contrato; trocar FPS não autoriza mover contato, alcance ou invulnerabilidade.

Em beat-em-up, distinga posição de chão, altura visual de salto e profundidade. Confira alinhamento X/Y no início do ataque e no momento do acerto. Um perseguidor pode precisar alinhar a lane antes de atacar; projéteis e ataques de área podem ter regras diferentes. Não transforme uma escolha de gênero em proibição universal de diagonais.

Hitbox e hurtbox são contratos de gameplay independentes do padding, da arma e do tamanho total da imagem. Verifique direção, escala efetiva, âncoras, câmera e limites. Compare contato visual e dano com posições extremas, adversário em movimento, agachamento e troca de forma.

Identifique a sessão de ataque e os alvos já atingidos. Registre contato uma vez por janela, salvo multihit explícito. Interrupção por hurt, morte, cancel ou troca de cena deve desativar as áreas e limpar marcadores de sua propriedade. Não dependa apenas de animationcomplete para liberar o ataque.

Hitstop tem dono e motivo: o fim de um efeito não pode desfazer pausa de menu, derrota ou outro efeito ainda ativo. Separe relógio visual, física e timers de combate; ensaie sobreposição e timeScale.

Encontros devem oferecer sinais e oportunidades de resposta legíveis. Meça pressão simultânea, lugares válidos de spawn e recuperação; não compense bug de IA com HP. Parâmetros de balanceamento ficam na configuração consumida pelo sistema.

Teste dano duplicado, fora da lane, último alvo morto, cancel no contato, pausa durante hitstop e progressão da onda. Combine contratos de lógica com captura/runtime; um mock isolado não comprova hitbox na tela.
