import pygame
from pygame.sprite import Group, Sprite
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self,ai_sttrings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect=pygame.Rect(0,0,ai_sttrings.bullet_width,ai_sttrings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        # Store the bullet's position as a decimal value.
        self.Y=float(self.rect.y)
        self.colors=ai_sttrings.bullet_colors
        self.speed_fact=ai_sttrings.bullet_speed_fact
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.Y -=self.speed_fact
        # Update the rect position.
        self.rect.y = self.Y


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen,self.colors,self.rect)

     


     
  