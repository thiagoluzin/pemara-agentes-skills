# Agentes e skills PEMARA

Coleção pública de instruções e perfis para produção audiovisual, música, desenvolvimento de jogos, educação e engenharia de software. O [catálogo por nome](catalogo.json) indica a origem de cada entrada e os arquivos disponíveis nesta edição. Há **599 identificadores de skills** e **158 identificadores de agentes e papéis** com definição ou adaptação neste repositório.

| Coleção | Conteúdo |
|---|---|
| [PEMARA](pemara/README.md) | 87 skills de projeto e 58 perfis. Vídeo, música, jogos e as rotas de engenharia ficam organizados por função. |
| [Clientes](clientes/README.md) | Agentes do Codex, perfis e prompts do OpenCode e skills portáveis, incluindo Decision AI e os papéis do Krita. |
| [Projetos](projetos/) | A Terra Devolve, Kobukan, CICL-ND, PEMARA EDU, Mira e versões anônimas das quatro skills de narrativa familiar. |
| [Kits de jogos](kits/) | 46 skills dos kits públicos de Phaser, Unity e Blender. |
| [Variantes](variantes/README.md) | Perfis do Gemini, Antigravity, Loja e Ritmos. Os adaptadores identificam o corpo de instruções usado por cada projeto ou cliente. |
| [Integrações](integracoes/) | Papéis e etapas do Maestro, perfis do Harness e ferramentas de conferência. |
| [Componentes de terceiros](terceiros/) | 236 pacotes NVIDIA, HyperFrames, extensões Unity, AIQ, ai-memory e outras coleções com origem e atribuições. |

## Usar uma entrada

Procure o nome no catálogo e abra um dos caminhos em \`arquivos\`. Para uma skill, copie a pasta que contém \`SKILL.md\` com seus arquivos de apoio para a raiz de skills do cliente. Se a entrada for um adaptador ou depender de referências entre pastas, mantenha a estrutura da coleção conforme o README correspondente. Para agentes, escolha o formato do cliente. O módulo \`teachingAgents.ts\`, por exemplo, contém as definições e regras da aplicação educacional.

As dependências, modelos e credenciais são configurados no ambiente de destino. Revise permissões e os requisitos do projeto antes de executar ferramentas de um pacote. A distribuição publica definições. A aprovação de mídia, envio a serviços e uso de recursos externos dependem do projeto em que forem aplicadas.

## Cobertura e origem

O índice reúne 809 identificadores de skills e 167 de agentes e papéis. Entradas que trazem somente \`inventario\` identificam componentes dos clientes, cópias históricas ou procedimentos sem distribuição integral aqui. A origem e o caminho de destino distinguem papéis homônimos. Os materiais de produção, dados de usuários e configuração pessoal ficam fora da distribuição.

A [coleção NVIDIA](terceiros/nvidia/ORIGEM.md) preserva os 3.412 arquivos dos 236 pacotes da revisão indicada. As [variantes do projeto](variantes/README.md) preservam os papéis históricos em formato público. As adaptações de privacidade, referências portáveis e revisão defensiva estão descritas nas coleções pertinentes.

## Licenças

Consulte os arquivos LICENSE, NOTICE e ORIGEM nas respectivas pastas. A licença de um componente vale para aquele componente. O Mira mantém a **PolyForm Noncommercial 1.0.0** com a atribuição obrigatória ao Sandeco. [Aviso do Mira](projetos/mira/NOTICE.md) · [Créditos PEMARA](pemara/NOTICE.md) · [Origem NVIDIA](terceiros/nvidia/ORIGEM.md)
