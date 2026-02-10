import os, sys, subprocess, time
def run():
    win = os.name == 'nt'
    for n, c in [("LS", "dir" if win else "ls"), ("ENV", "echo %PATH%" if win else "echo $PATH"), ("CD", "cd"), ("IO", "echo 1 > t.tmp && type t.tmp" if win else "echo 1 > t.tmp && cat t.tmp")]:
        try:
            r = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=5)
            print(f"{n}: {'OK' if r.returncode==0 else 'FAIL'}")
        except: print(f"{n}: ERR")
    if os.path.exists("t.tmp"): os.remove("t.tmp")
if __name__ == "__main__":
    run()
