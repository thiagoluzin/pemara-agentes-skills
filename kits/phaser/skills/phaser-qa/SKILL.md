---
name: phaser-qa
description: "Criar regressões de lógica e testes de runtime para jogos Phaser usando entradas reais, transições contínuas e evidência diagnóstica."
---

# QA de jogos Phaser

Escolha evidência pelo risco: lógica pura para dano/cooldown/save; integração para consumidor e configuração; browser para carregamento, ponteiro, animação e cenas; aparelho para hardware/FPS. Cobertura de linhas e regex sobre código não comprovam comportamento visual.

Reproduza a falha antes da correção quando possível. Teste entradas/saídas observáveis, limites, repetição e interrupção. Não copie a fórmula de produção para formar o resultado esperado. Mocke uma fronteira indisponível, não o comportamento que deseja provar.

Em runtime, capture pageerror, console error, requisições falhas e HTTP inesperado. Espere readiness observável com timeout que preserve diagnóstico. Não use sleep fixo, retry cego ou boot forçado para fazer um teste passar. Registre versão servida, build, cenário e seed quando aplicável.

Setup determinístico pode posicionar o jogo; a ação testada deve atravessar sua entrada real. Teste pointercancel, soltura fora e dois ponteiros quando o problema envolver touch. Clique/callback direto não demonstra o mesmo caminho. Sintético no browser não certifica dispositivo físico.

Mantenha testes independentes, mas preserve intencionalmente a mesma instância de jogo no teste de progressão contínua. Compare listeners, timers, áudio e overlays antes/depois de várias fases; reiniciar a página a cada etapa esconde vazamentos de Scene reutilizada.

Golden detecta diferença, não qualidade. Não rebase para esconder regressão; registre a mudança aprovada. Abra capturas antes de afirmar aparência e veja clipes em movimento para avaliar animação.

No pacote de skills, validação de nomes/links é estrutural. Testar um exemplo executável prova apenas aquele exemplo. Avaliação de agente exige tarefa real com entradas e saída observada; não chame um teste de palavras-chave de prova comportamental.

Entregue comando, exit code, artefatos, cobertura e limitações. Execute gates exigidos pelo projeto sem mascarar exit por pipes. Amplie testes se houver mudança nova, falha ou risco ainda aberto, sem repetir baterias caras por ritual.
