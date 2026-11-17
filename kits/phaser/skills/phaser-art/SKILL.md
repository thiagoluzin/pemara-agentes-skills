---
name: phaser-art
description: "Produzir e revisar assets, cenários, alpha, pixel art, iluminação e FX em Phaser com referências aprovadas e verificação no renderer alvo."
---

# Arte e cenografia Phaser

Identifique estilo, resolução de uso, família visual e referências aprovadas. Preserve a fonte e a identidade antes de editar. Para geração, use a ferramenta autorizada no ambiente, confira custo/quantidade e faça um piloto quando o lote depender de consistência. O kit não exige provedor, palette size fixo ou geração paga.

Antes de integrar, abra o resultado e confira silhueta na escala de gameplay, proporções, luz, alpha e bordas sobre fundos claros/escuros. Alpha binário não é uma cura universal para halo: pode destruir antialias, transparência e cabelo. Diferencie matte contaminado, premultiplicação e transparência intencional. Preserve RGB oculto quando a operação exigir ida e volta sem alteração de pixels.

Para pixel art, escolha nearest quando redimensionar; para pintura/foto, use o filtro adequado. Não imponha escala inteira a toda arte HD. Separe tamanho anatômico, enquadramento e resolução da textura. Transformações técnicas precisam manter pivôs e coordenadas esperadas pelo consumidor.

Cenário serve à leitura do jogo: ancore elementos em landmarks reais da arte e preserve contraste de personagens, telegraphs e pista. Diferencie parallax do mundo de overlay de tela. Calibre alpha/blend por captura da fase e arena após fades, na câmera real. Nenhum modo de blend é bom ou proibido em todos os projetos.

Antes de luz, normal map, máscara ou bloom, confira APIs da versão e renderer usados. Não copie receitas de pipelines Phaser 3 para Phaser 4. Uma textura de normal carregada isoladamente pode não estar associada ao diffuse; verifique a vinculação no loader/atlas. Não afirme FX em alta resolução se o render target inteiro é de baixa resolução.

Meça custo de FX com áudio e gameplay ativos. Limpe timers, listeners, partículas e overlays na transição. Aumentar efeitos sem medição pode piorar legibilidade e frame pacing.

Entregue a fonte final no caminho acordado, origem/licença, medidas e comparação visual. Contato com chão, cor e efeito precisam ser vistos em runtime; validação estrutural não aprova estética.
