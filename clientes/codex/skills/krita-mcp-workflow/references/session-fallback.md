# MCP disponível fora do registro atual

Use este fallback somente se as ferramentas nativas Krita não estiverem disponíveis na sessão atual. Não reinicie o Codex ou este chat. Verifique a existência dos arquivos antes de usar; caminhos locais podem mudar.

Quando o projeto instalar o cliente autorizado `krita_mcp_client.py`, use o Python do mesmo ambiente do servidor Krita MCP e confirme o contrato com `--help`. O cliente usa o SDK MCP e o servidor STDIO instalado, sem HTTP bruto, execução arbitrária no Krita ou captura da interface.

Comece por `--list` para confirmar os esquemas reais. Chamadas usam `--tool krita_nome`, `--arguments caminho-absoluto.json` com argumentos UTF-8 e `--result caminho-absoluto.json` para recibo. Quando precisar das imagens retornadas pelo MCP, passe `--image-dir diretorio-novo`: são PNGs nativos da projeção da arte e podem ser inspecionados com `view_image`, não screenshots da interface.

Crie arquivos de argumentos/recibos numa pasta de evidências autorizada e preserve entradas existentes. Não use essa ponte para contornar raízes, capacidades ou autorização. As mesmas regras de escritor único, IDs explícitos e resultado desconhecido após timeout continuam válidas. `NO_ACTIVE_DOCUMENT` pode ser normal com Krita aberto sem documento; inspecione a lista e identifique o alvo dentro do escopo autorizado.
