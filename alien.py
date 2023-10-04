import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represnt a single alien in the fleet'''

    def __init__ (self, ai_game):
        '''Initiaize the alien and set starting postition'''
        super().__init__()
        self.screen=ai_game.screen
        self.image = pygame.image.load('images\space-removebg-preview.bmp')
        newheight=50
        newwidth=50
        self.image=pygame.transform.scale(self.image,(newwidth,newheight))
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)