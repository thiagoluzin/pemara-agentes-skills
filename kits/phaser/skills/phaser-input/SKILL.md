---
name: phaser-input
description: "Diagnosticar teclado, gamepad e touch em Phaser, incluindo estado preso, cancelamento de ponteiros, remapeamento, foco e navegação de menus."
---

# Input e menus Phaser

Trace dispositivo → browser → normalização → intenção → cena consumidora. Preserve comandos e layout aprovados. Leia o estado bruto do gamepad, mapping, eixos e botões antes de culpar o gerenciador; conexão por cabo e Bluetooth pode expor layouts diferentes. Não presuma que axes[0] existe.

Separe held de pressed/released. Defina quem consome a borda para não disparar duas vezes entre UI e gameplay. Um campo chamado attackPressed não pode receber diretamente isDown sem documentar que é estado mantido. Normalize deadzone com medidas do dispositivo e mantenha magnitude quando houver movimento analógico.

Em touch, acompanhe pointerId por controle. Exercite down/move/up/cancel, dois ponteiros, arrastar para fora, soltar fora do canvas, pointer capture e perda de foco. Um dedo soltando não deve limpar outro ainda ativo. Abertura de menu e blur precisam resolver estados mantidos sem introduzir disparo fantasma ao retomar.

Menu deve selecionar o item tocado antes de confirmar. Teste teclado/gamepad/touch na pausa, opções, retorno e reabertura repetida. Teclas pertencentes a uma cena devem ser removidas pelo plugin responsável quando necessário; destruir somente o objeto pode deixar referência registrada.

Confira defaults e migração do remapeamento. Mudança de esquema não deve apagar preferências sem necessidade. Atualize dicas de botão junto com o mapeamento quando este for alterado.

Teste pela entrada real. Chamar a função de ataque ou o callback de um botão só testa a função. Eventos sintéticos no browser permitem regressão automatizada; não comprovam hardware físico, latência do controle ou sistema operacional do dispositivo.

Registre modelo/conexão quando relevantes, camada da falha, sequências exercitadas e limitações. Não use teste de mouse único como prova de multitoque.
