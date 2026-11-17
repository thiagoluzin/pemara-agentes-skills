---
name: pemara-video-gauntlet
description: "Avalia de forma independente os três takes do piloto Gauntlet de vídeo do Maestro, usando referência visual, leitura de vídeo e um veredito rastreável."
---

# Piloto Gauntlet de vídeo

Use esta skill somente para o piloto de três takes criado pelo Maestro. Ela não
gera mídia, não altera prompts e não aprova o resultado: produz uma recomendação
independente para a decisão humana.

1. Obtenha o briefing do take em
   `GET /api/video-projects/{projectId}/takes/{takeId}/gauntlet/brief` no Maestro
   local. O briefing é a única fonte do trabalho do crítico; não leia a explicação
   ou o histórico de quem criou o take.
2. Execute `pemara_read_video` no `candidate.relativePath` resolvido contra o
   diretório do projeto. Execute `pemara_vision` na referência. Se um arquivo não
   puder ser aberto, não invente análise: use `BLOCKED`.
3. Julgue os cinco critérios do briefing. `noGeneratedText` recebe 5 somente se
   nenhum quadro inspecionado contiver texto, legenda, logo, watermark ou UI
   gerados. Não substitua a inspeção visual por uma leitura de prompt.
4. Envie um único veredito com `pemara_gauntlet_submit`. Inclua o SHA-256 do
   candidato, as cinco notas inteiras, a maior lacuna, um reparo curto de prompt
   e observações verificáveis. A API calcula o limite de duas regenerações e
   para por melhoria marginal.
5. Nunca aprove, regenere, faça upscale, modifique a fila ou inicie ComfyUI. O
   Maestro mantém a aprovação humana obrigatória.

O fluxo correto é: referência aprovada → candidato gerado → crítico novo →
recomendação rastreável → decisão humana.
