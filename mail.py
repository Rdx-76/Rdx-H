import smtplib
import time
import os
import subprocess
from colorama import Fore, Style, init

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

if __name__ == "__main__":
    # Play the audio file at the start
    play_audio_file("cd.mp3")

    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get sender's email
    sender_email = input(f"{Fore.CYAN}Enter your email: {Style.RESET_ALL}")

    # Set the default password
    pas = "Rdx76642"

    # Use the default password for login
    sender_password = pas

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
