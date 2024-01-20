from PIL import Image, ImageSequence
import time

def display_gif(file_path):
    try:
        image = Image.open(file_path)

        for frame in ImageSequence.Iterator(image):
            frame.show()
            time.sleep(0.1)  # Adjust the delay between frames if needed

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    gif_path = "2.gif"  # Replace with the path to your GIF file
    display_gif(gif_path)
