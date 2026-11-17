---
name: web-build-flow
description: "Fluxo orquestrado \"master turbo\" para desenvolvimento web Flask + SQL + JS — amarra requisitos, schema, API Flask, frontend e testes na ordem certa, com checkpoints e contratos entre etapas. Use para construir/expandir um app ou microserviço web do plano ao testado. Triggers on flask, app web, microserviço, api, sql, schema, backend, frontend, fullstack, pipeline web, web flow."
---

# Web Build Flow — Flask + SQL + JS (master turbo)

Você conduz o desenvolvimento web do plano ao testado, **amarrando os especialistas** com contratos claros entre etapas. Qualidade master: nada de remendo, ajuste direto no código, tudo registrado.


## O pipeline (com checkpoints)

| # | Etapa | Especialista | Entrega | ✅ Checkpoint pra avançar |
|---|-------|--------------|---------|---------------------------|
| 1 | Requisitos & plano | `product-owner` → `project-planner` | user stories + tarefas pequenas + critérios | Escopo e "sad path" claros? |
| 2 | Dados / SQL | `database-architect` | schema, índices, migração, queries | Migração aplica; queries sem N+1 |
| 3 | API Flask | `backend-specialist` | blueprints, rotas, auth, **sessão persistente** | Endpoints respondem; sessão sobrevive a restart |
| 4 | Frontend JS | `web-frontend-vanilla` | HTML/CSS/JS integrando a API | Renderiza, navega por teclado, trata erro |
| 5 | Revisão | `reviewer` | achados acionáveis | Bugs cross-cutting pegos |
| 6 | Testes | `test-engineer` → `qa-automation-engineer` | unit + E2E | Suite verde; fluxo crítico coberto |

> 💡 Sessão Flask que cai é dor recorrente — a etapa 3 deve usar **flask-session (filesystem)** com `PERMANENT_SESSION_LIFETIME` e testar persistência através de restart do worker. Registre o conserto no FIXLOG.

## Contrato da API (trava antes do front)
Antes da etapa 4, **congele o contrato** (rotas, payloads, códigos de erro). Front e back trabalham contra o mesmo contrato — muda contrato, avisa os dois lados. Isso evita o retrabalho que mais queima cota.

## Anti-remendo no fluxo
Bug de sessão/schema/query se conserta na **causa raiz** (config de sessão, schema, índice), não com `try/except` por cima nem flag mágica. Ajuste direto no código, entrada no `FIXLOG.md`.

## Quando me usar
- Construir/expandir um app ou microserviço Flask
- Coordenar requisitos → SQL → API → front → testes
- Padronizar qualidade "master turbo" num projeto web
