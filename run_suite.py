
import subprocess
import sys
import os
import argparse
import platform

def run_suite():
    parser = argparse.ArgumentParser(description="Aerominal Dev Tools Suite")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show full output of each test")
    args = parser.parse_args()

    current_os = platform.system()
    other_os = "Linux" if current_os == "Windows" else "Windows"

    print("=" * 60)
    print("   AEROMINAL PRE-PRODUCTION SUITE   ")
    print("   Running on: {:<32} ".format(current_os))
    print("=" * 60)
    
    scripts = [
        ("Platform Audit", "platform_audit.py"),
        ("Config Integrity", "config_audit.py"),
        ("Font Availability", "font_audit.py"),
        ("ANSI Color Verification", "ansi_colors.py"),
        ("Command Execution Tests", "command_tester.py"),
        ("Performance Benchmark", "benchmark.py"),
        ("Theme Integrity Check", "theme_validator.py"),
        ("UI Stability Stress Test", "stress_test.py"),
    ]

    dev_tools_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
    results = []

    for name, script in scripts:
        if args.verbose:
            print(f"\n>>> Running {name}...")
        
        script_path = os.path.join(dev_tools_dir, script)
        
        try:
            if not args.verbose:
                process = subprocess.run(
                    [sys.executable, script_path], 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                results.append((name, "PASS"))
            else:
                subprocess.run([sys.executable, script_path], check=True)
                results.append((name, "PASS"))
        except subprocess.CalledProcessError as e:
            results.append((name, "FAIL"))
            if not args.verbose:
                print(f"[!] {name} failed. Run with -v for details.")
        except Exception as e:
            results.append((name, "ERROR"))
            print(f"[!] Error running {name}: {e}")

    print("\n\n" + "=" * 30)
    print("      FINAL RESULTS      ")
    print("=" * 30)
    print(f"{'Test Name':<30} | {'Status':<10}")
    print("-" * 43)
    
    all_passed = True
    for name, status in results:
        indicator = "[✓]" if status == "PASS" else "[✗]"
        print(f"{name:<30} | {indicator} {status}")
        if status != "PASS":
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("   [✓] ALL DIAGNOSTICS PASSED ON {}".format(current_os.upper()))
        print("   [!] IMPORTANT: ENSURE YOU ALSO TEST ON {}".format(other_os.upper()))
    else:
        print("         DIAGNOSTICS FAILED - CHECK LOGS ABOVE         ")
    print("=" * 60)

if __name__ == "__main__":
    run_suite()
