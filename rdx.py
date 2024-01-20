import os
import subprocess
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("mpg123 speech.mp3")

def call_script(script_name):
    subprocess.call(['python', script_name])

def main():
    speak("Welcome Sir")

    while True:
        print("\nOptions:")
        print("1. Cloning")
        print("2. FB Target ID")
        print("3. Massage")
        print("4. Mail")
        print("5. NID Details")
        print("6. Location")
        print("7. Wifi")
        print("8. About")
        print("9. Exit")

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
            call_script("wifi.py")
        elif choice == "8":
            call_script("about.py")
        elif choice == "9":
            speak("Good bye sir")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
