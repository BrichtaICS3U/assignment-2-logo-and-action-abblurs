# ICS3U
# Assignment 2: Action
# Abbey Jayne

#Sprite Module Code

import pygame
WHITE = (255, 255, 255)
BLUE = (79, 184, 219)
 
class Rain(pygame.sprite.Sprite):
    #Rain class that derives from the pygame "Sprite" class
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)
 
        # Draw the car 
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
         
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def fall(self, pixels):
        #self.rect.x += pixels
        self.rect.x += 4
        self.rect.y += 3
