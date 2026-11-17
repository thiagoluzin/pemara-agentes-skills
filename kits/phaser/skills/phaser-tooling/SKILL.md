---
name: phaser-tooling
description: "Auditar e consolidar agentes, skills e ferramentas de produção Phaser, automatizando operações repetidas sem acoplamento a um jogo."
---

# Ferramentas e manutenção Phaser

Inventarie fontes reais antes de contar capacidades: skills instaladas, instruções de agentes, scripts, entrypoints e referências. Nome no roteador não prova instalação; arquivo sem referência não prova lixo, pois pode ser uma ferramenta manual. Separe código ativo, teste, receita, script pontual, resultado gerado e cache.

Avalie utilidade por tarefa e evidência. Mantenha invariantes de ciclo de vida, medidas e contratos que evitam defeitos. Una responsabilidades sobrepostas em uma fonte; referências sob demanda preservam detalhes específicos. Retire do núcleo personas genéricas repetidas, promessas de qualidade, números sem fonte e regras de um único projeto apresentadas como universais.

Ferramentas que dependem de personagens, caminhos, cenas ou schemas locais permanecem no projeto até terem uma API genérica demonstrada. Não exporte arquivos privados para ganhar volume. Conteúdo de terceiros exige origem/licença; se incertas, referencie ou reescreva orientação própria, sem copiar a implementação.

Automação deve ter entradas/saídas explícitas, logs úteis, códigos de saída reais e limites de caminho. Pré-visualização é valiosa em mutações em lote. Retry de leitura idempotente pode ajudar; geração paga, upload e outros efeitos precisam de política explícita para não duplicar trabalho ou gastos. Não faça retry universal.

Instalação deve ser local ao projeto, recusar colisões, preservar edições e deixar recibo de arquivos próprios. Não repurponha configuração global ou remova pastas arbitrárias. Teste diretórios com espaços, Unicode, symlinks/junctions, instalação repetida, falha parcial e desinstalação.

O verificador do pacote comprova estrutura, metadados, links e higiene conhecida; não certifica qualidade de todos os agentes, ausência de todo segredo ou runtime de qualquer jogo. Experimentos comportamentais exigem execução observada e escopo permitido, sem autoridade implícita para delegar.

Entregue decisões por item, dependências, testes e limitações. Use palavras/bytes medidos para tamanho do pacote, não porcentagens inventadas de economia de tokens ou produtividade.
