import os
import subprocess

def play_audio_file(file_path):
    subprocess.run(["play-audio", file_path])

def main():
    os.system("clear")  # Clear the console screen

    while True:
        print("\033[96m")  # Set text color to cyan
        print("1. Premium")
        print("2. Demo")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("python pre.py")
        elif choice == "2":
            os.system("python demo.py")
        elif choice == "3":
            play_audio_file("dcd.mp3")
            os.system("kill -9 $$")  # Kill the script instantly after playing audio
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
