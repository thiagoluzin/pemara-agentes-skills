---
name: terra-helena-wan-sprites
description: "Produza e integre candidatos de sprites completos da Helena com Wan2.2 e Krita, validando identidade, direções próprias e animação renderizada no Godot."
---

# Helena: Wan2.2, sprites e jogo

Leia `AGENTS.md`, `TerraDevolveGodot/README.md`, `ANIMACAO_REQUISITOS.md`, `Docs/README.md`, `06_PIPELINE_DE_ASSETS.md` e a preparação em `art_source/Helena_Redesenho_6/PixelAnimate_v21/`. Para runtime, leia também `01_ESCOPO_GDD.md`, `02_ARQUITETURA_TECNICA.md` e `10_CONTROLES_E_MIRA_FIXA.md`. A skill Gemini Decision 1 obrigatória não autoriza envio de imagens, custo ou mudança de motor.

## Escolha de autoria e identidade

O proprietário escolheu Wan2.2 para esta etapa e pediu a mesma Helena da caminhada recuperada: `ATD_Helena_Design_v2.png`, cabelo preso, camisa bege, jeans, botas e bolsa à esquerda anatômica. A referência legada `assets/helena.png` tem cabelo ondulado e jaqueta ocre; preserve-a como fonte histórica, sem misturar os designs nas novas ações. Preserve fontes e hashes. Não gerar outra pessoa apenas a partir da descrição; não colar rosto/cabeça recortados em corpos gerados.

Cada quadro contém Helena inteira em 2D, com desenho temporal coerente. Sem 3D, rig de recortes, espelhamento integral ou deformação/cópia contados como novos quadros. Folhas novas têm no máximo seis quadros; múltiplas folhas compõem ciclos maiores. As folhas legadas ativas são provisórias e não autorizam repetir suas falhas.

## Verificar o workflow real

Distinga `Wan2.2 Animate 14B` do adaptador `Wan2.2 Pixel Animate` sobre I2V A14B high/low noise. Não são nomes intercambiáveis nem workflows automaticamente compatíveis. Leia a [model card do adaptador](https://huggingface.co/styly-agents/Wan2-2-pixel-animate) e o workflow escolhido; descubra schemas/nodes e modelos reais no servidor configurado. Valide compatibilidade de pesos, precisão, VAE, encoder e condicionamento antes de execução. Não copie comandos de instalação da model card nem execute código externo sem revisão.

Confirme servidor, GPU, memória e fila a cada sessão. Use ferramentas ComfyUI conectadas quando suficientes. Não interrompa, apague ou reordene trabalhos alheios; respeite conteúdo e acesso do servidor. Gere apenas lote necessário ao pedido. Guarde workflow exato, modelo/hash/revisão, seed, prompt, fontes, resultado e decisão de revisão. Um diagnóstico antigo não prova indisponibilidade atual.

O proprietário informou que a caminhada já foi concluída no registro de aprovação do projeto. O relato desse trabalho descreve 256 quadros, 32 por direção em oito direções, 48 folhas com até seis quadros, com pequenas variações/emendas ainda sujeitas a revisão artística. A fonte dessa produção é `ATD_Helena_Design_v2.png`, aprovada naquele chat; preserve também `assets/helena.png` e reconcilie as duas identidades sem substituir fontes silenciosamente.

Para continuar esse lote em ações novas, use a referência e as âncoras de `ATD_Helena_Design_v2.png` recuperadas com ele; não reinstale automaticamente a jaqueta/cabelo da personagem legada nos quadros de arma. O pacote está identificado em `art_source/Wan_8direcoes_Importacao/`. Suas fontes RGB são opacas: a importação candidata deriva apenas alpha e pivôs, preservando RGB/geometria. Frente selecionada é `south_v2`. O modo `--wan-candidate` permite revisão no jogo sem promover o lote à arte padrão ou alterar o save do jogador.

Primeiro localize as folhas desse trabalho, compare arquivos/hashes e reconcilie com os ativos do jogo. Não refaça a caminhada por iniciativa própria nem trate a documentação anterior de pendência como prova contra essa informação. O relato do chat e a correspondência exata entre arquivos locais são evidências diferentes; se o link não abrir, registre o limite e procure fontes locais preservadas. A conclusão técnica de 256 quadros não significa aprovação artística ou cumprimento do requisito de mil quadros da cobertura total.

Reutilize e integre o material identificado conforme a autorização vigente, com revisão renderizada. Para cobertura que realmente faltar, valide um ciclo em uma direção antes de multiplicar a produção. Wan fica para novas ações como sacar/mirar/atirar/recarregar e direções faltantes, conforme escopo autorizado. Esses estados devem mostrar pegada, postura, recuo e recuperação plausíveis com bolsa e mãos consistentes. Oito direções são um conjunto finito; não prometer “todas” sem listá-las e medir cobertura.

## Autoria no Krita por MCP

O MCP local do Krita está configurado no usuário para todos os projetos. Prefira suas ferramentas nativas de documento, camadas, pintura e preview; leia `krita-mcp-workflow`. Confirme as capacidades da sessão, use IDs explícitos e mantenha um único agente escritor no Krita. Se o registro do chat for anterior à instalação, a referência de fallback dessa skill descreve o cliente MCP STDIO já instalado, sem reiniciar o Codex nem depender da captura da interface. O MCP não altera o motor Wan escolhido nem concede aprovação artística. Para animação e crítica independente, consulte as skills globais `krita-sprite-animation` e `krita-art-review`, mantendo os requisitos específicos deste projeto.

## Vídeo não é folha aprovada

Wan pode produzir sequência de vídeo: extração, transparência e montagem de atlas são passos distintos. Remoção de fundo deve preservar dedos, cabelo, arma e botas. Extraia apenas fases úteis; cópias, interpolação e quadros defeituosos não aumentam contagem autoral. RIFE para apresentação de vídeo não cria novos desenhos aprovados de sprites. Se houver render/upscale, declare `content_kind=animation` e siga o contrato do proprietário; isso não impõe upscale aos atlas.

Inspecione alternância dos membros do quadril à bota, contato, transferência de peso, folga do pé, identidade e fechamento do ciclo, normal e lento. Krita serve à limpeza com master em camadas e original preservado; verifique a autorização para controle de tela na tarefa. Candidato rejeitado permanece fora da arte ativa; referência não equivale a autorização de promoção.

## Integrar sem mascarar defeitos de pose

O runtime usa `scripts/helena_frames.gd`/`assets/helena/regioes.json`, `Sprite2D`, pivô pelas solas e fase pela distância realmente percorrida após colisão. Preserve essa intenção; não troque para reprodução por tempo ou ping-pong para disfarçar passada incorreta. Só altere estrutura de atlas quando necessário, com durações, ordem, direção e pivô explícitos.

Revise candidato numa cena isolada renderizada no tamanho das duas salas antes de substituir ativos. Confira parada, giro, colisão, profundidade e acessórios assimétricos. Para arma, associe disparo lógico e quadro visual sem causar dano duas vezes; câmera continua fixa. Rode `Testar.ps1` para alterações de runtime. Compare fontes e arte ativa por hash e registre evidência; bounds corretos não certificam caminhada natural nem aprovação humana.

A [documentação Godot de animação 2D](https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html) descreve opções de engine, não exige substituir a implementação existente. Valide APIs na 4.7.2 local.
