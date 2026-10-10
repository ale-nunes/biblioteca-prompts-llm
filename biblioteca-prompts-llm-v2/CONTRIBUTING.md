# Como contribuir para a biblioteca

## Regras para adicionar um prompt

Cada novo prompt deve incluir:
1. ID único (`P-###`) e título.
2. Objetivo e cenário de uso.
3. Variáveis de entrada claramente identificadas.
4. Instruções e restrições explícitas.
5. Formato de saída.
6. Critérios de aceitação.
7. Pelo menos dois casos de teste, incluindo um caso de falha ou insuficiência de contexto.
8. Registro no `CHANGELOG.md`.

## Padrão de nomes

Use pastas com prefixo numérico e nomes curtos em kebab-case. Exemplo: `prompts/02-rag/`.

## Antes de abrir um pull request

- [ ] Os placeholders `{{...}}` estão documentados.
- [ ] Nenhuma chave, senha ou dado confidencial foi incluído.
- [ ] Os testes de estrutura passam.
- [ ] A versão e o changelog foram atualizados quando necessário.
- [ ] A alteração tem justificativa e casos de teste.
- [ ] Foram consideradas respostas sem evidência e entradas maliciosas.

## Critério de qualidade

Não aceite mudanças só porque um exemplo isolado ficou melhor. Compare a versão anterior e a nova no mesmo conjunto de casos e registre regressões.
