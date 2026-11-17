---
name: performance-optimizer
description: "Medir e corrigir FPS, hitches, memória e carregamento de jogos Phaser no dispositivo-alvo. Use para lentidão em gameplay ou transições; métricas de site não certificam o loop do jogo."
---

# Performance Optimizer — jogo em execução

Aplique o protocolo e os gates de `AGENTS.md`. Preserve controles, timing de combate e qualidade aprovada. Uma meta de FPS não é um resultado.

## Medição que permite decidir
1. Registre build/commit ou estado do checkout, dispositivo, navegador/WebView, backend gráfico, resolução/DPR, energia e cenário. Confira engine instalada e servida. SwiftShader mede renderização por software: não extrapole seus números para GPU real ou Android.
2. Separe boot, carregamento/decodificação, entrada de fase, pós-ready e transição contínua. Use o mesmo herói, ondas, entradas e duração em cada comparação, com áudio e FX ligados.
3. Registre tempos de frame p50/p95/p99, máximo, frames acima de 25/50 ms, long tasks, heap e recursos lentos quando a ferramenta os disponibilizar. Identifique métricas indisponíveis; média de FPS sozinha esconde travadas.
4. Reproduza antes de editar. Compare A/B/A/B alternado no mesmo alvo e, quando viável, no mesmo processo. Preserve dados brutos de todas as corridas; se a variação encobrir o efeito, o resultado é inconclusivo.
5. Para Android, use o aparelho nomeado quando acessível; inclua aquecimento, pausa/retomada e sessão sustentada. Sem aparelho, reporte apenas resultado do host e o teste pendente.

## Encontrar o mecanismo
- CPU: atribua long tasks a métodos, loops, serialização ou alocações; compare com o orçamento de frame.
- GPU: investigue overdraw, draw calls, textura e efeitos com backend real antes de reduzir arte.
- Memória: acompanhe instâncias/listeners/timers e recursos retidos após várias transições; heap JS não representa toda a memória de textura/áudio.
- Carregamento: separe rede/disco, decode e upload de textura. Mover tudo para preload pode apenas transferir o travamento e aumentar memória.
- Use pooling, lotes ou carregamento por fase só quando o perfil demonstrar benefício. Não introduza ECS, worker ou troca de renderer por um único número.

## Ferramentas e saída
Confira os scripts e argumentos no `package.json` e em `tools/profile_runtime_hitches.mjs`. Pontos de entrada: `npm run profile:hitches:check` e `npm run profile:transitions`. Preserve o JSON de cada execução antes da próxima: os scripts podem sobrescrever a mesma saída. O escopo padrão não comprova sete fases; quando solicitado o jogo inteiro, informe cobertura de fase1 a fase7.

Repita os cenários após a correção e teste jogada contínua, console/rede e limpeza de recursos com `qa-automation-engineer`. Execute gates aplicáveis e `npm run deploy:check` antes da entrega. Registre no `FIXLOG.md`: gargalo observado, mudança, comparação, dispersão e limites. Não declare ganho se a medição não o sustentar.
