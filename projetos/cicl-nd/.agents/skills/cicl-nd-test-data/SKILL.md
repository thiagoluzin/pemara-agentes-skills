---
name: cicl-nd-test-data
description: "Dados sintéticos, factories, fixtures e estratégias de teste para CICL-ND."
---

# CICL-ND — Skill de Dados Sintéticos e Testes

## Domínio

Transversal: geração de dados sintéticos, factories, fixtures e validação de testes.

## Quando usar

- Criar factories para entidades;
- gerar dados sintéticos para teste;
- configurar fixtures de integração;
- criar cenários de teste adversariais;
- validar isolamento de tenant com dados;
- preparar dados para testes de IA;
- gerar dados extremos para edge cases.

## Documentos de referência

- `docs/13_TESTES_E_VALIDACAO.md`
- `docs/25_DADOS_SINTETICOS_E_FIXTURES.md`
- `AGENTS.md` (proibições: dados reais)

## Regras obrigatórias

1. Dados de teste exclusivamente sintéticos.
2. Nunca copiar prontuários reais.
3. Nunca usar dados parciais ou inferidos de pacientes reais.
4. Nunca inserir dados clínicos reais em serviços públicos de IA.
5. Factories geram dados realistas mas fictícios.
6. Tenants de teste isolados.
7. Seeds apenas para ambiente local.
8. Dados sensíveis gerados de forma determinística para testes repetíveis.

## Estrutura de factories

```typescript
// Exemplo de factory
import { faker } from '@faker-js/faker';

class PatientFactory {
  static create(tenantId: string, override?: Partial<Patient>) {
    return {
      id: generateUuid(),
      tenantId,
      name: faker.person.fullName(),
      dateOfBirth: faker.date.past({ years: 15 }),
      gender: faker.helpers.arrayElement(['M', 'F', 'NB', 'U']),
      status: 'ACTIVE',
      ...override,
    };
  }

  static createBatch(tenantId: string, count: number): Patient[] {
    return Array.from({ length: count }, () => this.create(tenantId));
  }
}
```

## Cenários de teste obrigatórios

### Isolamento de tenant

```typescript
describe('Tenant Isolation', () => {
  it('should not allow cross-tenant read', async () => {
    const tenantA = createTenant();
    const tenantB = createTenant();
    const patientA = patientFactory.create(tenantA.id);
    const patientB = patientFactory.create(tenantB.id);

    const result = await api.getPatient(patientB.id, { tenant: tenantA });
    expect(result.status).toBe(403);
  });
});
```

### Dados extremos

- Paciente sem data de nascimento.
- Medição com componentes inconsistentes.
- Evidência sem proveniência.
- Documento sem data.
- Série temporal com lacunas longas.
- Amostra única para tendência.
- Valores fora de unidade esperada.
- Condições conflitantes em fontes diferentes.

### Testes de IA

- Prompt com dados sintéticos.
- Saída validada contra schema.
- Abstinência com amostra insuficiente.
- Contradição detectada corretamente.
- Tendência `insufficient_data` com 1 ponto.
- Fonte científica expirada não usada.
- Citação verificável.
- Sem hallucinação de referência.

### Testes de segurança

- Acesso sem autenticação: 401.
- Acesso sem autorização: 403.
- Acesso cruzado entre tenants: 403.
- Upload de executável: rejeitado.
- Upload com malware: quarentena.
- Prompt injection no documento: bloqueado.
- Rate limit excedido: 429.
- Erro sem conteúdo clínico.

## Fluxo de trabalho

### TD-001: Criar factories

1. Factory para cada entidade.
2. Método `create` com override.
3. Método `createBatch` para volume.
4. Dados realistas mas fictícios.
5. Determinísticos para testes repetíveis.

### TD-002: Configurar fixtures

1. Fixtures para testes de integração.
2. Setup e teardown por teste.
3. Transações rollback para limpeza.
4. Tenants isolados por suite.

### TD-003: Gerar dados de seed

1. Script de seed para ambiente local.
2. Tenants de demonstração.
3. Profissionais, pacientes, responsáveis.
4. Documentos, evidências, sessões.
5. Metas, medições, eventos contextuais.
6. Fontes científicas.
7. Dados claramente marcados como sintéticos.

### TD-004: Cenários adversariais

1. Tentativa de acesso cruzado.
2. Injeção de prompt em documento.
3. Upload de arquivo poliglota.
4. Medição com unidade inválida.
5. Evidência sem proveniência.
6. IA com amostra insuficiente.
7. Condições conflitantes.

## Testes obrigatórios

- Factories geram dados válidos.
- Isolamento de tenant com dados de teste.
- Dados extremos não quebram o sistema.
- IA abstém com amostra insuficiente.
- Segurança: acessos negados corretamente.
- Auditoria registrada para ações de teste.
- Logs sem dados de teste sensíveis.

## Saída obrigatória

```text
Tarefa:
Fase: transversal — Dados Sintéticos e Testes
Arquivos alterados:
Migrações:
Testes executados:
Resultado:
Riscos pendentes:
Decisões necessárias:
Próxima tarefa permitida: conforme fase ativa
```
