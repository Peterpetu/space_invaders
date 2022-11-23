import pygame
import sys # jotta voidaan käyttää sys.exit() = poistua ohjelmasta

class Events:
    def check_keys(self, game_ship): # vastaanotetaan näppäinkomentoja          
        for event in pygame.event.get():            
            if event.type == pygame.QUIT: # mikäli ikkuna suljetaan
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    game_ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    game_ship.fire_bullet()
        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    game_ship.moving_left = False