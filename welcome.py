import time
from tkinter import Tk, Label, font
from colorama import init, Fore, Back, Style
import subprocess

init(autoreset=True)  # Initialize colorama for cross-platform color support

class WelcomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome App")
        self.root.geometry("400x200")  # Adjusted width to accommodate the longer text
        self.root.configure(bg="black")

        welcome_font = font.Font(family="Times New Roman", size=16, weight="bold")
        rdx_tech_font = font.Font(family="Brush Script MT", size=8, weight="bold")
        version_font = font.Font(family="Roboto", size=4)

        self.label = Label(root, text="", font=welcome_font, fg="cyan", bg="black")
        self.label.pack(expand=True, fill="both")

        version_text = '[ Version 00.00.01 ]'
        brand_text = 'RDX TECH'

        self.footer_frame = Label(root, bg="black")
        self.footer_frame.pack(side="bottom", pady=2)

        self.footer_label_rdx_tech = Label(self.footer_frame, text=brand_text, font=rdx_tech_font, fg="cyan", bg="black")
        self.footer_label_rdx_tech.grid(row=0, column=0, pady=2)

        self.footer_label_version = Label(self.footer_frame, text=version_text, font=version_font, fg="cyan", bg="black")
        self.footer_label_version.grid(row=0, column=1, pady=2)

        self.start_animation()

    def start_animation(self):
        self.label.config(text="")
        speed = 50  # Adjust the speed from 1 to 100
        message = "Welcome Boss"

        for char in message:
            self.label.config(text=self.label.cget("text") + char)
            self.root.update_idletasks()
            time.sleep(1 / (speed * 0.1))  # Adjust speed here

        # Call another script after writing "Welcome Boss"
        subprocess.run(["python", "rdx.py"])

if __name__ == "__main__":
    root = Tk()
    welcome_app = WelcomeApp(root)
    root.mainloop()
