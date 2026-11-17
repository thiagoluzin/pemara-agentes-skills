---
name: video-production
description: "Especialista em CRIAÇÃO e EDIÇÃO de vídeo — geração IA (Veo, Higgsfield, Flow, Sora, Kling), edição/montagem ffmpeg (corte, concat, overlay, legendas, mix de áudio, loudnorm, upscale), QC visual por contact sheet, e formatos/codecs por destino. Para intro/cutscene DE JOGO com registro de marca, rotear pra ai-video-intro-pipeline. Triggers on vídeo, video, editar vídeo, criar vídeo, gerar vídeo, ffmpeg, corte, montagem, render, codec, mp4, veo, sora, kling, flow, upscale vídeo, legenda, contact sheet."
---

# Video Production (criar e editar vídeo)

Você produz vídeo de ponta a ponta: gera com IA, monta com ffmpeg, mede com ffprobe, e só aprova o que passou por QC visual de verdade. Clipes de IA são **matéria-prima**, nunca entrega final.


## Pipeline IA 2026 (aprendido em produção + estado da arte)
1. **Clipes curtos modulares** (5-8s cada), nunca "um vídeo de 60s de uma vez" — montagem modular simplifica revisão e regeneração pontual.
2. **Rascunho barato → seleção → final caro**: variantes com modelo leve (Veo Fast/Lite), escolha a mais forte, regenere só ela no modelo cinematográfico. Meça **custo por vídeo APROVADO**, não por segundo gerado.
3. **Prompt com proibições explícitas**: modelos alucinam texto/posters/rostos/formas humanoides — proíba no prompt o que a direção de arte veta (aprendido no take 01/05 da intro).
4. **QC por take**: contact sheet + ffprobe (resolução/fps/duração exatos) antes de aceitar no timeline.
5. **Áudio por último**: monte o vídeo mudo (validação visual limpa), aplique trilha/mix num passo final separado com loudnorm medido.
6. Modelos (estado 2026): Veo 3.x (físicas/cinemática, áudio nativo), Sora 2, Kling 3.0, Higgsfield (MCP no projeto). Flow = camada de edição sobre Veo.

## Receitas ffmpeg essenciais (todas já validadas no projeto)
```bash
# medir (SEMPRE antes e depois)
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate,codec_name -of default=nw=1 in.mp4
# concat sem re-encode (só se codec/fps/res idênticos!)  → senão, re-encode uniforme
ffmpeg -f concat -safe 0 -i lista.txt -c copy out.mp4
# re-encode uniforme de take IA (24fps, alta qualidade p/ intermediário)
ffmpeg -i take.mp4 -r 24 -vf scale=1280:720:flags=lanczos -c:v libx264 -crf 14 -preset slow -an take_norm.mp4
# contact sheet p/ QC visual
ffmpeg -i in.mp4 -vf "select=not(mod(n\,48)),scale=320:-1,tile=6x5" -frames:v 1 qc_sheet.jpg
# upscale FHD com nitidez
ffmpeg -i in.mp4 -vf "scale=1920:1080:flags=lanczos,unsharp=5:5:0.6" -c:v libx264 -crf 16 out_fhd.mp4
# trilha + loudness broadcast (2-pass: medir, depois aplicar)
ffmpeg -i vid.mp4 -i musica.mp3 -filter:a loudnorm=I=-16:TP=-1.5:LRA=11 -map 0:v -map 1:a -c:v copy -shortest out.mp4
# imagem única sem warning de sequência
... -update 1 -frames:v 1 out.jpg
```
Gotchas do projeto: `-frames:v 1` precisa de `-update 1` p/ JPG único; NUNCA pipe `| tail` em render (mascara exit code); `.env` de API keys sem BOM (PowerShell grava UTF-16 por padrão).

## Formatos por destino
| Destino | Container/codec | Notas |
|---------|-----------------|-------|
| Jogo (.exe/web) | MP4 H.264 + AAC | compatibilidade máxima; CRF 16-20 |
| Intermediário de edição | H.264 CRF 14 preset slow | quase-lossless, ainda leve |
| Social vertical | MP4 H.264 9:16 | usar `reframe`/crop consciente, não squash |
| Arquivo/master | original intocado | nunca sobrescrever master |

## Anti-padrões
| ❌ Não | ✅ Faça |
|--------|---------|
| Aprovar sem olhar frames | contact sheet + inspeção visual |
| Concat de takes com fps/res mistos | normalizar tudo antes |
| "Um vídeo de 60s numa geração" | clipes modulares + montagem |
| Fade em todo corte "pra disfarçar" | corte seco onde a música pede |
| Custo medido por segundo gerado | custo por vídeo APROVADO |
| Sobrescrever o master original | trabalhar em cópia, master intocado |

## Quando me usar
- Criar vídeo com IA (qualquer modelo) ou montar/editar vídeo existente
- Converter, cortar, legendar, upscalar, mixar áudio em vídeo
- Diagnosticar problema de render/codec/sync
- **Intro/cutscene de JOGO com logo/registro** → `ai-video-intro-pipeline` (fluxo completo específico)
