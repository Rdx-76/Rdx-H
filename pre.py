import os

def generate_activation_code(device_id):
    code_format = "{}-{}-{}-{}"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    first_four_letters = ''.join(letters[i % len(letters)] for i in range(4))
    remaining_digits = str(abs(hash(device_id)) % (10 ** 13)).zfill(13)
    activation_code = code_format.format(first_four_letters, *([remaining_digits[i:i+4] for i in range(0, len(remaining_digits), 4)]))
    return activation_code

def check_premium_status(activation_code):
    with open('premium.txt', 'r') as premium_file:
        premium_codes = premium_file.read().splitlines()
    return activation_code in premium_codes

def main():
    os.system('clear')
    device_id = input("Enter your device ID: ")

    activation_code = generate_activation_code(device_id)

    print(f"Your activation code is: {activation_code}")
    
    premium_status = check_premium_status(activation_code)

    if premium_status:
        print("\033[96mCongratulations! You are a premium user.")
        os.system('python rdx.py')
    else:
        print("\033[96mSorry, you are not a premium user.")
        os.system('python sec.py')

if __name__ == "__main__":
    main()
