---
name: kobukan-validacao
description: Selecionar e executar validações proporcionais de mudanças no JUDO_KOBUKAN, distinguindo testes locais, bancos descartáveis, ensaios remotos e aceite físico dos dois aplicativos Android.
---

# Validar uma mudança Kobukan

Leia `docs/assistentes/VALIDACAO.md` na raiz do repositório. Parta do diff e do comportamento solicitado; selecione a linha correspondente e abra o teste para conferir dependências, fixtures, destinos e efeitos antes de executar. Não rode todas as suítes por padrão.

Mantenha banco de alunos separado de competições. Testes com banco usam ambiente descartável conforme seus próprios preparadores. Não apontar testes ao banco real para suprir configuração ausente. `check_event_write.php` pode executar commits; não é apenas consulta.

Para Python, escolha o ambiente descrito em `painel-flask/RUNTIME.md` quando o teste depender do painel. Para Flutter, use o diretório do aplicativo correto. Preserve locks e assinatura; não gere outra identidade. Compare modos Twig/legado quando o comportamento de ambas as apresentações for afetado.

Registre comando, resultado e limitações. Resultado histórico de `alunos/VALIDACAO.md` não é teste executado agora. Build/DOM não comprovam aceite visual, câmera, impressão ou uso físico. Mudança somente de documentação requer validar referências e formatos, sem iniciar serviços. Produção, envio SMTP, release e carga dependem do escopo e autorização da tarefa; esta skill não os autoriza.
