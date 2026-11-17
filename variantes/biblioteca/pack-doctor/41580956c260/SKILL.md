---
name: pack-doctor
description: "Auditar o pacote local de agentes de jogos: roteador, specs, skills, referências e comandos canônicos. Use para verificar instalação ou manutenção do pacote; não certifica gameplay, qualidade artística ou release."
---

# Pack Doctor — integridade dos agentes de jogos

## TURBO OPERATING PROTOCOL
Leia `AGENTS.md`, confira o estado real e preserve alterações existentes. O pacote local tem fonte em `.agents/` e descoberta em `.agents/skills/`. Conte arquivos a cada auditoria; não use uma contagem histórica como meta fixa.

## Auditoria determinística
1. Execute `npm run audit:agent-pack`, definido no `package.json`. Ele testa o próprio verificador e executa `tools/verify_agent_pack.py` sobre o pacote. Guarde a saída e o código de saída real, sem escondê-lo por filtros ou pipelines.
2. O verificador cobre arquivos obrigatórios, nomes/frontmatter, corpo não vazio, paridade de inventário, referências de skills, tabelas de encaminhamento para agentes e links de specs canônicos. Os comandos npm de todos os specs, skills e do roteador devem existir no `package.json`; isso comprova existência, não execução nem cobertura.
3. Nas skills com link **Spec canônico**, leia o arquivo vinculado antes de executar a tarefa; altere o procedimento no spec. A skill conserva nome e descrição para descoberta. Outros pares podem ter conteúdo especializado distinto: diferença de texto não é, por si só, defeito.
4. Valide ferramentas adicionais apenas quando solicitadas ou presentes como instalação ativa. Não declare Claude, Cursor ou OpenCode instalados porque o roteador menciona seus formatos; uma pasta de configurações não comprova um pacote de agentes.
5. Revise o sentido do encaminhamento: arquivo existente não prova que o especialista é adequado. `pack-doctor` valida agentes; `qa-automation-engineer` valida jogo em execução; `demo-release-engineer` valida o pacote distribuído.

## Avaliação de comportamento
Só reporte teste comportamental quando tiver executado a tarefa com o agente/skill. Se delegação estiver permitida, use uma tarefa independente e limitada, sem editar o jogo ou consumir geração paga. Caso contrário, faça revisão estática e declare essa limitação.

Casos úteis para ensaiar, sem entregar a resposta esperada ao avaliador:
- “Crie um encontro de beat-em-up Phaser para Android preservando os controles aprovados.”
- “A música duplica só depois de passar para a próxima fase.”
- “O herói muda de tamanho ao atacar; corrija preservando os assets travados.”

Avalie evidências consultadas, escolha do especialista, respeito às decisões do usuário e método de verificação. Falar no personagem ou repetir o protocolo não prova qualidade. Um ensaio de planejamento não equivale a implementação ou playtest.

## Encerramento
Corrija no arquivo real e registre no `FIXLOG.md`. Se mudar o verificador, adicione testes de falha em diretório temporário para a classe de regressão corrigida; nunca corrompa o pacote real para testar. Não gere caches Python no repositório. Execute `npm run audit:agent-pack` novamente e `npm run deploy:check` antes de entrega, preservando qualquer bloqueio encontrado.

Reporte contagem, escopo verificado, mudanças, testes com resultado e limitações. Integridade do pacote não comprova desempenho, diversão, qualidade das respostas nem build do jogo.
