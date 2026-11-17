---
name: terra-audio-integracao
description: "Integre a trilha escolhida e desenhe ambientes, silêncio e sinais de perigo de A Terra Devolve no Godot, preservando fontes e informação acessível."
---

# Áudio de sobrevivência

Leia `AGENTS.md`, `TerraDevolveGodot/README.md`, `ANIMACAO_REQUISITOS.md`, `Docs/README.md`, `01_ESCOPO_GDD.md` e `09_DIRECAO_CRIATIVA_A_TERRA_DEVOLVE.md`. Para runtime, acrescente `02_ARQUITETURA_TECNICA.md` e `10_CONTROLES_E_MIRA_FIXA.md`. Siga a skill Gemini Decision 1 obrigatória sem criar dependência online ou custo por áudio.

## Decisão musical do proprietário

A ordem vigente é produzir **músicas originais no YuE2 local** e **vozes no Google Gemini 3.8 Flash TTS** (`gemini-3.8-flash-tts`), usando as instalações/configurações existentes. Essa ordem substitui a espera anterior por arquivos de Akira Yamaoka; ele permanece referência de atmosfera, sem autoria atribuída às composições geradas. Leia `Docs/18_AUDIO_YUE2_GOOGLE_TTS.md` para estado e contratos.

Para YuE2, confirme servidor, fila, VRAM, nodes e pesos reais. Use planejamento/ABC quando pertinente, com compasso/tempo coerentes e validação antes de síntese. Produza cues limitados às situações jogáveis; preserve fonte lossless, workflows, seed e recibo. Não confundir tags instrumentais com garantia de ausência de canto: conferir o resultado. Não trocar por Lyria nem interromper outro projeto.

Para falas, use vozes predefinidas do modelo 3.8 como candidatas por personagem, em português brasileiro; transcrição literal e direção no campo de estilo. O conector existente de replicação usa um perfil pessoal de outro trabalho: não reutilizá-lo como personagem automaticamente. A rota genérica configurada aceita voz predefinida e credencial em memória, sem enviar áudio de terceiros. Clonagem não foi solicitada para o jogo. Preserve texto, papel dramático, voz, estilo, versão e WAV nativo. Verifique a autorização da síntese e do custo no pedido atual. Nunca colocar credenciais no projeto.

## Fazer o som informar o risco

Monte cues por estado do jogo: chegada, abrigo, investigação, proximidade, preparação, confronto e alívio. Música não deve ocupar todo espaço nem revelar sempre ameaça antes do jogador percebê-la. Reserve frequências e dinâmica para passos, raízes, recarga e ataque; silêncio é uma decisão de tensão, não ausência acidental de áudio.

Para cada sinal crítico registre fonte, estado disparador, alcance/oclusão, repetição, prioridade e alternativa visual/legenda. As três batidas não significam ataque inevitável a cada documento. Se o som indicar perigo real, a relação deve ser consistente e ensinada. Não usar apenas áudio para resolver puzzle ou evitar dano.

Santa Amália em 1994: chuva, madeira, terra vermelha, rádio AM e cisterna sustentam lugar e época. Separe música diegética de trilha extradiegética; não ponha uma faixa num rádio de época sem que isso faça sentido no roteiro. Um efeito sintetizado pode ser provisório útil; origem, nível e condição devem ser claros.

## Integrar e verificar

Preserve arquivos de origem, duração, canais e hashes; crie cópias de trabalho para importação. Use buses separados para música, ambiente, efeitos e UI conforme necessidade; mute, pausa, troca de sala e carga não podem duplicar streams ou deixar música presa. Não normalize/remasterize fontes silenciosamente. Mantenha volume de chuva interior/exterior coerente com o runtime existente.

Rode `Testar.ps1` quando alterar código, usando save separado. Ouça capturas reais de transição, combate e silêncio: ausência de clipping nos números não prova mixagem boa. Confira legendas de eventos e modo sem som. Registre track/cue, fonte, edição/import settings, pontos de entrada/saída e aprovação humana pendente.

Confirme APIs de reprodução e buses na [documentação oficial de áudio Godot](https://docs.godotengine.org/en/stable/tutorials/audio/index.html), testando na 4.7.2 instalada. Não instalar plugins de áudio, contratar novos serviços ou publicar faixas como consequência automática desta skill. Verifique a autorização para síntese externa na tarefa atual.
