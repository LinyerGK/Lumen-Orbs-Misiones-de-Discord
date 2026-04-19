import subprocess
import os
import shutil
import time

def test_ghost():
    source = r"C:\Windows\notepad.exe"
    target = os.path.join(os.environ.get("TEMP", "C:/Temp"), "LumenTest", "Valorant.exe")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copy2(source, target)
    
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = 6 # SW_MINIMIZE
    
    print(f"Starting {target} minimized...")
    p = subprocess.Popen([target], startupinfo=si)
    print(f"PID: {p.pid}. Waiting 10 seconds...")
    time.sleep(10)
    p.kill()
    print("Done.")

test_ghost()
