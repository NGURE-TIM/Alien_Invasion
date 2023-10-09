class Settings:
    '''A class to store all settings'''

    def __init__(self):
        '''Initialize the game settings'''
        self.screen_width=1200
        self.screen_height=800
        self.ship_speed = 1.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_speed=1.5
        self.bullet_color=(60,60,60)
        self.bullets=3
        self.alien_speed=1.0
        self.fleet_drop_speed=6
        self.fleet_direction=1
        self.ship_limit=3