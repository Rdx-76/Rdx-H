import smtplib
import time
import os
import subprocess
from colorama import Fore, Style, init
import keyring

# Initialize colorama
init()

def send_email(sender_email, sender_password, to_email, subject, message):
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Create the email message
        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(sender_email, to_email, email_message)

        print(Fore.GREEN + "Email sent successfully!" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}" + Style.RESET_ALL)

    finally:
        # Close the server connection
        server.quit()

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Waiting for {Fore.CYAN}{i}{Style.RESET_ALL} seconds...", end='\r')
        time.sleep(1)

def play_audio_file(file_path):
    try:
        subprocess.run(["play-audio", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error playing audio: {str(e)}" + Style.RESET_ALL)

def get_password_from_keyring(email):
    try:
        password = keyring.get_password("gmail_sender", email)
        if not password:
            raise Exception("Password not found in keyring")
        return password
    except Exception as e:
        print(Fore.RED + f"Error retrieving password: {str(e)}" + Style.RESET_ALL)
        return None

def set_password_to_keyring(email, password):
    try:
        keyring.set_password("gmail_sender", email, password)
    except Exception as e:
        print(Fore.RED + f"Error setting password: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    # Play the audio file at the start
    play_audio_file("cd.mp3")

    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get sender's email
    sender_email = input(f"{Fore.CYAN}Enter your email: {Style.RESET_ALL}")

    # Retrieve the password from the keyring
    sender_password = get_password_from_keyring(sender_email)

    # If the password is not found, ask for it and store it in the keyring
    if not sender_password:
        sender_password = input(f"{Fore.CYAN}Enter your email password: {Style.RESET_ALL}")
        set_password_to_keyring(sender_email, sender_password)

    # Get recipient's email
    to_email = input(f"{Fore.CYAN}Enter recipient's email: {Style.RESET_ALL}")

    # Get email details
    subject = input(f"{Fore.CYAN}Enter email subject: {Style.RESET_ALL}")
    message = input(f"{Fore.CYAN}Enter email message: {Style.RESET_ALL}")

    # Get the total number of emails to send
    limit = int(input(f"{Fore.CYAN}Enter the total number of emails to send: {Style.RESET_ALL}"))

    # Get the waiting time between emails
    wait_time = int(input(f"{Fore.CYAN}Enter the waiting time (in seconds) between emails: {Style.RESET_ALL}"))

    # Send emails after the specified waiting time until the specified limit is reached
    for i in range(limit):
        send_email(sender_email, sender_password, to_email, subject, message)

        # Display countdown before sending the next email
        if i < limit - 1:
            countdown_timer(wait_time)
    
    print("\nEmail sending completed.")
