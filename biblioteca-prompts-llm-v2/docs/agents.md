# Desenho de agentes

## Comece simples

Use uma chamada de modelo ou um fluxo determinístico se isso resolver o problema. Multiagentes aumentam latência, custo, complexidade e superfície de falha; adote-os quando houver benefício mensurável.

## Contrato de cada agente

- Objetivo único.
- Entrada validada.
- Saída estruturada.
- Ferramentas autorizadas.
- Limite de iterações e tempo.
- Critério de conclusão.
- Tratamento de falhas.
- Regras de escalonamento para pessoa.

## Ferramentas

- Use allowlists.
- Valide argumentos.
- Restrinja permissões ao mínimo.
- Exija aprovação humana para ações irreversíveis ou externas de impacto.
- Não permita que documentos recuperados concedam novas permissões.
- Registre operações sem armazenar segredos ou conteúdo sensível desnecessário.

## Testes essenciais

- Ferramenta indisponível.
- Entrada inválida.
- Resultado conflitante.
- Pedido fora de escopo.
- Tentativa de injeção de prompt.
- Limite de iteração atingido.
- Aprovação humana ausente.
