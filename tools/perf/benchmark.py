import time, sys, os
def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(4):
        d = os.path.dirname(d)
        if os.path.exists(os.path.join(d, 'src')): return d
    return d
sys.path.append(find_root())
try: from src.core.ansi_parser import ANSIParser
except: ANSIParser = None
def run():
    txt = "\n".join([f"\033[38;5;{i%256}mLine {i} \033[1mB\033[0m \033[4mU\033[0m" for i in range(1000)])
    if ANSIParser:
        s = time.perf_counter()
        ANSIParser.parse(txt)
        print(f"Parse: {(time.perf_counter()-s)*1000:.2f}ms")
    else: print("SKIP")
if __name__ == "__main__":
    run()
