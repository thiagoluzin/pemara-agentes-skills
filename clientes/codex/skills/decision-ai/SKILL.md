---
name: decision-ai
description: Use Gemini Decision 1 for typed semantic judgments, routing, verification and multimodal triage in projects using this workflow; keep deterministic operations in code.
---

# Decisões semânticas tipadas

Usar Gemini Decision 1 para julgamentos semânticos no fluxo PEMARA e respeitar a escolha explícita do provedor. A regra não exige inferência para operações determinísticas nem autoriza mídia, gastos sem escopo ou troca dos motores de produção.

Leia a documentação viva pertinente antes de integrar: [anúncio e contrato](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/), [índice oficial](https://aistudio.google.com/llms.txt) e [tipos oficiais do SDK](https://github.com/googleapis/python-genai/tree/main/google/genai/_gaos/types/decisions). O endpoint qualificado é `POST https://generativelanguage.googleapis.com/v1beta/decisions`, modelo `gemini-decision-1`, `input` compartilhado e `questions`. Não confundir campos da antiga API TypeSafe com este contrato.

Use choice para alternativas exclusivas, noul para ocorrência e score para rubricas ordenadas. Inclua unknown quando a evidência puder faltar. Separe dimensões independentes. Uma distribuição concentrada não prova correção; avalie limiares com casos rotulados pelo proprietário. Não presuma que a amostragem de vídeo de outra API se aplica a Decisions.

Mantenha execução e limites em código: validar tipos/distribuições, limitar chamadas e tamanho, salvar evidências e consumo, encaminhar incerteza. Nenhum retry pago automático nem fallback silencioso. Forneça `GEMINI_API_KEY` pelo ambiente privado do processo. Preserve o sigilo da chave.

Para uma decisão avulsa, grave um JSON com input e questions e execute `python scripts/decide.py --request caminho.json --output recibo.json` a partir desta skill. O cliente portátil está em `scripts/decision_provider.py` e usa a biblioteca padrão do Python.

Para vídeos PEMARA, use `$pemara-video-inspection`. Decision faz triagem; o próprio Codex examina evidências e explica sem API OpenAI. Regeneração automática está desativada.

Após execução concluída do ComfyUI conduzida pelo agente, aplicar a skill instalada `performance-optimizer` e seu módulo `references/post-comfyui.md`. Interpretar gargalos com Decision quando necessário; medições determinísticas permanecem em código. Preferir scripts/terminal para uso próprio quando apropriado, sem prometer redução da memória do modelo apenas por retirar a interface.

Quando o projeto usa ai-memory, a busca e a indexação determinísticas dispensam API. A integração conserva a configuração de memória já autorizada.
