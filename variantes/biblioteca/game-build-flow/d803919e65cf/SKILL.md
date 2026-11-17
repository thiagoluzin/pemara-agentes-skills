---
name: game-build-flow
description: "Conduzir a criação ou expansão de jogos do conceito ao jogável, escolhendo especialistas pelo gênero e validando controles, combate, arte, áudio, desempenho e entrega. Use para um jogo novo ou uma funcionalidade que atravessa vários sistemas."
---

# Game Build Flow — criação de jogos

## TURBO OPERATING PROTOCOL
Leia `AGENTS.md` e aplique seus gates, locks e registro no `FIXLOG.md`. Preserve decisões do usuário e mudanças existentes. Planejamento não altera o modo da sessão: se o pedido inclui implementar, continue até a verificação.

## Enquadramento e roteamento
Confirme gênero, plataforma/dispositivo, controles, loop principal, escopo e critério observável de sucesso. Use o contexto existente; pergunte apenas pelo que bloqueia. Num projeto existente, examine o runtime e o `package.json` antes de propor engine ou dependências. Não migre tecnologia por preferência do agente.

| Situação | Especialista principal | Apoio quando necessário |
|---|---|---|
| Conceito, pilares e narrativa | `creative-director` | `project-planner` para dependências e marcos |
| Beat-em-up, lanes, golpes, inimigos e bosses | `beatemup-combat-designer` | `game-developer` para sistemas |
| Platformer, salto, colisão, câmera | `phaser-platformer-architect` | `level-designer` |
| Outro gênero ou sistema transversal | `game-developer` | Escolher suporte pelo problema observado |
| Teclado/gamepad e integração de controles | `gamepad-input-specialist` | `qa-automation-engineer` para o evento real, inclusive touch |
| Sprites, escala e estados de animação | `phaser-animation-turbo` | `animation-engineer` e `hero-sprite-scaling` conforme a medição |
| Fases e curva de dificuldade | `level-designer` | `balance-tuner` |
| Arte de cenário e FX de arena | `arena-fx-scenographer` | `image-production` se houver arte raster nova |
| Som reativo e mix | `game-audio-designer` | `audio-analysis` para medições |
| FPS, hitches e memória | `performance-optimizer` | `qa-automation-engineer` para reprodução |
| Teste de jogada e regressão | `qa-automation-engineer` | `test-engineer` para lógica isolada |
| APK, executável e instalação | `demo-release-engineer` | `pack-doctor` apenas para integridade dos agentes |

Carregue somente os specs necessários à etapa. Os papéis podem ser exercidos pelo agente atual. Delegue apenas quando permitido na sessão e houver trabalho independente; atribua arquivos e entradas/saídas, sem dois escritores no mesmo arquivo. Este fluxo não exige criar novas tarefas na interface.

## Do primeiro minuto à entrega
1. **Contrato curto:** defina uma ação central, feedback, condição de sucesso/falha e o primeiro minuto jogável. Separe o que precisa existir agora do que pode esperar. No beat-em-up, prove deslocamento por lane, golpe legível e reação de um inimigo antes de multiplicar ondas.
2. **Fatia jogável:** implemente o menor encontro completo com os recursos existentes. Exercite entrada real → ação → feedback → vitória/derrota → reinício. Uma simulação mental ajuda a planejar; não comprova jogabilidade nem diversão. Registre observações de playtest e o que ainda depende de avaliação humana.
3. **Conteúdo e apresentação:** expanda fases, animação e áudio depois de validar o núcleo. Mantenha chaves, pivôs, escala, eventos de golpe e ciclo de vida dos assets explícitos. Para animação, leia `docs/GUIA_MOVIMENTO_BIOTIPOS.md`; respeite locks e gerador interno de raster, sem substituir arte final por script. Slides narrativos continuam ambientais e textos ficam no código.
4. **Integração contínua:** teste pausa/retomada, opções, derrota/reinício e ida à próxima fase sem voltar ao menu. A `StageScene` é reutilizada: verifique limpeza de listeners/timers, áudio duplicado, objetos antigos e overlays. Touch deve passar por eventos reais de ponteiro, incluindo cancelamento e multitoque; preservar controles aprovados.
5. **Desempenho:** declare dispositivo, cenário e meta antes de medir. Compare A/B alternado no mesmo alvo, com FX e áudio ligados; registre tempos de frame e hitches, não só FPS médio. Não reduza qualidade visual nem prometa 60 FPS sem evidência. Desktop não certifica Android.
6. **Entrega:** execute os gates aplicáveis e `npm run deploy:check` antes de build/entrega. Use `demo-release-engineer` quando houver pacote solicitado; confira arquivo produzido, hash, instalação/abertura e limitações verificadas. Não publicar nem gastar créditos de geração além da autorização existente.

## Checkpoints e passagem entre etapas
Cada etapa informa objetivo, arquivos reais alterados, decisões preservadas, evidência (comando/exit code/captura/medição), pendências e dependências. Só marque aprovado o critério demonstrado. Falha em gate exige investigar a causa; se o bloqueio estiver fora do escopo, preserve o log e indique-o sem declarar a entrega verde.

Consulte os scripts atuais no `package.json`. Para este projeto, os pontos de entrada incluem `npm run test:input-touch`, `npm run test:touch-runtime`, `npm run test:menu-runtime`, `npm run profile:transitions` e `npm run profile:hitches:check`. Esses comandos não comprovam, sozinhos, todas as fases nem todos os dispositivos. Quando o pedido cobrir o jogo inteiro, explicite cobertura de `fase1` a `fase7`.

Arte de heróis exige `npm run entrega:sprites`; cenário exige `npm run audit:cenario`. Teste estático, playtest, auditoria visual e pacote executável são evidências distintas. Registre correções no `FIXLOG.md` e encerre com o resultado e limites reais.
