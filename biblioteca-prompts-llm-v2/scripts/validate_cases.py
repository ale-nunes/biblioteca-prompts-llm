#!/usr/bin/env python3
"""Valida a estrutura de tests/cases.jsonl usando apenas a biblioteca padrão."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests" / "cases.jsonl"
REQUIRED = {"id", "prompt_id", "category", "input", "expected", "severity"}
VALID_SEVERITIES = {"normal", "high", "critical"}

def main() -> int:
    if not CASES_PATH.exists():
        print(f"ERRO: arquivo não encontrado: {CASES_PATH}")
        return 1

    seen = set()
    errors = []
    count = 0
    for line_no, raw in enumerate(CASES_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        count += 1
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"Linha {line_no}: JSON inválido: {exc}")
            continue

        missing = REQUIRED - set(case)
        if missing:
            errors.append(f"Linha {line_no}: campos ausentes: {', '.join(sorted(missing))}")
            continue

        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"Linha {line_no}: id precisa ser texto não vazio")
        elif case_id in seen:
            errors.append(f"Linha {line_no}: id duplicado: {case_id}")
        seen.add(case_id)

        if not isinstance(case["input"], dict):
            errors.append(f"Linha {line_no}: input precisa ser objeto JSON")
        if not isinstance(case["expected"], dict):
            errors.append(f"Linha {line_no}: expected precisa ser objeto JSON")
        if case["severity"] not in VALID_SEVERITIES:
            errors.append(f"Linha {line_no}: severity deve ser um de {sorted(VALID_SEVERITIES)}")

    if errors:
        print("Validação FALHOU:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validação estrutural OK: {count} casos, IDs únicos.")
    print("Observação: este script não avalia a qualidade semântica das respostas da LLM.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
