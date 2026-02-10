import os, sys, platform, ctypes
def audit():
    print(f"{platform.system()} {platform.release()} ({platform.machine()})")
    if os.name == 'nt':
        try:
            e = ctypes.c_int()
            ctypes.windll.dwmapi.DwmIsCompositionEnabled(ctypes.byref(e))
            print(f"DWM: {e.value}")
            print(f"Admin: {ctypes.windll.shell32.IsUserAnAdmin() != 0}")
        except: pass
    else:
        print(f"DISPLAY: {os.environ.get('DISPLAY')}")
        try:
            import pty
            print("PTY: OK")
        except: print("PTY: NO")
if __name__ == "__main__":
    audit()
