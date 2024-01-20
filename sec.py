# sec.py

import os
import sys
import subprocess

def main_menu():
    print("\033[96m1. Premium")
    print("2. Demo")
    print("3. Exit\033[0m")

def launch_premium():
    print("\033[96mLaunching premium...\033[0m")
    os.system("python pre.py")

def launch_demo():
    print("\033[96mLaunching demo...\033[0m")
    os.system("python demo.py")

def play_exit():
    print("\033[96mPlaying dcd.mp3 and exiting...\033[0m")
    subprocess.run(["play-audio", "dcd.mp3"])
    sys.exit()

if __name__ == "__main__":
    os.system("clear")  # Clear the terminal screen

    while True:
        main_menu()
        choice = input("\033[96mEnter your choice (1, 2, or 3): \033[0m")

        if choice == '1':
            launch_premium()
        elif choice == '2':
            launch_demo()
        elif choice == '3':
            play_exit()
        else:
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")
            print("Invalid choice. Please enter 1, 2, or 3.")
