import json, sys
from pathlib import Path
def audit():
    p = Path.home() / '.aerominal' / 'config' / 'settings.json'
    if not p.exists(): return True
    try:
        with open(p, 'r') as f:
            c = json.load(f)
        for s in ['window', 'appearance', 'behavior']:
            if s not in c: return False
        return True
    except: return False
if __name__ == "__main__":
    sys.exit(0 if audit() else 1)
