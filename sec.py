# sec.py

import os
import sys
import subprocess

def main_menu():
    print("1. Premium")
    print("2. Demo")
    print("3. Exit")

def launch_premium():
    print("Launching premium...")
    os.system("python pre.py")

def launch_demo():
    print("Launching demo...")
    os.system("python demo.py")

def play_exit():
    print("Playing dcd.mp3 and exiting...")
    subprocess.Popen(["start", "dcd.mp3"], shell=True)
    sys.exit()

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            launch_premium()
        elif choice == '2':
            launch_demo()
        elif choice == '3':
            play_exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
