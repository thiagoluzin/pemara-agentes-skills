---
name: cicl-nd-ai-longitudinal
description: "Motor de inteligência longitudinal, análise descritiva, detecção de lacunas, gateway de IA e governança para CICL-ND."
---

# CICL-ND — Skill de IA Longitudinal

## Domínio

Fase 10: Análise longitudinal descritiva, detecção de lacunas, padrões, abstinência e governança de IA.

## Quando usar

- Implementar motor de análise longitudinal;
- calcular tendências descritivas;
- detectar lacunas e contradições;
- gerar perguntas sugeridas;
- implementar gateway de IA com políticas;
- registrar execuções de IA com proveniência;
- implementar abstinência segura;
- configurar feature flags de IA.

## Documentos de referência

- `docs/01_ESCOPO_E_REQUISITOS.md` (RF-022, RF-023, RF-028)
- `docs/02_ARQUITETURA_DE_REFERENCIA.md` (seção 4.4, Gateway de IA)
- `docs/08_INTELIGENCIA_LONGITUDINAL.md`
- `docs/12_GOVERNANCA_CLINICA_REGULATORIA_IA.md`
- `fases/FASE_10_IA_LONGITUDINAL.md`

## Regras obrigatórias

1. IA é apoio, nunca autora da decisão final.
2. Descrição antes de predição.
3. Ausência de dado não é zero.
4. Relatos de fontes diferentes não são fundidos.
5. Mudanças temporais não implicam causa.
6. Comparações com própria linha de base.
7. Indicador precisa de versão.
8. Dado pendente não entra no gráfico oficial.
9. Cada cálculo reproduzível.
10. Abster quando amostra insuficiente.
11. Sem pontuação global sem instrumento validado.
12. Saída de IA registrada com modelo, versão, prompt, parâmetros, hashes, fontes.
13. Gateway aplica política por tenant.
14. Gateway remove/pseudonimiza campos quando exigido.
15. Gateway impede ferramentas não permitidas.
16. Gateway valida JSON Schema.
17. Gateway calcula hashes.
18. Gateway bloqueia conteúdo não fundamentado.
19. Gateway tem rate limit e circuit breaker.
20. Gateway tem fallback e abstinência.

## Camadas da análise

1. **Factual**: itens confirmados e intervalos temporais.
2. **Métrica**: valores determinísticos derivados de medições.
3. **Contextual**: medicação, escola, terapeuta, rotina, eventos.
4. **Analítica**: tendências descritivas, lacunas, inconsistências.
5. **Narrativa**: resumo com links para evidências.

## Funções do MVP

- Ordenar eventos.
- Normalizar datas e intervalos.
- Detectar documentos sem data clara.
- Agrupar por domínio.
- Calcular contagens, taxas, medianas, percentuais definidos.
- Janelas móveis opcionais.
- Tendência robusta simples.
- Dados ausentes.
- Comparação com linha de base.
- Anotar eventos contextuais.
- Apontar contradições.
- Sugerir perguntas para revisão.
- Resumo por período.

## Classes de tendência

```
insufficient_data
stable
increasing
decreasing
variable
```

## Estados de sugestão de IA

```
GENERATED -> BLOCKED (regra de segurança)
GENERATED -> PENDING_CLINICAL_REVIEW
PENDING_CLINICAL_REVIEW -> ACCEPTED / EDITED / REJECTED
ACCEPTED -> EXPIRED
EDITED -> EXPIRED
```

## Fluxo de trabalho

### AI-001: Motor de análise longitudinal

1. Receber evidências aceitas e medições confirmadas.
2. Normalização temporal.
3. Cálculos determinísticos.
4. Timeline agregada.
5. Qualidade e lacunas.
6. Análise descritiva.
7. Resumo com fontes.
8. Revisão humana.

### AI-002: Detecção de contradições

1. Datas incompatíveis.
2. Doses diferentes em fontes.
3. Diagnóstico com status divergente.
4. Relato familiar diferente do escolar.
5. Valor fora da unidade esperada.
6. Meta medida com versão antiga.
7. Sinalizar, não escolher automaticamente.

### AI-003: Perguntas sugeridas

1. "Qual período o relato da escola abrange?"
2. "A alteração de sono ocorreu antes ou depois da mudança de rotina?"
3. "Confirme a unidade da medida."
4. "Há linha de base para esta meta?"

### AI-004: Gateway de IA

1. Aplicar política por tenant.
2. Remover/pseudonimizar campos.
3. Selecionar provedor/modelo autorizado.
4. Impedir ferramentas não permitidas.
5. Validar JSON Schema.
6. Registrar prompt e versão.
7. Calcular hashes.
8. Bloquear conteúdo não fundamentado.
9. Rate limit.
10. Circuit breaker.
11. Fallback e abstinência.

### AI-005: Registro de execução de IA

1. `AiRun` com modelo, versão, prompt, parâmetros.
2. Hash do prompt e da saída.
3. Fontes usadas.
4. Evidências do paciente.
5. Incertezas declaradas.
6. Decisão humana.

### AI-006: Abstinência segura

1. Verificar suporte suficiente.
2. Recusar conclusão quando insuficiente.
3. Declarar limitação explicitamente.
4. Não completar lacunas.

### AI-007: Feature flags de IA

1. Desligar OCR externo por tenant.
2. Desligar IA externa por tenant.
3. Desligar RAG por tenant.
4. Desligar apoio clínico por tenant.
5. Controle por ambiente.

## Migrações

```sql
CREATE TABLE ai_model (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    provider TEXT,
    status TEXT NOT NULL DEFAULT 'APPROVED',
    approved_by UUID REFERENCES "user"(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE ai_prompt (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    version INT NOT NULL,
    content TEXT NOT NULL,
    hash TEXT NOT NULL,
    task_type TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    supersedes_id UUID REFERENCES ai_prompt(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(name, version)
);

CREATE TABLE ai_run (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID REFERENCES patient(id),
    model_id UUID NOT NULL REFERENCES ai_model(id),
    prompt_id UUID NOT NULL REFERENCES ai_prompt(id),
    prompt_version INT NOT NULL,
    parameters_json JSONB,
    prompt_hash TEXT NOT NULL,
    output_hash TEXT,
    sources_json JSONB,
    patient_evidence_refs JSONB,
    uncertainties TEXT[],
    abstentions TEXT[],
    status TEXT NOT NULL DEFAULT 'COMPLETED',
    human_decision TEXT,
    human_decision_by UUID REFERENCES "user"(id),
    human_decision_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE suggestion (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    ai_run_id UUID NOT NULL REFERENCES ai_run(id),
    type TEXT NOT NULL,
    claim TEXT NOT NULL,
    patient_evidence_refs JSONB,
    scientific_evidence_refs JSONB,
    uncertainties TEXT[],
    abstained_from TEXT[],
    status TEXT NOT NULL DEFAULT 'PENDING_CLINICAL_REVIEW',
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE feature_flag (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenant(id),
    flag_name TEXT NOT NULL,
    enabled BOOLEAN NOT NULL DEFAULT FALSE,
    environment TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ,
    UNIQUE(flag_name, COALESCE(tenant_id, ''::uuid), environment)
);
```

## Esquema de saída longitudinal

```json
{
  "period": {
    "start": "2026-06-01",
    "end": "2026-07-31"
  },
  "domains": [
    {
      "code": "functional-communication",
      "measurements": ["ms_1", "ms_2"],
      "summary": "Quatro medições confirmadas no período.",
      "trend": {
        "kind": "descriptive",
        "direction": "increasing",
        "method": "median-window",
        "limitations": ["Amostra pequena"]
      }
    }
  ],
  "missingness": [
    "Não há medição entre 12 e 28 de junho"
  ],
  "contradictions": [
    {
      "evidenceRefs": ["ev_1", "ev_2"],
      "description": "Frequências informadas em períodos diferentes"
    }
  ],
  "abstentions": [
    "Não é possível atribuir a mudança à alteração de medicação"
  ]
}
```

## Testes obrigatórios

- Análise longitudinal: cálculos repetíveis.
- Ausência de dado não vira zero.
- Proveniência de cada ponto.
- Versão de métrica respeitada.
- Sem causalidade inferida.
- Abstinência com amostra insuficiente.
- Gateway: política aplicada, hash calculado.
- Feature flags: IA desligável por tenant.
- Dados sintéticos extremos testados.
- Tabela acessível equivalente ao gráfico.
- Isolamento de tenant em AI runs.
- Auditoria de toda execução de IA.

## Portão de saída da Fase 10

- Motor longitudinal funcional.
- Gateway de IA com políticas.
- Abstinência operando.
- Registro completo de execuções.
- Feature flags ativos.
- Aprovação de segurança clínica e regulatória.

## Saída obrigatória

```text
Tarefa:
Fase: 10 — IA Longitudinal
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_11_HARDENING_PILOTO (após aprovação)
```
