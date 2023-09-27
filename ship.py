import pygame

class Ship:
    '''A class to manage the ship.'''

    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen=ai_game.screen
        self.screen_rect =self.screen.get_rect()
        
          
        self.image = pygame.image.load('images\space-removebg-preview.bmp')
        newheight=100
        newwidth=100
        self.image=pygame.transform.scale(self.image,(newwidth,newheight))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draw the ship at its current location.'''
        try:

            self.screen.blit(self.image, self.rect)
        except:
            print(e)