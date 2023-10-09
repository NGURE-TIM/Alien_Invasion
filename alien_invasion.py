import sys
import pygame
from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

class AlienInvasion:
    '''Overall class to manage game assets and behaviours'''

    def __init__(self):
        '''Initialize the game and create game resources.'''

        pygame.init()
        self.settings=Settings()
        self.screen =pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bg_color=(230,230,230)
        pygame.display.set_caption('Alien Invasion')
        self.stats=GameStats(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
    def _ship_hit(self):
         if self.stats.ship_left > 0:
              self.stats.ship_left -= 1
              self.aliens.empty()
              self.bullets.empty()
              self._create_fleet()
              self.bullets.empty()
              sleep(0.5)
         else:
              self.stats.game_active=False
              
         
         
    def _create_fleet(self):
         '''Create the fleet of aliens'''
         alien=Alien(self)
         alien_width, alien_height=alien.rect.size
         available_space_x=self.settings.screen_width-(2*alien_width)
         number_aliens_x=available_space_x//(2*alien_width)
         ship_height=self.ship.rect.height
         available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
         number_rows=available_space_y//(2*alien_height)
         for row_number in range(number_rows):
           for alien_number in range(number_aliens_x):
              self._create_alien(alien_number,row_number)
              
    def _create_alien(self,alien_number,row_number):
         alien=Alien(self)
         alien_width,alien_height=alien.rect.size
         alien.x=alien_width+2 * alien_width*alien_number
         alien.rect.x=alien.x
         alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
         self.aliens.add(alien)
              
         
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
         new_bullet=Bullet(self)
         self.bullets.add(new_bullet)   
         '''Create a new bullet and add it to bullets''' 
    def _update_aliens(self):
         '''Update alien postion in the fleet'''
         self._check_fleet_edges()
         self.aliens.update()
         if pygame.sprite.spritecollideany(self.ship, self.aliens):
              self._ship_hit()
         self._check_aliens_bottom()
     
    
    def _check_aliens_bottom(self):
         screen_rect=self.screen.get_rect()
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= screen_rect.bottom:
                   self._ship_hit()
                   break
          
         
          
 
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *=-1
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            if self.stats.game_active:
                 
                self.ship.update()
                self._update_aliens()  


            self.bullets.update() 
            
                  
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites(): 
              bullet.draw_bullet()
            self.aliens.draw(self.screen)
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0 :
                      self.bullets.remove(bullet)
            collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
            pygame.display.flip()
    
if __name__ == '__main__':
        ai=AlienInvasion()
        ai.run_game()
        