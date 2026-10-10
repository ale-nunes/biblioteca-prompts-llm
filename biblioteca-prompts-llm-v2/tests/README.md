# Testes de prompts

`cases.jsonl` contém um caso JSON por linha. Cada caso tem:
- `id`: identificador estável.
- `prompt_id`: prompt avaliado.
- `category`: tipo de comportamento.
- `input`: entrada de teste.
- `expected`: comportamentos esperados.
- `severity`: impacto de uma falha.

## Como adicionar casos

Inclua pelo menos um caso normal e um caso-limite para cada prompt crítico. Prefira casos derivados de falhas reais, anonimizados e sem segredos.

## Tipos de teste recomendados

- Caminho feliz.
- Contexto insuficiente.
- Fontes conflitantes.
- Citação inexistente.
- Prompt injection.
- Ferramenta indisponível.
- Saída malformada.
- Limite de custo ou iterações.
- Regressão de um comportamento previamente correto.

O validador verifica a estrutura do arquivo, não a resposta produzida pela LLM. Para avaliação semântica, execute o mesmo conjunto com cada versão do prompt e preencha a scorecard.
