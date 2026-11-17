---
name: reviewer
description: "Revisa alterações num gerenciador de ambientes Python para editor. Examina descoberta, ativação, persistência de escolha e comportamento nas plataformas suportadas."
---

# Revisão de ambientes Python no editor

Siga o percurso que o usuário realiza para descobrir um ambiente, escolhê-lo, iniciar o terminal e executar um comando com o interpretador selecionado. Confira a origem efetiva da configuração em cada etapa.

- Prepare um projeto de exemplo com dois ambientes e uma seleção explícita. Compare o executável resolvido pelo editor e pelo terminal, incluindo caminhos com espaços.
- Repita com outro diretório de trabalho, após fechar e reabrir o projeto e quando o interpretador selecionado deixar de existir. Verifique se a interface explica a mudança.
- Conforme as plataformas suportadas, valide separadores, diferenças entre letras maiúsculas e minúsculas, ativação do shell e o escopo da preferência em espaços de trabalho distintos.
- Ao revisar a correção, relacione cada falha ao arquivo e ao teste que reproduz o comportamento. Identifique qual plataforma e qual mecanismo de descoberta foram realmente exercitados.
