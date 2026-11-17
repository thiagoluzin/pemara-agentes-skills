---
name: phaser-performance
description: "Investigar FPS, frame pacing, memória e carregamento em jogos Phaser mediante perfil no dispositivo alvo e comparação A/B."
---

# Desempenho Phaser

Registre build, dispositivo, navegador/WebView, renderer, resolução/DPR, energia e cenário. SwiftShader e GPU real são condições distintas; desktop não certifica telefone. Uma meta de FPS não é resultado e Lighthouse não mede toda a jogada.

Separe boot, download/leitura, decode, upload de textura, entrada de cena, gameplay e transição. Mantenha personagem, ondas, entradas, duração, áudio e FX equivalentes. Para mobile, inclua aquecimento e sessão sustentada quando o aparelho estiver disponível.

Colete tempos de frame p50/p95/p99, máximo, contagens acima de limites relevantes, long tasks e memória disponível. Guarde dados brutos por corrida. JS heap não inclui toda memória gráfica e de áudio; métricas indisponíveis devem ser explicitadas.

Compare A/B/A/B alternado no mesmo alvo; mesma sessão/processo quando viável. Se a dispersão encobrir o efeito, conclua inconclusivo. Uma única corrida antes e outra depois não isolam carga de fundo e aquecimento.

Localize o mecanismo: CPU por tarefas e alocações; GPU por overdraw/texturas/efeitos; memória por retenção ao trocar cenas; carregamento por estágios. Mover tudo para preload pode transferir a travada e aumentar retenção. Pooling, atlases, workers e redução de qualidade só entram quando o perfil sustentar a decisão.

Preserve controles, combate e apresentação aprovada. Teto de pool deve ter comportamento definido quando esgota, especialmente para objetos essenciais. Não descarte inimigo necessário à progressão só para limitar alocação.

Após corrigir, repita o cenário e transições contínuas. Relate efeito, variabilidade, custo visual, dispositivo e limites. Não prometa 60 FPS ou melhora de bateria a partir de análise estática.
