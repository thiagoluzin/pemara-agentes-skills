---
name: krita-sprite-animation
description: Produza ou corrija ciclos de sprites no Krita, com quadros completos, registro, timing e exportação verificável. Use para animação e folhas; edição geral pertence a krita-mcp-workflow e crítica independente a krita-art-review.
---

# Sprites e ciclos no Krita

Use [krita-mcp-workflow](../krita-mcp-workflow/SKILL.md) para conexão, capacidades, escritor único, IDs explícitos, KRA versionado e recuperação de timeout. Leia regras do projeto sobre identidade, direções, estilo, engine, limite por folha e rejeitados. Não imponha um máximo global de quadros nem acione GPU/API ou troca de motor sem autorização específica.

## Construir movimento legível

- Inspecione referências e ciclo existente; diferencie original, candidato e rejeitado. Referências locais existentes, inclusive JPEG e outros formatos compatíveis, podem ser vistas diretamente com `view_image`, sem importação, reexportação ou alteração dos originais. Pixels do candidato/documento aberto precisam de preview MCP ou exportação real do Krita; não use captura programática da interface como desvio. Defina ação, direção, duração, contato/apoio/passagem e âncoras temporais antes dos intermediários. Cada quadro contém a personagem inteira e margem para a maior pose; preserve identidade, roupa, proporções, objetos e lateralidade.
- Estabeleça canvas/célula, chão, escala e pivô compartilhados. Use bounds e alpha renderizado para detectar cortes; evite crop independente por quadro, que pode criar saltos. Contato dos pés, transferência de peso e deslocamento corporal devem sustentar o movimento, não apenas transladar a imagem inteira.
- Desenhe mudanças reais de pose com recursos nativos e confira cada alteração em preview. Quando proibido pelo projeto, não conte cópias, espelhamento, recortes articulados, warp ou deformações como desenhos novos. Reuso permitido como referência/registro permanece identificado.
- Compare poses consecutivas e emenda último→primeiro: trajetória, volume, mãos/pés, apoios, velocidade e silhueta. Examine velocidade normal, lenta e quadro a quadro por recurso de reprodução disponível. Se não houver reprodução observável, declare essa lacuna; quadro isolado não comprova ciclo.

## Exportar e validar

- Confirme suporte real antes de `krita_asset(action="export_animation")`. No MCP 0.2.2 esta ação interpreta filhos diretos de pintura/grupo como frames; não controla toda a timeline nativa, onion skin ou keyframes. Declare ordem por `frame_ids`.
- Configure duração, loop, colunas, padding e pivô conforme o projeto. Use `crop="canvas"` ou `crop="union"` para crop compartilhado; confira margem e pivô após recorte. Não presuma duração variável pelo parâmetro único `frame_duration_ms`: preserve o timing em evidência e use um fluxo compatível autorizado.
- Exporte para diretório candidato novo; preserve KRA, frames, folha e manifest. O pacote 0.2.2 usa nomes/esquemas Unity; isso não autoriza trocar a engine. Adapte somente metadados necessários ao destino solicitado, preservando fontes e hashes.
- Confira PNGs reais: quantidade, ordem, dimensões, alpha, bounds, offsets, pivô, timing e SHA-256. Manifest coerente não prova movimento. Não sobrescreva diretórios desconhecidos nem integre rejeitados.
- Para mudança no jogo autorizada, confira o ciclo renderizado na engine selecionada: registro, cadência, transições e leitura em movimento. Sem essa execução, entregue candidato de autoria com revisão em jogo pendente. Diferencie exportado, integrado, verificado tecnicamente e aprovado pelo proprietário.

Entregue caminhos absolutos do KRA/pacote, hashes finais, comparação observada com referências, defeitos, lacunas e ponto exato de retomada.
