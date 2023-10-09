import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represnt a single alien in the fleet'''

    def __init__ (self, ai_game):
        '''Initiaize the alien and set starting postition'''
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.image = pygame.image.load('images\ship-removebg-preview.bmp')
        newheight=50
        newwidth=50
        self.image=pygame.transform.scale(self.image,(newwidth,newheight))
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
    def check_edges(self):
        '''Return True if alien is at edge of screen.'''
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
   


    def update(self):
        '''Move alien to right'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x