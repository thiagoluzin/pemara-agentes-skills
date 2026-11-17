---
name: cicl-nd-cadastro-consentimento
description: "Cadastro de organização, profissionais, pacientes, responsáveis e gestão de consentimentos e finalidades para CICL-ND."
---

# CICL-ND — Skill de Cadastro e Consentimento

## Domínio

Fase 03: Cadastro mínimo e gestão de consentimentos e finalidades de tratamento.

## Quando usar

- Implementar cadastro de organização e unidade;
- cadastrar profissionais com especialidade e vínculos;
- cadastrar paciente/criança e responsáveis legais;
- registrar finalidades de tratamento e bases legais;
- gerenciar consentimentos e autorizações;
- implementar revogação de consentimento;
- vincular acesso profissional-paciente.

## Documentos de referência

- `docs/01_ESCOPO_E_REQUISITOS.md` (RF-002, RF-003, RF-004)
- `docs/04_MODELO_DE_DOMINIO_E_DADOS.md`
- `docs/05_PROCESSOS_E_MAQUINAS_DE_ESTADO.md` (seção 14)
- `docs/11_SEGURANCA_PRIVACIDADE_LGPD.md` (seções 3, 4)
- `docs/20_MATRIZ_DE_PERMISSOES.md`
- `docs/21_DICIONARIO_DE_DADOS.md`
- `fases/FASE_03_CADASTRO_CONSENTIMENTO.md`

## Regras obrigatórias

1. Todo registro clínico contém `tenant_id`.
2. Consentimento não é presumido como única base legal.
3. Revogação interrompe processamentos futuros opcionais.
4. Poderes do responsável devem ser verificados.
5. Finalidades devem ser separadas.
6. Não condicionar cuidado a uso opcional de IA.
7. Assentimento da criança quando aplicável.
8. Versão do texto de consentimento registrada.
9. Efeitos da revogação documentados.
10. Retenção remanescente após revogação avaliada.

## Entidades

```
tenant
  └── organization
        └── facility
        └── user -> professional
        └── patient
              └── guardian_link -> guardian
              └── patient_access_grant -> user
              └── processing_purpose
              └── consent
              └── clinical_condition
```

## Fluxo de trabalho

### CS-001: Cadastro de organização

1. CRUD de organização com `tenant_id`.
2. CRUD de unidade/facility vinculada à organização.
3. Validação de campos obrigatórios.
4. Auditoria de criação e alteração.

### CS-002: Cadastro de profissionais

1. Vinculação de `user` a `professional`.
2. Campos: especialidade, registro profissional, CRM/CREFITO/etc.
3. Vinculo com organização e unidade.
4. Múltiplas especialidades permitidas.
5. Ativação/desativação.

### CS-003: Cadastro de paciente e responsáveis

1. Paciente com `tenant_id`, dados mínimos.
2. Responsável legal com poderes especificados.
3. Link paciente-responsável com tipo de vínculo.
4. Histórico de responsáveis.
5. Dados sensíveis com controle de acesso reforçado.

### CS-004: Condições clínicas

1. Registro de condição confirmada, hipótese, informação familiar, documental.
2. Preservação de fonte e data.
3. Status da condição (ativa, em investigação, resolvida).
4. Código de terminologia quando aplicável.

### CS-005: Finalidades de tratamento

1. CRUD de `processing_purpose`.
2. Campos: descrição, base legal, justificativa, responsável.
3. Vinculo com paciente.
4. Ativação/desativação.

### CS-006: Consentimentos e autorizações

1. Registro de consentimento com versão do texto.
2. Campos: finalidade, base legal, consentido, data, versão.
3. Revogação com efeitos documentados.
4. Histórico de versões.
5. Assentimento da criança quando aplicável.

### CS-007: Revogação de consentimento

1. Validar identidade e poderes.
2. Localizar finalidades afetadas.
3. Registrar revogação.
4. Interromper processamentos futuros opcionais.
5. Cancelar jobs quando seguro.
6. Avaliar retenção obrigatória.
7. Ajustar acessos/compartilhamentos.
8. Registrar comunicação.
9. Auditar.

### CS-008: Grants de acesso

1. `patient_access_grant` vincula profissional a paciente.
2. Critérios: função, especialidade, equipe.
3. Revisão periódica de acesso.
4. Auditoria de criação e remoção.

## Migrações

```sql
CREATE TABLE organization (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    name TEXT NOT NULL,
    cnpj TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ
);

CREATE TABLE facility (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    organization_id UUID NOT NULL REFERENCES organization(id),
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE professional (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    user_id UUID NOT NULL REFERENCES "user"(id),
    organization_id UUID NOT NULL REFERENCES organization(id),
    specialty TEXT NOT NULL,
    registration_number TEXT,
    council TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(user_id)
);

CREATE TABLE patient (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ
);

CREATE TABLE guardian (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    name TEXT NOT NULL,
    relationship TEXT,
    contact TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE guardian_link (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    guardian_id UUID NOT NULL REFERENCES guardian(id),
    powers TEXT[],
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(patient_id, guardian_id)
);

CREATE TABLE patient_access_grant (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    user_id UUID NOT NULL REFERENCES "user"(id),
    purpose TEXT,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at TIMESTAMPTZ,
    UNIQUE(patient_id, user_id)
);

CREATE TABLE processing_purpose (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID REFERENCES patient(id),
    description TEXT NOT NULL,
    legal_basis TEXT NOT NULL,
    justification TEXT,
    responsible_id UUID REFERENCES "user"(id),
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE consent (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    guardian_id UUID REFERENCES guardian(id),
    purpose_id UUID REFERENCES processing_purpose(id),
    text_version TEXT NOT NULL,
    consented BOOLEAN NOT NULL,
    revoked_at TIMESTAMPTZ,
    revocation_reason TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by UUID REFERENCES "user"(id)
);

CREATE TABLE clinical_condition (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    type TEXT NOT NULL,
    code_system TEXT,
    code TEXT,
    display TEXT NOT NULL,
    source TEXT NOT NULL,
    source_id TEXT,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    effective_at DATE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by UUID REFERENCES "user"(id)
);
```

## Testes obrigatórios

- CRUD de organização, profissional, paciente, responsável.
- Vinculo profissional-paciente funciona como gate de acesso.
- Consentimento registra versão do texto.
- Revogação interrompe finalidades corretamente.
- Condição clínica preserva fonte e data.
- Isolamento de tenant em todas as entidades.
- Auditoria de criação, alteração e revogação.

## Portão de saída da Fase 03

- Cadastro mínimo funcional.
- Consentimentos e finalidades gerenciáveis.
- Revogação com efeitos corretos.
- Testes de isolamento de tenant verdes.
- Aprovação de privacidade e clínico.

## Saída obrigatória

```text
Tarefa:
Fase: 03 — Cadastro e Consentimento
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_04_INGESTAO_DOCUMENTAL (após aprovação)
```
