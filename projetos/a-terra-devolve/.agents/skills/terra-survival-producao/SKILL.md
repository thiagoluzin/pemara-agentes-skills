---
name: terra-survival-producao
description: "Organize marcos, especialistas e entregas de A Terra Devolve, conciliando combate, investigação, puzzles, narrativa e evidência jogável no Godot."
---

# Produzir A Terra Devolve

Use para coordenar uma entrega do jogo, escolher o próximo incremento ou reconciliar trabalho de várias disciplinas. Uma correção pequena pode ser feita diretamente.

## Contexto e fontes

Localize a raiz pelo `AGENTS.md`; o executável é `TerraDevolveGodot/project.godot`. Leia as instruções aplicáveis, `README.md`, `ANIMACAO_REQUISITOS.md` e `Docs/README.md`. Para gameplay, acrescente `Docs/01_ESCOPO_GDD.md`, `02_ARQUITETURA_TECNICA.md` e `10_CONTROLES_E_MIRA_FIXA.md`. Consulte `09_DIRECAO_CRIATIVA_A_TERRA_DEVOLVE.md` e a revisão narrativa mais recente para conteúdo. Preserve a distinção entre decisão vigente, proposta, candidato rejeitado e implementado.

A skill Gemini Decision 1 é obrigatória neste computador: leia `a skill decision-ai` e a documentação viva pertinente. Isso não exige API num jogo offline, não autoriza custo ou envio de dados e não substitui regras determinísticas de progressão.

## Escolher uma entrega

Trabalhe de uma situação que o jogador possa experimentar: obter uma arma, abrir um atalho, deduzir uma passagem, resistir a um encontro. Expresse o antes/depois, dependências, arquivos, risco de regressão e evidência necessária. Preserve Godot 4.7.2, GDScript tipado, cenas 2D, sinais e uma única fonte de progresso. Extraia sistemas conforme necessidade real; não reescreva o protótipo para satisfazer uma arquitetura hipotética.

O núcleo combina investigação, puzzles e combate vulnerável. Avalie o custo de enfrentar, desviar e retornar; uma campanha que só oferece correr falha na direção do proprietário. Referências de RE1, Silent Hill, Alan Wake 2 e Tormented Souls orientam princípios, sem copiar mapas, personagens ou apresentar perfis como pessoas reais.

## Usar a equipe

Quando autorizado e útil, delegue tarefas independentes com propriedade de arquivos explícita e aviso de trabalho concorrente. Perfis locais em `.codex/agents/`: `survival-director`, `horror-narrative`, `puzzle-designer`, `godot-combat`, `godot-gameplay`, `horror-audio`, `godot-animator`, `krita-comfy-sprite`, `godot-runtime-qa`. Não simule a execução de um perfil que não foi carregado; use seu arquivo como orientação ou um agente disponível com responsabilidade equivalente.

Um responsável integra dependências e resolve contradições. Especialistas não podem aprovar o próprio resultado visual em nome do proprietário. Planejamento, autoria de sprites, implementação e revisão têm evidências distintas; evitar multiplicar relatórios quando uma entrega pequena basta.

## Fechar o incremento

Preserve fontes e saves. Rode `Testar.ps1` para runtime e inspecione logs; use slots de teste. Renderize mudanças visuais no tamanho do jogo e observe o comportamento, não apenas uma captura estática. Registre o que funciona, como reproduzir e o que depende de revisão humana. Aprovado em headless não significa arte, música, equilíbrio ou campanha aprovados.

Priorize uma slice pequena antes de produzir dezenas de salas. A criação de agentes não instala engine, plugin, MCP nem autoriza publicação.

Formato nativo e descoberta: [agentes do Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) e [skills locais](https://learn.chatgpt.com/docs/build-skills). Verifique as fontes oficiais ao modificar esse formato; skills ficam em `.agents/skills/`, perfis em `.codex/agents/`, sem impor modelo ou permissões.
