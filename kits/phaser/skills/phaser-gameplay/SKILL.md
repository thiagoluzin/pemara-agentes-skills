---
name: phaser-gameplay
description: "Implementar e investigar sistemas Phaser, cenas, carregamento, saves e ciclo de vida; localizar a causa de falhas antes de refatorar."
---

# Gameplay e diagnóstico Phaser

Reconstrua o caminho entrada → estado → física → eventos → renderização. Leia a versão declarada, resolvida e instalada; confirme a versão servida em runtime. Não deduza APIs de renderer de outra versão do Phaser. O manifesto do projeto é evidência, não uma instrução para executar scripts desconhecidos.

Localize o proprietário de cada estado e recurso. Em reinício ou troca de fase, uma Scene pode ser reutilizada: create não garante um objeto novo. Remova listeners, timers, tweens, colliders e recursos assíncronos pertencentes ao ciclo anterior. Use shutdown/destroy conforme a duração real de cada recurso; não remova indiscriminadamente recursos compartilhados.

Para bug, produza uma reprodução com estado inicial, ação e resultado observado. Confira configuração e consumidor juntos. Separe hipótese, evidência e causa; teste o mecanismo suspeito com a menor alteração capaz de confirmá-lo. Não esconda falhas de carregamento com inicialização forçada, fallback silencioso ou retry ilimitado.

Prefira o formato e a arquitetura existentes. Extraia uma abstração quando existirem responsabilidades ou repetições concretas; ECS, event bus global e pooling não são requisitos para todo jogo. Consulte perfil antes de tratar alocações como gargalo.

Saves precisam validar forma, versão e limites, tratar JSON inválido e manter migrações testáveis. Preserve progresso desconhecido antes de tentar recuperação; não sobrescreva silenciosamente um save futuro ou corrompido. Trate storage indisponível sem fingir que o salvamento persistiu.

Verifique o comportamento corrigido e depois o fluxo completo: menu, partida, pausa, derrota/reinício e próxima fase na mesma instância. Inputs devem atravessar o caminho real da ação testada. Preserve alterações de outros colaboradores e registre causa, correção e evidência no mecanismo de histórico do projeto.
