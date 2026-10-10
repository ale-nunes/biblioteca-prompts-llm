# P-006 — Planejamento de fluxo multiagente

Atue como arquiteto de sistemas multiagente. Use múltiplos agentes apenas quando houver benefício claro em especialização, paralelismo ou isolamento de responsabilidades.

Para cada agente, defina:
- Nome e responsabilidade exclusiva.
- Entradas e saídas estruturadas.
- Ferramentas e permissões.
- Critério de conclusão.
- Condições de erro e escalonamento.
- Dados que pode acessar.
- Como suas afirmações serão verificadas.

Defina também:
- Grafo de execução e transições.
- Estado compartilhado mínimo.
- Limites de iteração e orçamento.
- Estratégia de retry com limite.
- Tratamento de falhas parciais.
- Pontos de aprovação humana.
- Testes de integração e critérios para escolher uma arquitetura mais simples.

Evite agentes redundantes, loops sem saída e delegação sem critério de aceitação. Não invente APIs específicas de frameworks.
