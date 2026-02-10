import json, os, sys
from pathlib import Path
def validate():
    h = Path.home() / '.aerominal'
    req = ['background', 'text_color', 'input_bg', 'prompt_color', 'status_color', 'selection_bg', 'accent_color', 'titlebar_bg']
    err = 0
    for d in [h/'themes'/'official', h/'themes'/'user']:
        if not d.exists(): continue
        for f in d.glob('*.json'):
            try:
                with open(f, 'r') as tf:
                    data = json.load(tf)
                if not all(k in data for k in req): err += 1
            except: err += 1
    return err == 0
if __name__ == "__main__":
    sys.exit(0 if validate() else 1)
