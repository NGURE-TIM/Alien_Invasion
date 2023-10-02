import sys
import pygame
from settings import Settings 
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''Overall class to manage game assets and behaviours'''

    def __init__(self):
        '''Initialize the game and create game resources.'''

        pygame.init()
        self.settings=Settings()
        self.screen =pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bg_color=(230,230,230)
        pygame.display.set_caption('Alien Invasion')
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
    
    def _check_events(self):
         
         '''Responds to keypresses and mouse events'''
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RIGHT:
                          self.ship.moving_right=True
                     elif event.key==pygame.K_LEFT:
                          self.ship.moving_left=True
                     elif event.key==pygame.K_q:
                          sys.exit()
                     elif event.key==pygame.K_SPACE:
                          self._fire_bullet()

                elif event.type==pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right=False
                     elif event.key==pygame.K_LEFT:
                          self.ship.moving_left=False
    def _fire_bullet(self):
         '''Create a new bullet and add it to bullets'''
         new_bullet=Bullet(self)
         self.bullets.add(new_bullet)
         

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
              bullet.draw_bullet()
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0 :
                      self.bullets.remove(bullet)
            print(len(self.bullets))
            pygame.display.flip()
    
if __name__ == '__main__':
        ai=AlienInvasion()
        ai.run_game()
        