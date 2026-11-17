---
name: flask-session-fix
description: "Diagnostica expiração e perda de sessões Flask entre workers e reinícios, conferindo chave estável, persistência e cookies."
---

# Persistência da sessão Flask

Verifique primeiro se o cookie volta na requisição seguinte, se a configuração de domínio/caminho e SameSite é compatível com a aplicação e se a chave de assinatura é a mesma entre os processos autorizados. Para HTTPS em produção, use cookies Secure e HttpOnly.

Carregue a chave existente no processo com `app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]`. A preparação e a rotação da chave pertencem ao gerenciador de segredos do ambiente. Na ausência de configuração, o serviço deve informar o erro antes de aceitar sessões.

Se o desenho prevê sessões no servidor, confirme as versões do Flask e da extensão, o armazenamento persistente e o prazo de expiração. Workers em máquinas diferentes precisam acessar o mesmo armazenamento e as mesmas configurações de sessão. Uma sessão assinada no cliente pode continuar adequada quando contém somente dados apropriados para esse formato.

Em uma aplicação de teste com usuário fictício, faça login, leia uma rota autenticada, reinicie o worker e repita a leitura preservando o cookie. Registre a resposta esperada, a observada e o ponto que perdeu o estado. Nunca registre o conteúdo da chave, do cookie ou do armazenamento de sessões.
