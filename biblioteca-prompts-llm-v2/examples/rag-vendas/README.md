# Exemplo — RAG/assistente de vendas

## Cenário

Um assistente responde perguntas sobre uma base interna de vendas. Para métricas numéricas, SQL ou uma camada analítica validada deve ser a fonte de verdade; RAG pode apoiar a recuperação de definições, documentação e contexto textual.

## Exemplo de entrada

```text
Pergunta: Quais são as regras de cálculo da receita líquida?
Contexto recuperado:
[doc-12, trecho 3] Receita líquida = receita bruta - descontos - devoluções,
conforme a definição adotada neste conjunto de dados.
```

## Comportamento esperado

- Responder com a fórmula encontrada.
- Citar `[doc-12, trecho 3]` no formato de citação do sistema.
- Não inferir valores de receita sem consultar a fonte analítica.
- Se a definição não estiver recuperada, informar que não há evidência suficiente.
- Se o usuário pedir um número, identificar período, filtros e definição da métrica antes de calcular.

## Prompt recomendado

Use `prompts/02-rag/P-003-rag-fundamentado/` e adapte as regras para separar perguntas documentais de consultas numéricas.
