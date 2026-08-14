import json
from pathlib import Path

def load_config(config_path : str = "config.json") -> dict:
    with open(config_path, "r", encoding = "utf-8") as f:
        return json.load(f)

def scan_markdown_files(roots: list[str], ignore_dir: list[str]) ->list[Path]:
    #Recursively find all .md files under the given roots, skipping ignored dirs.
    found = []
    ignore_set = set(ignore_dir)

    for root in roots:
        root_path = Path(root)
        if not root_path.exists():
            continue
        for md_file in root_path.rglob("*.md"):
            if any(part in ignore_set for part in md_file.parts):
                continue
            found.append(md_file)

    return found