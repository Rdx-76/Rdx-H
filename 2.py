import pygame
from pygame.locals import *
import sys

def display_gif(gif_path):
    pygame.init()
    
    # Load the GIF
    gif = pygame.image.load(gif_path)
    
    # Set the display mode
    width, height = gif.get_size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("GIF Display")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Display the GIF
        screen.blit(gif, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # Replace '2.gif' with the path to your GIF file
    gif_path = '2.gif'
    display_gif(gif_path)
