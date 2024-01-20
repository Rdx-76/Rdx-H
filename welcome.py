import time
import os

def print_welcome(speed):
    message = "Welcome Boss"
    
    for char in message:
        print(f"\033[1;36m{char}", end='', flush=True)
        time.sleep(1 / (speed * 0.1))  # Adjust speed here
    print("\033[0m")  # Reset color

def main():
    speed = 50  # Adjust the speed from 1 to 100
    
    print("\033[40m")  # Set background color to black
    print(" " * os.get_terminal_size().columns)  # Adjust space for the black background
    
    print_welcome(speed)

    # Call another script after writing "Welcome Boss"
    os.system("python rdx.py")

if __name__ == "__main__":
    main()
