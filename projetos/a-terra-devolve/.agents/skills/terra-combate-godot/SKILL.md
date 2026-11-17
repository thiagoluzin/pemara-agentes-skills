---
name: terra-combate-godot
description: "Implemente ou revise armas, mira fixa, inimigos e economia de recursos no survival horror Godot 2D A Terra Devolve."
---

# Combate de sobrevivência no Godot

Leia `AGENTS.md`, `TerraDevolveGodot/README.md`, `ANIMACAO_REQUISITOS.md`, `Docs/README.md`, `01_ESCOPO_GDD.md`, `02_ARQUITETURA_TECNICA.md` e `10_CONTROLES_E_MIRA_FIXA.md`. Confirme o código ativo: uma intenção de design não prova combate existente. Siga a skill Gemini Decision 1 obrigatória; regras de dano e progressão permanecem determinísticas e offline.

## Construir um encontro antes de generalizar

O primeiro encontro usa `scripts/revolver_combat.gd`, ligado por `scripts/patio.gd`, com arte em `scripts/revolver_frames.gd` e contrato em `Docs/16_COMBATE_REVOLVER.md`. Confirme a implementação e os resultados atuais antes de ampliá-lo. Preserve câmera fixa e movimento relativo à tela. Mirar planta Helena e muda sua orientação; câmera não aproxima. Entrada de menu não dispara, recarrega ou mantém movimento preso. No modo revólver, R recarrega e F6 solicita nova partida; preserve essa separação.

Separe definição da arma do estado de munição e do sprite. Um disparo válido consome recurso uma vez; tiro vazio não causa dano. Origem lógica da arma, cone frontal, alcance e obstáculos no plano 2D regem o acerto. Não derive acerto do tamanho aparente da arte nem permita dano através de parede, porta fechada ou pilar. Retenção e troca de alvo precisam ser estáveis e legíveis.

## Ameaça e recursos

Defina estados explícitos de percepção, aproximação, preparação, ataque, recuperação, interrupção e desativação. Dano depende de janela/alcance válidos, não de animação que parece próxima. Telegráficos devem ter sinal visual além de áudio; inimigo fora do quadro não causa golpe inevitável. Salas de alívio e leitura modal seguem regras ensinadas.

Faça a arma valer o gasto: interrupção previsível, abertura de passagem ou neutralização persistente de inimigos ordinários conforme design. Não use respawn gratuito na revisita para anular combate. Corpo-Seco tem contenção temporária e confronto dirigido; não torna todo inimigo invulnerável. Ajuste números por playtest, sem declarar equilíbrio pelo teste lógico.

Evite bloqueio permanente por munição gasta: o caminho crítico precisa de desvio, mecanismo ou outra recuperação desenhada. Ferramenta de emergência não deve trivializar todos os confrontos. Curar, recarregar, receber dano e trocar de sala têm cancelamentos explícitos; não duplique dano/consumo por callback.

## Persistência e evidência

Godot 4.7.2, GDScript tipado, cenas 2D, sinais e fonte única de estado. Extraia responsabilidades de `scripts/patio.gd` conforme necessidade. Ao acrescentar recursos/inimigos ao save v1, preserve backup e migração; UI consulta o mesmo estado. Coleção de munição não reaparece ao carregar ou revisitar.

Rode `Testar.ps1` e regressões do encontro com slot separado: acerto bloqueado por obstáculos, alvo atrás, dois alvos, munição vazia, morte/retorno, carga durante encontro e menus. Renderize o percurso no jogo para avaliar composição, animação e legibilidade. Uma animação de tiro sem sistema de dano não é combate implementado; testes técnicos não aprovam sensação ou dificuldade.

Consulte APIs pertinentes na [documentação oficial Godot](https://docs.godotengine.org/en/stable/) e valide na engine 4.7.2 instalada; não presuma que `stable` remoto seja essa versão.
