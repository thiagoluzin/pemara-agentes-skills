# Acabamento de âncoras e vídeo

Declare o tipo da fonte antes da execução. Aceite `live_action`, `animation` ou `mixed`; se a classificação for incerta, resolva-a com a produção.

| Fonte e finalidade | Processamento no workflow PEMARA |
| --- | --- |
| Âncora ou imagem-base nova | DLSS 5 Natural integral no quadro, escala NR 1×, intensidade, estrutura, pele e detalhe em 1; tom e cor em 0, máscara automática desligada. Guardar fonte e recibo da execução. |
| Vídeo live action ou misto | Redimensionamento Lanczos, codificação NVENC e RIFE 4.25 a 60 FPS exatos no acabamento autorizado. |
| Vídeo de animação | SeedVR2 3B int8 na rota de upscale e RIFE 4.25 a 60 FPS exatos. |

Takes, montagens, conectores e quadros extraídos de vídeo ficam fora do processamento DLSS 5. Preserve a duração, geometria e o áudio original. Confira o resultado completo e registre qual versão o responsável avaliou.
