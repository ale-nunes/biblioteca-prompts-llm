# Qualidade de RAG

## Diagnóstico em camadas

### 1. Ingestão
O texto foi extraído corretamente? Há páginas, tabelas, metadados ou caracteres perdidos?

### 2. Chunking
Os trechos preservam contexto suficiente? O tamanho e a sobreposição foram avaliados empiricamente?

### 3. Recuperação
Os documentos relevantes aparecem no top-k? Teste consultas representativas, sinônimos, filtros e perguntas ambíguas.

### 4. Reranking e contexto
Os melhores trechos ficam no contexto final? Há excesso, duplicação ou contradição?

### 5. Geração
A resposta usa apenas evidências? Citações apontam para trechos reais? O sistema se abstém quando necessário?

### 6. Avaliação
Mantenha um conjunto de referência com perguntas, documentos esperados e comportamento esperado. Meça recuperação e qualidade da resposta separadamente.

## Nota para assistentes de dados

RAG não substitui consultas analíticas exatas. Para somas, médias, contagens e indicadores comerciais, prefira SQL validado ou uma camada semântica controlada; use RAG para definições, documentação e contexto textual quando apropriado.
