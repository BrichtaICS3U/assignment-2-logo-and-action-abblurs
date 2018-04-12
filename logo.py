# ICS3U
# Assignment 2: Logo
# Abbey Jayne

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
WHITE = (255, 255, 255)
BACKGROUNDGREEN = (99, 184, 86)
DARKGREEN = (50, 140, 38)
BEIGE = (242, 203, 46)
BROWN = (138, 118, 40)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Abbey's Google Classroom Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    pygame.draw.rect(screen, BEIGE, [35, 30, 330, 250], 0) #backgrounds
    pygame.draw.rect(screen, BACKGROUNDGREEN, [55, 50, 290, 210], 0)
    pygame.draw.ellipse(screen, DARKGREEN, [95, 120, 40, 40], 0) #student heads
    pygame.draw.ellipse(screen, DARKGREEN, [265, 120, 40, 40], 0)
    pygame.draw.rect(screen, DARKGREEN, [80, 185, 70, 20], 0) #student bodies
    pygame.draw.ellipse(screen, DARKGREEN, [80, 175, 70, 20], 0)
    pygame.draw.rect(screen, DARKGREEN, [250, 185, 70, 20], 0)
    pygame.draw.ellipse(screen, DARKGREEN, [250, 175, 70, 20], 0)
    pygame.draw.ellipse(screen, WHITE, [170, 90, 60, 60], 0) #teacher head
    pygame.draw.rect(screen, WHITE, [125, 175, 150, 30], 0) #teacher body
    pygame.draw.ellipse(screen, WHITE, [125, 160, 150, 30], 0)
    pygame.draw.rect(screen, WHITE, [225, 247, 70, 13], 0) #chalk
    pygame.draw.polygon(screen, BROWN, [[225, 260], [240, 260],[240, 279]], 0) #chalk shadow
    pygame.draw.polygon(screen, BROWN, [[295, 260], [295, 279],[310, 279]], 0)
    pygame.draw.rect(screen, BROWN, [240, 260, 55, 20], 0)
    font = pygame.font.SysFont("Calibri", 90, True)   #Text
    text = font.render("Classroom", 3, (115, 115, 115))
    screen.blit(text, (10, 300))
    
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
