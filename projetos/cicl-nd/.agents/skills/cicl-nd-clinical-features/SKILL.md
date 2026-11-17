---
name: cicl-nd-clinical-features
description: "Sessões multimodais, metas, medições, timeline, relatórios e gráficos para CICL-ND."
---

# CICL-ND — Skill de Funcionalidades Clínicas

## Domínio

Fases 06-08: Sessões multimodais, metas e medições, timeline, relatórios e gráficos.

## Quando usar

- Implementar registro de sessões terapêuticas;
- gravar e transcrever áudio de sessão;
- criar notas de sessão com assinatura;
- definir metas clínicas e métricas;
- registrar medições com contexto;
- montar timeline longitudinal;
- gerar gráficos descritivos;
- criar rascunhos de relatórios;
- implementar assinatura e adendo.

## Documentos de referência

- `docs/01_ESCOPO_E_REQUISITOS.md` (RF-013 a RF-019)
- `docs/04_MODELO_DE_DOMINIO_E_DADOS.md` (seções 8-9)
- `docs/05_PROCESSOS_E_MAQUINAS_DE_ESTADO.md` (seções 3-8)
- `docs/08_INTELIGENCIA_LONGITUDINAL.md`
- `docs/10_RELATORIOS_GRAFICOS_E_UX.md`
- `fases/FASE_06_SESSOES_MULTIMODAIS.md`
- `fases/FASE_07_METAS_MEDICOES_TIMELINE.md`
- `fases/FASE_08_RELATORIOS.md`

## Regras obrigatórias

1. Sessão gravada exige consentimento/finalidade.
2. Gravação sem upload automático antes da confirmação.
3. Transcrição editada preserva original e diff.
4. Nota assinada é imutável; correção por adendo.
5. Medição registra componentes, não apenas resultado.
6. Valor derivado é recalculável pelos componentes.
7. Ausência de dado não é zero.
8. Dado pendente não entra no gráfico oficial.
9. Sem suavização enganosa em gráficos.
10. Sem pontuação global de gravidade sem instrumento validado.
11. Evento contextual mostra coincidência, nunca causalidade.
12. Relatório gera snapshot para congelar dados.
13. Assinatura registra hash da versão.
14. PDF é determinístico e reprodutível.

## Estados de sessão

```
DRAFT -> TRANSCRIBING -> DRAFT -> PENDING_REVIEW -> SIGNED
SIGNED -> AMENDED
SIGNED -> VOIDED (justificativa excepcional)
```

## Estados de relatório

```
DRAFT -> UNDER_REVIEW -> DRAFT -> APPROVED -> SIGNED -> PUBLISHED
PUBLISHED -> SUPERSEDED
PUBLISHED -> REVOKED
```

## Fluxo de trabalho

### SF-001: Sessão por texto e formulário

1. Criar encounter.
2. Preencher formulário estruturado: objetivos, estratégias, resposta, ajuda, intercorrências, conduta.
3. Salvar como rascunho.
4. Enviar para revisão.
5. Assinar.

### SF-002: Sessão por áudio

1. Botão de gravação na UI.
2. Upload por URL temporária.
3. Cria artefato em quarentena.
4. Job de transcrição.
5. Texto + timecodes salvos como rascunho.
6. Terapeuta corrige e estrutura.
7. Envia para assinatura.
8. API bloqueia versão assinada.

### SF-003: Assinatura e adendo

1. Assinatura vincula identidade, data/hora, hash da versão.
2. Impede alteração da versão assinada.
3. Adendo é registro independente vinculado.
4. Motivo e trecho referenciados.
5. Assinatura do adendo.
6. Visualização atualizada sem alterar versão anterior.
7. Evento emitido.
8. Auditoria.

### SF-004: Meta clínica

1. Descrição funcional.
2. Domínio.
3. Data de início.
4. Profissional responsável.
5. Prioridade.
6. Critério de revisão.
7. Origem da decisão.

### SF-005: Definição de métrica

1. Nome e definição operacional.
2. Unidade (UCUM quando possível).
3. Numerador e denominador.
4. Contexto.
5. Nível de ajuda.
6. Janela de observação.
7. Regra de dados ausentes.
8. Linha de base.
9. Versão.

### SF-006: Medição

1. Valor bruto e componentes.
2. Unidade.
3. Data/hora.
4. Contexto.
5. Coletor.
6. Fonte.
7. Qualidade.
8. Status de validação.
9. Versão da definição usada.
10. Cálculo do derivado no servidor.

### SF-007: Timeline

1. Agregar evidências, sessões, medições e eventos contextuais.
2. Ordenar temporalmente.
3. Normalizar datas e intervalos.
4. Preservar precisão temporal.
5. Não inventar dia ou hora.

### SF-008: Gráficos

1. Série temporal de medições confirmadas.
2. Dados ausentes visíveis.
3. Pontos pendentes diferenciados.
4. Eventos contextuais anotados.
5. Linha de base marcada.
6. Eixo e unidade claros.
7. Fórmula acessível.
8. Exportação com tabela.
9. Sem cor como único canal.

### SF-009: Eventos contextuais

1. Início/fim de medicamento.
2. Alteração de dose.
3. Doença, internação.
4. Mudança de escola, terapeuta, rotina.
5. Férias, mudança familiar.
6. Gráfico mostra coincidência, não causalidade.

### SF-010: Relatórios

1. Selecionar período e finalidade.
2. Congelar snapshot de evidências.
3. Calcular agregados determinísticos.
4. Montar resumo com fontes.
5. Marcar lacunas e inconsistências.
6. Gerar rascunho.
7. Revisão humana.
8. Assinatura.
9. PDF e versão.
10. Liberação autorizada.

## Migrações

```sql
CREATE TABLE encounter (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    professional_id UUID NOT NULL REFERENCES professional(id),
    type TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL,
    ended_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE session_note (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    encounter_id UUID NOT NULL REFERENCES encounter(id),
    status TEXT NOT NULL DEFAULT 'DRAFT',
    objectives TEXT,
    strategies TEXT,
    response TEXT,
    help_level TEXT,
    occurrences TEXT,
    conduct TEXT,
    version INT NOT NULL DEFAULT 1,
    signed_at TIMESTAMPTZ,
    signed_by UUID REFERENCES "user"(id),
    signature_hash TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ
);

CREATE TABLE session_note_version (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    session_note_id UUID NOT NULL REFERENCES session_note(id),
    version INT NOT NULL,
    content_json JSONB NOT NULL,
    hash TEXT NOT NULL,
    supersedes_id UUID REFERENCES session_note_version(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE goal (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    description TEXT NOT NULL,
    domain TEXT NOT NULL,
    start_date DATE NOT NULL,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    responsible_id UUID NOT NULL REFERENCES professional(id),
    priority TEXT,
    review_criteria TEXT,
    decision_origin TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE metric_definition (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    goal_id UUID NOT NULL REFERENCES goal(id),
    name TEXT NOT NULL,
    operational_definition TEXT NOT NULL,
    unit TEXT NOT NULL,
    numerator_desc TEXT,
    denominator_desc TEXT,
    context TEXT,
    help_level TEXT,
    observation_window TEXT,
    missing_data_rule TEXT,
    baseline_value DECIMAL,
    baseline_context TEXT,
    version INT NOT NULL DEFAULT 1,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE measurement (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    metric_definition_id UUID NOT NULL REFERENCES metric_definition(id),
    observed_at TIMESTAMPTZ NOT NULL,
    components_json JSONB NOT NULL,
    derived_value DECIMAL,
    unit TEXT NOT NULL,
    context TEXT,
    collector_id UUID REFERENCES "user"(id),
    source_type TEXT,
    source_id TEXT,
    quality TEXT,
    validation_status TEXT NOT NULL DEFAULT 'PENDING',
    metric_version INT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE context_event (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    type TEXT NOT NULL,
    description TEXT NOT NULL,
    event_at TIMESTAMPTZ,
    source TEXT,
    source_id TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by UUID REFERENCES "user"(id)
);

CREATE TABLE timeline_event (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    event_at TIMESTAMPTZ NOT NULL,
    source_type TEXT NOT NULL,
    source_id UUID NOT NULL,
    summary TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE report (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    type TEXT NOT NULL,
    period_start DATE,
    period_end DATE,
    purpose TEXT,
    status TEXT NOT NULL DEFAULT 'DRAFT',
    snapshot_id TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE report_version (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    report_id UUID NOT NULL REFERENCES report(id),
    version INT NOT NULL,
    content_html TEXT NOT NULL,
    hash TEXT NOT NULL,
    signed_at TIMESTAMPTZ,
    signed_by UUID REFERENCES "user"(id),
    signature_hash TEXT,
    pdf_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## Testes obrigatórios

- Sessão: criar, transcrever, revisar, assinar.
- Assinatura: imutabilidade verificada.
- Adendo: vinculado, sem alterar original.
- Meta e métrica: CRUD com validação.
- Medição: cálculo do derivado correto.
- Timeline: ordenação temporal correta.
- Gráfico: dados ausentes visíveis, pendentes diferenciados.
- Evento contextual: coincidência, não causalidade.
- Relatório: snapshot, revisão, assinatura, PDF.
- Isolamento de tenant em todas as entidades.
- Auditoria de todas as operações.

## Portão de saída das Fases 06-08

- Sessões multimodais funcionais.
- Metas, medições e timeline operacionais.
- Gráficos descritivos corretos.
- Relatórios com assinatura e PDF.
- Aprovação clínica e jurídica.

## Saída obrigatória

```text
Tarefa:
Fase: 06-08 — Funcionalidades Clínicas
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_09_BIBLIOTECA_CIENTIFICA (após aprovação)
```
