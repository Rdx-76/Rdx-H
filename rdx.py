import os
import subprocess
from gtts import gTTS

CYAN = '\033[96m'
ENDC = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def speak(text, filename="s.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    play_audio_file(filename)

def play_audio_file(file_path):
    subprocess.run(["play-audio", file_path])

def call_script(script_name):
    subprocess.call(['python', script_name])

def main():
    clear_screen()
    play_audio_file("s.mp3")

    while True:
        print(CYAN + "\nOptions:" + ENDC)
        print(CYAN + "1. Cloning" + ENDC)
        print(CYAN + "2. FB Target ID" + ENDC)
        print(CYAN + "3. Massage" + ENDC)
        print(CYAN + "4. Mail" + ENDC)
        print(CYAN + "5. NID Details" + ENDC)
        print(CYAN + "6. Location" + ENDC)
        print(CYAN + "7. Wifi" + ENDC)
        print(CYAN + "8. About" + ENDC)
        print(CYAN + "9. Exit" + ENDC)

        choice = input("Enter your choice: ")

        if choice == "1":
            call_script("clone.py")
        elif choice == "2":
            call_script("FBTI.py")
        elif choice == "3":
            call_script("sms.py")
        elif choice == "4":
            call_script("mail.py")
        elif choice == "5":
            call_script("nid.py")
        elif choice == "6":
            call_script("track.py")
        elif choice == "7":
            call_script("2.py")
        elif choice == "8":
            call_script("about.py")
        elif choice == "9":
            play_audio_file("dcd.mp3")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
