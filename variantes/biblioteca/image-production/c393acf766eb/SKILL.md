---
name: image-production
description: "Especialista em CRIAÇÃO e EDIÇÃO de imagem/foto — geração IA com consistência de estilo (referência + paleta + luz travadas), edição técnica (recorte, alpha, chroma, upscale, remoção de fundo), QC visual obrigatório e integração do asset na pasta real. Para MEDIR/fatiar spritesheet existente, rotear pra sprite-image-reading; para look HD-2D, modern-pixel-art-hd. Triggers on imagem, foto, gerar imagem, editar imagem, arte, asset visual, background, ilustração, remover fundo, chroma, upscale imagem, paleta, referência de estilo, imagegen."
---

# Image Production (criar e editar imagem)

Você produz arte raster de ponta a ponta: gera com IA mantendo consistência de estilo, edita com precisão técnica, e só entrega asset que passou por QC visual e chegou na pasta real do projeto.


## Consistência de estilo em geração IA (estado da arte 2026)
A IA de 2026 é forte em arte de frame único (personagem parado, ícone, fundo, concept) e ainda fraca em frames de animação consistentes e tiles perfeitos. Pra manter um conjunto coeso:
1. **Trave o estilo**: mesma imagem de referência + mesmo template de prompt em toda geração da família.
2. **Trave a paleta**: 8-16 cores nomeadas no prompt; mais que isso deriva. Elemento importante contrasta por VALOR, não só matiz.
3. **Trave a luz**: uma direção declarada (ex.: "luz do topo-esquerda") em TODOS os assets — só isso já faz o conjunto parecer do mesmo jogo.
4. **Varie a partir de uma base**, não do zero: gerar variações de um asset aprovado > gerar irmãos independentes.
5. **IA pra volume, mão pra acabamento**: gere N variações, escolha as melhores, refine no editor (Aseprite/Krita). Quem entrega usa os dois.
6. **Proibições no prompt**: sem texto/letreiro/marca d'água/rosto extra — modelos adoram alucinar tipografia.

## Edição técnica (Pillow/ffmpeg — receitas do projeto)
```python
from PIL import Image
import numpy as np
img = Image.open("in.png").convert("RGBA")
print(img.size, img.mode)
a = np.array(img)
# bbox real do conteúdo (ignora transparente)
ys, xs = np.where(a[...,3] > 8)
print("bbox:", xs.min(), ys.min(), xs.max(), ys.max())
```
- **Recorte de alpha sem halo**: binarize alpha com limiar baixo (>8), NÃO preencha buracos que carregam matte escuro (aprendido na extração da logo).
- **Chroma key**: distância no espaço de cor + limpeza de borda (precedente: pipeline green-magenta dos inimigos F2).
- **Upscale**: Lanczos + unsharp leve pra foto/pintura; pixel art SÓ inteiro (2×/3×, nearest) — nunca Lanczos em pixel art.
- **Remoção de fundo**: ferramenta dedicada (MCP remove_background / rembg) > threshold manual, exceto em chroma controlado.
- Nomenclatura: `[tipo]_[objeto]_[variante]_[estado].png`; prompt usado salvo em `.json`/`.md` ao lado (padrão `pen_drive/imagegen_outputs`).

## QC de imagem (gate de saída)
| Checagem | Como |
|----------|------|
| Estilo bate com a família | lado a lado com referência aprovada |
| Silhueta legível | preview em thumbnail/preto chapado |
| Alpha limpo | fundo quadriculado ou sobre cor viva |
| Dimensões/escala | Pillow + teste no destino real (jogo/tela) |
| Sem alucinação | zoom em texto/mãos/bordas |

## Anti-padrões
| ❌ Não | ✅ Faça |
|--------|---------|
| Arte final por script procedural | geração IA + validação visual (regra do projeto) |
| Prompt novo do zero a cada asset | template + referência + paleta travados |
| Aprovar sem abrir a imagem | QC visual sempre |
| Lanczos/blur em pixel art | escala inteira nearest |
| Alpha com halo/matte | limiar correto, sem preencher buraco escuro |
| Asset órfão fora da pasta real | copiar pro destino + testar carregando |

## Quando me usar
- Gerar imagem/foto/arte nova com IA (personagem, fundo, UI, ilustração, foto tratada)
- Editar: recortar, redimensionar, limpar alpha, chroma, upscale, converter
- Montar famílias de assets consistentes (estilo/paleta/luz travados)
- **Medir/fatiar spritesheet existente** → `sprite-image-reading` · **Look HD-2D/polish** → `modern-pixel-art-hd`
