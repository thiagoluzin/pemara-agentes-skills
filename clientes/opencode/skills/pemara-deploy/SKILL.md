---
name: pemara-deploy
description: Preparar e executar deploys autorizados com preflight, artefato identificável, smoke test, observabilidade e rollback. Usar em publicação, release, migração, atualização de serviço ou preparação de pipeline de implantação.
---

# Deploy Pemara

1. Confirmar destino, artefato, versão, autorização e plano de rollback.
2. Fazer preflight de configuração, dependências, migrações, capacidade e segredos sem exibi-los.
3. Validar o artefato a publicar com `pemara_quality_verify`.
4. Publicar somente dentro da autorização atual; pedir decisão para ação externa nova ou irreversível.
5. Fazer smoke test no destino e verificar logs ou métricas relevantes.
6. Registrar versão, evidências e estado de rollback; reverter com segurança se os critérios falharem.

O retorno zero do comando de publicação não prova saúde. Confirmar o comportamento no destino.
