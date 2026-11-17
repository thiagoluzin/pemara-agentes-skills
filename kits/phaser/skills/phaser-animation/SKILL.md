---
name: phaser-animation
description: "Corrigir clipes, interrupções, eventos por frame, spritesheets, atlas e variação de porte em Phaser com revisão temporal e referências anatômicas."
---

# Animação e sprites Phaser

Compare fonte, configuração e runtime antes de mudar arte. Leia grade/atlas, trim, rotação, sourceSize, spriteSourceSize, sequência, repeat/yoyo, origem, escala e duração real. Padding transparente não define anatomia. Não infira grade apenas por faixas vazias: elas também podem existir dentro de uma pose.

Meça célula, alpha, bordas, pé, centro e landmarks de cabeça/torso. Bbox total detecta corte e enquadramento; armas, cabelo e FX não devem encolher o corpo. Compare poses no mesmo zoom alinhadas pelo chão. Agachamento ocupar menos altura é esperado. Um limiar automático de glint ou escala é triagem, não autorização para modificar detalhe aprovado.

Animações têm sessões e saídas explícitas: término, stop, substituição, hurt, morte e shutdown. animationcomplete não é emitido por todo encerramento e loops infinitos não completam. Registre listeners de sua propriedade e remova-os quando a sessão termina; callback antigo não pode liberar uma ação nova.

Marcadores de passo/poeira podem repetir por ciclo; acerto de combate costuma ser uma vez por sessão/janela. Não use um Set global limpo somente no complete. Confira índice do frame, eventos pulados, primeiro frame, yoyo e política de repetir antes de definir um marcador. Não torne renderização a única autoridade de dano quando a lógica usa outro relógio.

Use o [exemplo de sessão](scripts/animation-session.mjs) se precisar de um proprietário de callbacks para uma animação. O contrato, limites e testes estão no comentário do módulo. Sua callback de encerramento informa o motivo; cabe ao controlador escolher o próximo estado, sem retornar ao idle durante morte ou pausa.

Tempo de cada frame pode diferir de 1000/frameRate. Confira duração positiva, timeScale, hitstop e o consumidor na versão real. Preserve alcance, hitboxes e timing aprovados ao corrigir apresentação.

Abra as imagens e assista ao ciclo em velocidade real. Confira passos alternados, pés plantados, volume, contato e transições; uma prancha estática ou comparação pixel a pixel não demonstra qualidade temporal. Se gerar arte, use o fluxo e referências autorizados pelo projeto. Scripts técnicos não devem introduzir alterações artísticas silenciosas.

Entrega: cobertura medida versus esperada, antes/depois, clipes exercitados, gates pertinentes e estado separado para verificação automática e aprovação estética.
