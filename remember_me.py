from pathlib import Path
import json

names = []
while True:
    name = input('enter your name or \'q\' to quit')
    if name == 'q':
        break
    else:
        names.append(name)

path = Path('names.json')
contents = json.dumps(names)
path.write_text(contents)