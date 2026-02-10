import tkinter as tk
from tkinter import font
import sys, os, json
from pathlib import Path
def audit(list_all=False):
    p = Path.home() / '.aerominal' / 'config' / 'settings.json'
    f_fam = "Consolas"
    if p.exists():
        try:
            with open(p, 'r') as f: f_fam = json.load(f).get('appearance', {}).get('font_family', f_fam)
        except: pass
    try:
        r = tk.Tk()
        r.withdraw()
        avail = font.families()
        if list_all:
            for f in sorted(avail)[:20]: print(f)
            r.destroy()
            return True
        res = f_fam in avail
        r.destroy()
        return res
    except: return False
if __name__ == "__main__":
    sys.exit(0 if audit("--list" in sys.argv) else 1)
