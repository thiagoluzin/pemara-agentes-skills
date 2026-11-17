---
name: ai-video-intro-pipeline
description: "Pipeline para criar, refazer ou finalizar intros/cutscenes de jogo com video IA (Veo, Higgsfield, Flow ou similar), montagem ffmpeg, QC visual, musica/SFX, logo oficial, upscaling FHD e pacote de registro. Use quando o pedido mencionar intro, abertura, cutscene, video IA, Veo, cinematic, logo no final, sincronizar musica, upscale/FHD, registros de marca ou direitos autorais de audiovisual."
---

# AI Video Intro Pipeline

Use esta skill para produzir ou corrigir uma intro/cutscene de jogo com takes gerados por IA, montagem local e validacao tecnica. O objetivo e evitar retrabalho caro: primeiro fechar o material visual certo, depois audio, logo, upscale e registro.

## Ordem de trabalho

1. Leia o brief atual, `intro-60s.md` se existir, prompts em `projeto_animacao_introducao/prompts/`, scripts de render e assets oficiais usados no fechamento.
2. Separe direcao criativa de montagem tecnica: use `creative-director` para prompts/storyboard, `automation-engineer` para scripts/render, `game-audio-designer` ou `audio-analysis` para musica/SFX, e `sprite-image-reading` apenas para medir/extrair assets existentes.
3. Gere ou refaca takes animados antes de montar. Se o problema for falta de cenarios, movimento ruim, pixel art, sprite look, texto falso, pessoas/silhuetas ou cenario repetido, refaca o take. Nao esconda o problema com stills, fotos ou PNGs inseridos no meio do video.
4. Monte primeiro um preview sem audio temporario. Audio ruim mascara erro visual e torna o diagnostico confuso.
5. So depois de aprovar visualmente, aplique musica, SFX, logo oficial, normalizacao, export final e FHD.
6. Atualize `assets/videos`, `docs/registro_marca`, pacote `direitos_autorais` e `FIXLOG.md` quando a entrega mudar arquivos finais.

## Geracao de takes

- Use takes curtos e idempotentes, normalmente 8s, com nomes estaveis (`01_...mp4`, `02_...mp4`).
- Prompts de cutscene/transicao deste projeto devem ser ambientais: sem personagens, corpos, rostos, olhos, silhuetas, bosses, monstros, texto legivel, watermark, UI ou logos gerados pelo modelo.
- Reforce estilo quando necessario: `hand-drawn anime cel animation`, `not pixel art`, `not sprites`, `not gameplay footage`.
- Scripts de API devem ter `--dry-run`, `--force`, log, retomada, timeout e tratamento claro de quota/rate limit. Nunca imprimir chave de API.
- Quando houver quota ou chave instavel, registre no log qual take ficou pendente e nunca sobrescreva take bom por arquivo parcial.

## QC visual

Antes de chamar qualquer versao de final:

- Gere contact sheet ou frames amostrados dos takes e da montagem.
- Verifique duracao, resolucao, FPS, frame count e ausencia/presenca de audio conforme a etapa.
- Reprove take com pixel art/16-bit quando o pedido for animacao de verdade.
- Reprove texto falso, logos gerados por IA, rostos/olhos/silhuetas e qualquer ator em slide ambiental.
- Se o usuario apontar defeito de qualidade, investigue causa raiz no take/render/composicao. Evite remendo de camada por cima.

## Montagem e audio

- Preview visual deve ser video-only quando a trilha final ainda nao esta fechada.
- Prefira encode unico com cortes limpos a concatenar segmentos reencodados com fades em todo corte.
- Para musica final, medir duracao, sample rate, loudness, clipping e silences quando necessario.
- Mix final deve ter headroom para SFX; alvo pratico: perto de `-16 LUFS`, true peak abaixo de `-1.5 dBTP` quando possivel.
- SFX pontuais entram depois da musica base aprovada: impacto, static, neon, cabos, pulso, hit de titulo.

## Logo oficial e encerramento

- Extraia a logo de fonte oficial do projeto, como `assets/backgrounds/menu_bg.png`; salve tambem em `assets/ui` quando o usuario pedir.
- Se a alpha extraction carregar matte escuro ou parecer colada via Paint, nao use overlay RGBA cru. Use composicao por luz, por exemplo `blend=screen`, glow ou recorte melhor a partir da fonte oficial.
- Nao deixe fade-to-black acidental no encerramento. Se a logo e o titulo devem fechar a intro, mantenha a composicao visivel ate o ultimo frame.
- Valide frame de logo e ultimo frame. Quando a visualizacao falhar, meca luminancia do frame para descartar tela preta.

## FHD e upscale

- Upscale local aceitavel para entrega: `scale=1920:1080:flags=lanczos` com `unsharp` leve, CRF baixo e bitrate alto.
- Chame isso de upscale local, nao de AI upscale.
- Use upscale/enhance externo por IA so depois de o corte base estar aprovado, porque consome creditos e nao corrige direcao ruim.
- Publique sempre o 720p corrigido e a versao FHD quando ambos forem relevantes.

## Registro e rastreabilidade

- Copie finais para `assets/videos/` e para `docs/registro_marca/`.
- Atualize `docs/registro_marca/README.md` com SHA256 dos arquivos finais.
- Reconstrua `docs/registro_marca/direitos_autorais/MANIFEST.csv` quando adicionar ou trocar video, frame, musica, logo ou script relevante.
- Append em `FIXLOG.md` com: data, arquivo:linha, problema, causa raiz, correcao e verificacao.


## Práticas 2026 (verificadas em produção + mercado)
- **Clipes modulares** (5-8s) + montagem ffmpeg > geração longa única; regeneração pontual fica barata.
- **Rascunho barato → final caro**: variantes em modelo rápido (Veo Fast/Lite), regenerar só o take escolhido no modelo cinematográfico. Medir **custo por vídeo APROVADO**.
- Veo 3.x tem **áudio nativo** na geração — avaliar antes de assumir trilha externa; Flow = camada de edição sobre Veo.
- Prompt com **proibições explícitas** (texto, posters, rostos, silhuetas humanoides) — regra da casa pros slides ambientais.
- Edição/receita geral de vídeo (corte, concat, loudnorm, upscale, QC) → agente `video-production`.

## Verificacao minima

Use comandos equivalentes aos do projeto:

```powershell
node --check tools\finalize_veo_intro_60s_audio.mjs
npm run render:intro:veo60
npm run render:intro:veo60:final
py -3 -m py_compile tools\asset_pipeline\build_copyright_package.py
py -3 tools\asset_pipeline\build_copyright_package.py
rg -n "ritmos_intro_60s_final_fhd" docs\registro_marca\direitos_autorais\MANIFEST.csv
```

Nao declare pronto sem pelo menos: render OK, duracao/FPS/frame count OK, audio final medido, frame de logo conferido, ultimo frame sem tela preta e registros atualizados.
