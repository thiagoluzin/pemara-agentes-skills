import argparse, json, sys
from pathlib import Path
from decision_provider import DecisionClient, ProviderError
parser = argparse.ArgumentParser(description="Gemini Decision: uma tentativa, sem fallback")
parser.add_argument("--request", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
if args.output.exists(): parser.error("O recibo já existe; escolha outro caminho, sem sobrescrever histórico.")
request = json.loads(args.request.read_text(encoding="utf-8-sig"))
if set(request) - {"input", "questions", "model"}: parser.error("Campos não suportados")
if request.get("model", "gemini-decision-1") != "gemini-decision-1": parser.error("Somente Decision")
try:
    result = DecisionClient().evaluate(request["input"], request["questions"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream: json.dump(result, stream, ensure_ascii=False, indent=2)
    print(json.dumps({"ok": True, "receipt": str(args.output.resolve()), "usage": result.get("usage")}))
except ProviderError as error:
    print(json.dumps({"ok": False, "code": error.code})); sys.exit(1)
