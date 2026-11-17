---
name: cicl-nd-identity-tenancy
description: "Identidade, autenticação OIDC, RBAC/ABAC, multi-tenancy, RLS e auditoria básica para CICL-ND."
---

# CICL-ND — Skill de Identidade e Tenancy

## Domínio

Fase 02: Identidade, autenticação, autorização, isolamento de tenant e auditoria básica.

## Quando usar

- Implementar autenticação OIDC;
- configurar RBAC e ABAC;
- implementar Row Level Security;
- criar contexto de tenant por transação;
- implementar auditoria de acesso;
- testar isolamento entre tenants;
- configurar break-glass.

## Documentos de referência

- `docs/02_ARQUITETURA_DE_REFERENCIA.md` (seção 4.2, Identity Context)
- `docs/04_MODELO_DE_DOMINIO_E_DADOS.md` (seção 11, isolamento por tenant)
- `docs/11_SEGURANCA_PRIVACIDADE_LGPD.md` (seção 6, IAM)
- `docs/20_MATRIZ_DE_PERMISSOES.md`
- `fases/FASE_02_IDENTIDADE_TENANCY.md`

## Regras obrigatórias

1. `tenant_id NOT NULL` em toda tabela clínica.
2. RLS habilitado em todas as tabelas clínicas.
3. Contexto de tenant definido por transação.
4. Chave estrangeira composta `(tenant_id, id)` quando necessário.
5. Testes negativos de isolamento obrigatórios.
6. Cache inclui tenant na chave.
7. Storage prefixado e protegido por tenant.
8. Vetores filtrados por tenant e coleção.
9. Break-glass não contorna isolamento de tenant.
10. Sem contas compartilhadas.

## Perfis de acesso

| Perfil | Permissão principal |
|---|---|
| Recepção | cadastro administrativo e upload autorizado |
| Terapeuta | pacientes atribuídos, sessões, metas da área |
| Médico | informações clínicas necessárias e decisões médicas |
| Psicólogo | área compartilhada e registros privativos |
| Coordenador | visão multiprofissional autorizada |
| Revisor clínico | revisão de extrações e saídas de IA |
| Curador científico | biblioteca científica, sem prontuário |
| DPO/privacidade | finalidades, consentimentos, auditoria |
| Auditor | logs e evidências autorizadas |
| Responsável legal | conteúdo explicitamente liberado |
| Administrador técnico | configuração; acesso clínico excepcional e auditado |

## Regras de autorização

A decisão deve considerar:
- função;
- organização;
- vínculo com o paciente;
- finalidade do acesso;
- sensibilidade do registro;
- especialidade;
- status do consentimento/autorização;
- ambiente;
- horário e contexto;
- break-glass.

## Fluxo de trabalho

### ID-001: Configurar Keycloak local

1. Realm CICL-ND no Docker Compose.
2. Clients: web-app, api-service, worker-service, fhir-gateway.
3. Roles iniciais conforme matriz de permissões.
4. Mappers para claims: tenant_id, roles, scopes.
5. MFA para profissionais.

### ID-002: Implementar Identity Context na API

1. Middleware de autenticação OIDC.
2. Extração de claims do token.
3. Guard de tenant context.
4. Injeção de `tenant_id` em todas as queries.
5. Interceptor de auditoria de autenticação.

### ID-003: Row Level Security no PostgreSQL

1. Políticas RLS por tabela clínica.
2. Função `set_tenant_context(tenant_id)`.
3. Função `get_tenant_context()`.
4. Políticas de leitura: `tenant_id = get_tenant_context()`.
5. Políticas de escrita: mesma restrição.
6. Exceções para administradores com auditoria reforçada.
7. Testes automatizados de isolamento.

### ID-004: RBAC/ABAC na API

1. Decoradores `@Roles()`, `@TenantIsolated()`, `@PatientAccess()`.
2. Guards que verificam claims + contexto.
3. Policy engine para ABAC.
4. Vinculo profissional-paciente como critério.
5. Finalidade do acesso como critério.

### ID-005: Auditoria básica

1. Tabela `audit_event` com hash chain.
2. Interceptor global de auditoria.
3. Eventos: login, logout, leitura clínica, busca, alteração.
4. Redaction de dados pessoais nos logs.
5. Append-only (sem delete/update).

### ID-006: Testes de isolamento

1. Criar 2 tenants de teste.
2. Criar dados em cada tenant.
3. Tentar acessar dados do tenant B com token do tenant A.
4. Verificar que todas as queries retornam vazio ou 403.
5. Testar RLS diretamente no banco.
6. Testar cache com tenant na chave.

### ID-007: Break-glass

1. Endpoint de solicitação de acesso emergencial.
2. Motivo obrigatório.
3. Verificação de perfil elegível.
4. Acesso temporário com expiração.
5. Banner permanente na sessão.
6. Auditoria reforçada.
7. Notificação ao responsável.

## Migrações

```sql
CREATE TABLE tenant (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE organization (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    oidc_sub TEXT NOT NULL,
    email TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(oidc_sub)
);

CREATE TABLE role_assignment (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    user_id UUID NOT NULL REFERENCES "user"(id),
    role_code TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(user_id, role_code)
);

CREATE TABLE audit_event (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenant(id),
    actor_id UUID,
    actor_role TEXT,
    action TEXT NOT NULL,
    resource TEXT,
    resource_id TEXT,
    reason TEXT,
    purpose TEXT,
    correlation_id TEXT,
    result TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    prev_hash TEXT,
    hash TEXT
);
```

## Testes obrigatórios

- Autenticação OIDC: login, logout, token refresh.
- Isolamento de tenant: leitura cruzada bloqueada.
- RLS: políticas aplicadas em todas as tabelas.
- RBAC: acesso negado sem role.
- ABAC: acesso negado sem vínculo com paciente.
- Auditoria: eventos registrados para login, leitura, alteração.
- Break-glass: fluxo completo com auditoria.
- Cache: tenant na chave, sem vazamento.

## Portão de saída da Fase 02

- Autenticação OIDC funcionando.
- RBAC/ABAC implementado.
- RLS ativo e testado.
- Isolamento de tenant provado por testes.
- Auditoria básica operando.
- Break-glass funcional.
- Aprovação de segurança.

## Saída obrigatória

```text
Tarefa:
Fase: 02 — Identidade e Tenancy
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_03_CADASTRO_CONSENTIMENTO (após aprovação)
```
