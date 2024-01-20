import tkinter as tk
from tkinter import PhotoImage

def show_gif():
    # Create the main window
    window = tk.Tk()
    window.title("GIF Viewer")

    # Load the GIF
    gif_path = "2.gif"
    gif = PhotoImage(file=gif_path)

    # Create a label to display the GIF
    label = tk.Label(window, image=gif)
    label.pack()

    # Run the main loop
    window.mainloop()

# Call the function to show the GIF
show_gif()
