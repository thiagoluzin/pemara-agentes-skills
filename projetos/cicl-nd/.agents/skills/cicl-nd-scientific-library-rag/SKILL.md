---
name: cicl-nd-scientific-library-rag
description: "Biblioteca científica curada, RAG controlado, curadoria e busca controlada para CICL-ND."
---

# CICL-ND — Skill de Biblioteca Científica e RAG

## Domínio

Fase 09: Biblioteca científica, curadoria, versionamento e busca controlada.

## Quando usar

- Implementar cadastro de fontes científicas;
- configurar pipeline de curadoria;
- implementar indexação com embeddings;
- criar RAG controlado;
- validar citações e fundamentação;
- gerenciar versões e validade das fontes;
- separar fontes globais e internas.

## Documentos de referência

- `docs/01_ESCOPO_E_REQUISITOS.md` (RF-020, RF-021)
- `docs/09_BIBLIOTECA_CIENTIFICA_E_RAG.md`
- `fases/FASE_09_BIBLIOTECA_CIENTIFICA.md`

## Regras obrigatórias

1. Busca científica separada do prontuário.
2. Dados identificáveis nunca enviados à internet.
3. Fonte aprovada antes de indexação.
4. Licença registrada.
5. Versão e validade obrigatórias.
6. Chunking sem perder seção.
7. Embeddings versionados.
8. Hash do conteúdo.
9. Filtro por status, população e versão.
10. Exclusão lógica de fonte retirada.
11. Citação obrigatória para toda afirmação substantiva.
12. Citação suporta exatamente a afirmação.
13. Fonte vigente.
14. População compatível ou diferença declarada.
15. Conflito entre diretrizes mostrado.
16. Ausência de evidência gera abstinência.
17. Resumo não ultrapassa o que a fonte diz.
18. Modelos não podem inventar referências.
19. Curador não acessa prontuários.
20. Clínico revisor não altera fonte publicada.

## Níveis de fonte

```
TIER_A: diretriz oficial ou revisão sistemática de alta qualidade
TIER_B: consenso ou revisão com limitações
TIER_C: estudo primário relevante
TIER_D: protocolo interno aprovado
```

## Estados de fonte

```
SUBMITTED -> SCREENING -> TECHNICAL_REVIEW -> CLINICAL_REVIEW
-> APPROVED -> PUBLISHED -> REVIEW_DUE -> UPDATED / RETIRED
```

## Saídas permitidas

- Áreas para avaliação.
- Perguntas para reunião.
- Possibilidades gerais descritas na literatura.
- Critérios de elegibilidade presentes ou ausentes.
- Alertas de dados faltantes.
- Resumo de evidência.
- Diferenças entre fontes.

## Saídas bloqueadas no MVP

- "a criança deve fazer X".
- Frequência/dose automática.
- Substituição do julgamento profissional.
- Ranking de terapias para um caso.
- Prognóstico individual.
- Comunicação direta à família.

## Fluxo de trabalho

### SL-001: Cadastro de fontes

1. CRUD de `scientific_source`.
2. Metadados completos: título, autores, data, versão, população, condição, licença.
3. Upload do documento.
4. Estado inicial: SUBMITTED.

### SL-002: Pipeline de curadoria

1. Triagem: fonte elegível?
2. Revisão metodológica.
3. Revisão clínica.
4. Aprovação e publicação.
5. Indexação.
6. Data de revisão programada.

### SL-003: Indexação

1. Chunking sem perder seção.
2. Metadados em cada fragmento.
3. Embeddings versionados com pgvector.
4. Hash do conteúdo.
5. Filtro por status, população e versão.
6. Teste de recuperação.

### SL-004: RAG controlado

1. Prompt recebe pergunta profissional.
2. Resumo mínimo do caso, preferencialmente pseudonimizado.
3. Evidências do paciente por IDs.
4. Fragmentos científicos aprovados.
5. Instrução de não extrapolar.
6. Obrigação de citar.
7. Obrigação de declarar limitações.
8. Schema estruturado.
9. Output validator.

### SL-005: Validação de fundamentação

1. Toda afirmação substantiva tem citação.
2. Citação suporta exatamente a afirmação.
3. Fonte vigente.
4. População compatível ou diferença declarada.
5. Conflito entre diretrizes mostrado.
6. Ausência de evidência gera abstinência.

### SL-006: Isolamento da biblioteca

1. Fontes globais aprovadas.
2. Fontes internas do tenant.
3. Fontes expiradas.
4. Rascunhos.
5. Busca separa as categorias.

### SL-007: Gestão de versões e validade

1. `published_at`, `review_due_at`, `retired_at`.
2. Motivo de retirada.
3. Versão substituta.
4. Jobs impedem uso de fonte vencida.
5. Execuções antigas mantêm referência.

## Migrações

```sql
CREATE TABLE scientific_source (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT,
    organization TEXT,
    published_at DATE,
    language TEXT NOT NULL DEFAULT 'pt',
    population TEXT,
    age_range TEXT,
    condition TEXT,
    study_type TEXT,
    quality TEXT,
    limitations TEXT,
    conflicts TEXT,
    license TEXT,
    source_url TEXT,
    identifier TEXT,
    tier TEXT NOT NULL DEFAULT 'TIER_C',
    status TEXT NOT NULL DEFAULT 'SUBMITTED',
    review_due_at DATE,
    retired_at DATE,
    retirement_reason TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE scientific_source_version (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenant(id),
    source_id UUID NOT NULL REFERENCES scientific_source(id),
    version INT NOT NULL,
    document_id UUID REFERENCES clinical_document(id),
    published_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    approved_by UUID REFERENCES "user"(id),
    review_due_at DATE,
    status TEXT NOT NULL DEFAULT 'PUBLISHED',
    supersedes_id UUID REFERENCES scientific_source_version(id),
    UNIQUE(source_id, version)
);

CREATE TABLE scientific_chunk (
    id UUID PRIMARY KEY,
    tenant_id UUID REFERENCES tenant(id),
    source_version_id UUID NOT NULL REFERENCES scientific_source_version(id),
    section TEXT,
    content TEXT NOT NULL,
    embedding VECTOR(1536),
    embedding_model TEXT,
    embedding_version TEXT,
    content_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## Contrato de resposta RAG

```json
{
  "question": "...",
  "patientEvidenceRefs": ["ev_..."],
  "findings": [
    {
      "statement": "...",
      "scientificSourceRefs": ["srcv_..."],
      "applicability": "partial",
      "limitations": ["..."]
    }
  ],
  "missingInformation": ["..."],
  "abstentions": ["..."],
  "reviewStatus": "PENDING_CLINICAL_REVIEW"
}
```

## Testes obrigatórios

- Cadastro de fonte com metadados completos.
- Pipeline de curadoria: estados transitados corretamente.
- Indexação: chunks com metadados e embeddings.
- Retrieval: fontes relevantes recuperadas.
- Citação: correta e verificável.
- Fonte expirada: não usada em novas respostas.
- Prompt injection: conteúdo científico não executa ferramenta.
- Sem dados de paciente na busca externa.
- Sem referências inventadas.
- Isolamento de tenant para fontes internas.

## Portão de saída da Fase 09

- Biblioteca curada e versionada.
- RAG com citações verificáveis.
- Fontes expiradas bloqueadas.
- Testes de recuperação e fundamentação verdes.
- Aprovação da comissão científica.

## Saída obrigatória

```text
Tarefa:
Fase: 09 — Biblioteca Científica
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: FASE_10_IA_LONGITUDINAL (após aprovação)
```
