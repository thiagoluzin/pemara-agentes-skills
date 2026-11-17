---
name: krita-mcp-workflow
description: Edite pinturas, camadas, seleções e paletas no Krita pelo MCP nativo, preservando o KRA e conferindo a arte. Para ciclos use krita-sprite-animation; para crítica sem edição use krita-art-review.
---

# Edição nativa no Krita

Leia instruções e referências do projeto; mantenha estilo, motores e escopo escolhidos. Esta skill é global: identidade, engine e máximo de quadros por folha pertencem ao projeto. Execute as etapas reversíveis já autorizadas sem pedir confirmação a cada passo. Não instale componentes, amplie raízes permitidas ou acione geração GPU/API por implicação.

## Conectar e delimitar

- Descubra primeiro ferramentas Krita no registro nativo. Leia `krita_state` e, se necessário, `krita_document(action="compatibility")`: examine `runtime_compatibility`, recursos e problemas com ferramentas afetadas; evite operações indisponíveis. Instalação ou versão nominal não comprova funcionamento.
- Se Krita não aparecer no registro, a descoberta pode exigir uma nova sessão do Codex. Informe a limitação; não reinicie o aplicativo ou este chat. Não substitua ferramenta ausente por screenshot via código.
- Somente quando o registro ainda não expuser Krita, consulte [fallback de sessão](references/session-fallback.md) para o cliente MCP STDIO já instalado. `NO_ACTIVE_DOCUMENT` indica ausência de documento ativo, não comprova falha da conexão: use a listagem de documentos antes de concluir.
- Liste documentos, identifique o alvo por caminho/conteúdo e use `document_id` explícito em leituras e alterações; confira o UUID da camada. IDs de documentos expiram ao fechar/reabrir ou reiniciar Krita: releia os IDs substitutos. Não dependa apenas do documento ativo.
- Um único agente escreve na sessão compartilhada do Krita por vez, inclusive entre documentos. Combine a posse com o coordenador; leitores não devem alternar seleção, clipboard ou visibilidade durante a edição. Não reverta trabalho alheio. Se houver edição manual, releia estado e preview: `bridge_revision` só conta mutações da ponte, não todas as alterações externas.

## Editar e conferir

1. Inspecione preview, dimensões, camadas, seleção e estado modificado. Preserve originais e trabalhos abertos; salve KRA candidato versionado numa raiz já permitida com `krita_save_export`, sem sobrescrever. Trabalhe na cópia identificada e não feche descartando alterações.
2. Use ferramentas nativas: `krita_brush`, `krita_draw`, `krita_paint_path`, `krita_layers`, `krita_edit` e `krita_color`, conforme o esquema disponível. Produza mudanças reais; camadas vazias não comprovam pintura. Referências importadas precisam de autorização/proveniência e devem permanecer distinguíveis da autoria nova.
   No backend 0.2.2 instalado, `krita_layers(action="create")` anexa a camada no topo e ignora `above_id`; confirme a pilha retornada. Para posicionar a camada, use depois `action="reorder"` com `above_id` explícito e confira novamente estado e preview. Criar camadas na ordem inversa pode ocultar braços e outros elementos já pintados; não repinte conteúdo oculto antes de corrigir a pilha.
3. Edite em lotes pequenos; inspecione `krita_preview` após mudanças reais de conteúdo. Confira canvas inteiro e detalhes relevantes. Sucesso de chamada, bounds ou `verified_content_change` não substituem observar a arte.
4. Salve o candidato e exporte PNG quando útil. Entregue caminhos absolutos, SHA-256 dos arquivos finais, alterações observadas e limitações. Revisão técnica não concede aprovação artística do proprietário.

## Recuperação e limites

- Em timeout de mutação com resultado desconhecido, inclusive `BRIDGE_TIMEOUT` com `operation_may_complete=true`, não repita a chamada. Espere a operação terminar, respeite `BRIDGE_BUSY` e inspecione estado, preview e arquivos. Só repita quando puder demonstrar que a mudança não foi aplicada. Falha persistente encerra a sequência dependente com evidência do bloqueio.
- `krita_paint_path` pode criar um undo por segmento; outras operações têm contratos distintos. Use as contagens retornadas, nunca desfaça trabalho manual concorrente.
- Antes de transformar, leia os limites instalados. No contrato 0.2.2, máscaras e transformações diretas têm guardas de sequência/backend, backups e diferenças de undo. Respeite `UNSAFE_TRANSFORM_*`, sem contornar limites por repetição. Salvar/reabrir pode trocar IDs; reiniciar Krita exige preservar todos os documentos e autorização aplicável.
- Para comprovar os pixels do candidato/documento aberto, prefira o preview MCP ou um PNG realmente exportado pelo Krita; se a imagem MCP não for entregue, use `view_image` nesse PNG. Fontes e referências locais existentes, inclusive JPEG e outros formatos compatíveis, podem ser inspecionadas diretamente com `view_image`, sem importar, reexportar ou modificar os originais. Isso não autoriza screenshot externo ou captura programática da interface como desvio, nem pintura por biblioteca de imagens ou rerenderização em outro motor.

Para detalhes consulte o esquema atual e `docs/tool-reference.md da versão instalada do Krita MCP`. Não generalize um teste bem-sucedido para todas as capacidades.
