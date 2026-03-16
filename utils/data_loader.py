import json
from pathlib import Path

def load_test_data():
    file_path = Path(__file__).resolve().parent.parent / "config" / "test_data.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)