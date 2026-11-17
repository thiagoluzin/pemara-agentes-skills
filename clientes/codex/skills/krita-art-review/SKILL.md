---
name: krita-art-review
description: Faça crítica independente de pinturas e sprites do Krita sem editar a arte, vinculando achados a arquivos exatos e evidência visual. Use para revisão, comparação e diagnóstico; correção pertence às skills de edição ou animação.
---

# Crítica independente de arte

Leia pedido, referências canônicas e regras do projeto. Avalie artefatos reais sem adotar a conclusão do autor. Não pinte, transforme, altere seleção/visibilidade, salve o documento ou corrija arte durante a crítica. Informe defeitos ao coordenador para autoria separada. Revisão não autoriza promoção nem aprovação em nome do proprietário.

## Fixar a evidência

- Identifique caminhos absolutos e SHA-256 de KRA, PNGs, folha e manifest disponíveis, com versão/data observada. Documento aberto com mudanças não salvas não corresponde necessariamente ao KRA em disco. Declare essa diferença; solicite ao escritor responsável checkpoint candidato/exportação, sem descartar trabalho ou assumir escrita.
- Prefira ferramentas nativas `krita_state`, `krita_document(action="compatibility")` e `krita_preview`, com `document_id` explícito. Observe problemas de compatibilidade e ferramentas afetadas; conexão não prova cada recurso. Não ative documentos ou camadas durante a revisão da sessão compartilhada.
- Para examinar pixels do candidato/documento aberto, use imagens MCP ou um PNG realmente exportado pelo Krita; se faltar a imagem MCP, `view_image` pode ler esse PNG. Se a exportação necessária não existir, solicite ao escritor. Fontes e referências locais existentes, inclusive JPEG e outros formatos compatíveis, podem ser vistas diretamente com `view_image`, sem importar, reexportar ou modificar os originais. Não use screenshot via código ou captura externa da interface como desvio. Sem evidência visual, limite o parecer ao que os dados demonstram.
- Se o registro não expuser Krita, informe a possível necessidade de nova sessão do Codex; não reinicie Codex ou este chat. Não instale ferramentas, amplie raízes nem acione geração GPU/API para viabilizar a análise.

## Julgar o observado

Confira identidade, silhueta, proporções, lateralidade, cor, textura, anatomia, alpha e corte no canvas inteiro e detalhes relevantes. Para ciclos, compare quadros consecutivos, apoio, chão, pivô, escala, timing e emenda último→primeiro. Cópia/warp não comprova pose nova quando proibido pelo projeto. Folha estática não comprova fluidez ou execução no jogo; solicite evidência apropriada pela via autorizada, sem afirmar execução inexistente.

Relate arquivo/quadro/região, observação, regra/referência, consequência e correção sugerida. Separe defeito verificável, preferência estética e evidência insuficiente. Não invente medidas precisas a partir de miniatura.

O parecer deve indicar artefatos/hashes realmente examinados; achados priorizados; verificações técnicas, observações visuais e lacunas de reprodução/in-game distintas; e recomendação de correção ou prontidão para revisão humana. Aprovação artística permanece com o proprietário. Se o escritor mudar o candidato, o parecer vale somente para a versão examinada.

Leituras com timeout podem ser repetidas quando não alteram a sessão; resultado desconhecido de mutação alheia precisa ser esclarecido pelo escritor antes de inferir o estado.
