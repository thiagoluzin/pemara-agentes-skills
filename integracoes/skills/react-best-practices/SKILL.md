---
name: react-best-practices
description: "Revisa o custo de carregamento e renderização de telas em React e Next.js."
---

# Desempenho em React e Next.js

Escolha um fluxo real da aplicação. Registre o tempo até a primeira tela útil, as requisições que bloqueiam conteúdo e o custo dos componentes no profiler. Verifique se buscas independentes podem começar juntas e se dados compartilhados podem ser reutilizados com invalidação compatível com a sessão do usuário.

Compare a fronteira servidor/cliente com o que o usuário de fato precisa manipular. Adie o carregamento de módulos grandes usados apenas depois de uma ação. Para renderizações repetidas, localize a origem das mudanças de estado antes de aplicar memoização. Repita a medição no mesmo fluxo e verifique carregamento, erro e navegação.

Esta é uma edição funcional do catálogo, escrita para uso portátil.
