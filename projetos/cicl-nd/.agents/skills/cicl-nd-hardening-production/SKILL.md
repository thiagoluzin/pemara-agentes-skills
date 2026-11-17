---
name: cicl-nd-hardening-production
description: "Hardening, observabilidade, testes de segurança, piloto e produção para CICL-ND."
---

# CICL-ND — Skill de Hardening, Piloto e Produção

## Domínio

Fases 11-12: Hardening, observabilidade, testes de segurança, piloto com dados reais e produção multi-tenant.

## Quando usar

- Implementar observabilidade completa;
- configurar SLOs, alertas e dashboards;
- executar testes de segurança;
- preparar plano de incidentes;
- configurar backups e disaster recovery;
- executar piloto controlado;
- preparar produção multi-tenant;
- implementar WAF, SIEM e segregação.

## Documentos de referência

- `docs/11_SEGURANCA_PRIVACIDADE_LGPD.md`
- `docs/13_TESTES_E_VALIDACAO.md`
- `docs/14_DEVOPS_OBSERVABILIDADE_SRE.md`
- `docs/15_IMPLANTACAO_E_OPERACAO.md`
- `docs/18_RISCOS_E_CONTROLES.md`
- `docs/23_CRITERIOS_DE_ESCALA.md`
- `docs/24_FEATURE_FLAGS_E_CONFIGURACAO.md`
- `fases/FASE_11_HARDENING_PILOTO.md`
- `fases/FASE_12_PRODUCAO_ESCALA.md`
- `runbooks/`

## Regras obrigatórias

1. RIPD atualizado antes do piloto real.
2. Dados reais somente no piloto autorizado.
3. IA em modo silencioso no piloto.
4. Sugestão clínica individualizada desabilitada por padrão.
5. Pentest independente antes de produção.
6. SLOs definidos e monitorados.
7. Backups testados periodicamente.
8. Plano de incidentes com runbooks.
9. Segregação de ambientes.
10. Go/no-go com evidências.

## SLOs de referência

| Ambiente | Disponibilidade | RPO | RTO |
|---|---|---|---|
| Piloto | 99,5% | 15 min | 4h |
| Produção | 99,9% | 15 min | 4h |

## Estágios de escala

```
S0: Docker Compose local, dados sintéticos, um nó
S1: Piloto, uma organização, banco gerenciado, storage privado
S2: Produção multi-tenant, RLS, autoscaling, WAF, SIEM
S3: Enterprise, banco/chave dedicada, residência de dados, HA regional
```

## Fluxo de trabalho

### HP-001: Observabilidade

1. OpenTelemetry em API, workers e gateway.
2. Métricas: latência, erro, saturação, jobs.
3. Traces distribuídos.
4. Logs sem dados clínicos.
5. Prometheus/Grafana/Loki/Tempo.
6. Dashboards por serviço.
7. Alertas com thresholds.
8. Correlação por IDs técnicos.

### HP-002: Testes de segurança

1. SAST no CI.
2. DAST em ambiente de staging.
3. SCA para dependências.
4. SBOM gerado.
5. Container scan.
6. IaC scan.
7. Pentest independente.
8. Testes de autorização em toda rota.
9. Testes de isolamento de tenant.

### HP-003: Backups e DR

1. Backup automático do banco.
2. Backup do object storage.
3. Criptografia dos backups.
4. Chaves separadas por ambiente.
5. Teste de restauração periódico.
6. RPO/RTO validados.
7. Runbook de restore.

### HP-004: Plano de incidentes

1. Runbooks para cada cenário.
2. Break-glass.
3. Falha de ingestão.
4. Indisponibilidade de IA.
5. Vazamento de dados.
6. Restore de backup.
7. Comunicação e escalariação.
8. Post-mortem obrigatório.

### HP-005: Piloto controlado

1. Uma organização.
2. População definida.
3. Duração definida.
4. IA em modo silencioso.
5. Sugestão desabilitada.
6. Monitoramento reforçado.
7. Coleta de feedback.
8. Go/no-go com evidências.

### HP-006: Produção multi-tenant

1. RLS ativo e testado.
2. Autoscaling de workers.
3. Réplicas de leitura quando necessário.
4. WAF.
5. SIEM.
6. Segregação de ambientes.
7. SLOs monitorados.
8. Expansão controlada.

## Runbooks obrigatórios

- `RUNBOOK_BREAK_GLASS.md`
- `RUNBOOK_FALHA_INGESTAO.md`
- `RUNBOOK_INDISPONIBILIDADE_IA.md`
- `RUNBOOK_RESTORE_BACKUP.md`
- `RUNBOOK_VAZAMENTO_DADOS.md`

## Testes obrigatórios

- SLOs atendidos no piloto.
- Pentest sem vulnerabilidades críticas.
- Backup restaurado com sucesso.
- Runbooks executados em drill.
- Isolamento de tenant em produção.
- Autorização em toda rota.
- Logs sem dados clínicos.
- Alertas funcionando.
- Feature flags operando.

## Portão de saída da Fase 11

- Observabilidade completa.
- Segurança validada por pentest.
- Backups testados.
- Runbooks validados.
- Piloto concluído com go/no-go.
- Aprovação de direção e DPO.

## Portão de saída da Fase 12

- Produção multi-tenant operando.
- SLOs atendidos.
- Expansão controlada.
- Operação estável.
- Aprovação de direção e DPO.

## Saída obrigatória

```text
Tarefa:
Fase: 11-12 — Hardening e Produção
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: operação contínua
```
