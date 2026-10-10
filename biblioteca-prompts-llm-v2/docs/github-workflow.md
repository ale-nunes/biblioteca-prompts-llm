# Fluxo GitHub: publicar e manter a biblioteca

## 1. Criar repositório

Crie um repositório no GitHub com nome sugerido `biblioteca-prompts-llm`. Para o primeiro envio, pode ser privado; torne público apenas depois de revisar conteúdo, licença e ausência de dados confidenciais.

## 2. Preparar arquivos

Extraia o ZIP, abra um terminal na pasta do projeto e execute:

```bash
python scripts/validate_cases.py
git init
git add .
git status
```

Confira `git status` e garanta que não há `.env`, chaves, documentos privados ou dados de clientes.

## 3. Primeiro commit

```bash
git commit -m "feat: adiciona biblioteca de prompts LLM v2"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/biblioteca-prompts-llm.git
git push -u origin main
```

Substitua a URL pelo repositório criado. Se o remoto já tiver README ou commits, sincronize e resolva conflitos antes do push; não force o envio sem entender a divergência.

## 4. Fluxo de evolução

```bash
git checkout -b feat/novo-prompt-avaliacao
# editar prompt, casos e changelog
python scripts/validate_cases.py
git diff
git add prompts tests evaluation CHANGELOG.md
git commit -m "feat: adiciona prompt de avaliação"
git push -u origin feat/novo-prompt-avaliacao
```

Abra um Pull Request, revise o diff e só então integre à `main`.

## 5. Versionamento

- `PATCH`: correção de clareza sem mudança do comportamento esperado.
- `MINOR`: novo prompt ou capacidade compatível.
- `MAJOR`: alteração incompatível de contrato ou organização.

Registre mudanças no `CHANGELOG.md`. Para uma versão marcada, use tags:

```bash
git tag v2.0.0
git push origin v2.0.0
```

## 6. Boas práticas

- Prefira commits pequenos e mensagens semânticas (`feat`, `fix`, `docs`, `test`).
- Use Issues para registrar falhas e ideias.
- Não inclua chaves em exemplos; use placeholders.
- Não trate um teste estrutural como prova de qualidade semântica.
- Para alterações importantes, registre comparação da versão antiga e nova.
