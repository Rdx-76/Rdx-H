import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
import time
import os

def print_centered(text, size):
    columns = os.get_terminal_size().columns
    padding = (columns - size) // 2
    print(f"\033[1;36m{' ' * padding}{text}\033[0m")

def print_lower(text, size):
    columns = os.get_terminal_size().columns
    padding = (columns - size) // 2
    print(f"\033[1;33m{' ' * padding}{text}\033[0m")

def print_welcome(speed, welcome_size, rdx_tech_size, version_size):
    message = "Welcome Boss"
    
    for char in message:
        print(f"\033[1;36m{char}", end='', flush=True)
        time.sleep(1 / (speed * 0.1))  # Adjust speed here
    print("\033[0m")  # Reset color

    print_lower('RDX TECH', rdx_tech_size)
    print_lower(f'[ Version 00.00.01 ]', version_size)

def main():
    speed = 50  # Adjust the speed from 1 to 100
    welcome_size = 16
    rdx_tech_size = 10
    version_size = 6
    
    print("\033[40m")  # Set background color to black
    print(" " * os.get_terminal_size().columns)  # Adjust space for the black background
    
    print_welcome(speed, welcome_size, rdx_tech_size, version_size)

    # Call another script after writing "Welcome Boss"
    os.system("python rdx.py")

if __name__ == "__main__":
    main()
