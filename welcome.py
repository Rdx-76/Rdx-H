import time
import os
import subprocess

def clear_screen():
    os.system('clear')  # For Linux/Mac
    # Uncomment the line below for Windows
    # os.system('cls')

def play_audio(file_path):
    subprocess.Popen(["mpg123", file_path])

def print_welcome(speed, size):
    message = "Welcome Boss"
    padding = (os.get_terminal_size().columns - len(message)) // 2

    print("\n" * (os.get_terminal_size().lines // 3))  # Move to the middle of the screen

    play_audio("w.mp3")

    for char in message:
        print(f"\033[1;36m{char}", end='', flush=True)
        time.sleep(1 / (speed * 0.1))  # Adjust speed here
    print("\033[0m")  # Reset color

def print_footer(speed, rdx_tech_size, version_size):
    rdx_tech_message = 'RDX TECH'
    version_message = '[ Version 00.00.01 ]'

    rdx_tech_padding = (os.get_terminal_size().columns - len(rdx_tech_message) - len(version_message)) // 2

    print()  # Move to the next line

    play_audio("v.mp3")

    for char in rdx_tech_message:
        print(f"\033[1;33m{char}", end='', flush=True)
        time.sleep(1 / (speed * 0.1))  # Adjust speed here
    print("\033[0m", end=' ' * rdx_tech_padding)  # Reset color and add padding

    for char in version_message:
        print(f"\033[1;33m{char}", end='', flush=True)
        time.sleep(1 / (speed * 0.1))  # Adjust speed here
    print("\033[0m")  # Reset color

def main():
    speed = 50  # Adjust the speed from 1 to 100
    welcome_size = 16
    rdx_tech_size = 10
    version_size = 6
    
    clear_screen()

    print("\033[40m")  # Set background color to black
    print(" " * os.get_terminal_size().columns)  # Adjust space for the black background
    
    print_welcome(speed, welcome_size)
    
    print_footer(speed, rdx_tech_size, version_size)

    # Call another script after writing "Welcome Boss"
    os.system("python rdx.py")

if __name__ == "__main__":
    main()
