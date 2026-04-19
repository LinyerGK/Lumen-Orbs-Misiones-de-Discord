import os
import subprocess
import sys

def build():
    print("Building Lumen Orbs with PyInstaller...")
    
    command = [
        "pyinstaller",
        "--noconfirm",
        "--onedir",
        "--windowed",
        "--icon", "assets/icon.ico",
        "--name", "Lumen Orbs",
        "--hidden-import", "pypresence",
        "--hidden-import", "psutil",
        "--hidden-import", "customtkinter",
        "--add-data", "assets;assets/",
        "src/main.py"
    ]
    
    try:
        subprocess.run(command, check=True)
        print("\nBuild complete! Check the 'dist' folder for your executable.")
    except Exception as e:
        print(f"Error during build: {e}")

if __name__ == "__main__":
    build()
