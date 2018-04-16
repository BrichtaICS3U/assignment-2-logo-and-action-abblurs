# ICS3U
# Assignment 2: Action
# Abbey Jayne

#Sprite Module Code

import pygame
import random
WHITE = (255, 255, 255)
BLUE = (79, 184, 219)
 
class Rain(pygame.sprite.Sprite):
    #Rain class that derives from the pygame "Sprite" class
    
    def __init__(self, color, width, height):
        super().__init__()
        
        # Set color, x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the droplet 
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
         
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # Get random x/y coordinates
        self.rect.x = random.randrange(10, 630)
        self.rect.y = random.randrange(-200, -100)
        
    def fall(self):
        self.rect.x += 4
        self.rect.y += 3

        if self.rect.y > 427:
            self.rect.y = -200

        if self.rect.x > 640:
            self.rect.x = -50

class Cloud(pygame.sprite.Sprite):
    #Cloud class that derives from the pygame "Sprite" class
    
    def __init__(self, color, width, height):
        super().__init__()

        # Set color, x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the cloud 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
         
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # Get x/y coordinates
        self.rect.x = random.randrange(5, 630)
        self.rect.y = random.randrange(5, 50)

    def fall(self):
        self.rect.x += 10
        

        

    
