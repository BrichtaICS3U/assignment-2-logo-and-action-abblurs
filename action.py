# ICS3U
# Assignment 2: Action
# Abbey Jayne

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame
#Import Rain class
from rain import Rain
pygame.init()

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('GoodMusic.mp3')
pygame.mixer.music.play(0) #-1 means loops for ever, 0 means play just once)
#https://www.youtube.com/watch?v=X2WH8mHJnhM

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (79, 184, 219)

# Set the screen size
SCREENWIDTH = 640
SCREENHEIGHT = 427

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Recorder Animation")

rain_list = pygame.sprite.Group() #List that will containing all sprites
 
rain1 = Rain(BLUE, 30, 50)
 
# Add the rain to the list of objects
rain_list.add(rain1)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
background_image = pygame.image.load("background.png")
#http://davidgmiller.typepad.com/lovelandmagazine/2014/01/montessori-school-holds-winter-performance.html

#---------Main Program Loop----------
while carryOn:
        # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    screen.blit(background_image, [0, 0])
    

    # --- Game logic goes here
    rain_list.update()
    
    # --- Draw code goes here

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    

# Once the main program loop is exited, stop the game engine
pygame.quit()
