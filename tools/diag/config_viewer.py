from pathlib import Path
import json
p = Path.home() / '.aerominal' / 'config' / 'settings.json'
if p.exists(): print(json.dumps(json.loads(p.read_text()), indent=2))
