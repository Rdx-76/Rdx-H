import os
import subprocess

def play_audio_file(file_path):
    subprocess.run(["play-audio", file_path])

def main():
    os.system('clear')  # Clears the console
    print("\033[36m")  # Sets text color to cyan
    
    while True:
        print("Options:")
        print("1. Premium")
        print("2. Demo")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            os.system('python pre.py')  # Assuming pre.py is the file for the premium option
        elif choice == "2":
            os.system('python demo.py')  # Assuming demo.py is the file for the demo option
        elif choice == "3":
            play_audio_file("dcd.mp3")
            exit()  # Exits the program after playing the audio
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
