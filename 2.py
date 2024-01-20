import tkinter as tk
from tkinter import PhotoImage

def show_gif(gif_path):
    root = tk.Tk()
    root.title("GIF Viewer")

    # Load the GIF
    gif = PhotoImage(file=gif_path)

    # Create a label to display the GIF
    label = tk.Label(root, image=gif)
    label.pack()

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    # Replace 'path/to/2.gif' with the actual path to your GIF file
    gif_path = 'path/to/2.gif'
    show_gif(gif_path)
