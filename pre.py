import random
import re
import os

def generate_premium_code():
    code = '-'.join([''.join(random.choices('0123456789', k=4)) for _ in range(4)])
    return code

def save_code_to_file(code):
    with open('premium.txt', 'a') as file:
        file.write(code + '\n')

def check_premium_status(input_code):
    with open('premium.txt', 'r') as file:
        codes = file.read().splitlines()
    return input_code in codes

def main():
    print("Welcome to Premium Membership!")

    # Generate a unique premium code
    premium_code = generate_premium_code()
    print(f"Your Premium Code: {premium_code}")

    # Save the generated code to premium.txt
    save_code_to_file(premium_code)

    # Ask the user to input their code
    user_input = input("Enter your Premium Code: ").strip()

    # Validate the input format
    if re.match(r'\d{4}-\d{4}-\d{4}-\d{5}', user_input):
        # Check if the input code is a valid premium code
        if check_premium_status(user_input):
            print("Congratulations! You are a Premium User.")
            os.system('python rdx.py')  # Redirect to rdx.py
        else:
            print("Sorry, the entered code is not valid for Premium Membership.")
            os.system('python sec.py')  # Redirect to sec.py
    else:
        print("Invalid code format. Please enter a valid Premium Code.")

if __name__ == "__main__":
    main()

