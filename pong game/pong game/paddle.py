import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

#below are the two event handler's of our paddle which will move our paddle up or down based on the keys pressed. these are called methods in OOP.

#the moveUp method take two argument first is self and the other is pixels
#self is implicit and refers to the current object.
#the second one refers to the number of pixels to move the paddle
    def moveUp(self, pixels):
        self.rect.y -=pixels
        #check that you are not going too far off the screen
        if self.rect.y<0:
            self.rect.y=0
            
    def moveDown(self, pixels):
        self.rect.y +=pixels
        #check that you are not going too far off the screen
        if self.rect.y >400:
            self.rect.y=400;
        
        
        
        
        
        
        
        
