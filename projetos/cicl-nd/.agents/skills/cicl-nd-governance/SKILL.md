---
name: cicl-nd-governance
description: "Governança clínica, compliance LGPD, RIPD, limites regulatórios e decisões de finalidade para CICL-ND."
---

# CICL-ND — Skill de Governança e Compliance

## Domínio

Fase 00: Governança, finalidade, limites clínicos e regulatórios.

## Quando usar

- Iniciar o projeto CICL-ND;
- definir finalidade de uso e fronteira regulatória;
- produzir RIPD inicial;
- mapear riscos clínicos e de privacidade;
- preparar matrizes de decisão humana;
- revisar consentimentos e bases legais;
- avaliar se um módulo pode ser habilitado;
- responder a incidente de dados pessoais.

## Documentos de referência

- `docs/00_VISAO_E_PRINCIPIOS.md`
- `docs/11_SEGURANCA_PRIVACIDADE_LGPD.md`
- `docs/12_GOVERNANCA_CLINICA_REGULATORIA_IA.md`
- `docs/18_RISCOS_E_CONTROLES.md`
- `docs/26_THREAT_MODEL_INICIAL.md`
- `fases/FASE_00_GOVERNANCA.md`
- `templates/RIPD_TEMPLATE.md`
- `templates/ADR_TEMPLATE.md`
- `templates/INCIDENTE_SEGURANCA_TEMPLATE.md`

## Regras obrigatórias

1. O agente nunca presume a resposta de uma decisão pendente.
2. Finalidade de uso exige aprovação de sponsor, clínico, DPO e regulatório.
3. Nenhum dado real de criança entra em desenvolvimento ou teste.
4. Módulo E (sugestão clínica individualizada) começa desabilitado.
5. Módulo F (diagnóstico/prescrição autônomo) é proibido.
6. RIPD deve existir antes de piloto com dados reais.
7. Base legal não é presumida como consentimento.
8. Retenção de dados exige tabela aprovada por tipo e profissão.
9. Transferência internacional exige avaliação jurídica e mecanismo válido.
10. Todo risco registrado deve ter controle e responsável.

## Fluxo de trabalho

### GOV-001: Definir finalidade e limites

1. Ler `docs/00_VISAO_E_PRINCIPIOS.md` seção 6 e 7.
2. Preencher `templates/RIPD_TEMPLATE.md` com os campos de finalidade.
3. Listar os módulos de risco e sua situação inicial.
4. Produzir rascunho de `docs/status/DECISIONS_PENDING.md`.
5. Parar em `BLOCKED_HUMAN` para aprovação.

### GOV-002: Mapeamento de riscos

1. Ler `docs/18_RISCOS_E_CONTROLES.md`.
2. Preencher `docs/status/RISK_REGISTER.md`.
3. Classificar cada risco por impacto clínico, privacidade e regulatório.
4. Definir controles e responsáveis.
5. Parar em `BLOCKED_HUMAN`.

### GOV-003: RIPD inicial

1. Usar `templates/RIPD_TEMPLATE.md`.
2. Cobrir todas as finalidades do escopo.
3. Incluir bases legais, retenção, fornecedores e transferência.
4. Parar em `BLOCKED_HUMAN` para revisão jurídica.

## Artefatos produzidos

- `docs/status/EXECUTION_STATUS.md`
- `docs/status/DECISIONS_PENDING.md`
- `docs/status/RISK_REGISTER.md`
- RIPD inicial (template preenchido)
- ADRs para decisões arquiteturais pendentes

## Portão de saída da Fase 00

Todos os itens acima aprovados por:
- sponsor;
- responsável clínico;
- DPO/jurídico;
- responsável regulatório.

## Saída obrigatória

```text
Tarefa:
Fase: 00 — Governança
Arquivos alterados:
Migrações: nenhuma
Testes executados: nenhum (fase documental)
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: bloqueada até aprovação humana
```

## Interdições

- Não avançar para Fase 01 sem portão humano.
- Não criar código sem aprovação da finalidade.
- Não incluir dados reais, parciais ou inferidos de pacientes.
- Não habilitar IA clínica sem Fase 10 autorizada.
