import os
import subprocess
import sys

def build():
    print("Building Lumen Orbs with PyInstaller...")
    
    command = [
        "pyinstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--icon", "assets/icon.ico",
        "--name", "Lumen Orbs",
        "--add-data", "assets;assets/",
        "--add-data", "games.json;.",
        "src/main.py"
    ]
    
    try:
        subprocess.run(command, check=True)
        print("\nBuild complete! Check the 'dist' folder for your executable.")
    except Exception as e:
        print(f"Error during build: {e}")

if __name__ == "__main__":
    build()
