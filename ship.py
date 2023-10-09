import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    '''A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect =self.screen.get_rect()
        
        
        self.image = pygame.image.load('images\space-removebg-preview.bmp')
        newheight=100
        newwidth=100
        self.image=pygame.transform.scale(self.image,(newwidth,newheight))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.moving_right=False
        self.moving_left=False
    def  update(self):
        '''Update ship postion'''
        if self.moving_right  and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            
            self.x -= self.settings.ship_speed
        self.rect.x=self.x
        
    def blitme(self):
        '''Draw the ship at its current location.'''
        try:

            self.screen.blit(self.image, self.rect)
        except:
            print(e)
    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
