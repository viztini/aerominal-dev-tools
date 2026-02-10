import sys, time, random
def run():
    s = time.time()
    for i in range(5000):
        sys.stdout.write(f"\033[{random.randint(31,37)}m[STRESS] {i:04}\033[0m\n")
        if i % 100 == 0: sys.stdout.flush()
    print(f"Done: {time.time()-s:.2f}s")
if __name__ == "__main__":
    run()
