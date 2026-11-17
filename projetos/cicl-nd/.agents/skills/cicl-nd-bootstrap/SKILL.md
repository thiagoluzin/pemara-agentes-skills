---
name: cicl-nd-bootstrap
description: "Bootstrap do monorepo CICL-ND: estrutura, CI, Docker Compose, convenções e padrões de código."
---

# CICL-ND — Skill de Bootstrap e Arquitetura

## Domínio

Fase 01: Bootstrap do repositório, estrutura monorepo, CI/CD, ambientes locais e convenções.

## Quando usar

- Criar a estrutura inicial do monorepo;
- configurar CI com SAST, testes e SBOM;
- definir Docker Compose para desenvolvimento;
- estabelecer convenções de código TypeScript estrito;
- configurar linters, formatters e type-checkers;
- criar pacotes compartilhados;
- preparar scripts de bootstrap.

## Documentos de referência

- `docs/02_ARQUITETURA_DE_REFERENCIA.md`
- `docs/03_ARVORE_REPOSITORIO.md`
- `docs/14_DEVOPS_OBSERVABILIDADE_SRE.md`
- `fases/FASE_01_BOOTSTRAP.md`
- `AGENTS.md` (regras de implementação)

## Stack de referência

| Camada | Tecnologia |
|---|---|
| Web | Next.js + React + TypeScript |
| API | NestJS + TypeScript |
| Validação | Zod |
| ORM | Prisma + SQL controlado |
| Banco | PostgreSQL |
| Vetores | pgvector |
| Cache/fila | Redis + BullMQ |
| Objetos | S3 compatível (MinIO no dev) |
| Identidade | OIDC (Keycloak local) |
| Antimalware | ClamAV |
| Observabilidade | OpenTelemetry |
| Contêiner | Docker |
| CI/CD | pipeline com SAST, testes, SBOM |

## Regras obrigatórias

1. TypeScript em modo estrito, sem `any`.
2. Nomes de domínio em inglês no código.
3. `snake_case` no banco, `camelCase` em JSON.
4. IDs UUIDv7 ou ULID.
5. Datas em UTC (`timestamptz`).
6. Sem importação circular.
7. Sem lógica clínica em componentes de UI.
8. Sem acesso direto ao storage pelo navegador.
9. Sem dados sensíveis em commits.
10. Segredos nunca no repositório.

## Estrutura do monorepo

```
cicl-nd/
├── apps/
│   ├── web/          # Next.js
│   ├── api/          # NestJS
│   ├── worker/       # Jobs assíncronos
│   └── fhir-gateway/ # FHIR R4
├── services/
│   ├── ai-gateway/   # Gateway de IA
│   └── model-runtime/
├── packages/
│   ├── domain/       # Entidades e regras puras
│   ├── contracts/    # Schemas e tipos
│   ├── database/     # Cliente, tenant context, outbox
│   ├── auth/         # Claims, policies, decorators
│   ├── audit/        # Eventos, hash chain, redaction
│   ├── observability/
│   ├── feature-flags/
│   ├── fhir/
│   ├── ui/
│   ├── test-factories/ # Dados sintéticos
│   └── config/
├── prisma/
│   ├── schema.prisma
│   ├── migrations/
│   └── seeds/
├── infra/
│   ├── compose/
│   ├── terraform/
│   ├── kubernetes/
│   ├── monitoring/
│   └── policies/
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── clinical/
│   ├── privacy/
│   ├── security/
│   ├── validation/
│   ├── status/
│   └── adr/
├── scripts/
├── tests/
└── .github/
```

## Fluxo de trabalho

### BS-001: Criar estrutura do monorepo

1. Criar diretórios conforme `docs/03_ARVORE_REPOSITORIO.md`.
2. Configurar `package.json`, `pnpm-workspace.yaml`, `turbo.json`.
3. Configurar `.editorconfig`, `.gitignore`, `.env.example`.
4. Criar `tsconfig.base.json` com strict mode.

### BS-002: Configurar CI

1. Pipeline com stages: lint, typecheck, test, build, SAST, SBOM.
2. Branch protection rules.
3. Pull request template.
4. Secret scanning.

### BS-003: Docker Compose local

1. PostgreSQL com extensões (pgvector).
2. Redis.
3. MinIO.
4. Keycloak.
5. ClamAV.
6. Prometheus/Grafana/Loki.
7. healthchecks e dependências.

### BS-004: Pacotes compartilhados

1. `packages/domain` — entities, value objects.
2. `packages/contracts` — Zod schemas, types.
3. `packages/database` — Prisma client, tenant context.
4. `packages/auth` — decorators, policies.
5. `packages/audit` — audit event writer.
6. `packages/test-factories` — factories sintéticas.

### BS-005: API skeleton

1. NestJS app com bootstrap.
2. Módulo de health check.
3. Configuração de logging sem dados clínicos.
4. Error filter com Problem Details.
5. OpenAPI generator.

### BS-006: Web skeleton

1. Next.js app router.
2. Layout base com acessibilidade.
3. Configuração i18n.
4. Componentes UI compartilhados.
5. Test setup.

## Convenções de código

### Módulos de domínio

```
module/
├── domain/          # entities, value objects, events
├── application/     # use cases, ports
├── infrastructure/  # repository, external services
├── presentation/    # controllers, DTOs
└── tests/
```

### Regras de dependência

```
presentation -> application -> domain
infrastructure -> application/domain
domain -> nenhum framework
```

### Commits

- Uma branch por tarefa: `feat/ID-descricao`, `fix/ID-descricao`, `docs/ID-descricao`.
- Commits pequenos, sem dados sensíveis.
- PR obrigatória.

## Testes obrigatórios

- Lint passa.
- Typecheck passa.
- Build passa.
- Testes unitários dos pacotes.
- Docker Compose sobe e healthchecks passam.
- API responde health check.

## Portão de saída da Fase 01

- Monorepo funcional localmente.
- CI pipeline verde.
- Docker Compose com todos os serviços.
- Skeleton da API e Web funcionando.
- Pacotes compartilhados com testes.
- Aprovação de arquitetura.

## Saída obrigatória

```text
Tarefa:
Fase: 01 — Bootstrap
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_02_IDENTIDADE_TENANCY (após aprovação)
```
