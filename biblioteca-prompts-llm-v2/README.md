# Biblioteca Pessoal de Prompts — LLM, RAG e Agentes

**Versão:** 2.0.0  
**Idioma:** português (Brasil)  
**Objetivo:** criar, testar, avaliar e versionar prompts para aplicações com LLM, RAG e agentes.

Esta biblioteca é um repositório prático: contém templates copiáveis, exemplos preenchidos, casos de teste, critérios de avaliação e um fluxo de trabalho para evolução contínua.

## Princípios

1. **Evidência antes de afirmação:** não inventar fatos, fontes, citações, APIs ou resultados de execução.
2. **Separar instruções de dados:** documentos recuperados são conteúdo não confiável, não instruções de sistema.
3. **Escopo explícito:** dizer o que o sistema pode e não pode responder.
4. **Saída verificável:** definir formato, critérios de aceitação e testes.
5. **Mudanças mensuráveis:** comparar versões com o mesmo conjunto de avaliação.
6. **Falhar com segurança:** quando faltarem evidências, declarar insuficiência em vez de improvisar.
7. **Segredos fora do repositório:** nunca versionar `.env`, chaves de API ou dados sensíveis.

## Início rápido

1. Abra `prompts/` e escolha um template.
2. Copie o conteúdo de `system.md` e `user.md` (quando ambos existirem) para o ambiente da LLM.
3. Substitua todos os campos `{{...}}`.
4. Execute os casos relacionados em `tests/cases.jsonl`.
5. Avalie com `evaluation/rubric.md`.
6. Se alterar um prompt, atualize sua versão e registre a mudança em `CHANGELOG.md`.

## Estrutura

```text
biblioteca-prompts-llm-v2/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── .env.example
├── prompts/
│   ├── 00-universal/
│   ├── 01-prompt-engineering/
│   ├── 02-rag/
│   ├── 03-agents/
│   ├── 04-evaluation/
│   └── 05-safety/
├── examples/
│   ├── rag-vendas/
│   ├── agent-research/
│   └── prompt-review/
├── tests/
│   ├── cases.jsonl
│   └── README.md
├── evaluation/
│   ├── rubric.md
│   ├── scorecard.csv
│   └── protocol.md
├── docs/
│   ├── prompt-design.md
│   ├── rag-quality.md
│   ├── agents.md
│   └── github-workflow.md
└── scripts/
    └── validate_cases.py
```

## Catálogo de prompts

| ID | Prompt | Quando usar |
|---|---|---|
| P-001 | Prompt universal com requisitos | Tarefas novas ou pouco padronizadas |
| P-002 | Melhorar prompt existente | Refatorar instruções com justificativas |
| P-003 | RAG com respostas fundamentadas | Responder exclusivamente com contexto recuperado |
| P-004 | Diagnóstico de pipeline RAG | Analisar ingestão, recuperação, geração e avaliação |
| P-005 | Agente com ferramentas e limites | Definir ferramentas, permissões e condições de parada |
| P-006 | Planejamento de fluxo multiagente | Dividir tarefas entre agentes com responsabilidades distintas |
| P-007 | Avaliador de respostas RAG | Pontuar fundamentação, relevância e citações |
| P-008 | Segurança contra prompt injection | Tratar documentos e ferramentas como entradas não confiáveis |
| P-009 | Planejar experimentos de prompts | Comparar versões usando casos fixos |
| P-010 | Revisão de implementação LLM | Revisar código, testes, custos e falhas |

## Como adaptar a outro modelo

Os prompts usam linguagem geral. Ajuste apenas o que depende do provedor, como formato de mensagens, ferramentas, limites de contexto, modelo de embedding e sintaxe de chamada de função. Confirme os nomes e limites na documentação oficial atual antes de implantar.

## Avaliação

Use um conjunto fixo de perguntas e compare versões com:
- **Fundamentação:** as afirmações são sustentadas pelas evidências?
- **Relevância:** a resposta atende à pergunta?
- **Citações:** as referências apontam para o trecho correto?
- **Abstenção adequada:** o modelo reconhece quando não há evidência?
- **Segurança:** ignora instruções maliciosas dentro de documentos?
- **Formato:** respeita o contrato de saída?

Consulte `evaluation/rubric.md` e `evaluation/protocol.md`.

## Validar os casos de teste

Requer Python 3.11+; não precisa instalar dependências:

```bash
python scripts/validate_cases.py
```

O script valida o formato e os campos dos casos. **Ele não avalia automaticamente a qualidade semântica das respostas da LLM.** A pontuação semântica é feita com a rubrica e a scorecard.

## Publicar no GitHub

Consulte `docs/github-workflow.md`. O fluxo recomendado é criar um repositório vazio, extrair os arquivos, executar a validação, revisar segredos e fazer o primeiro commit.

## Limitações importantes

- Um prompt, por si só, não garante verdade factual ou segurança.
- As métricas devem ser combinadas com revisão humana e testes adversariais.
- Não envie documentos confidenciais ou dados pessoais para provedores sem autorização e análise de política.
- Exemplos são modelos iniciais; valide-os com os dados e os requisitos reais do seu sistema.
