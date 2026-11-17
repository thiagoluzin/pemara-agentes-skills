# Contrato de compactação e retomada

Crie um handoff factual para o próximo ciclo. A compactação preserva o trabalho; ela não redefine,
reduz nem encerra a tarefa autorizada.

Use obrigatoriamente esta ordem:

1. `Objetivo original do usuário`: mantenha o pedido de nível mais alto e suas palavras restritivas,
   especialmente “até finalizar”, “inteiro”, “todos”, “exatamente”, “não”, “nunca” e equivalentes.
2. `Última instrução direta`: copie com fidelidade a instrução mais recente que alterou o escopo.
3. `Critérios de aceite`: checklist observável, sem trocar requisitos por uma interpretação mais fácil.
4. `Todos atuais`: preserve cada item e seu estado exato (`pending`, `in_progress`, `completed`).
5. `Concluído com evidência`: somente fatos comprovados por arquivos, comandos ou resultados reais.
6. `Estado ativo`: ponto exato da execução, processo ou ferramenta ainda em andamento.
7. `Pendências e falhas`: inclua testes não executados, erros e riscos; não os esconda em “próximos passos”.
8. `Próxima ação executável`: o primeiro passo concreto para continuar sem pedir “vai” ou “continue”.
9. `Checkpoint e controles`: preserve o ID da sessão, o objetivo registrado, pausas, evidência
   pendente e o caminho do projeto real. Recupere `pemara_task_checkpoint` sem criar outro projeto.

Regras duras:

- Concluir um subproblema não conclui o objetivo original.
- Não transforme uma tarefa ampla em resumo de apenas um bug recente.
- Não marque a tarefa como concluída enquanto existir todo `pending` ou `in_progress`.
- Não invente arquivo, teste, resultado, decisão, autorização ou bloqueio.
- Se o usuário pediu parada, cancelamento ou aprovação humana, preserve esse portão e não continue.
- Preserve o modelo escolhido e a janela de contexto configurada; compactar não autoriza reduzir esse limite.
