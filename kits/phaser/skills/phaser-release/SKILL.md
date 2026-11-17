---
name: phaser-release
description: "Empacotar e verificar jogos Phaser para web, desktop ou Android, conferindo o conteúdo efetivamente distribuído e sua inicialização."
---

# Build e entrega Phaser

Descubra scripts, versão, saída e plataforma reais antes de construir. Leia os comandos e filtros; um package.json externo não é autorização para executar scripts arbitrários. Use lockfile e dependências do projeto. Não imponha Electron, Capacitor ou migração para um pedido de build web.

Execute os gates exigidos pelo consumidor. Antes de repetir build demorada, teste o estágio alterado e preserve log e exit code. Não masque falha com pipe, ignore scripts de verificação ou rebase de referência.

Inspecione o produto: assets incluídos, pares convertidos, caminhos relativos/base path, fontes, vídeos, áudio e chunks. Dev server funcionar não comprova protocolo desktop, subdiretório web, cache/service worker ou WebView. Confira versão/hash dentro do pacote quando possível.

Teste o artefato produzido: menu, iniciar partida, pausa, áudio, próximo trecho, derrota e reinício. Compare tamanho com a composição esperada. Para Android, registre assinatura/tipo de build, versão e instalação/abertura no aparelho acessível; fonte compilada não é APK entregue. Para desktop, dist/ não é executável validado.

Não desative assinatura ou proteção por padrão para contornar erro de ambiente. Distinga distribuição de teste local de release assinada. Não introduza obfuscação como requisito de segurança ou desempenho.

Para publicação autorizada, prepare a árvore final e confirme que só o conteúdo pretendido será exposto: assets licenciados, ausência de credenciais, arquivos privados, histórico indevido e configurações locais. Use destino/visibilidade solicitados. Não publique por inferência de um mero pedido de compilar.

Conclua com caminho/URL, hash, build/commit, comando e exit code, conteúdo conferido e testes feitos no pacote. Informe instalação não exercitada, assinatura ausente ou dispositivo indisponível sem chamar isso de release totalmente validada.
