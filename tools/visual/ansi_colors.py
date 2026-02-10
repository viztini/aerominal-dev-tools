import sys
def run():
    for i in range(8): sys.stdout.write(f"\033[3{i}m C{i} \033[1;3{i}m B{i} \033[0m")
    print()
    for i in range(0, 256, 16):
        for j in range(16): sys.stdout.write(f"\033[38;5;{i+j}m {i+j:3} \033[0m")
        print()
if __name__ == "__main__":
    run()
