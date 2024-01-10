from pathlib import Path
import json
path = Path('names.json')
if path.exists():
    contents = path.read_text()
    names = json.loads(contents)


name = input('enter your name')
if name in names:
    print(f"{name} welcome")
