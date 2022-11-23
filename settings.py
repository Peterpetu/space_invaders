from dataclasses import dataclass #2017

@dataclass
class Settings:
    
        # screen settings
        screen_width = 800
        screen_height = 600
        caption = "Space Invaders"
        #RGB (red, green, blue, 0-255 kunkin arvo)        
        bg_color = (0,0,255)

        # ship settings
        ship_speed = 0.5

        # bullet settings
        bullet_width = 3
        bullet_height = 15
        bullet_color = (255,255,255)
        bullet_speed = 0.5
        bullets_allowed = 3

        # alien settings
        alien_speed = 0.3