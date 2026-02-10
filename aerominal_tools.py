import sys, os, argparse, subprocess

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("-v", "--verbose", action="store_true")
    run_parser.add_argument("-c", "--category", type=str, choices=["diag", "perf", "visual"])
    subparsers.add_parser("list")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    tools_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools")
    if args.command == "list":
        for cat in ["diag", "perf", "visual"]:
            cat_path = os.path.join(tools_dir, cat)
            if os.path.exists(cat_path):
                print(f"[{cat}]")
                for f in sorted(os.listdir(cat_path)):
                    if f.endswith(".py"): print(f" - {f}")
    elif args.command == "run":
        suite_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_suite.py")
        cmd = [sys.executable, suite_path]
        if args.verbose: cmd.append("-v")
        if args.category: cmd.extend(["--cat", args.category])
        subprocess.run(cmd)

if __name__ == "__main__":
    main()
