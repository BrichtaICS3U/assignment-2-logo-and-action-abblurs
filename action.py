# ICS3U
# Assignment 2: Action
# Abbey Jayne

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame
import random #to randomize rain fall
#Import Rain class
from rain import Rain
#from rain import Cloud

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

#Lists that will contain all rain / cloud sprites 
raindrops = pygame.sprite.Group()
#clouds = pygame.sprite.Group()

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

background_image = pygame.image.load("background.png")
#http://davidgmiller.typepad.com/lovelandmagazine/2014/01/montessori-school-holds-winter-performance.html

#Making the rain drops
for i in range(100):   
        drop = Rain(BLUE, 3, 7)
        raindrops.add(drop)

#Making the clouds
#for i in range(6):
    #cloud = Cloud(WHITE, 6, 4)
    #clouds.add(cloud)

#---------Main Program Loop----------
while carryOn:
        # --- Main event loop ---
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #Player clicked space bar
            carryOn = False

    screen.blit(background_image, [0, 0])
    
    #Rainfall
    for rain in raindrops:
        rain.fall()

    #Clouds moving
    #for cloud in clouds:
        #cloud.fall()
    
    raindrops.draw(screen)
    raindrops.update()
    #clouds.draw(screen)
    #clouds.update()
    
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    

# Once the main program loop is exited, stop the game engine
pygame.quit()
