# Portões do Pemara Quality Unify

## Escopo padrão

O scanner lê arquivos de texto e ignora `.git`, `node_modules`, ambientes virtuais, caches, builds e cobertura. Binários são inventariados, mas não decodificados.

## Erros bloqueantes

- `unicode.invalid_utf8`: bytes que não formam UTF-8.
- `unicode.mojibake`: sequências típicas de UTF-8 lido como Windows-1252.
- `skill.frontmatter`: `SKILL.md` sem frontmatter, `name` ou `description` válidos.
- `skill.duplicate_name`: duas skills com o mesmo nome no escopo.
- `plugin.manifest`: JSON ausente, inválido ou sem campos obrigatórios.
- `manifest.path`: item declarado sem arquivo correspondente ou fora da raiz.
- `manifest.checksum`: SHA-256 diferente do manifesto.
- `security.secret_file`: arquivo de segredo, chave privada ou `.env` dentro do pacote.

## Avisos

- arquivo de texto muito grande;
- PowerShell com texto não ASCII sem BOM;
- skill acima de 500 linhas, exceto pacote de fornecedor assinado que não pode ser reescrito sem invalidar a assinatura;
- item não classificado no manifesto.

Use `--fail-on-warning` no portão final de um instalador.

## Reparação de Unicode

A edição pública 1.0.1 ignora links simbólicos e pontos de reanálise. Aplique em uma árvore estável, com o diretório de backup separado da origem. Cada backup é criado com exclusividade. Se o nome do backup já existir, esse arquivo fica pendente e o relatório registra um erro. O reparo preserva o BOM de arquivos UTF-8 e substitui o arquivo por renomeação local após criar o backup e conferir os bytes originais.

`repair-unicode` tenta a reversão Windows-1252 → UTF-8 somente quando reduz marcadores de mojibake e não introduz caracteres de substituição ou controles. Sem `--apply`, não escreve. Com `--apply`, exige `--backup-root`, que deve ficar fora da árvore de origem.

## Relatório

O JSON contém versão do schema, data UTC, raiz, contadores, veredito e achados. Códigos de saída: `0` aprovado, `1` erros, `2` avisos quando `--fail-on-warning` estiver ativo.
