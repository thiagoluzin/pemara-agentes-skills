---
name: cicl-nd-ingestion-evidence
description: "Ingestão documental, OCR, transcrição, extração estruturada, evidências com proveniência e revisão para CICL-ND."
---

# CICL-ND — Skill de Ingestão Documental e Evidências

## Domínio

Fases 04-05: Upload, quarentena, OCR, transcrição, extração estruturada, evidências com proveniência e revisão humana.

## Quando usar

- Implementar upload protegido de documentos;
- configurar quarentena e antimalware;
- implementar pipeline de OCR;
- implementar transcrição de áudio;
- criar extração estruturada com IA;
- gerar evidências com proveniência;
- implementar tela de revisão lado a lado;
- gerenciar estados de evidência.

## Documentos de referência

- `docs/01_ESCOPO_E_REQUISITOS.md` (RF-005 a RF-012)
- `docs/04_MODELO_DE_DOMINIO_E_DADOS.md` (seções 4-7)
- `docs/05_PROCESSOS_E_MAQUINAS_DE_ESTADO.md` (seções 1-2)
- `docs/06_API_EVENTOS_E_INTEGRACOES.md` (seção 3)
- `docs/07_INGESTAO_OCR_AUDIO_TEXTO.md`
- `fases/FASE_04_INGESTAO_DOCUMENTAL.md`
- `fases/FASE_05_EVIDENCIAS_PROVENIENCIA.md`

## Regras obrigatórias

1. Original nunca é alterado.
2. Arquivo em quarentena até validação completa.
3. Antimalware obrigatório.
4. Extensão real e MIME validados.
5. OCR com bounding boxes e confiança por bloco.
6. STT com timecodes e idioma PT-BR.
7. Extração estruturada com proveniência obrigatória.
8. Campos críticos nunca autoaceitos.
9. Documentos são conteúdo não confiável (prompt injection).
10. Revisão humana obrigatória para relevância clínica.
11. Retry idempotente.
12. Logs sem conteúdo clínico.

## Pipeline documental

```
Upload -> Quarentena -> Detecção de tipo -> Malware scan -> Checksum
-> Extração direta -> OCR (se necessário) -> Layout -> Classificação
-> Extração estruturada -> Proveniência -> Revisão
```

## Estados de documento

```
RECEIVED -> QUARANTINED -> REJECTED (malware/formato)
QUARANTINED -> VALIDATED -> PROCESSING -> PROCESSING_FAILED
PROCESSING_FAILED -> PROCESSING (retry)
PROCESSING -> READY_FOR_REVIEW -> APPROVED / REJECTED
APPROVED -> ARCHIVED
```

## Estados de evidência

```
GENERATED -> PENDING_REVIEW -> ACCEPTED / EDITED_AND_ACCEPTED / REJECTED
ACCEPTED -> SUPERSEDED
EDITED_AND_ACCEPTED -> SUPERSEDED
```

## Tipos de evidência

```
DOCUMENT_FACT
CAREGIVER_REPORT
SCHOOL_REPORT
CLINICIAN_OBSERVATION
OBJECTIVE_MEASUREMENT
AI_INFERENCE
PROFESSIONAL_CONCLUSION
```

`AI_INFERENCE` nunca promovida silenciosamente a fato.

## Fluxo de trabalho

### IG-001: Upload protegido

1. Endpoint de criação de sessão de upload.
2. URL temporária para S3/MinIO.
3. Validação de tamanho, MIME e extensão real.
4. Checksum SHA-256.
5. Documento criado em estado QUARANTINED.
6. Idempotência com chave.

### IG-002: Quarentena e malware scan

1. Job de verificação de arquivo.
2. ClamAV ou serviço equivalente.
3. Detecção de executáveis e políglotas.
4. Limite de páginas/pixels.
5. Remoção de EXIF desnecessário.
6. Transição para VALIDATED ou REJECTED.

### IG-003: OCR

1. Extração direta de texto do PDF quando possível.
2. OCR por página para PDFs digitalizados.
3. Normalização de orientação, deskew, ruído.
4. Texto e bounding boxes por bloco.
5. Confiança por palavra/bloco.
6. Manuscrito marcado como experimental.
7. Campos críticos pendentes de revisão.

### IG-004: Transcrição de áudio

1. Upload de áudio em quarentena.
2. Verificação de finalidade/consentimento.
3. STT em PT-BR com timecodes.
4. Diarização opcional, nunca presumida como identidade.
5. Sem biometria de voz.
6. Sem inferência de emoção.
7. Revisão obrigatória.
8. Retenção de áudio configurável.

### IG-005: Classificação documental

1. Sugestão de tipo de documento.
2. Sem alteração no prontuário até revisão.
3. Confiança da classificação.

### IG-006: Extração estruturada

1. IA recebe tipo documental, esquema, texto com IDs de bloco.
2. Instrução de não inferir.
3. Obrigação de citar blocos.
4. Saída validada contra JSON Schema.
5. Campos críticos marcados.
6. Proveniência com página, bbox, trecho citado.
7. Saída inválida rejeitada.

### IG-007: Evidências com proveniência

1. `EvidenceItem` com tipo, conceito, valor, data, fonte.
2. `EvidenceProvenance` com localização exata.
3. Confiança técnica separada por origem.
4. Estado de revisão.
5. Tenant isolation.

### IG-008: Revisão

1. API de decisão: aceitar, editar, rejeitar.
2. Optimistic concurrency com versão.
3. Registro de revisor, motivo e alterações.
4. Auditoria de decisão.
5. Eventos `evidence.accepted.v1`, etc.

### IG-009: Prompt injection protection

1. Encapsular conteúdo do documento.
2. Ignorar instruções internas.
3. Impedir chamadas de ferramenta originadas no documento.
4. Allowlist de tarefas.
5. Limitar tamanho e contexto.
6. Detectar padrões de injeção.
7. Registrar bloqueios.

## Migrações

```sql
CREATE TABLE clinical_document (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    original_name TEXT NOT NULL,
    mime_type TEXT NOT NULL,
    size_bytes BIGINT NOT NULL,
    checksum_sha256 TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'RECEIVED',
    uploaded_by UUID REFERENCES "user"(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE ingestion_job (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    document_id UUID NOT NULL REFERENCES clinical_document(id),
    job_type TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'PENDING',
    provider TEXT,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    error TEXT,
    retry_count INT NOT NULL DEFAULT 0,
    idempotency_key TEXT UNIQUE
);

CREATE TABLE extraction_run (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    document_id UUID NOT NULL REFERENCES clinical_document(id),
    ingestion_job_id UUID NOT NULL REFERENCES ingestion_job(id),
    extraction_type TEXT NOT NULL,
    model_version TEXT,
    prompt_version TEXT,
    status TEXT NOT NULL DEFAULT 'GENERATED',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE evidence_item (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    patient_id UUID NOT NULL REFERENCES patient(id),
    extraction_run_id UUID NOT NULL REFERENCES extraction_run(id),
    type TEXT NOT NULL,
    concept_system TEXT,
    concept_code TEXT,
    concept_display TEXT,
    value_kind TEXT NOT NULL,
    value_json JSONB NOT NULL,
    effective_at DATE,
    review_status TEXT NOT NULL DEFAULT 'PENDING_REVIEW',
    confidence_kind TEXT,
    confidence_score DECIMAL(3,2),
    version INT NOT NULL DEFAULT 1,
    supersedes_id UUID REFERENCES evidence_item(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE evidence_provenance (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    evidence_id UUID NOT NULL REFERENCES evidence_item(id),
    source_type TEXT NOT NULL,
    document_id UUID REFERENCES clinical_document(id),
    page_number INT,
    bounding_box JSONB,
    quoted_text TEXT,
    audio_id UUID,
    start_ms INT,
    end_ms INT,
    transcript_segment TEXT,
    form_id UUID,
    field_path TEXT,
    author_id UUID REFERENCES "user"(id),
    recorded_at TIMESTAMPTZ,
    artifact_checksum TEXT,
    extraction_version TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE review_decision (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    evidence_id UUID NOT NULL REFERENCES evidence_item(id),
    decision TEXT NOT NULL,
    edited_value_json JSONB,
    reason TEXT,
    reviewer_id UUID NOT NULL REFERENCES "user"(id),
    expected_version INT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## Testes obrigatórios

- Upload com validação de MIME e tamanho.
- Quarentena e malware scan.
- OCR com bbox e confiança.
- STT com timecodes.
- Extração estruturada com proveniência.
- Revisão: aceitar, editar, rejeitar.
- Optimistic concurrency na revisão.
- Prompt injection: conteúdo não executa ferramenta.
- Isolamento de tenant em documentos e evidências.
- Auditoria de upload, extração e revisão.
- Retry idempotente de job.

## Portão de saída das Fases 04-05

- Pipeline de ingestão funcional.
- OCR e STT com proveniência.
- Extração estruturada com revisão.
- Evidências com proveniência completa.
- Testes de segurança e isolamento verdes.
- Aprovação clínica.

## Saída obrigatória

```text
Tarefa:
Fase: 04-05 — Ingestão e Evidências
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_06_SESSOES_MULTIMODAIS (após aprovação)
```
