import json
from datetime import datetime
from pathlib import Path

def save_chat_log(logs: list, filename="chat_logs.jsonl"):
    Path("logs").mkdir(exist_ok=True)
    with open(Path("logs") / filename, "a", encoding="utf-8") as f:
        for entry in logs:
            data = {"timestamp": datetime.utcnow().isoformat(), **entry}
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
