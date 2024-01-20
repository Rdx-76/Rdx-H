import os
import random
from termcolor import colored

# Function to generate a 17-digit code
def generate_code():
    letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
    digits = ''.join(random.choices('0123456789', k=13))
    return f'{letters}-{digits}'

# Function to display colored text
def print_cyan(text):
    print(colored(text, 'cyan'))

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to check if the provided code is in premium.txt
def check_premium(code):
    with open('premium.txt', 'r') as file:
        premium_codes = file.read().splitlines()
    return code in premium_codes

# Main function
def main():
    clear_console()

    # Check if the device has a stored code
    if os.path.exists('device_code.txt'):
        with open('device_code.txt', 'r') as file:
            code = file.read().strip()
    else:
        # Generate a new code for the device
        code = generate_code()
        with open('device_code.txt', 'w') as file:
            file.write(code)

    # Display the generated code
    print_cyan(f'Your Premium Code: {code}')

    # Input option to enter the code
    user_input = input(colored('Enter your Premium Code: ', 'cyan')).strip()

    # Check if the entered code is valid
    if check_premium(user_input):
        print_cyan('Congratulations! You are a Premium User.')
        os.system('python rdx.py')
    else:
        print_cyan('Sorry, you are not a Premium User.')
        os.system('python sec.py')

if __name__ == "__main__":
    main()
