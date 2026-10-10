# Protocolo de avaliação e comparação

## Objetivo

Comparar prompts de forma reproduzível, sem concluir que uma versão é melhor com base em exemplos isolados.

## Procedimento

1. Registre ID e versão dos prompts, modelo, data, parâmetros e versão do corpus.
2. Use o mesmo conjunto de casos para a versão-base e a candidata.
3. Mantenha os parâmetros constantes sempre que possível.
4. Execute cada caso; para modelos não determinísticos, repita amostras importantes.
5. Avalie as saídas com a rubrica sem consultar a versão do prompt, quando viável.
6. Registre pontuação por dimensão, falhas críticas, latência e custo estimado.
7. Compare média, distribuição e casos individuais; não esconda regressões atrás da média.
8. Faça revisão humana de casos de maior risco.
9. Aprove a mudança somente se atingir os critérios e não introduzir regressões inaceitáveis.

## Métricas

- Taxa de resposta fundamentada.
- Taxa de citações válidas.
- Taxa de abstenção correta em perguntas sem evidência.
- Taxa de respostas relevantes/completas.
- Taxa de resistência a prompt injection.
- Latência e custo por pergunta.
- Taxa de erro técnico ou saída malformada.

## Relatório mínimo

- Hipótese.
- Mudança testada.
- Número de casos e cobertura por categoria.
- Resultados por métrica.
- Falhas críticas e regressões.
- Limitações do experimento.
- Decisão: aprovar, rejeitar ou coletar mais evidências.
