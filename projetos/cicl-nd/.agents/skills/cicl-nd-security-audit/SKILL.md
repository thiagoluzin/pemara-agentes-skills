---
name: cicl-nd-security-audit
description: "Segurança transversal, auditoria, criptografia, IAM, LGPD e controles de proteção para CICL-ND."
---

# CICL-ND — Skill de Segurança e Auditoria Transversal

## Domínio

Transversal: segurança, auditoria, privacidade e LGPD aplicáveis a todas as fases.

## Quando usar

- Revisar qualquer código sob ótica de segurança;
- implementar auditoria em novo módulo;
- configurar criptografia;
- revisar controles LGPD;
- validar isolamento de tenant;
- implementar redaction de logs;
- revisar permissões e IAM;
- preparar para pentest.

## Documentos de referência

- `docs/11_SEGURANCA_PRIVACIDADE_LGPD.md`
- `docs/18_RISCOS_E_CONTROLES.md`
- `docs/20_MATRIZ_DE_PERMISSOES.md`
- `docs/26_THREAT_MODEL_INICIAL.md`
- `AGENTS.md` (proibições absolutas, regras de implementação)

## Regras obrigatórias

1. OWASP ASVS 5.0 nível 2 (nível 3 para acesso clínico, admin, auditoria, exportação).
2. Privacy by design em toda funcionalidade.
3. Minimização de dados.
4. Finalidade documentada.
5. `tenant_id` em toda tabela clínica.
6. RLS habilitado.
7. Contexto de tenant por transação.
8. Sem dados pessoais em logs.
9. Sem dados clínicos em erros.
10. Auditoria append-only.
11. Hash chain em audit_event.
12. Redaction nos logs.
13. Criptografia em trânsito e em repouso.
14. KMS para gerenciamento de chaves.
15. Segredos em secret manager.
16. Sem segredos no repositório.
17. URLs de upload temporárias e curtas.
18. Sem acesso direto ao storage pelo navegador.
19. Rate limit em toda API.
20. Proteção contra enumeração.

## Classificação de dados

| Classe | Exemplo | Controle |
|---|---|---|
| Público | material institucional | normal |
| Interno | documentação operacional | acesso interno |
| Confidencial | contratos e configuração | mínimo privilégio |
| Clínico altamente sensível | prontuário, áudio, laudo | controles máximos |

## O que NÃO logar

- Nome, CPF/CNS.
- Laudo, transcrição.
- Prompt clínico.
- Conteúdo de relatório.
- Token, URL assinada.

Usar IDs opacos, códigos de erro e correlação.

## O que auditar

- Login e falha.
- Leitura clínica.
- Busca.
- Alteração.
- Assinatura.
- Download, impressão, exportação.
- Uso de IA.
- Decisão de revisão.
- Administração.
- Break-glass.
- Tentativa negada.

## Checklist de segurança por módulo

### API

- [ ] Autenticação OIDC
- [ ] Autorização por política
- [ ] Tenant isolation (RLS + app level)
- [ ] Idempotência em comandos
- [ ] Problem Details para erros
- [ ] Rate limit
- [ ] Proteção contra enumeração
- [ ] CORS restrito
- [ ] CSRF quando aplicável
- [ ] Logs redigidos
- [ ] Auditoria em toda operação clínica

### Upload

- [ ] URL temporária
- [ ] Tamanho máximo
- [ ] Detecção de arquivo real
- [ ] Rejeição de executáveis
- [ ] Malware scan
- [ ] Checksum SHA-256
- [ ] Storage privado
- [ ] Processamento sandbox

### IA

- [ ] Política por tenant
- [ ] Pseudonimização
- [ ] Provedor autorizado
- [ ] Sem ferramentas não permitidas
- [ ] JSON Schema validation
- [ ] Hash do prompt e saída
- [ ] Bloqueio de conteúdo não fundamentado
- [ ] Rate limit
- [ ] Circuit breaker
- [ ] Fallback e abstinência
- [ ] Audit trail completo

### Banco

- [ ] RLS habilitado
- [ ] tenant_id NOT NULL
- [ ] Constraints de estado
- [ ] FKs compostas com tenant
- [ ] Transações para estado + outbox + auditoria
- [ ] Optimistic lock em revisão
- [ ] Índices com tenant_id
- [ ] Criptografia em repouso

### Web

- [ ] OIDC authentication
- [ ] Navegação por função
- [ ] Timeout de sessão
- [ ] Sem dados clínicos em URL
- [ ] Sem analytics publicitário
- [ ] Marca d'água em exportações
- [ ] Confirmação de destinatário
- [ ] WCAG 2.2 AA

## Fluxo de trabalho de revisão

### SA-001: Revisar módulo para segurança

1. Verificar autenticação e autorização.
2. Verificar tenant isolation.
3. Verificar auditoria.
4. Verificar redaction de logs.
5. Verificar validação de entrada.
6. Verificar rate limit.
7. Verificar tratamento de erros.
8. Verificar criptografia.
9. Verificar segredos.
10. Listar gaps e recomendações.

### SA-002: Implementar auditoria em módulo

1. Identificar ações auditáveis.
2. Criar eventos de auditoria.
3. Interceptor ou middleware.
4. Hash chain.
5. Redaction.
6. Testes de auditoria.

### SA-003: Configurar RLS

1. Políticas por tabela.
2. Função de contexto de tenant.
3. Testes de isolamento.
4. Testes negativos.

## Testes obrigatórios

- Isolamento de tenant: leitura cruzada bloqueada.
- Autorização: acesso negado sem permissão.
- Auditoria: evento registrado para ação.
- Redaction: logs sem dados pessoais.
- Upload: malware detectado e rejeitado.
- IA: política aplicada, hash calculado.
- Erros: sem conteúdo clínico.
- Rate limit: aplicado e respeitado.

## Saída obrigatória

```text
Tarefa:
Fase: transversal — Segurança e Auditoria
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: conforme fase ativa
```
