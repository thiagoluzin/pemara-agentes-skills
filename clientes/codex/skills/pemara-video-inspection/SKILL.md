---
name: pemara-video-inspection
description: Inspect video defects with Gemini Decision, investigate the saved temporal evidence inside Codex, and attach explanations to PEMARA timeline markers without automatic regeneration or an OpenAI API key.
---

# Inspeção Decision + Codex

O CLI e os serviços de vídeo são dependências do Maestro. Os caminhos a seguir são relativos à raiz desse checkout. Para usar o modo de explicação, o job já deve conter a evidência e os hashes correspondentes.

Use para analisar um MP4 autorizado ou explicar um job existente. Não gerar, regenerar, substituir, aprovar ou publicar mídia. Decision faz triagem; GPT explica aqui no Codex, sem API OpenAI. Preserve a fonte, o áudio e aspectos aprovados. ComfyUI não participa desta etapa.

CLI canônica: `pemara/scripts/inspect_video.py`. Funciona sem servidor nem navegador. O painel PEMARA oferece a mesma inspeção e uma timeline própria; não altera composições do HyperFrames.

## Analisar

Execute `python pemara/scripts/inspect_video.py analyze --source CAMINHO --content-kind animation|live_action|mixed [--reference IMAGEM] [--expected-state TEXTO] [--fps 2|12|24] [--max-calls 40]`. Prefira 12/24 FPS em ação rápida. Não use material privado sem autorização de envio ao Google. O piloto aceita até 60 s, quatro referências de até 2 MB e orçamento explícito de chamadas. Não reexecute um job interrompido sem verificar o recibo: `--request-id` existente apenas retorna o resultado, sem repetir cobrança.

Resultados: `pemara/dados/studio/video_inspection/JOB/`. O CLI mostra relatório, pedido ao Codex e métricas de RAM. A fonte importada fica no editor_suite, com hash. O processo recebe `GEMINI_API_KEY` pelo ambiente privado.

## Investigar aqui no Codex

Leia `codex_request.md`, `record.json` e `evidence.json`. Antes de concluir, confira hashes e examine imagens reais dos índices de cada marcador com view_image. Referências são os padrões canônicos; frames extraídos não se tornam referências aprovadas. Examine sequência temporal e contatos, sem afirmar que viu o vídeo inteiro se só observou amostras. Trechos selecionados não provam qualidade do restante. A localização do marcador é a janela examinada, não um milissegundo descoberto pelo modelo.

Para cada marcador revisado, diferencie `observed_defect`, `false_positive` ou `uncertain`. Relate observação concreta, hipótese de causa separada e sugestão de correção que preserve os aspectos aprovados. Não transformar o palpite do Decision em fato. Sem áudio efetivamente revisado, sincronismo permanece uncertain; o backend não aceita confirmação sonora por análise apenas visual.

Grave JSON com `origin: "codex"`, `sourceSha256`, `evidenceSha256` copiados do relatório e `explanations`: lista de objetos com `markerId`, `verdict`, `observed`, `hypothesis`, `correction`, `frameIndices`. Os índices precisam pertencer à janela do marcador. Não inventar campos, evidências, aprovação humana ou execução de correção.

Importe com `python pemara/scripts/inspect_video.py explain --job JOB --file CAMINHO.json`. O backend valida fonte e evidências por hash, preserva cada versão da explicação e atualiza os marcadores. Atualize a inspeção no painel. `REVIEW_READY` significa disponível para revisão do proprietário, nunca aprovação artística.

## Acompanhar

`status --job JOB` consulta; `cancel --job JOB` pede cancelamento entre operações limitadas; a chamada externa atual pode levar até 60 s. `recover --job JOB` só marca um processo morto como interrompido e não reenvia nada. Falha de provedor é explícita e não usa Jev ou fallback. Limiares são experimentais: medir falsos positivos, defeitos perdidos e custo em casos rotulados pelo proprietário antes de automatizar correção.
